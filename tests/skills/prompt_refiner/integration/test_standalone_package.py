"""Exercise the shipped prompt-refiner folder through real package validation."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_distribution import validate_distribution
from scripts.validate_repository import validate_repository

ROOT = Path(__file__).resolve().parents[4]


class PromptRefinerPackageTests(unittest.TestCase):
    def setUp(self):
        temp_root = ROOT / "tests/.tmp"
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_root)
        self.addCleanup(self.temp.cleanup)

    def selected_package(self):
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        entries = [entry for entry in catalog["skills"]
                   if entry["name"] == "prompt-refiner" and entry["status"] == "available"]
        self.assertEqual(len(entries), 1, "The requested standalone capability is unavailable")
        package = Path(self.temp.name) / "selected-package"
        package.mkdir()
        selected = {"schema_version": 1, "name": "devcraft-toolkit", "skills": entries}
        (package / "catalog.json").write_text(json.dumps(selected), encoding="utf-8")
        shutil.copytree(ROOT / entries[0]["path"], package / entries[0]["path"])
        # Root manifests/assets belong to the validator fixture, not to the installed skill.
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
                         ["prompt-refiner"])
        self.assertFalse((package / "docs").exists())
        source = ROOT / "skills/prompt-refiner"
        copied = package / "skills/prompt-refiner"
        original = {path.relative_to(source).as_posix(): path.read_bytes()
                    for path in source.rglob("*") if path.is_file()}
        transferred = {path.relative_to(copied).as_posix(): path.read_bytes()
                       for path in copied.rglob("*") if path.is_file()}
        self.assertEqual(transferred, original)

    def test_missing_presentation_fails_existing_distribution_contract(self):
        package = self.selected_package()
        (package / "skills/prompt-refiner/agents/openai.yaml").unlink()
        issues = validate_distribution(package)
        self.assertTrue(any(issue.code == "distribution-skill-interface"
                            and issue.path == "skills/prompt-refiner/agents/openai.yaml"
                            for issue in issues))
