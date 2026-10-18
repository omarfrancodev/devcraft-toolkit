import tempfile
import unittest
from pathlib import Path

from tests.support.git_fixtures import _git, git_fixture, snapshot_repository


class RepositoryContextFixtureTests(unittest.TestCase):
    def setUp(self):
        temp_root = Path(__file__).resolve().parents[4] / "tests" / ".tmp"
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_root)
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def git(self, repo, *args):
        return _git(list(args), cwd=Path(repo)).stdout.strip()

    def test_normal_fixture_supports_spaces_and_unicode(self):
        with git_fixture("normal", self.root, dirname="repo con espacio ü") as repo:
            self.assertEqual("repo con espacio ü", repo.name)
            self.assertEqual("true", self.git(repo, "rev-parse", "--is-inside-work-tree"))
            self.assertEqual("Fixture User", self.git(repo, "config", "--local", "user.name"))
            self.assertTrue((repo / "README.md").is_file())

    def test_unborn_fixture_has_main_branch_and_untracked_readme(self):
        with git_fixture("unborn", self.root) as repo:
            self.assertEqual("main", self.git(repo, "symbolic-ref", "--short", "HEAD"))
            self.assertIn("?? README.md", self.git(repo, "status", "--short"))
            self.assertNotEqual(0, _git(["rev-parse", "--verify", "HEAD"], cwd=repo, check=False).returncode)

    def test_linked_worktree_has_separate_git_and_common_directories(self):
        with git_fixture("linked-worktree", self.root) as repo:
            git_dir = Path(self.git(repo, "rev-parse", "--git-dir"))
            common_dir = Path(self.git(repo, "rev-parse", "--git-common-dir"))
            self.assertNotEqual(git_dir.resolve(), common_dir.resolve())

    def test_unicode_linked_worktree_paths_and_index_are_snapshotted(self):
        with git_fixture("linked-worktree", self.root, dirname="linked 中文") as repo:
            top_level = self.git(repo, "rev-parse", "--show-toplevel")
            self.assertTrue(top_level)
            snapshot = snapshot_repository(repo)
            self.assertNotEqual("<missing>", snapshot["index"])
            self.assertIn("working:README.md", snapshot)

    def test_detached_fixture_has_head_without_branch(self):
        with git_fixture("detached", self.root) as repo:
            self.assertEqual("", self.git(repo, "branch", "--show-current"))
            self.assertTrue(self.git(repo, "rev-parse", "--verify", "HEAD"))

    def test_snapshot_captures_refs_head_index_and_working_files(self):
        with git_fixture("normal", self.root) as repo:
            snapshot = snapshot_repository(repo)
            self.assertIn("refs", snapshot)
            self.assertIn("HEAD", snapshot)
            self.assertIn("index", snapshot)
            self.assertIn("working:README.md", snapshot)
            self.assertIn("working-mode:README.md", snapshot)

            pseudo_ref = repo / ".git" / "ORIG_HEAD"
            pseudo_ref.write_text("fixture pseudo-ref\n", encoding="utf-8")
            after_pseudo_ref = snapshot_repository(repo)
            self.assertNotIn("git:common/ORIG_HEAD", snapshot)
            self.assertIn("git:common/ORIG_HEAD", after_pseudo_ref)

    def test_snapshot_detects_symbolic_head_change_at_same_commit(self):
        with git_fixture("normal", self.root) as repo:
            self.git(repo, "branch", "same-commit")
            before = snapshot_repository(repo)
            self.git(repo, "switch", "same-commit")
            after = snapshot_repository(repo)
            self.assertEqual(before["HEAD"], after["HEAD"])
            self.assertNotEqual(before["symbolic-HEAD"], after["symbolic-HEAD"])

    def test_read_only_context_queries_preserve_repository_snapshot(self):
        with git_fixture("normal", self.root, dirname="repo con espacio ü") as repo:
            before = snapshot_repository(repo)
            self.git(repo, "rev-parse", "--show-toplevel")
            self.git(repo, "rev-parse", "--git-dir")
            self.git(repo, "rev-parse", "--git-common-dir")
            self.git(repo, "rev-parse", "--show-superproject-working-tree")
            self.git(repo, "symbolic-ref", "--short", "-q", "HEAD")
            self.git(repo, "rev-parse", "--verify", "HEAD")
            self.git(repo, "--no-optional-locks", "status", "--short", "--branch")
            self.git(repo, "config", "--show-origin", "--get", "user.name")
            self.git(repo, "config", "--show-origin", "--get", "user.email")
            self.assertEqual(before, snapshot_repository(repo))

    def test_git_status_instructions_disable_optional_locks(self):
        repo_root = Path(__file__).resolve().parents[4]
        for relative in (
            "skills/git-working-directory-policy/SKILL.md",
            "skills/git-safety-check/SKILL.md",
        ):
            with self.subTest(skill=relative):
                instructions = (repo_root / relative).read_text(encoding="utf-8")
                self.assertIn("git --no-optional-locks status", instructions)


if __name__ == "__main__":
    unittest.main()
