"""Windows filesystem probes for the report directory create-and-pin contract."""

import ctypes
import os
import struct
import sys
import tempfile
import unittest
from contextlib import contextmanager
from ctypes import wintypes
from pathlib import Path


FILE_LIST_DIRECTORY = 0x0001
GENERIC_READ = 0x80000000
GENERIC_WRITE = 0x40000000
FILE_READ_ATTRIBUTES = 0x0080
FILE_WRITE_ATTRIBUTES = 0x0100
SYNCHRONIZE = 0x00100000
FILE_SHARE_READ = 0x0001
FILE_SHARE_WRITE = 0x0002
FILE_SHARE_DELETE = 0x0004
FILE_CREATE = 2
FILE_CREATED = 2
FILE_LINK_INFORMATION_CLASS = 11
OPEN_EXISTING = 3
FILE_DIRECTORY_FILE = 0x0001
FILE_SYNCHRONOUS_IO_NONALERT = 0x0020
FILE_NON_DIRECTORY_FILE = 0x0040
FILE_FLAG_OPEN_REPARSE_POINT = 0x00200000
FILE_FLAG_BACKUP_SEMANTICS = 0x02000000
OBJ_DONT_REPARSE = 0x00001000
FSCTL_SET_REPARSE_POINT = 0x000900A4
FSCTL_DELETE_REPARSE_POINT = 0x000900AC
IO_REPARSE_TAG_MOUNT_POINT = 0xA0000003
STATUS_OBJECT_NAME_COLLISION = 0xC0000035
STATUS_REPARSE_POINT_ENCOUNTERED = 0xC000050B
STATUS_REPARSE_POINT_NOT_RESOLVED = 0xC0000280
DUPLICATE_SAME_ACCESS = 0x00000002
ERROR_SHARING_VIOLATION = 32
JUNCTION_SETUP_UNAVAILABLE = {1, 5, 50, 1314}
HARD_LINK_UNAVAILABLE = {0xC0000010, 0xC0000022, 0xC0000061, 0xC00000BB}


class UnicodeString(ctypes.Structure):
    _fields_ = [
        ("length", wintypes.USHORT),
        ("maximum_length", wintypes.USHORT),
        ("buffer", wintypes.LPWSTR),
    ]


class ObjectAttributes(ctypes.Structure):
    _fields_ = [
        ("length", wintypes.ULONG),
        ("root_directory", wintypes.HANDLE),
        ("object_name", ctypes.POINTER(UnicodeString)),
        ("attributes", wintypes.ULONG),
        ("security_descriptor", ctypes.c_void_p),
        ("security_qos", ctypes.c_void_p),
    ]


class IoStatusBlock(ctypes.Structure):
    _fields_ = [("status_or_pointer", ctypes.c_void_p), ("information", ctypes.c_size_t)]


class LinkInformation(ctypes.Structure):
    _fields_ = [
        ("replace_if_exists", wintypes.BOOLEAN),
        ("root_directory", wintypes.HANDLE),
        ("file_name_length", wintypes.ULONG),
        ("file_name", wintypes.WCHAR),
    ]


@unittest.skipUnless(sys.platform == "win32", "Requires Windows native file sharing")
class WindowsOutputDirectoryTests(unittest.TestCase):
    folder_name = "activities-report"
    report_name = "activity-report-2026-11-02.md"
    report_bytes = b"# Activity report\n"

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.folder = self.root / self.folder_name
        self.moved = self.root / "moved-report-directory"

        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        self.open_file = kernel32.CreateFileW
        self.open_file.argtypes = [
            wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, ctypes.c_void_p,
            wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE,
        ]
        self.open_file.restype = wintypes.HANDLE
        self.close_handle = kernel32.CloseHandle
        self.close_handle.argtypes = [wintypes.HANDLE]
        self.close_handle.restype = wintypes.BOOL
        self.duplicate_handle = kernel32.DuplicateHandle
        self.duplicate_handle.argtypes = [
            wintypes.HANDLE, wintypes.HANDLE, wintypes.HANDLE, ctypes.POINTER(wintypes.HANDLE),
            wintypes.DWORD, wintypes.BOOL, wintypes.DWORD,
        ]
        self.duplicate_handle.restype = wintypes.BOOL
        self.device_io_control = kernel32.DeviceIoControl
        self.device_io_control.argtypes = [
            wintypes.HANDLE, wintypes.DWORD, ctypes.c_void_p, wintypes.DWORD,
            ctypes.c_void_p, wintypes.DWORD, ctypes.POINTER(wintypes.DWORD), ctypes.c_void_p,
        ]
        self.device_io_control.restype = wintypes.BOOL

        self.create_file = ctypes.WinDLL("ntdll").NtCreateFile
        self.create_file.argtypes = [
            ctypes.POINTER(wintypes.HANDLE), wintypes.ULONG, ctypes.POINTER(ObjectAttributes),
            ctypes.POINTER(IoStatusBlock), ctypes.c_void_p, wintypes.ULONG, wintypes.ULONG,
            wintypes.ULONG, wintypes.ULONG, ctypes.c_void_p, wintypes.ULONG,
        ]
        self.create_file.restype = ctypes.c_long

        self.set_information = ctypes.WinDLL("ntdll").NtSetInformationFile
        self.set_information.argtypes = [
            wintypes.HANDLE, ctypes.POINTER(IoStatusBlock), ctypes.c_void_p,
            wintypes.ULONG, wintypes.ULONG,
        ]
        self.set_information.restype = ctypes.c_long

    @contextmanager
    def pin_directory(self, path, access=FILE_LIST_DIRECTORY | FILE_READ_ATTRIBUTES, share=FILE_SHARE_READ):
        handle = self.open_file(
            str(path), access, share,
            None, OPEN_EXISTING, FILE_FLAG_BACKUP_SEMANTICS | FILE_FLAG_OPEN_REPARSE_POINT, None,
        )
        if handle == wintypes.HANDLE(-1).value:
            raise ctypes.WinError(ctypes.get_last_error())
        try:
            yield handle
        finally:
            self.close_handle(handle)

    def create_and_pin_report_directory(self, parent):
        return self.create_relative(
            parent, self.folder_name, FILE_LIST_DIRECTORY | FILE_READ_ATTRIBUTES, FILE_DIRECTORY_FILE,
        )

    @contextmanager
    def create_relative(self, parent, component, access, kind):
        buffer = ctypes.create_unicode_buffer(component)
        name = UnicodeString(
            ctypes.sizeof(buffer) - ctypes.sizeof(ctypes.c_wchar),
            ctypes.sizeof(buffer), ctypes.cast(buffer, wintypes.LPWSTR),
        )
        attributes = ObjectAttributes(
            ctypes.sizeof(ObjectAttributes), parent, ctypes.pointer(name), OBJ_DONT_REPARSE,
        )
        handle = wintypes.HANDLE()
        io_status = IoStatusBlock()
        status = self.create_file(
            ctypes.byref(handle), access | SYNCHRONIZE,
            ctypes.byref(attributes), ctypes.byref(io_status), None, 0,
            FILE_SHARE_READ, FILE_CREATE, kind | FILE_SYNCHRONOUS_IO_NONALERT,
            None, 0,
        )
        try:
            yield status & 0xFFFFFFFF, io_status.information, handle.value
        finally:
            if handle.value:
                self.close_handle(handle)

    def write_exclusive_report(self):
        report = self.folder / self.report_name
        with report.open("xb") as stream:
            stream.write(self.report_bytes)
        self.assertEqual(report.read_bytes(), self.report_bytes)
        return report

    def write_and_read_report_handle(self, handle):
        import msvcrt

        current_process = wintypes.HANDLE(-1)
        duplicate = wintypes.HANDLE()
        if not self.duplicate_handle(
            current_process, handle, current_process, ctypes.byref(duplicate),
            0, False, DUPLICATE_SAME_ACCESS,
        ):
            raise ctypes.WinError(ctypes.get_last_error())
        try:
            descriptor = msvcrt.open_osfhandle(duplicate.value, os.O_RDWR | os.O_BINARY)
        except OSError:
            self.close_handle(duplicate)
            raise
        with os.fdopen(descriptor, "r+b") as stream:
            stream.write(self.report_bytes)
            stream.flush()
            stream.seek(0)
            self.assertEqual(stream.read(), self.report_bytes)

    def test_two_step_creation_accepts_a_substituted_directory(self):
        old_share = FILE_SHARE_READ | FILE_SHARE_WRITE
        with self.pin_directory(self.root, share=old_share):
            self.folder.mkdir()
            self.folder.rename(self.moved)
            self.folder.mkdir()
            with self.pin_directory(self.folder, share=old_share):
                self.write_exclusive_report()
        self.assertEqual(list(self.moved.iterdir()), [])
        self.assertEqual([path.name for path in self.folder.iterdir()], [self.report_name])

    def test_atomic_creation_pins_directory_before_first_write(self):
        with self.pin_directory(self.root) as parent:
            with self.create_and_pin_report_directory(parent) as (status, information, handle):
                self.assertEqual(status, 0, hex(status))
                self.assertEqual(information, FILE_CREATED)
                self.assertIsNotNone(handle)
                with self.assertRaises(PermissionError) as denied:
                    self.folder.rename(self.moved)
                self.assertEqual(denied.exception.winerror, ERROR_SHARING_VIOLATION)
                with self.assertRaises(OSError) as write_denied:
                    with self.pin_directory(self.folder, access=GENERIC_WRITE):
                        self.fail("A competing handle acquired write access")
                self.assertEqual(write_denied.exception.winerror, ERROR_SHARING_VIOLATION)
                self.assertEqual(list(self.folder.iterdir()), [])
                file_access = GENERIC_READ | GENERIC_WRITE
                with self.create_relative(handle, self.report_name, file_access, FILE_NON_DIRECTORY_FILE) as (
                    file_status, file_information, report_handle,
                ):
                    self.assertEqual((file_status, file_information), (0, FILE_CREATED))
                    self.write_and_read_report_handle(report_handle)
                with self.create_relative(handle, self.report_name, file_access, FILE_NON_DIRECTORY_FILE) as (
                    collision_status, _, collision_handle,
                ):
                    self.assertEqual(collision_status, STATUS_OBJECT_NAME_COLLISION)
                    self.assertIsNone(collision_handle)
        self.assertFalse(self.moved.exists())
        self.assertEqual((self.folder / self.report_name).read_bytes(), self.report_bytes)

    def test_atomic_creation_rejects_a_competing_directory(self):
        with self.pin_directory(self.root) as parent:
            self.assertFalse(self.folder.exists())
            self.folder.mkdir()
            with self.create_and_pin_report_directory(parent) as (status, _, handle):
                self.assertEqual(status, STATUS_OBJECT_NAME_COLLISION, hex(status))
                self.assertIsNone(handle)
        self.assertEqual(list(self.folder.iterdir()), [])

    def change_reparse_point(self, operation, reparse_data):
        buffer = ctypes.create_string_buffer(reparse_data)
        with self.pin_directory(self.folder, access=FILE_WRITE_ATTRIBUTES) as directory:
            returned = wintypes.DWORD()
            if not self.device_io_control(
                directory, operation, buffer, len(reparse_data),
                None, 0, ctypes.byref(returned), None,
            ):
                raise ctypes.WinError(ctypes.get_last_error())

    def set_junction(self, target):
        substitute_name = ("\\??\\" + str(target)).encode("utf-16-le")
        print_name = str(target).encode("utf-16-le")
        names = substitute_name + b"\0\0" + print_name + b"\0\0"
        reparse_data = struct.pack(
            "<I6H", IO_REPARSE_TAG_MOUNT_POINT, 8 + len(names), 0,
            0, len(substitute_name), len(substitute_name) + 2, len(print_name),
        ) + names
        try:
            self.change_reparse_point(FSCTL_SET_REPARSE_POINT, reparse_data)
        except OSError as exc:
            if exc.winerror not in JUNCTION_SETUP_UNAVAILABLE:
                raise
            self.skipTest(f"Cannot prepare a Windows junction: {exc}")

    def test_atomic_creation_does_not_follow_a_dangling_junction(self):
        target = self.root / "missing-junction-target"
        target.mkdir()
        self.folder.mkdir()
        self.set_junction(target)
        target.rmdir()

        with self.pin_directory(self.root) as parent:
            with self.create_and_pin_report_directory(parent) as (status, _, handle):
                self.assertEqual(status, STATUS_REPARSE_POINT_ENCOUNTERED, hex(status))
                self.assertIsNone(handle)
        self.assertEqual(self.folder.lstat().st_reparse_tag, IO_REPARSE_TAG_MOUNT_POINT)
        self.assertFalse(target.exists())

    def test_relative_child_creation_does_not_follow_in_place_junction(self):
        sibling = self.root / "junction-target"
        sibling.mkdir()
        with self.pin_directory(self.root) as parent:
            with self.create_and_pin_report_directory(parent) as (status, information, directory):
                self.assertEqual((status, information), (0, FILE_CREATED))
                self.set_junction(sibling)
                self.assertEqual(self.folder.lstat().st_reparse_tag, IO_REPARSE_TAG_MOUNT_POINT)

                # The disposable control demonstrates why a literal absolute path is insufficient.
                (self.folder / "absolute-control.md").write_bytes(self.report_bytes)
                self.assertEqual((sibling / "absolute-control.md").read_bytes(), self.report_bytes)

                with self.create_relative(directory, self.report_name, GENERIC_WRITE, FILE_NON_DIRECTORY_FILE) as (
                    relative_status, _, handle,
                ):
                    self.assertIn(relative_status, (STATUS_REPARSE_POINT_NOT_RESOLVED, STATUS_REPARSE_POINT_ENCOUNTERED))
                    self.assertIsNone(handle)
                    self.assertFalse((sibling / self.report_name).exists())

                self.change_reparse_point(
                    FSCTL_DELETE_REPARSE_POINT, struct.pack("<IHH", IO_REPARSE_TAG_MOUNT_POINT, 0, 0),
                )
        self.assertEqual(list(self.folder.iterdir()), [])
        self.assertEqual([path.name for path in sibling.iterdir()], ["absolute-control.md"])

    def add_hard_link(self, original, alias):
        name = ("\\??\\" + str(alias)).encode("utf-16-le")
        offset = LinkInformation.file_name.offset
        data = ctypes.create_string_buffer(max(offset + len(name), ctypes.sizeof(LinkInformation)))
        info = LinkInformation.from_buffer(data)
        info.file_name_length = len(name)
        ctypes.memmove(ctypes.addressof(data) + offset, name, len(name))
        io_status = IoStatusBlock()
        share = FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE
        try:
            with self.pin_directory(original, access=FILE_WRITE_ATTRIBUTES, share=share) as handle:
                status = self.set_information(
                    handle, ctypes.byref(io_status), data, len(data), FILE_LINK_INFORMATION_CLASS,
                ) & 0xFFFFFFFF
        except OSError as exc:
            if exc.winerror not in (1, 5, 50, 1314):
                raise
            self.skipTest(f"Cannot open a Windows hard-link fixture: {exc}")
        if status in HARD_LINK_UNAVAILABLE:
            self.skipTest(f"Cannot create a Windows hard-link fixture: NTSTATUS {status:#010x}")
        self.assertEqual(status, 0, hex(status))

    def test_late_hard_link_can_alias_an_existing_report(self):
        self.folder.mkdir()
        sibling = self.root / "outside-reports"
        sibling.mkdir()
        existing = self.folder / self.report_name
        existing.write_bytes(b"# Old report\n")
        replacement_alias = sibling / "replacement.md"
        access = GENERIC_READ | GENERIC_WRITE

        with self.pin_directory(existing, access=access, share=0) as writer:
            self.assertEqual(existing.stat().st_nlink, 1)
            self.add_hard_link(existing, replacement_alias)
            self.write_and_read_report_handle(writer)
        self.assertEqual(replacement_alias.read_bytes(), self.report_bytes)

    def test_late_hard_link_can_alias_a_newly_created_report(self):
        self.folder.mkdir()
        sibling = self.root / "outside-reports"
        sibling.mkdir()
        access = GENERIC_READ | GENERIC_WRITE
        fresh = self.folder / "fresh.md"
        fresh_alias = sibling / "fresh.md"
        with self.pin_directory(self.folder) as parent:
            with self.create_relative(parent, fresh.name, access, FILE_NON_DIRECTORY_FILE) as (
                status, information, writer,
            ):
                self.assertEqual((status, information), (0, FILE_CREATED))
                self.assertEqual(fresh.stat().st_nlink, 1)
                self.add_hard_link(fresh, fresh_alias)
                self.write_and_read_report_handle(writer)
        self.assertEqual(fresh_alias.read_bytes(), self.report_bytes)
