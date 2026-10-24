"""Real Git controls for the analyzer's documented recipes, not an agent simulator."""
import hashlib
import tempfile
import unittest
from pathlib import Path

from tests.support.git_fixtures import _git, git_fixture, snapshot_repository


SAFE = [
    "--no-pager", "--no-optional-locks", "--no-lazy-fetch",
    "-c", "core.fsmonitor=false", "-c", "core.untrackedCache=false",
    "-c", "core.splitIndex=false", "-c", "submodule.recurse=false",
]


class InspectionRecipeTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[3] / ".tmp"
        root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=root)
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def git(self, repo, *args, check=True):
        return _git([*SAFE, *args], cwd=repo, check=check).stdout

    def test_partial_staging_has_distinct_patches_without_writes(self):
        with git_fixture("normal", self.root) as repo:
            path = repo / "README.md"
            path.write_text("Staged rounding fix.\n", encoding="utf-8")
            _git(["add", "--", "README.md"], cwd=repo)
            path.write_text("Staged rounding fix.\nUnstaged debug.\n", encoding="utf-8")
            before = snapshot_repository(repo)
            status = self.git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignore-submodules=all")
            staged = self.git(repo, "diff", "--cached", "--no-ext-diff", "--no-textconv", "--ignore-submodules=all")
            unstaged = self.git(repo, "diff", "--no-ext-diff", "--no-textconv", "--ignore-submodules=all")
            self.assertIn("MM README.md\0", status)
            self.assertIn("+Staged rounding fix.", staged)
            self.assertNotIn("Unstaged debug.", staged)
            self.assertIn("+Unstaged debug.", unstaged)
            self.assertEqual(before, snapshot_repository(repo))

    def test_nul_paths_rename_delete_binary_and_literal_selection(self):
        with git_fixture("normal", self.root) as repo:
            _git(["mv", "README.md", "renamed file.md"], cwd=repo)
            for name in ("[draft].txt", "other.txt", "$(noop).txt", "sample.bin"):
                (repo / name).write_bytes(b"\0\xff" if name.endswith(".bin") else b"first\n")
            _git(["add", "--", "[draft].txt", "other.txt", "$(noop).txt", "sample.bin"], cwd=repo)
            (repo / "[draft].txt").write_text("second\n", encoding="utf-8")
            (repo / "other.txt").unlink()
            before = snapshot_repository(repo)
            status = self.git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignore-submodules=all")
            self.assertIn("R  renamed file.md\0README.md\0", status)
            self.assertIn("AM [draft].txt\0", status)
            self.assertIn("AD other.txt\0", status)
            self.assertIn("A  $(noop).txt\0", status)
            patch = self.git(repo, "--literal-pathspecs", "diff", "--no-ext-diff", "--no-textconv", "--", "[draft].txt")
            self.assertIn("+second", patch)
            self.assertNotIn("other.txt", patch)
            self.assertIn("Binary files", self.git(repo, "diff", "--cached", "--no-ext-diff", "--no-textconv"))
            self.assertEqual(before, snapshot_repository(repo))

    def test_helpers_are_disabled_and_no_sentinel_is_created(self):
        with git_fixture("normal", self.root) as repo:
            # Any executed helper writes a visible sentinel.
            helper = "echo helper-ran > helper-sentinel"
            for key in ("diff.external", "diff.fixture.textconv", "core.fsmonitor"):
                _git(["config", "--local", key, helper], cwd=repo)
            (repo / ".gitattributes").write_text("README.md diff=fixture\n", encoding="utf-8")
            (repo / "README.md").write_text("Changed\n", encoding="utf-8")
            before = snapshot_repository(repo)
            self.git(repo, "status", "--porcelain=v1", "-z", "--ignore-submodules=all")
            self.git(repo, "diff", "--no-ext-diff", "--no-textconv", "--ignore-submodules=all")
            self.assertFalse((repo / "helper-sentinel").exists())
            self.assertEqual(before, snapshot_repository(repo))

    def test_configured_filter_gate_uses_metadata_without_hashing_worktree(self):
        with git_fixture("normal", self.root) as repo:
            _git(["config", "--local", "filter.fixture.clean", "echo filter-ran > filter-sentinel"], cwd=repo)
            _git(["config", "--local", "filter.fixture.process", "echo filter-ran > filter-sentinel"], cwd=repo)
            (repo / ".gitattributes").write_text("* filter=fixture\n", encoding="utf-8")
            (repo / "README.md").write_text("Unhashed worktree change\n", encoding="utf-8")
            before = snapshot_repository(repo)
            filters = self.git(repo, "config", "--get-regexp", r"^filter\..*\.(clean|process)$", check=False)
            self.assertIn("filter.fixture.clean", filters)
            self.assertIn("filter.fixture.process", filters)
            self.assertIn("README.md\0", self.git(repo, "ls-files", "--stage", "-z"))
            self.git(repo, "diff", "--cached", "--no-ext-diff", "--no-textconv", "--ignore-submodules=all")
            # This gate deliberately does NOT run status or a worktree diff.
            self.assertFalse((repo / "filter-sentinel").exists())
            self.assertEqual(before, snapshot_repository(repo))

    def test_content_guard_detects_same_status_edit(self):
        with git_fixture("dirty", self.root) as repo:
            args = ("status", "--porcelain=v1", "-z", "--ignore-submodules=all")
            status_before = self.git(repo, *args)
            path = repo / "README.md"
            digest_before = hashlib.sha256(path.read_bytes()).hexdigest()
            path.write_text("Different unstaged contents\n", encoding="utf-8")
            self.assertEqual(status_before, self.git(repo, *args))
            self.assertNotEqual(digest_before, hashlib.sha256(path.read_bytes()).hexdigest())

    def test_unborn_detached_conflicted_and_missing_identity_remain_inspectable(self):
        for kind in ("unborn", "detached", "conflicted", "missing-identity"):
            with self.subTest(kind=kind), git_fixture(kind, self.root, dirname=kind) as repo:
                before = snapshot_repository(repo)
                self.git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignore-submodules=all")
                self.git(repo, "ls-files", "--stage", "-z")
                self.git(repo, "diff", "--cached", "--no-ext-diff", "--no-textconv", "--ignore-submodules=all")
                self.assertEqual(before, snapshot_repository(repo))

    def test_gitlink_is_in_inventory_without_submodule_traversal(self):
        with git_fixture("normal", self.root) as repo:
            head = self.git(repo, "rev-parse", "HEAD").strip()
            _git(["update-index", "--add", "--cacheinfo", f"160000,{head},vendor"], cwd=repo)
            before = snapshot_repository(repo)
            self.assertIn("160000", self.git(repo, "ls-files", "--stage", "-z"))
            self.git(repo, "status", "--porcelain=v1", "-z", "--ignore-submodules=all")
            self.assertFalse((repo / "vendor").exists())
            self.assertEqual(before, snapshot_repository(repo))


