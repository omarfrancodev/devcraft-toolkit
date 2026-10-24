"""Fixtures establish selection/freshness facts; assistant grouping is evaluated separately."""
import hashlib
import tempfile
import unittest
from pathlib import Path

from tests.support.git_fixtures import _git, git_fixture, snapshot_repository
from tests.skills.git_analyze_changes.integration.test_inspection_recipes import SAFE


class PlanningFixtureTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[3] / ".tmp"
        root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=root)
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def git(self, repo, *args):
        return _git([*SAFE, *args], cwd=repo).stdout

    def test_staged_selection_retains_implementation_tests_and_docs_without_debug(self):
        with git_fixture("normal", self.root) as repo:
            (repo / "README.md").write_text("Use precise decimal totals.\n", encoding="utf-8")
            (repo / "total.py").write_text("from decimal import Decimal\n", encoding="utf-8")
            (repo / "test_total.py").write_text("assert str(Decimal('1.00')) == '1.00'\n", encoding="utf-8")
            _git(["add", "--", "README.md", "total.py", "test_total.py"], cwd=repo)
            (repo / "total.py").write_text("from decimal import Decimal\nprint('debug')\n", encoding="utf-8")
            (repo / "notes.txt").write_text("Unknown intent\n", encoding="utf-8")
            before = snapshot_repository(repo)
            staged = self.git(repo, "diff", "--cached", "--name-only", "-z", "--no-ext-diff", "--no-textconv")
            self.assertEqual({"README.md", "total.py", "test_total.py"}, set(staged.rstrip("\0").split("\0")))
            staged_blob = self.git(repo, "show", ":total.py")
            self.assertNotIn("debug", staged_blob)
            self.assertIn("debug", (repo / "total.py").read_text(encoding="utf-8"))
            self.assertNotIn("notes.txt", staged)
            self.assertEqual(before, snapshot_repository(repo))

    def test_empty_staged_selection_does_not_imply_clean_worktree(self):
        with git_fixture("dirty", self.root) as repo:
            (repo / "untracked.txt").write_text("Untracked\n", encoding="utf-8")
            before = snapshot_repository(repo)
            staged = self.git(repo, "diff", "--cached", "--name-only", "-z", "--no-ext-diff", "--no-textconv")
            status = self.git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignore-submodules=all")
            self.assertEqual("", staged)
            self.assertIn(" M README.md\0", status)
            self.assertIn("?? untracked.txt\0", status)
            self.assertEqual(before, snapshot_repository(repo))

    def test_captured_index_guard_invalidates_after_new_staged_selection(self):
        with git_fixture("staged", self.root) as repo:
            index_text = self.git(repo, "rev-parse", "--git-path", "index").strip()
            index = Path(index_text)
            if not index.is_absolute():
                index = repo / index
            captured = hashlib.sha256(index.read_bytes()).hexdigest()
            (repo / "staged.txt").write_text("Different selected contents\n", encoding="utf-8")
            _git(["add", "--", "staged.txt"], cwd=repo)
            self.assertNotEqual(captured, hashlib.sha256(index.read_bytes()).hexdigest())
            self.assertEqual("Different selected contents\n", self.git(repo, "show", ":staged.txt"))

    def test_captured_worktree_guard_invalidates_without_changing_selected_index(self):
        with git_fixture("staged", self.root) as repo:
            before = snapshot_repository(repo)
            path = repo / "README.md"
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            path.write_text("Independent later edit\n", encoding="utf-8")
            after = snapshot_repository(repo)
            self.assertEqual(before["index"], after["index"])
            self.assertEqual(before["HEAD"], after["HEAD"])
            self.assertNotEqual(digest, hashlib.sha256(path.read_bytes()).hexdigest())

