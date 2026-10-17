import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import validate_repository


INVENTORY = {
    "using-devcraft-toolkit": "entry",
    "git-commit-builder": "coordinator",
    "git-publish-work": "coordinator",
    "git-activity-report": "coordinator",
    "git-analyze-changes": "capability",
    "git-plan-commits": "capability",
    "git-stage-changes": "capability",
    "git-sync-branch": "capability",
    "git-publish-changes": "capability",
    "git-manage-pull-request": "capability",
    "git-promote": "capability",
    "git-safety-check": "support",
    "git-working-directory-policy": "support",
    "conventional-commits-style": "support",
    "validation-discovery": "support",
    "natural-language-report-writer": "support",
    "todo-workflow-controller": "support",
}


class RepositoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[2])
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def catalog(self, skills):
        (self.root / "catalog.json").write_text(
            json.dumps({"schema_version": 1, "name": "devcraft-toolkit", "skills": skills}),
            encoding="utf-8",
        )

    @staticmethod
    def entry(name="alpha", role="support", status="planned", path=None, requires=None):
        return {
            "name": name,
            "role": role,
            "status": status,
            "path": path or f"skills/{name}",
            "requires": requires or [],
        }

    def codes_and_paths(self):
        return {(issue.code, issue.path) for issue in validate_repository(self.root)}

    def test_valid_small_catalog(self):
        self.catalog([self.entry()])
        self.assertEqual([], validate_repository(self.root))

    def test_accepts_project_inventory_of_seventeen_names(self):
        self.catalog([self.entry(name, role) for name, role in INVENTORY.items()])
        self.assertEqual([], validate_repository(self.root))

    def test_duplicate_name(self):
        self.catalog([self.entry("alpha"), self.entry("alpha", path="skills/other")])
        self.assertIn(("duplicate-name", "catalog.json"), self.codes_and_paths())

    def test_absolute_or_parent_path(self):
        self.catalog([self.entry("alpha", path="../outside")])
        self.assertIn(("invalid-path", "catalog.json:skills[0]"), self.codes_and_paths())

    def test_unknown_dependency(self):
        self.catalog([self.entry("alpha", requires=["missing-skill"])])
        self.assertIn(("unknown-dependency", "catalog.json"), self.codes_and_paths())

    def test_dependency_cycle(self):
        self.catalog([
            self.entry("alpha", requires=["beta"]),
            self.entry("beta", requires=["alpha"]),
        ])
        self.assertIn(("dependency-cycle", "catalog.json"), self.codes_and_paths())

    def test_available_requires_planned(self):
        self.catalog([
            self.entry("alpha", status="available", requires=["beta"]),
            self.entry("beta"),
        ])
        self.assertIn(("unavailable-dependency", "catalog.json"), self.codes_and_paths())

    def test_wrong_entry_types_are_reported_without_traceback(self):
        entry = self.entry()
        entry["role"] = []
        entry["status"] = {}
        self.catalog([entry])
        self.assertIn(("catalog-schema", "catalog.json:skills[0]"), self.codes_and_paths())


if __name__ == "__main__":
    unittest.main()
