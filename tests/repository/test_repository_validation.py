import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

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
        temp_root = Path(__file__).resolve().parents[2] / "tests" / ".tmp"
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_root)
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

    def skill_tree(self, entry=None, *, text=None, resource=None):
        entry = entry or self.entry("alpha", status="available")
        self.catalog([entry])
        skill_root = self.root / entry["path"]
        skill_root.mkdir(parents=True, exist_ok=True)
        if text is None:
            text = f"---\nname: {entry['name']}\ndescription: A useful test skill.\n---\n\nInstructions for using {entry['name']}.\n"
        (skill_root / "SKILL.md").write_text(text, encoding="utf-8")
        if resource is not None:
            resource_path, resource_text = resource
            target = skill_root / resource_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(resource_text, encoding="utf-8")
        return skill_root

    def test_valid_small_catalog(self):
        self.catalog([self.entry()])
        self.assertEqual([], validate_repository(self.root))

    def test_schema_version_requires_an_exact_integer(self):
        for schema_version in (True, 1.0):
            with self.subTest(schema_version=schema_version):
                (self.root / "catalog.json").write_text(
                    json.dumps({"schema_version": schema_version, "name": "devcraft-toolkit", "skills": []}),
                    encoding="utf-8",
                )
                self.assertIn(("catalog-schema", "catalog.json"), self.codes_and_paths())

    def test_accepts_project_inventory_of_seventeen_names(self):
        self.catalog([self.entry(name, role) for name, role in INVENTORY.items()])
        self.assertEqual([], validate_repository(self.root))

    def test_duplicate_name(self):
        self.catalog([self.entry("alpha"), self.entry("alpha", path="skills/other")])
        self.assertIn(("duplicate-name", "catalog.json"), self.codes_and_paths())

    def test_duplicate_entries_still_validate_each_dependency_list(self):
        self.catalog([
            self.entry("alpha"),
            self.entry("alpha", path="skills/other", requires=["missing-skill"]),
        ])
        self.assertIn(("unknown-dependency", "catalog.json"), self.codes_and_paths())

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

    def test_multiple_dependency_cycles_produce_one_aggregate_issue(self):
        self.catalog([
            self.entry("alpha", requires=["beta"]),
            self.entry("beta", requires=["alpha"]),
            self.entry("gamma", requires=["delta"]),
            self.entry("delta", requires=["gamma"]),
        ])
        self.assertEqual(1, sum(issue.code == "dependency-cycle" for issue in validate_repository(self.root)))

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

    def test_malformed_skill_frontmatter_is_reported(self):
        self.skill_tree(text="---\nname: [invalid\n---\nbody\n")
        self.assertIn("skill-frontmatter", {item[0] for item in self.codes_and_paths()})

    def test_deep_frontmatter_is_reported_without_traceback(self):
        nested = "[" * 1500 + "null" + "]" * 1500
        text = f"---\nname: alpha\ndescription: A useful test skill.\nmetadata: {nested}\n---\nbody\n"
        self.skill_tree(text=text)
        self.assertIn("skill-frontmatter", {item[0] for item in self.codes_and_paths()})

    def test_missing_yaml_dependency_does_not_skip_skill_layout_checks(self):
        skill_root = self.skill_tree()
        (skill_root / "tests").mkdir()
        with patch("scripts.validate_repository.yaml", None):
            codes = {issue.code for issue in validate_repository(self.root)}
        self.assertIn("missing-dependency", codes)
        self.assertIn("skill-local-tests", codes)

    def test_skill_frontmatter_requires_matching_name_and_description(self):
        self.skill_tree(text="---\nname: other\ndescription: ''\n---\nbody\n")
        self.assertIn("skill-frontmatter", {item[0] for item in self.codes_and_paths()})

    def test_skill_name_and_description_limits_are_enforced(self):
        long_description = "x" * 1025
        text = f"---\nname: {'a' * 65}\ndescription: {long_description}\n---\nbody\n"
        self.skill_tree(text=text)
        self.assertIn("skill-frontmatter", {item[0] for item in self.codes_and_paths()})

    def test_skill_body_must_be_substantive(self):
        self.skill_tree(text="---\nname: alpha\ndescription: A useful test skill.\n---\n   \n")
        self.assertIn("skill-body", {item[0] for item in self.codes_and_paths()})

    def test_missing_local_resource_is_reported(self):
        self.skill_tree(text="---\nname: alpha\ndescription: A useful test skill.\n---\n\nRead [context](references/missing.md).\n")
        self.assertIn("missing-resource", {item[0] for item in self.codes_and_paths()})

    def test_local_link_supports_angle_bracket_destination_with_spaces(self):
        text = "---\nname: alpha\ndescription: A useful test skill.\n---\n\nRead [context](<references/context notes.md>).\n"
        self.skill_tree(text=text, resource=("references/context notes.md", "Context"))
        self.assertEqual(set(), self.codes_and_paths())

    def test_empty_local_link_destination_is_reported_without_crashing(self):
        text = "---\nname: alpha\ndescription: A useful test skill.\n---\n\nRead [context]( ).\n"
        self.skill_tree(text=text)
        self.assertEqual(set(), self.codes_and_paths())

    def test_resource_escape_is_reported(self):
        self.skill_tree(text="---\nname: alpha\ndescription: A useful test skill.\n---\n\nRead [outside](../outside.md).\n")
        self.assertIn("resource-escape", {item[0] for item in self.codes_and_paths()})

    def test_skill_symlink_cannot_escape_its_root(self):
        skill_root = self.skill_tree()
        outside = self.root / "outside.md"
        outside.write_text("outside", encoding="utf-8")
        link = skill_root / "references" / "outside.md"
        link.parent.mkdir()
        try:
            os.symlink(outside, link)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"OS does not permit symlink fixture: {exc}")
        self.assertIn("resource-escape", {item[0] for item in self.codes_and_paths()})

    def test_available_skill_cannot_contain_local_tests(self):
        skill_root = self.skill_tree()
        (skill_root / "tests").mkdir()
        (skill_root / "test_example.py").write_text("", encoding="utf-8")
        self.assertIn("skill-local-tests", {item[0] for item in self.codes_and_paths()})

    def test_available_skill_detects_common_python_test_file_names(self):
        skill_root = self.skill_tree()
        for filename in ("conftest.py", "tests.py", "test_alpha.PY", "testfoo.py"):
            (skill_root / filename).write_text("", encoding="utf-8")
        self.assertIn("skill-local-tests", {item[0] for item in self.codes_and_paths()})

    def test_planned_skill_must_not_expose_skill_md(self):
        entry = self.entry("alpha", status="planned")
        skill_root = self.root / entry["path"]
        skill_root.mkdir(parents=True)
        (skill_root / "SKILL.md").write_text("planned", encoding="utf-8")
        self.catalog([entry])
        self.assertIn("planned-placeholder", {item[0] for item in self.codes_and_paths()})

    def test_uncataloged_skill_is_reported(self):
        self.catalog([self.entry("alpha")])
        orphan = self.root / "skills" / "orphan-skill"
        orphan.mkdir(parents=True)
        (orphan / "SKILL.md").write_text("---\nname: orphan-skill\ndescription: Orphan.\n---\nbody\n", encoding="utf-8")
        self.assertIn("unlisted-skill", {item[0] for item in self.codes_and_paths()})

    def test_nested_skill_markdown_is_not_hidden_from_catalog_checks(self):
        planned = self.entry("alpha", status="planned")
        self.catalog([planned])
        nested = self.root / "skills" / "alpha" / "docs"
        nested.mkdir(parents=True)
        (nested / "SKILL.md").write_text("nested", encoding="utf-8")
        self.assertIn("planned-placeholder", {item[0] for item in self.codes_and_paths()})

        self.catalog([self.entry("alpha")])
        nested_unlisted = self.root / "skills" / "group" / "hidden"
        nested_unlisted.mkdir(parents=True)
        (nested_unlisted / "SKILL.md").write_text("nested", encoding="utf-8")
        self.assertIn("unlisted-skill", {item[0] for item in self.codes_and_paths()})

    def test_local_links_ignore_urls_code_and_inline_examples(self):
        text = (
            "---\nname: alpha\ndescription: A useful test skill.\n---\n\n"
            "Read [context](references/context.md#setup) and https://example.com.\n"
            "`[inline](missing-inline.md)`\n\n```md\n[example](missing-fenced.md)\n```\n"
        )
        self.skill_tree(text=text, resource=("references/context.md", "Context"))
        self.assertEqual(set(), self.codes_and_paths())

    def test_inline_code_does_not_close_on_a_shorter_run(self):
        text = (
            "---\nname: alpha\ndescription: A useful test skill.\n---\n\n"
            "An unmatched run ``` surrounds [outside](../outside.md) before a shorter run ``.\n"
        )
        self.skill_tree(text=text)
        self.assertIn("resource-escape", {item[0] for item in self.codes_and_paths()})

    def test_escaped_literal_backtick_does_not_hide_resource_links(self):
        text = (
            "---\nname: alpha\ndescription: A useful test skill.\n---\n\n"
            "Use the \\` character literally. See [escape](../outside.md) and "
            "[gone](references/gone.md), then `code`.\n"
        )
        self.skill_tree(text=text)
        self.assertEqual(
            {"resource-escape", "missing-resource"},
            {code for code, _path in self.codes_and_paths()},
        )

    def test_unmatched_inline_delimiter_does_not_cross_paragraphs(self):
        text = (
            "---\nname: alpha\ndescription: A useful test skill.\n---\n\n"
            "Use the ` character literally. See [escape](../outside.md).\n\n"
            "A later inline example is `code`.\n"
        )
        self.skill_tree(text=text)
        self.assertIn("resource-escape", {item[0] for item in self.codes_and_paths()})

    def test_backtick_in_fence_info_string_does_not_open_code_block(self):
        text = (
            "---\nname: alpha\ndescription: A useful test skill.\n---\n\n"
            "``` a`b\n[inside](missing-fenced.md)\n```\n"
        )
        self.skill_tree(text=text)
        self.assertIn("missing-resource", {item[0] for item in self.codes_and_paths()})

    def test_unclosed_fence_hides_examples_through_end_of_document(self):
        text = (
            "---\nname: alpha\ndescription: A useful test skill.\n---\n\n"
            "```md\n[example](missing-fenced.md)\n"
        )
        self.skill_tree(text=text)
        self.assertNotIn("missing-resource", {item[0] for item in self.codes_and_paths()})

    def test_root_test_ownership_accepts_normalized_skill_package(self):
        self.skill_tree(self.entry("git-working-directory-policy", status="available"))
        package = self.root / "tests" / "skills" / "git_working_directory_policy"
        package.mkdir(parents=True)
        (package / "test_alpha.py").write_text("", encoding="utf-8")
        self.assertNotIn("test-ownership", {item[0] for item in self.codes_and_paths()})

    def test_root_test_ownership_rejects_unknown_skill_package(self):
        self.catalog([self.entry("alpha")])
        package = self.root / "tests" / "skills" / "unknown_skill"
        package.mkdir(parents=True)
        (package / "test_unknown.py").write_text("", encoding="utf-8")
        self.assertIn("test-ownership", {item[0] for item in self.codes_and_paths()})

    def test_root_test_ownership_rejects_loose_python_modules(self):
        self.catalog([self.entry("alpha")])
        skill_tests = self.root / "tests" / "skills"
        skill_tests.mkdir(parents=True)
        (skill_tests / "test_orphan.py").write_text("", encoding="utf-8")
        issues = validate_repository(self.root)
        self.assertIn(("test-ownership", "tests/skills/test_orphan.py"), {(issue.code, issue.path) for issue in issues})

    def test_root_test_ownership_allows_skills_package_marker(self):
        self.catalog([self.entry("alpha")])
        package_marker = self.root / "tests" / "skills" / "__init__.py"
        package_marker.parent.mkdir(parents=True)
        package_marker.write_text("", encoding="utf-8")
        self.assertNotIn("test-ownership", {item[0] for item in self.codes_and_paths()})

    def test_root_test_ownership_covers_the_entire_skill_subtree(self):
        self.catalog([self.entry("alpha")])
        nested = self.root / "tests" / "skills" / "alpha" / "eval" / "ghost_skill"
        nested.mkdir(parents=True)
        (nested / "test_nested.py").write_text("", encoding="utf-8")
        self.assertNotIn("test-ownership", {item[0] for item in self.codes_and_paths()})

    def test_python_cache_is_not_treated_as_skill_test_package(self):
        self.catalog([self.entry("alpha")])
        (self.root / "tests" / "skills" / "__pycache__").mkdir(parents=True)
        self.assertNotIn("test-ownership", {item[0] for item in self.codes_and_paths()})


if __name__ == "__main__":
    unittest.main()
