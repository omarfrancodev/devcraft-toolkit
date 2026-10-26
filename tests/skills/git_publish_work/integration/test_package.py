import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[4]
class PublicationPackage(unittest.TestCase):
    def entries(self):return {e["name"]:e for e in json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))["skills"]}
    def closure(self,names):
        entries=self.entries();found=set()
        def visit(n):
            if n in found:return
            found.add(n)
            for d in entries[n]["requires"]:visit(d)
        for n in names:visit(n)
        return found
    def test_publication_available_with_five_folder_closure(self):
        e=self.entries()["git-publish-work"];self.assertEqual("available",e["status"])
        self.assertEqual({"git-publish-changes","todo-workflow-controller"},set(e["requires"]))
        self.assertEqual({"git-publish-work","git-publish-changes","todo-workflow-controller","git-working-directory-policy","git-safety-check"},self.closure(["git-publish-work"]))
        for n in self.closure(["git-publish-work"]):self.assertTrue((ROOT/"skills"/n/"SKILL.md").is_file())
    def test_optional_publication_union_is_fifteen_folders(self):
        selected=["git-publish-work","git-create-work-branch","git-commit-builder","git-sync-branch","git-manage-pull-request","git-promote"]
        self.assertEqual({"git-publish-work","git-publish-changes","todo-workflow-controller","git-working-directory-policy","git-safety-check","git-create-work-branch","git-commit-builder","git-plan-commits","git-stage-changes","git-analyze-changes","conventional-commits-style","validation-discovery","git-sync-branch","git-manage-pull-request","git-promote"},self.closure(selected))
