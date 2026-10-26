"""Availability/closure invariants, not model behavior assertions."""
import json
import unittest
from pathlib import Path
from scripts.validate_repository import validate_repository
ROOT=Path(__file__).resolve().parents[4]
class ManagementPackageTests(unittest.TestCase):
    def test_management_available_with_exact_two_skill_closure(self):
        entries={s["name"]:s for s in json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))["skills"]}
        self.assertEqual("available",entries["git-manage-pull-request"]["status"])
        self.assertEqual(["git-working-directory-policy"],entries["git-manage-pull-request"]["requires"])
        self.assertEqual([],entries["git-working-directory-policy"]["requires"])
        self.assertEqual([],validate_repository(ROOT))
