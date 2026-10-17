import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from tests.support.git_fixtures import git_fixture, snapshot_repository


class GitPreflightFixtureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[4])
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def git(self, repo, *args, check=True):
        return subprocess.run(["git", *args], cwd=repo, check=check, capture_output=True, text=True).stdout.rstrip()

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
            result = subprocess.run(["git", "config", "--get", "user.name"], cwd=repo, capture_output=True, text=True)
            self.assertNotEqual(0, result.returncode)
            self.assertEqual("", result.stdout.strip())

    def test_global_identity_origin_is_observable_without_changing_repository(self):
        with git_fixture("missing-identity", self.root) as repo:
            before = snapshot_repository(repo)
            global_config = Path(os.environ["GIT_CONFIG_GLOBAL"])
            global_config.write_text("[user]\n\tname = Fixture Global\n\temail = global@example.invalid\n", encoding="utf-8")
            name_origin = self.git(repo, "config", "--show-origin", "--get", "user.name")
            email_origin = self.git(repo, "config", "--show-origin", "--get", "user.email")
            self.assertIn("Fixture Global", name_origin)
            self.assertIn("global@example.invalid", email_origin)
            self.assertIn(global_config.name, name_origin)
            self.assertEqual(before, snapshot_repository(repo))

    def test_read_only_preflight_queries_preserve_all_fixture_states(self):
        for kind in ("normal", "unborn", "dirty", "staged", "conflicted", "detached", "missing-identity"):
            with self.subTest(kind=kind), git_fixture(kind, self.root, dirname=kind) as repo:
                before = snapshot_repository(repo)
                self.git(repo, "status", "--short", "--branch")
                self.git(repo, "rev-parse", "--verify", "HEAD", check=False)
                self.git(repo, "config", "--show-origin", "--get", "user.name", check=False)
                self.assertEqual(before, snapshot_repository(repo))


if __name__ == "__main__":
    unittest.main()
