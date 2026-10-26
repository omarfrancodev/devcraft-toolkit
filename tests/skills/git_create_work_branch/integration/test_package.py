import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
class BranchPackageTests(unittest.TestCase):
    def test_branch_available_with_two_folder_closure(self):
        entries={e["name"]:e for e in json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))["skills"]}
        self.assertIn("git-create-work-branch", entries)
        e=entries["git-create-work-branch"]
        self.assertEqual("available",e["status"])
        self.assertEqual(["git-working-directory-policy"],e["requires"])
        for name in (e["name"], *e["requires"]):
            self.assertTrue((ROOT/entries[name]["path"]/"SKILL.md").is_file())
        self.assertEqual([],entries["git-working-directory-policy"]["requires"])
