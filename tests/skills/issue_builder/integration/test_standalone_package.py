"""Exercise complete and incomplete shipped issue-builder folder selections."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_distribution import validate_distribution
from scripts.validate_repository import validate_repository

ROOT = Path(__file__).resolve().parents[4]


class IssueBuilderPackageTests(unittest.TestCase):
    def setUp(self):
        temporary_root = ROOT / "tests/.tmp"
        temporary_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temporary_root)
        self.addCleanup(self.temp.cleanup)

    def selected_package(self):
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        entries = [entry for entry in catalog["skills"]
                   if entry["name"] == "issue-builder" and entry["status"] == "available"]
        self.assertEqual(len(entries), 1, "The requested standalone capability is unavailable")
        self.assertEqual(entries[0]["requires"], [])
        package = Path(self.temp.name) / "selected-package"
        package.mkdir()
        selected = {"schema_version": 1, "name": "devcraft-toolkit", "skills": entries}
        (package / "catalog.json").write_text(json.dumps(selected), encoding="utf-8")
        shutil.copytree(ROOT / entries[0]["path"], package / entries[0]["path"])
        # Manifests and root assets are validator fixtures, not installed skill dependencies.
        for relative in ("plugin.json", ".claude-plugin/plugin.json",
                         ".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json"):
            destination = package / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, destination)
        shutil.copytree(ROOT / "assets", package / "assets")
        return package

    def test_complete_folder_validates_without_other_skills_or_root_docs(self):
        package = self.selected_package()
        self.assertEqual(validate_repository(package), [])
        self.assertEqual(validate_distribution(package), [])
        self.assertEqual(sorted(path.name for path in (package / "skills").iterdir()),
                         ["issue-builder"])
        self.assertFalse((package / "docs").exists())
        source = ROOT / "skills/issue-builder"
        copied = package / "skills/issue-builder"
        original = {path.relative_to(source).as_posix(): path.read_bytes()
                    for path in source.rglob("*") if path.is_file()}
        transferred = {path.relative_to(copied).as_posix(): path.read_bytes()
                       for path in copied.rglob("*") if path.is_file()}
        self.assertEqual(transferred, original)

    def test_missing_presentation_is_rejected(self):
        package = self.selected_package()
        (package / "skills/issue-builder/agents/openai.yaml").unlink()
        self.assertTrue(any(issue.code == "distribution-skill-interface"
                            and issue.path == "skills/issue-builder/agents/openai.yaml"
                            for issue in validate_distribution(package)))

    def test_missing_entrypoint_is_rejected(self):
        package = self.selected_package()
        (package / "skills/issue-builder/SKILL.md").unlink()
        self.assertTrue(any(issue.code == "skill-frontmatter"
                            and issue.path == "skills/issue-builder/SKILL.md"
                            for issue in validate_repository(package)))
