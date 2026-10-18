import os
import tempfile
import unittest
from pathlib import Path

from tests.support.git_fixtures import _git, git_fixture, snapshot_repository


class GitPreflightFixtureTests(unittest.TestCase):
    def setUp(self):
        temp_root = Path(__file__).resolve().parents[4] / "tests" / ".tmp"
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_root)
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def git(self, repo, *args, check=True):
        return _git(list(args), cwd=Path(repo), check=check).stdout.rstrip()

    def test_staged_fixture_keeps_index_selection(self):
        with git_fixture("staged", self.root) as repo:
            self.assertIn("A  staged.txt", self.git(repo, "status", "--short"))
            snapshot = snapshot_repository(repo)
            self.assertIn("working:staged.txt", snapshot)

    def test_dirty_fixture_has_unstaged_tracked_change(self):
        with git_fixture("dirty", self.root) as repo:
            self.assertIn(" M README.md", self.git(repo, "status", "--short"))

    def test_conflicted_fixture_has_unmerged_index(self):
        with git_fixture("conflicted", self.root) as repo:
            status = self.git(repo, "status", "--short")
            self.assertTrue(status.startswith("UU README.md"), status)
            self.assertIn("<<<<<<<", (repo / "README.md").read_text(encoding="utf-8"))

    def test_missing_identity_fixture_hides_inherited_global_identity(self):
        with git_fixture("missing-identity", self.root) as repo:
            result = _git(["config", "--get", "user.name"], cwd=repo, check=False)
            self.assertNotEqual(0, result.returncode)
            self.assertEqual("", result.stdout.strip())

    def test_fixture_does_not_mutate_process_git_environment(self):
        git_keys = (
            "GIT_CONFIG_GLOBAL", "GIT_CONFIG_NOSYSTEM", "GIT_AUTHOR_NAME", "GIT_AUTHOR_EMAIL",
            "GIT_COMMITTER_NAME", "GIT_COMMITTER_EMAIL",
        )
        before = {key: os.environ.get(key) for key in git_keys}
        with git_fixture("normal", self.root):
            self.assertEqual(before, {key: os.environ.get(key) for key in git_keys})

    def test_global_identity_origin_is_observable_without_changing_repository(self):
        with git_fixture("missing-identity", self.root) as repo:
            before = snapshot_repository(repo)
            global_config = self.root / ".fixture-global-config"
            global_config.write_text("[user]\n\tname = Fixture Global\n\temail = global@example.invalid\n", encoding="utf-8")
            global_config_before_queries = global_config.read_bytes()
            name_origin = self.git(repo, "config", "--show-origin", "--get", "user.name")
            email_origin = self.git(repo, "config", "--show-origin", "--get", "user.email")
            self.assertIn("Fixture Global", name_origin)
            self.assertIn("global@example.invalid", email_origin)
            self.assertIn(global_config.name, name_origin)
            self.assertEqual(before, snapshot_repository(repo))
            self.assertEqual(global_config_before_queries, global_config.read_bytes())

    def test_read_only_preflight_queries_preserve_all_fixture_states(self):
        for kind in ("normal", "unborn", "dirty", "staged", "conflicted", "detached", "missing-identity"):
            with self.subTest(kind=kind), git_fixture(kind, self.root, dirname=kind) as repo:
                before = snapshot_repository(repo)
                self.git(repo, "--no-optional-locks", "status", "--short", "--branch")
                self.git(repo, "rev-parse", "--verify", "HEAD", check=False)
                self.git(repo, "config", "--show-origin", "--get", "user.name", check=False)
                self.assertEqual(before, snapshot_repository(repo))

    def test_no_optional_locks_prevents_status_index_refresh(self):
        with git_fixture("normal", self.root, dirname="default-locks") as default_repo:
            with git_fixture("normal", self.root, dirname="no-optional-locks") as safe_repo:
                default_readme = default_repo / "README.md"
                safe_readme = safe_repo / "README.md"
                for readme in (default_readme, safe_readme):
                    current = readme.stat()
                    os.utime(readme, ns=(current.st_atime_ns, current.st_mtime_ns + 5_000_000_000))

                default_index = Path(self.git(default_repo, "rev-parse", "--git-path", "index"))
                default_index = default_index if default_index.is_absolute() else default_repo / default_index
                default_before = default_index.read_bytes()
                self.git(default_repo, "status", "--short", "--branch")
                self.assertNotEqual(default_before, default_index.read_bytes(), "control status should refresh stale index metadata")

                safe_index = Path(self.git(safe_repo, "rev-parse", "--git-path", "index"))
                safe_index = safe_index if safe_index.is_absolute() else safe_repo / safe_index
                safe_before = safe_index.read_bytes()
                self.git(safe_repo, "--no-optional-locks", "status", "--short", "--branch")
                self.assertEqual(safe_before, safe_index.read_bytes())


if __name__ == "__main__":
    unittest.main()
