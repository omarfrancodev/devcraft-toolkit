"""Primitive Git characterization; these do not execute installed instructions."""
import tempfile
import unittest
from pathlib import Path
from tests.support.git_fixtures import git_fixture
from tests.support.remote_git_fixtures import git, head, refs, hook, commit
from tests.support.work_branch_fixtures import branch_snapshot, create_branch

class BranchControls(unittest.TestCase):
    def setUp(self):
        root=Path(__file__).resolve().parents[3]/".tmp"; root.mkdir(parents=True,exist_ok=True)
        t=tempfile.TemporaryDirectory(dir=root); self.addCleanup(t.cleanup); self.root=Path(t.name)

    def test_dirty_partial_index_and_all_working_bytes_survive(self):
        with git_fixture("normal",self.root) as r:
            (r/"delete.txt").write_bytes(b"delete me"); (r/".gitignore").write_text(".env\n")
            git(r,"add","--","delete.txt",".gitignore"); git(r,"commit","-m","fixture: files")
            (r/"README.md").write_bytes(b"staged\n");git(r,"add","--","README.md")
            (r/"README.md").write_bytes(b"staged\nunstaged\n");(r/"delete.txt").unlink()
            (r/"diseÃ±o.txt").write_bytes(b"untracked\0bytes");(r/".env").write_bytes(b"ignored secret fixture")
            before=branch_snapshot(r); oid=head(r)
            result=create_branch(r,"feature/parser",oid)
            self.assertEqual(0,result.returncode,result.stderr);after=branch_snapshot(r)
            for key in ("index","files","config"):self.assertEqual(before[key],after[key],key)
            self.assertEqual(oid,head(r,"refs/heads/main"));self.assertEqual(oid,head(r,"refs/heads/feature/parser"))
            self.assertEqual(b"refs/heads/feature/parser\n",git(r,"symbolic-ref","HEAD").stdout)

    def test_literal_names_and_existing_refs_do_not_expand_or_reset(self):
        with git_fixture("normal",self.root) as r:
            original=head(r);git(r,"branch","feature/parser"); before=branch_snapshot(r)
            for name in ("feature/parser","bad..name","-bad","@{-1}"):
                # Canonical validation catches the expansion syntax BEFORE the branch primitive.
                if name=="@{-1}":
                    self.assertNotEqual(0,git(r,"check-ref-format","refs/heads/"+name,check=False).returncode)
                else:self.assertNotEqual(0,create_branch(r,name,original).returncode)
            self.assertEqual(before,branch_snapshot(r))
            git(r,"config","--local","branch.unused.remote","private")
            self.assertEqual(b"private\n",git(r,"config","--get","branch.unused.remote").stdout)
            self.assertNotIn("refs/heads/unused",refs(r))  # absence alone cannot exclude stale config

    def test_no_tracking_even_with_auto_setup_config(self):
        with git_fixture("normal",self.root) as r:
            git(r,"config","--local","branch.autoSetupMerge","always");git(r,"config","--local","branch.autoSetupRebase","always")
            before=branch_snapshot(r);self.assertEqual(0,create_branch(r,"feature/parser",head(r)).returncode)
            self.assertEqual(before["config"],branch_snapshot(r)["config"])
            self.assertEqual(1,git(r,"config","--get-regexp","^branch[.]feature/parser[.]",check=False).returncode)

    def test_detached_and_missing_identity_do_not_need_commits(self):
        for kind in ("detached","missing-identity"):
            with self.subTest(kind=kind),git_fixture(kind,self.root/kind) as r:
                oid=head(r);before=branch_snapshot(r);self.assertEqual(0,create_branch(r,"feature/parser",oid).returncode)
                self.assertEqual(oid,head(r));self.assertEqual(before["config"],branch_snapshot(r)["config"])

    def test_post_checkout_failure_can_leave_new_branch_selected(self):
        with git_fixture("normal",self.root) as r:
            hook(r,"post-checkout","exit 1");oid=head(r);before=branch_snapshot(r)
            result=create_branch(r,"feature/parser",oid)
            self.assertNotEqual(0,result.returncode);self.assertEqual(oid,head(r,"refs/heads/feature/parser"))
            self.assertEqual(b"refs/heads/feature/parser\n",git(r,"symbolic-ref","HEAD").stdout)
            for key in ("index","files","config"):self.assertEqual(before[key],branch_snapshot(r)[key])

    def test_linked_worktree_preserves_other_worktree(self):
        with git_fixture("linked-worktree",self.root) as r:
            source=self.root/"repo-source";before=branch_snapshot(source);oid=head(r)
            self.assertEqual(0,create_branch(r,"feature/parser",oid).returncode)
            after=branch_snapshot(source)
            for key in ("head","symbolic","index","files","config"):self.assertEqual(before[key],after[key],key)
            self.assertEqual(oid,head(r,"refs/heads/fixture-linked"))

    def test_pinned_operand_does_not_follow_source_movement(self):
        with git_fixture("normal",self.root) as r:
            pinned=head(r);advanced=commit(r,"advanced");self.assertNotEqual(pinned,advanced)
            result=create_branch(r,"feature/parser",pinned);self.assertEqual(0,result.returncode,result.stderr)
            self.assertEqual(pinned,head(r));self.assertEqual(advanced,head(r,"refs/heads/main"))
            # A client must stop on detected movement; pinning alone is not an atomic HEAD guard.

    def test_unborn_and_operation_markers_are_observable(self):
        with git_fixture("unborn",self.root/"unborn") as r:
            self.assertNotEqual(0,git(r,"rev-parse","--verify","HEAD",check=False).returncode)
            before=refs(r);self.assertNotEqual(0,create_branch(r,"feature/parser","0"*40).returncode);self.assertEqual(before,refs(r))
        with git_fixture("conflicted",self.root/"conflict") as r:
            self.assertTrue(git(r,"ls-files","--unmerged","-z").stdout)
            marker=Path(git(r,"rev-parse","--git-path","MERGE_HEAD").stdout.decode().strip())
            if not marker.is_absolute():marker=r/marker
            self.assertTrue(marker.is_file())  # policy stops before calling switch

    def test_reference_hook_effects_are_not_hidden(self):
        with git_fixture("normal",self.root) as r:
            hook(r,"reference-transaction","echo reference >> hook-effect")
            result=create_branch(r,"feature/parser",head(r));self.assertEqual(0,result.returncode,result.stderr)
            self.assertTrue((r/"hook-effect").is_file())  # effect requires approval; never bypass hook

    def test_submodule_work_is_not_recursed(self):
        with git_fixture("normal",self.root/"parent") as r,git_fixture("dirty",self.root/"child") as child:
            git(r,"-c","protocol.file.allow=always","submodule","add",str(child),"module")
            git(r,"commit","-m","fixture: submodule");module=r/"module"
            (r/".fixture-global-config").write_bytes((r.parent/".fixture-global-config").read_bytes())
            (module/"README.md").write_bytes(b"dirty submodule\n");before=branch_snapshot(module)
            self.assertEqual(0,create_branch(r,"feature/parser",head(r)).returncode)
            self.assertEqual(before,branch_snapshot(module))
