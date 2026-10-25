"""Package invariants for the history coordinator, not model behavior tests."""
import json
import unittest
from pathlib import Path
from scripts.validate_repository import validate_repository

ROOT = Path(__file__).resolve().parents[4]

class HistoryPackageTests(unittest.TestCase):
    def test_report_is_available_with_exact_standalone_closure(self):
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        entries = {s["name"]: s for s in catalog["skills"]}
        report = entries["git-activity-report"]
        self.assertEqual("available", report["status"])
        self.assertEqual({"git-working-directory-policy", "natural-language-report-writer"}, set(report["requires"]))
        closure = set()
        def visit(name):
            if name in closure: return
            closure.add(name)
            for dependency in entries[name]["requires"]: visit(dependency)
        visit("git-activity-report")
        self.assertEqual({"git-activity-report", "git-working-directory-policy", "natural-language-report-writer"}, closure)
        self.assertEqual([], validate_repository(ROOT))
        for name in closure:
            self.assertTrue((ROOT / entries[name]["path"] / "SKILL.md").is_file())
        versions = [json.loads((ROOT/p).read_text(encoding="utf-8"))["version"] for p in ("plugin.json", ".claude-plugin/plugin.json")]
        self.assertEqual(["0.1.0-preview.5"]*2, versions)
