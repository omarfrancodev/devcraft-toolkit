"""Real Git controls for path-specific filter inspection, not an agent simulator."""
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from tests.support.git_fixtures import _git, git_fixture, snapshot_repository
from tests.skills.git_analyze_changes.integration.test_inspection_recipes import SAFE


class FilterScopeRecipeTests(unittest.TestCase):
    def setUp(self):
        temp_root = Path(__file__).resolve().parents[3] / ".tmp"
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_root)
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def attributes(self, repo, paths):
        env = {key: value for key, value in os.environ.items()
               if not key.upper().startswith("GIT_")}
        env.update(GIT_CONFIG_NOSYSTEM="1",
                   GIT_CONFIG_GLOBAL=str(self.root / ".fixture-global-config"))
        result = subprocess.run(
            ["git", *SAFE, "check-attr", "-z", "--stdin", "filter"],
            cwd=repo, env=env, input="".join(path + "\0" for path in paths),
            capture_output=True, text=True, encoding="utf-8", check=True,
        )
        records = result.stdout.split("\0")
        self.assertEqual(records.pop(), "")
        self.assertEqual(len(records), 3 * len(paths))
        return [tuple(records[i:i + 3]) for i in range(0, len(records), 3)]

    def safe_diff(self, repo, *paths):
        return _git([
            *SAFE, "--literal-pathspecs", "-c", "diff.autoRefreshIndex=false",
            "diff", "--no-renames", "--no-ext-diff", "--no-textconv",
            "--ignore-submodules=all", "--", *paths,
        ], cwd=repo, env={"GIT_CONFIG_GLOBAL": str(self.root / ".fixture-global-config")}).stdout

    def configure_sentinel(self, repo, driver="fixture"):
        for operation in ("clean", "process"):
            _git(["config", "--local", f"filter.{driver}.{operation}",
                  "echo filter-ran > filter-sentinel"], cwd=repo)

    def test_registered_but_unused_inherited_filter_allows_real_delta(self):
        with git_fixture("normal", self.root) as repo:
            config = self.root / ".fixture-global-config"
            config.write_text(
                '[filter "lfs"]\n'
                '    clean = echo filter-ran > filter-sentinel\n'
                '    process = echo filter-ran > filter-sentinel\n',
                encoding="utf-8",
            )
            (repo / "README.md").write_text("Visible local change.\n", encoding="utf-8")
            before = snapshot_repository(repo)
            self.assertEqual(self.attributes(repo, ["README.md"]),
                             [("README.md", "filter", "unspecified")])
            result = _git([
                *SAFE, "--literal-pathspecs", "-c", "diff.autoRefreshIndex=false",
                "diff", "--no-renames", "--no-ext-diff", "--no-textconv",
                "--ignore-submodules=all", "--", "README.md",
            ], cwd=repo, env={"GIT_CONFIG_GLOBAL": str(config)}).stdout
            self.assertIn("+Visible local change.", result)
            self.assertFalse((repo / "filter-sentinel").exists())
            self.assertEqual(before, snapshot_repository(repo))

    def test_dirty_filtered_sibling_is_not_hashed_by_selected_diff(self):
        with git_fixture("normal", self.root) as repo:
            (repo / "picture.bin").write_bytes(b"original binary\0")
            (repo / ".gitattributes").write_text("*.bin filter=fixture\n", encoding="utf-8")
            _git(["add", "--", "picture.bin", ".gitattributes"], cwd=repo)
            _git(["commit", "-m", "fixture: add attributes"], cwd=repo)
            self.configure_sentinel(repo)
            (repo / "README.md").write_text("Selected change.\n", encoding="utf-8")
            (repo / "picture.bin").write_bytes(b"excluded changed binary\0")
            before = snapshot_repository(repo)
            self.assertEqual(self.attributes(repo, ["README.md"]),
                             [("README.md", "filter", "unspecified")])
            patch = self.safe_diff(repo, "README.md")
            self.assertIn("+Selected change.", patch)
            self.assertNotIn("picture.bin", patch)
            self.assertFalse((repo / "filter-sentinel").exists())
            self.assertEqual(before, snapshot_repository(repo))

    def test_mixed_scope_keeps_safe_patch_and_filtered_raw_evidence(self):
        with git_fixture("normal", self.root) as repo:
            (repo / "picture.bin").write_bytes(b"base\0")
            (repo / ".gitattributes").write_text("*.bin filter=fixture\n", encoding="utf-8")
            _git(["add", "--", "picture.bin", ".gitattributes"], cwd=repo)
            _git(["commit", "-m", "fixture: add binary"], cwd=repo)
            self.configure_sentinel(repo)
            (repo / "README.md").write_text("Safe text change.\n", encoding="utf-8")
            (repo / "picture.bin").write_bytes(b"changed\0")
            before = snapshot_repository(repo)
            self.assertEqual(self.attributes(repo, ["README.md", "picture.bin"]), [
                ("README.md", "filter", "unspecified"),
                ("picture.bin", "filter", "fixture"),
            ])
            self.assertIn("+Safe text change.", self.safe_diff(repo, "README.md"))
            _git([*SAFE, "diff", "--cached", "--no-ext-diff", "--no-textconv"], cwd=repo)
            self.assertEqual((repo / "picture.bin").read_bytes(), b"changed\0")
            self.assertFalse((repo / "filter-sentinel").exists())
            self.assertEqual(before, snapshot_repository(repo))

    def test_info_attributes_override_worktree_filter_without_config_changes(self):
        with git_fixture("normal", self.root) as repo:
            (repo / ".gitattributes").write_text("README.md filter=fixture\n", encoding="utf-8")
            (repo / ".git/info/attributes").write_text("README.md -filter\n", encoding="utf-8")
            self.configure_sentinel(repo)
            (repo / "README.md").write_text("Unfiltered by effective override.\n", encoding="utf-8")
            before = snapshot_repository(repo)
            self.assertEqual(self.attributes(repo, ["README.md"]),
                             [("README.md", "filter", "unset")])
            self.assertIn("+Unfiltered by effective override.", self.safe_diff(repo, "README.md"))
            self.assertFalse((repo / "filter-sentinel").exists())
            self.assertEqual(before, snapshot_repository(repo))

    def test_external_attributes_and_index_fallback_are_observed(self):
        with git_fixture("normal", self.root) as repo:
            external = self.root / "external-attributes"
            external.write_text("README.md filter=fixture\n", encoding="utf-8")
            _git(["config", "--local", "core.attributesFile", str(external)], cwd=repo)
            self.configure_sentinel(repo)
            before = snapshot_repository(repo)
            self.assertEqual(self.attributes(repo, ["README.md"]),
                             [("README.md", "filter", "fixture")])
            self.assertEqual(before, snapshot_repository(repo))
            self.assertFalse((repo / "filter-sentinel").exists())
        with git_fixture("normal", self.root, dirname="fallback") as repo:
            (repo / ".gitattributes").write_text("README.md filter=fixture\n", encoding="utf-8")
            _git(["add", "--", ".gitattributes"], cwd=repo)
            (repo / ".gitattributes").unlink()
            self.configure_sentinel(repo)
            before = snapshot_repository(repo)
            self.assertEqual(self.attributes(repo, ["README.md"]),
                             [("README.md", "filter", "fixture")])
            self.assertFalse((repo / "filter-sentinel").exists())
            self.assertEqual(before, snapshot_repository(repo))

    def test_nul_attribute_transport_preserves_literal_and_untracked_names(self):
        with git_fixture("normal", self.root) as repo:
            paths = ["[draft].txt", "space name.txt", "$(noop).txt"]
            for path in paths:
                (repo / path).write_text("Untracked input.\n", encoding="utf-8")
            (repo / ".gitattributes").write_text("*.txt filter=fixture\n", encoding="utf-8")
            self.configure_sentinel(repo)
            before = snapshot_repository(repo)
            self.assertEqual(self.attributes(repo, paths),
                             [(path, "filter", "fixture") for path in paths])
            self.assertFalse((repo / "filter-sentinel").exists())
            self.assertEqual(before, snapshot_repository(repo))

    def test_attribute_guard_detects_changed_decision_with_same_head_and_index(self):
        with git_fixture("normal", self.root) as repo:
            attr = repo / ".gitattributes"
            attr.write_text("README.md -filter\n", encoding="utf-8")
            self.configure_sentinel(repo)
            before = snapshot_repository(repo)
            first = self.attributes(repo, ["README.md"])
            attr.write_text("README.md filter=fixture\n", encoding="utf-8")
            second = self.attributes(repo, ["README.md"])
            after = snapshot_repository(repo)
            self.assertEqual(first, [("README.md", "filter", "unset")])
            self.assertEqual(second, [("README.md", "filter", "fixture")])
            self.assertEqual(before["HEAD"], after["HEAD"])
            self.assertEqual(before["index"], after["index"])
            self.assertNotEqual(before["working:.gitattributes"], after["working:.gitattributes"])
            self.assertFalse((repo / "filter-sentinel").exists())

    def test_named_driver_without_commands_does_not_need_external_conversion(self):
        with git_fixture("normal", self.root) as repo:
            (repo / ".gitattributes").write_text("README.md filter=unused\n", encoding="utf-8")
            (repo / "README.md").write_text("No conversion command exists.\n", encoding="utf-8")
            before = snapshot_repository(repo)
            self.assertEqual(self.attributes(repo, ["README.md"]),
                             [("README.md", "filter", "unused")])
            for operation in ("clean", "process"):
                result = _git([*SAFE, "config", "--null", "--get", f"filter.unused.{operation}"],
                              cwd=repo, check=False)
                self.assertEqual(result.returncode, 1)
            self.assertIn("+No conversion command exists.", self.safe_diff(repo, "README.md"))
            self.assertEqual(before, snapshot_repository(repo))

    def test_empty_local_command_overrides_inherited_executable_definition(self):
        with git_fixture("normal", self.root) as repo:
            config = self.root / ".fixture-global-config"
            config.write_text('[filter "fixture"]\n    process = echo filter-ran > filter-sentinel\n',
                              encoding="utf-8")
            _git(["config", "--local", "filter.fixture.process", ""], cwd=repo)
            (repo / ".gitattributes").write_text("README.md filter=fixture\n", encoding="utf-8")
            (repo / "README.md").write_text("Winning command is empty.\n", encoding="utf-8")
            before = snapshot_repository(repo)
            process = _git([*SAFE, "config", "--null", "--get", "filter.fixture.process"],
                           cwd=repo, env={"GIT_CONFIG_GLOBAL": str(config)})
            self.assertEqual(process.stdout, "\0")
            self.assertIn("+Winning command is empty.", self.safe_diff(repo, "README.md"))
            self.assertFalse((repo / "filter-sentinel").exists())
            self.assertEqual(before, snapshot_repository(repo))

    def test_nested_attributes_override_parent_rule_for_exact_literal_path(self):
        with git_fixture("normal", self.root) as repo:
            (repo / "docs").mkdir()
            (repo / "docs/[draft].txt").write_text("Base nested text.\n", encoding="utf-8")
            _git(["add", "--", "docs/[draft].txt"], cwd=repo)
            _git(["commit", "-m", "fixture: nested text"], cwd=repo)
            (repo / ".gitattributes").write_text("*.txt filter=fixture\n", encoding="utf-8")
            (repo / "docs/.gitattributes").write_text("*.txt -filter\n", encoding="utf-8")
            self.configure_sentinel(repo)
            (repo / "docs/[draft].txt").write_text("Nested override selected.\n", encoding="utf-8")
            before = snapshot_repository(repo)
            self.assertEqual(self.attributes(repo, ["docs/[draft].txt"]),
                             [("docs/[draft].txt", "filter", "unset")])
            self.assertIn("+Nested override selected.", self.safe_diff(repo, "docs/[draft].txt"))
            self.assertFalse((repo / "filter-sentinel").exists())
            self.assertEqual(before, snapshot_repository(repo))

    def test_reserved_attribute_output_can_name_an_executable_driver(self):
        for word, boolean_rule in (("unset", "-filter"), ("unspecified", "!filter")):
            with self.subTest(driver=word), git_fixture("normal", self.root, dirname=word) as repo:
                _git(["config", "--local", "core.autocrlf", "false"], cwd=repo)
                _git(["config", "--local", f"filter.{word}.clean",
                      "echo filter-ran > filter-sentinel; cat"], cwd=repo)
                attribute_file = repo / ".gitattributes"
                attribute_file.write_text(f"README.md {boolean_rule}\n", encoding="utf-8")
                boolean_result = self.attributes(repo, ["README.md"])
                attribute_file.write_text(f"README.md filter={word}\n", encoding="utf-8")
                before = snapshot_repository(repo)
                driver_result = self.attributes(repo, ["README.md"])
                self.assertEqual(boolean_result, [("README.md", "filter", word)])
                self.assertEqual(driver_result, boolean_result)
                command = _git([*SAFE, "config", "--null", "--get", f"filter.{word}.clean"],
                               cwd=repo)
                self.assertEqual(command.stdout, "echo filter-ran > filter-sentinel; cat\0")
                # Ambiguous output plus a same-named command cannot permit a worktree diff.
                self.assertFalse((repo / "filter-sentinel").exists())
                self.assertEqual(before, snapshot_repository(repo))
                # Positive control: deliberately run only this inspected fixture helper.
                # It proves the colliding word can execute a real clean driver; no LFS runs.
                result = _git([*SAFE, "hash-object", "--path=README.md", "README.md"], cwd=repo)
                expected_oid = _git(["rev-parse", "HEAD:README.md"], cwd=repo).stdout
                self.assertEqual(result.stdout, expected_oid)
                self.assertEqual((repo / "filter-sentinel").read_text(encoding="utf-8"),
                                 "filter-ran\n")
