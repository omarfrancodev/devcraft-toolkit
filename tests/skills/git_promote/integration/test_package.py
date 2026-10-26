import json
import unittest
from pathlib import Path
from scripts.validate_repository import validate_repository
ROOT=Path(__file__).resolve().parents[4]
class PromotionPackageTests(unittest.TestCase):
    def test_promotion_available_with_exact_three_skill_closure(self):
        entries={s["name"]:s for s in json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))["skills"]}
        self.assertEqual("available",entries["git-promote"]["status"])
        self.assertEqual(["git-manage-pull-request"],entries["git-promote"]["requires"])
        self.assertEqual(["git-working-directory-policy"],entries["git-manage-pull-request"]["requires"])
        self.assertEqual([],entries["git-working-directory-policy"]["requires"])
        self.assertEqual([],validate_repository(ROOT))
