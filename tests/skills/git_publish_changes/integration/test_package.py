"""Available publication closure, independent from sync or a hosting connector."""
import json
import unittest
from pathlib import Path
from scripts.validate_repository import validate_repository
ROOT=Path(__file__).resolve().parents[4]
class PublishPackageTests(unittest.TestCase):
    def test_publish_available_with_exact_three_skill_closure(self):
        entries={s["name"]:s for s in json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))["skills"]}
        entry=entries["git-publish-changes"]
        self.assertEqual("available",entry["status"])
        self.assertEqual({"git-working-directory-policy","git-safety-check"},set(entry["requires"]))
        closure=set()
        def visit(name):
            if name in closure:return
            closure.add(name)
            for child in entries[name]["requires"]:visit(child)
        visit("git-publish-changes")
        self.assertEqual({"git-publish-changes","git-working-directory-policy","git-safety-check"},closure)
        self.assertEqual([],validate_repository(ROOT))
