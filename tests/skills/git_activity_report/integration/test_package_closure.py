"""Package invariants for the history coordinator, not model behavior tests."""
import json
import re
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
        self.assertEqual(1, len(set(versions)))

    def test_installation_selections_match_available_catalog_closures(self):
        entries = {s["name"]:s for s in json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))["skills"]}
        available = {name for name,s in entries.items() if s["status"] == "available"}
        guide = (ROOT/"docs/installation/individual-skills.md").read_text(encoding="utf-8")
        rows = {}
        for name, cell in re.findall(r"^\| `([^`]+)` \| (.+) \|$", guide, re.M):
            names = set(" ".join(re.findall(r"`([^`]+)`", cell)).split()) if "`" in cell else {name}
            rows[name] = names
        self.assertEqual(available, set(rows))
        def closure(name):
            found = {name}
            for dependency in entries[name]["requires"]: found |= closure(dependency)
            return found
        for name in available:
            self.assertEqual(closure(name), rows[name], name)
        selection = re.search(r"^\$toolkitSkills = @\((.*)\)$", guide, re.M)
        self.assertIsNotNone(selection)
        self.assertEqual(available, set(re.findall(r"'([^']+)'", selection.group(1))))
