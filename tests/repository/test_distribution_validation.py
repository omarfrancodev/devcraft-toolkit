"""Contract tests for distribution validation using real temporary packages."""

from __future__ import annotations

import importlib.util
import json
import shutil
import struct
import zlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE = "scripts.validate_distribution"


class DistributionValidationTests(unittest.TestCase):
    def setUp(self):
        if importlib.util.find_spec(MODULE) is None:
            self.fail("Distribution validation API is not implemented")
        from scripts.validate_distribution import validate_distribution
        self.validate = validate_distribution
        temp_root = ROOT / "tests" / ".tmp"
        temp_root.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_root)
        self.addCleanup(self.temp.cleanup)

    def write_json(self, path: Path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def make_root(self) -> Path:
        root = Path(self.temp.name) / "package"
        root.mkdir()
        shutil.copy2(ROOT / "catalog.json", root / "catalog.json")
        shutil.copytree(ROOT / "skills", root / "skills")
        inventory = Path("docs/capability-inventory.md")
        (root / inventory).parent.mkdir(parents=True)
        shutil.copy2(ROOT / inventory, root / inventory)
        identity = {
            "name": "devcraft-toolkit",
            "version": "0.1.0-preview.2",
            "description": "Composable Git and development skills for coding agents.",
            "author": {"name": "omarfrancodev"},
        }
        (root / "assets").mkdir()
        self.write_png(root / "assets/logo.png")
        self.write_json(root / "plugin.json", {
            "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            **identity,
            "keywords": ["git", "commit", "report", "validation"],
            "extensions": {"com.openai": {"interface": {
                "displayName": "Devcraft Toolkit",
                "shortDescription": "Composable Git tools",
                "longDescription": identity["description"],
                "developerName": "omarfrancodev",
                "category": "Developer Tools",
                "websiteURL": "https://github.com/omarfrancodev/devcraft-toolkit",
                "logo": "./assets/logo.png",
                "composerIcon": "./assets/logo.png",
            }}},
        })
        self.write_json(root / ".claude-plugin/plugin.json", identity)
        self.write_json(root / ".agents/plugins/marketplace.json", {
            "name": "devcraft-toolkit",
            "interface": {"displayName": "Devcraft Toolkit"},
            "plugins": [{
                "name": "devcraft-toolkit",
                "source": {"source": "local", "path": "./"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                "category": "Developer Tools",
            }],
        })
        self.write_json(root / ".claude-plugin/marketplace.json", {
            "name": "devcraft-toolkit",
            "owner": {"name": "omarfrancodev"},
            "plugins": [{
                "name": "devcraft-toolkit",
                "source": "./",
                "description": identity["description"],
            }],
        })
        return root

    def write_png(self, path, width=64, height=64):
        # A real, independently constructed RGBA PNG, requiring no image library.
        def chunk(kind, data):
            return (struct.pack(">I", len(data)) + kind + data
                    + struct.pack(">I", zlib.crc32(kind + data)))
        rows = (b"\x00" + b"\x10\x1b\x2d\xff" * width) * height
        path.write_bytes(
            b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(rows)) + chunk(b"IEND", b""))

    def test_missing_or_malformed_openai_presentation_is_reported(self):
        root = self.make_root()
        for bad in (None, [], {}, {"com.openai": None},
                    {"com.openai": []}, {"com.openai": {}},
                    {"com.openai": {"interface": []}}):
            with self.subTest(extensions=bad):
                self.edit(root, "plugin.json", lambda v: v.update(extensions=bad))
                self.assertIn("distribution-interface", self.codes(root))
        self.edit(root, "plugin.json", lambda v: v.pop("extensions"))
        self.assertIn("distribution-interface", self.codes(root))

    def test_presentation_requires_both_icons(self):
        root = self.make_root()
        for field in ("logo", "composerIcon"):
            with self.subTest(field=field):
                self.edit(root, "plugin.json", lambda v:
                          v["extensions"]["com.openai"]["interface"].pop(field))
                self.assertIn("distribution-asset", self.codes(root))
                self.edit(root, "plugin.json", lambda v:
                          v["extensions"]["com.openai"]["interface"].update({field: "./assets/logo.png"}))

    def test_presentation_and_marketplace_categories_must_be_developer_tools(self):
        root = self.make_root()
        for bad in ("Productivity", "developer-tools", [], None):
            with self.subTest(category=bad):
                self.edit(root, "plugin.json", lambda v:
                          v["extensions"]["com.openai"]["interface"].update(category=bad))
                self.assertIn("distribution-interface", self.codes(root))
                self.edit(root, ".agents/plugins/marketplace.json", lambda v:
                          v["plugins"][0].update(category=bad))
                self.assertIn("distribution-metadata", self.codes(root))

    def test_presentation_cannot_override_components(self):
        root = self.make_root()
        self.edit(root, "plugin.json", lambda v:
                  v["extensions"]["com.openai"].update(skills="./foreign/"))
        self.assertIn("distribution-interface", self.codes(root))

    def test_missing_or_directory_icon_is_reported(self):
        root = self.make_root()
        icon = root / "assets/logo.png"
        icon.unlink()
        self.assertIn("distribution-asset", self.codes(root))
        icon.mkdir()
        self.assertIn("distribution-asset", self.codes(root))

    def test_icons_must_use_packaged_assets_paths(self):
        root = self.make_root()
        self.write_png(root.parent / "outside.png")
        for bad in (None, 17, [], "", "assets/logo.png", "./../outside.png",
                    "./assets/../../outside.png", "./plugin.json",
                    "https://example.com/logo.png", "C:/logo.png",
                    "./assets\\logo.png", "./assets/logo.png?raw=1"):
            with self.subTest(path=bad):
                self.edit(root, "plugin.json", lambda v:
                          v["extensions"]["com.openai"]["interface"].update(logo=bad))
                self.assertIn("distribution-asset", self.codes(root))

    def test_icon_symlink_cannot_escape_package(self):
        root = self.make_root()
        outside = root.parent / "outside.png"
        self.write_png(outside)
        icon = root / "assets/logo.png"
        icon.unlink()
        try:
            icon.symlink_to(outside)
        except OSError as exc:
            self.skipTest(f"Symlinks unavailable: {exc}")
        self.assertIn("distribution-asset", self.codes(root))

    def test_icon_must_be_a_complete_png(self):
        root = self.make_root()
        icon = root / "assets/logo.png"
        good = icon.read_bytes()
        corrupted = bytearray(good)
        corrupted[29] ^= 1  # IHDR checksum corruption.
        for bad in (b"not a PNG", good[:33], good[:-1], bytes(corrupted)):
            with self.subTest(size=len(bad)):
                icon.write_bytes(bad)
                self.assertIn("distribution-asset", self.codes(root))

    def test_icons_must_be_square_and_within_size_limits(self):
        root = self.make_root()
        icon = root / "assets/logo.png"
        for width, height in ((47, 47), (64, 48), (4097, 1)):
            with self.subTest(dimensions=(width, height)):
                self.write_png(icon, width, height)
                self.assertIn("distribution-asset", self.codes(root))
        icon.write_bytes(b"x" * (5 * 1024 * 1024 + 1))
        self.assertIn("distribution-asset", self.codes(root))

    def edit(self, root, path, change):
        file = root / path
        value = json.loads(file.read_text(encoding="utf-8"))
        change(value)
        self.write_json(file, value)

    def codes(self, root):
        return {issue.code for issue in self.validate(root)}

    def test_valid_distribution(self):
        self.assertEqual([], self.validate(self.make_root()))

    def test_portable_activation_keywords_are_accepted(self):
        root = self.make_root()
        self.edit(root, "plugin.json", lambda v: v.update(keywords=["git", "report"]))
        self.assertEqual([], self.validate(root))

    def test_missing_portable_activation_keywords_are_reported(self):
        root = self.make_root()
        self.edit(root, "plugin.json", lambda v: v.pop("keywords"))
        self.assertIn("distribution-keywords", self.codes(root))

    def test_empty_or_malformed_portable_keywords_are_reported(self):
        root = self.make_root()
        for bad in (None, [], "git", {}, [17], [""], ["  "], ["git", None]):
            with self.subTest(keywords=bad):
                self.edit(root, "plugin.json", lambda v: v.update(keywords=bad))
                self.assertIn("distribution-keywords", self.codes(root))

    def test_manifest_identity_must_match(self):
        root = self.make_root()
        self.edit(root, ".claude-plugin/plugin.json", lambda v: v.update(name="foreign"))
        self.assertIn("distribution-metadata", self.codes(root))

    def test_manifest_versions_must_match(self):
        root = self.make_root()
        self.edit(root, ".claude-plugin/plugin.json", lambda v: v.update(version="0.2.0"))
        self.assertIn("distribution-version", self.codes(root))

    def test_invalid_semver_is_reported(self):
        root = self.make_root()
        for bad in ("v0.1.0", "01.1.0", "0.1", "0.1.0-preview.01", "0.1.0-"):
            with self.subTest(version=bad):
                self.edit(root, "plugin.json", lambda v: v.update(version=bad))
                self.assertIn("distribution-version", self.codes(root))

    def test_malformed_metadata_is_reported(self):
        root = self.make_root()
        paths = ["plugin.json", ".claude-plugin/plugin.json",
                 ".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json"]
        for path in paths:
            original = (root / path).read_bytes()
            for invalid in ('{"unfinished":', '[]', 'null'):
                with self.subTest(path=path, value=invalid):
                    (root / path).write_text(invalid, encoding="utf-8")
                    self.assertIn("distribution-metadata", self.codes(root))
            (root / path).write_bytes(original)

    def test_missing_metadata_is_reported(self):
        root = self.make_root()
        (root / ".claude-plugin/plugin.json").unlink()
        self.assertIn("distribution-metadata", self.codes(root))

    def test_marketplace_source_resolves_repository_root(self):
        root = self.make_root()
        self.assertNotIn("distribution-source", self.codes(root))
        self.edit(root, ".agents/plugins/marketplace.json",
                  lambda v: v["plugins"][0]["source"].update(path="./skills"))
        self.assertIn("distribution-source", self.codes(root))

    def test_marketplace_source_cannot_escape(self):
        root = self.make_root()
        (root.parent / "outside").mkdir()
        self.edit(root, ".agents/plugins/marketplace.json",
                  lambda v: v["plugins"][0]["source"].update(path="../outside"))
        self.assertIn("distribution-source", self.codes(root))

    def test_missing_root_source_is_reported(self):
        root = self.make_root()
        self.edit(root, ".claude-plugin/marketplace.json",
                  lambda v: v["plugins"][0].update(source="./missing"))
        self.assertIn("distribution-source", self.codes(root))

    def test_duplicate_marketplace_plugin_is_reported(self):
        root = self.make_root()
        self.edit(root, ".claude-plugin/marketplace.json",
                  lambda v: v["plugins"].append(dict(v["plugins"][0])))
        self.assertIn("distribution-metadata", self.codes(root))

    def test_missing_available_skill_is_reported(self):
        root = self.make_root()
        shutil.rmtree(root / "skills/validation-discovery")
        self.assertIn("distribution-inventory", self.codes(root))

    def planned_fixture_entry(self, root):
        # Set the fixture status explicitly instead of inheriting roadmap maturity.
        name = "git-publish-work"
        catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
        entry = next(item for item in catalog["skills"] if item["name"] == name)
        entry.update(status="planned", requires=[])
        self.write_json(root / "catalog.json", catalog)
        path = root / entry["path"]
        self.assertTrue(path.resolve().is_relative_to(root.resolve()))
        if path.exists():
            shutil.rmtree(path)  # Only the verified owned temporary package copy.
        return entry

    def test_planned_skill_is_not_discoverable(self):
        root = self.make_root()
        entry = self.planned_fixture_entry(root)
        path = root / entry["path"]
        path.mkdir()
        (path / "SKILL.md").write_text(
            f"---\nname: {entry['name']}\ndescription: Planned\n---\nText.")
        self.assertIn("distribution-inventory", self.codes(root))

    def test_duplicate_skill_copy_is_reported(self):
        root = self.make_root()
        shutil.copytree(root / "skills/validation-discovery", root / "copied-skill")
        self.assertIn("distribution-inventory", self.codes(root))

    def test_missing_resource_is_reported(self):
        root = self.make_root()
        (root / "skills/natural-language-report-writer/assets/report.md").unlink()
        self.assertIn("distribution-inventory", self.codes(root))

    def test_dependency_closure_rejects_missing_or_planned_dependency(self):
        root = self.make_root()
        planned = self.planned_fixture_entry(root)
        for bad in ("missing-skill", planned["name"]):
            with self.subTest(dependency=bad):
                self.edit(root, "catalog.json", lambda v:
                          v["skills"][0].update(requires=[bad]))
                self.assertIn("distribution-inventory", self.codes(root))

    def test_component_overrides_are_rejected(self):
        root = self.make_root()
        self.edit(root, ".claude-plugin/plugin.json",
                  lambda v: v.update(skills="./skills/"))
        self.assertIn("distribution-metadata", self.codes(root))

    def test_unrelated_files_are_not_edited(self):
        root = self.make_root()
        before = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
        self.assertEqual([], self.validate(root))
        after = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_cli_reports_invalid_distribution_without_traceback(self):
        root = self.make_root()
        (root / "plugin.json").unlink()
        result = subprocess.run(
            [sys.executable, "-B", "-m", MODULE, "--root", str(root)],
            cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
        self.assertIn("distribution-metadata", result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stdout + result.stderr)
