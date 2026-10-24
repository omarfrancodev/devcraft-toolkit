"""Git index recipe controls; no runtime skill implementation."""
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from tests.support.git_fixtures import git_fixture, snapshot_repository

SAFE = ["--no-pager", "--no-optional-locks", "--no-lazy-fetch",
        "-c", "core.fsmonitor=false", "-c", "core.untrackedCache=false",
        "-c", "core.splitIndex=false", "-c", "submodule.recurse=false"]
PATCH = "--- a/README.md\n+++ b/README.md\n@@ -1 +1,2 @@\n Fixture repository.\n+Rounding correction.\n"


class IndexOperationTests(unittest.TestCase):
    def setUp(self):
        parent = Path(__file__).resolve().parents[3] / ".tmp"
        parent.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=parent)
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def git(self, repo, *args, data=None, check=True, raw=False):
        env = {k:v for k,v in os.environ.items() if not k.upper().startswith("GIT_")}
        env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=str(self.root/".fixture-global-config"))
        payload = data.encode("utf-8") if isinstance(data, str) else data
        result = subprocess.run(["git", *SAFE, *args], cwd=repo, env=env, input=payload,
                                capture_output=True, check=check)
        if not raw:
            result.stdout = result.stdout.decode("utf-8").replace("\r\n", "\n")
            result.stderr = result.stderr.decode("utf-8").replace("\r\n", "\n")
        return result

    def manifest(self, repo):
        return self.git(repo, "ls-files", "--stage", "-z").stdout

    def assert_index_only(self, before, after):
        for key in set(before) | set(after):
            if key == "git-mode:common/index" and key not in before:
                # An unborn repository may create its first index and mode.
                self.assertIn(key, after)
                continue
            if key not in {"index", "git:common/index"}:
                self.assertEqual(before.get(key), after.get(key), key)

    def test_cached_patch_stages_only_selected_hunk(self):
        with git_fixture("normal", self.root) as repo:
            # Establish an exact LF index baseline before the selected operation.
            (repo/"README.md").write_bytes(b"Fixture repository.\n")
            self.git(repo, "add", "--", "README.md")
            self.git(repo, "config", "--local", "--unset", "user.name")
            self.git(repo, "config", "--local", "--unset", "user.email")
            (repo/"keep.txt").write_text("Preserve this selection.\n", encoding="utf-8")
            self.git(repo, "add", "--", "keep.txt")
            keep = self.git(repo, "rev-parse", ":keep.txt").stdout
            (repo/"README.md").write_bytes(b"Fixture repository.\nRounding correction.\nDebug output.\n")
            base_bytes = self.git(repo, "show", ":README.md", raw=True).stdout
            before = snapshot_repository(repo)
            checked = self.git(repo, "apply", "--cached", "--check", "--whitespace=nowarn", "-", data=PATCH)
            self.assertEqual(0, checked.returncode)
            self.assertEqual(before, snapshot_repository(repo))
            self.git(repo, "apply", "--cached", "--whitespace=nowarn", "-", data=PATCH)
            self.assertEqual("Fixture repository.\nRounding correction.\n", self.git(repo, "show", ":README.md").stdout)
            self.assertEqual(base_bytes+b"Rounding correction.\n", self.git(repo, "show", ":README.md", raw=True).stdout)
            self.assertEqual(keep, self.git(repo, "rev-parse", ":keep.txt").stdout)
            self.assertNotIn("Debug output.", self.git(repo, "diff", "--cached", "--no-ext-diff", "--no-textconv").stdout)
            self.assert_index_only(before, snapshot_repository(repo))

    def test_stale_patch_check_writes_nothing(self):
        with git_fixture("normal", self.root) as repo:
            (repo/"README.md").write_text("Concurrent staged content.\n", encoding="utf-8")
            self.git(repo, "add", "--", "README.md")
            before = snapshot_repository(repo)
            result = self.git(repo, "apply", "--cached", "--check", "-", data=PATCH, check=False)
            self.assertNotEqual(0, result.returncode)
            self.assertEqual(before, snapshot_repository(repo))

    def test_literal_paths_deletion_and_unborn_stage(self):
        for kind in ("normal", "unborn"):
            with self.subTest(kind=kind), git_fixture(kind, self.root, dirname=kind) as repo:
                if kind=="normal":
                    (repo/"README.md").unlink()
                for name in ("[draft].txt", "$(noop).txt"):
                    (repo/name).write_text("Literal data.\n", encoding="utf-8")
                before = snapshot_repository(repo)
                names = ["[draft].txt", "$(noop).txt"] + (["README.md"] if kind=="normal" else [])
                self.git(repo, "--literal-pathspecs", "add", "--pathspec-from-file=-", "--pathspec-file-nul",
                         data="\0".join(names)+"\0")
                inventory = self.manifest(repo)
                self.assertIn("\t[draft].txt\0", inventory)
                self.assertIn("\t$(noop).txt\0", inventory)
                if kind=="normal":
                    self.assertNotIn("\tREADME.md\0", inventory)
                self.assert_index_only(before, snapshot_repository(repo))

    def test_authorized_reverse_patch_defers_only_selected_index_hunk(self):
        with git_fixture("normal", self.root) as repo:
            (repo/"README.md").write_bytes(b"Fixture repository.\nRounding correction.\nDebug output.\n")
            (repo/"keep.txt").write_text("Keep staged.\n", encoding="utf-8")
            self.git(repo, "add", "--", "README.md", "keep.txt")
            keep = self.git(repo, "rev-parse", ":keep.txt").stdout
            reverse = "--- a/README.md\n+++ b/README.md\n@@ -1,2 +1,3 @@\n Fixture repository.\n Rounding correction.\n+Debug output.\n"
            before = snapshot_repository(repo)
            self.git(repo, "apply", "--cached", "--reverse", "--check", "-", data=reverse)
            self.git(repo, "apply", "--cached", "--reverse", "-", data=reverse)
            self.assertEqual("Fixture repository.\nRounding correction.\n", self.git(repo, "show", ":README.md").stdout)
            self.assertEqual(keep, self.git(repo, "rev-parse", ":keep.txt").stdout)
            self.assert_index_only(before, snapshot_repository(repo))

    def test_index_write_hook_can_mutate_excluded_worktree(self):
        # Characterize the omitted effect: both recipes can run an index hook.
        for recipe in ("add", "cached"):
            for custom in (False, True):
                name = f"hook-{recipe}-{custom}"
                with self.subTest(recipe=recipe, custom=custom), git_fixture("normal", self.root, dirname=name) as repo:
                    target = b"Fixture repository.\nSelected correction.\n"
                    (repo/"README.md").write_bytes(target)
                    protected = repo/"protected.txt"
                    protected.write_bytes(b"Excluded original.\n")
                    hooks = repo/"custom-hooks" if custom else repo/".git"/"hooks"
                    hooks.mkdir(exist_ok=True)
                    hook = hooks/"post-index-change"
                    hook.write_bytes(b"#!/bin/sh\nprintf '%s\\n' 'Unexpected rewrite.' > protected.txt\n")
                    hook.chmod(0o755)
                    if custom:
                        self.git(repo, "config", "--local", "core.hooksPath", "custom-hooks")
                    before_index = self.manifest(repo)
                    before_head = self.git(repo, "rev-parse", "HEAD").stdout
                    if recipe == "cached":
                        patch = self.git(repo, "diff", "--no-ext-diff", "--no-textconv", "--", "README.md", raw=True).stdout
                        self.git(repo, "apply", "--cached", "--check", "--whitespace=nowarn", "-", data=patch)
                        self.assertEqual(b"Excluded original.\n", protected.read_bytes())
                        self.git(repo, "apply", "--cached", "--whitespace=nowarn", "-", data=patch)
                    else:
                        self.git(repo, "--literal-pathspecs", "add", "--", "README.md")
                    self.assertEqual(target, self.git(repo, "show", ":README.md", raw=True).stdout)
                    self.assertNotEqual(before_index, self.manifest(repo))
                    self.assertEqual(before_head, self.git(repo, "rev-parse", "HEAD").stdout)
                    self.assertEqual(b"Unexpected rewrite.\n", protected.read_bytes())
