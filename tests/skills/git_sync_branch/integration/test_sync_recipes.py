"""Real fetch/fast-forward controls, not model or native-loader tests."""
from pathlib import Path
import tempfile
import unittest
from tests.support.git_fixtures import snapshot_repository
from tests.support.remote_git_fixtures import remote_fixture,git,head,refs,commit,fetch_selected,fast_forward,working,hook

class SyncRecipeTests(unittest.TestCase):
    def setUp(self):
        parent=Path(__file__).resolve().parents[3]/".tmp";parent.mkdir(parents=True,exist_ok=True)
        self.temp=tempfile.TemporaryDirectory(dir=parent);self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)

    def test_exact_fetch_ignores_tags_prune_and_extra_refmaps(self):
        with remote_fixture(self.root) as f:
            old=head(f.local);new=commit(f.seed,"remote advance")
            git(f.seed,"tag","remote-tag");git(f.seed,"push","--","origin","main","refs/tags/remote-tag")
            git(f.local,"tag","local-tag");git(f.local,"update-ref","refs/remotes/origin/stale",old)
            git(f.local,"branch","keep")
            git(f.local,"config","--add","remote.origin.fetch","+refs/tags/*:refs/tags/*")
            for key,value in (("fetch.prune","true"),("fetch.pruneTags","true"),("remote.origin.tagOpt","--tags"),("fetch.writeCommitGraph","true")):
                git(f.local,"config","--local",key,value)
            marker=f.local/".git/FETCH_HEAD";marker.write_bytes(b"preserved fetch head\n")
            before=snapshot_repository(f.local);prior=refs(f.local)
            result=fetch_selected(f)
            self.assertEqual(0,result.returncode,result.stderr)
            expected=dict(prior);expected["refs/remotes/origin/main"]=new
            self.assertEqual(expected,refs(f.local));self.assertEqual(old,head(f.local))
            after=snapshot_repository(f.local)
            self.assertEqual(before["index"],after["index"]);self.assertEqual(working(before),working(after))
            self.assertEqual(before["git:common/config"],after["git:common/config"])
            self.assertEqual(b"preserved fetch head\n",marker.read_bytes())
            self.assertFalse((f.local/".git/objects/info/commit-graph").exists())

    def test_fast_forward_moves_only_current_branch(self):
        with remote_fixture(self.root) as f:
            old=head(f.local);new=commit(f.seed,"remote advance");git(f.seed,"push","--","origin","main")
            git(f.local,"branch","keep");before_config=(f.local/".git/config").read_bytes()
            self.assertEqual(0,fetch_selected(f).returncode)
            self.assertEqual(0,git(f.local,"merge-base","--is-ancestor",old,new).returncode)
            result=fast_forward(f.local,new)
            self.assertEqual(0,result.returncode,result.stderr)
            self.assertEqual(new,head(f.local));self.assertEqual(old,head(f.local,"refs/heads/keep"))
            self.assertEqual(new,head(f.local,"refs/remotes/origin/main"))
            self.assertEqual(old,head(f.local,"ORIG_HEAD"));self.assertEqual(b"",git(f.local,"status","--porcelain").stdout)
            self.assertEqual(before_config,(f.local/".git/config").read_bytes())

    def test_equal_ahead_and_diverged_are_not_reset(self):
        with remote_fixture(self.root) as f:
            self.assertEqual(0,fetch_selected(f).returncode)
            self.assertEqual(head(f.local),head(f.local,"refs/remotes/origin/main"))
            local=commit(f.local,"local work");remote=head(f.seed)
            self.assertEqual(0,git(f.local,"merge-base","--is-ancestor",remote,local).returncode)
            new=commit(f.seed,"independent remote work");git(f.seed,"push","--","origin","main")
            self.assertEqual(0,fetch_selected(f).returncode)
            self.assertEqual(1,git(f.local,"merge-base","--is-ancestor",local,new,check=False).returncode)
            self.assertEqual(1,git(f.local,"merge-base","--is-ancestor",new,local,check=False).returncode)
            self.assertEqual(local,head(f.local));self.assertEqual(new,head(f.local,"refs/remotes/origin/main"))

    def test_unrelated_and_missing_history_do_not_fast_forward(self):
        with remote_fixture(self.root) as f:
            original=head(f.local)
            git(f.seed,"switch","--orphan","unrelated");new=commit(f.seed,"unrelated history")
            git(f.seed,"push","--","origin","HEAD:refs/heads/unrelated")
            self.assertEqual(0,fetch_selected(f,"unrelated").returncode)
            self.assertEqual(1,git(f.local,"merge-base","--is-ancestor",original,new,check=False).returncode)
            rejected=fast_forward(f.local,new)
            self.assertNotEqual(0,rejected.returncode);self.assertEqual(original,head(f.local))
            (f.local/".git/shallow").write_text(original+"\n",encoding="ascii")
            self.assertEqual(b"true\n",git(f.local,"rev-parse","--is-shallow-repository").stdout)
            self.assertEqual(original,head(f.local))

    def test_dirty_conflicted_unborn_detached_write_gates(self):
        with remote_fixture(self.root) as f:
            (f.local/"dirty.txt").write_text("excluded\n",encoding="utf-8")
            self.assertIn(b"?? dirty.txt",git(f.local,"status","--porcelain").stdout)
            before=snapshot_repository(f.local)
            git(f.local,"rev-parse","--verify","HEAD")
            self.assertEqual(before,snapshot_repository(f.local))
            git(f.local,"checkout","--detach","HEAD")
            self.assertEqual(1,git(f.local,"symbolic-ref","-q","HEAD",check=False).returncode)
            empty=f.root/"unborn";git(f.root,"init","--initial-branch=main",str(empty))
            self.assertNotEqual(0,git(empty,"rev-parse","--verify","HEAD",check=False).returncode)
            # Active merge state is data to block, never an invitation to finish it.
            git(f.local,"switch","main")
            (f.local/".git/MERGE_HEAD").write_text(head(f.local)+"\n",encoding="ascii")
            self.assertTrue((f.local/".git/MERGE_HEAD").is_file())

    def test_reference_and_index_hooks_execute_in_real_recipes(self):
        with remote_fixture(self.root) as f:
            new=commit(f.seed,"advance for hooks");git(f.seed,"push","--","origin","main")
            ref_hook=hook(f.local,"reference-transaction","echo ref >> reference-events")
            r=fetch_selected(f);self.assertEqual(0,r.returncode,r.stderr)
            self.assertTrue((f.local/"reference-events").exists())
            ref_hook.unlink()
            hook(f.local,"post-index-change","echo index >> index-events")
            hook(f.local,"post-merge","echo merge >> merge-events")
            r=fast_forward(f.local,new);self.assertEqual(0,r.returncode,r.stderr)
            self.assertTrue((f.local/"index-events").exists());self.assertTrue((f.local/"merge-events").exists())
            # Raw controls show why unapproved effects must be gated beforehand.

    def test_ref_and_endpoint_movement_invalidate_snapshot(self):
        with remote_fixture(self.root) as f:
            before=head(f.local);endpoint=git(f.local,"remote","get-url","--all","origin").stdout
            after=commit(f.local,"concurrent local work")
            self.assertNotEqual(before,after)
            git(f.local,"remote","set-url","origin",str(f.root/"different.git"))
            self.assertNotEqual(endpoint,git(f.local,"remote","get-url","--all","origin").stdout)

    def test_literal_remote_paths_and_refs(self):
        with remote_fixture(self.root/"unicode space") as f:
            branch="feature/$(literal);name"
            self.assertEqual(0,git(f.seed,"check-ref-format","refs/heads/"+branch).returncode)
            git(f.seed,"branch",branch);git(f.seed,"push","--","origin",f"refs/heads/{branch}:refs/heads/{branch}")
            self.assertEqual(0,fetch_selected(f,branch).returncode)
            self.assertEqual(head(f.seed),head(f.local,"refs/remotes/origin/"+branch))
            self.assertFalse((f.root/"literal").exists())

    def test_fast_forward_preserves_ignored_file_collision(self):
        with remote_fixture(self.root) as f:
            local=f.local/"local.env";local.write_bytes(b"private local content\n")
            (f.local/".git/info/exclude").write_text("local.env\n",encoding="utf-8")
            target=commit(f.seed,"incoming tracked environment","local.env")
            git(f.seed,"push","--","origin","main")
            self.assertEqual(0,fetch_selected(f).returncode)
            before=snapshot_repository(f.local);old=head(f.local)
            self.assertEqual(b"",git(f.local,"status","--porcelain").stdout)
            result=fast_forward(f.local,target)
            self.assertNotEqual(0,result.returncode)
            after=snapshot_repository(f.local)
            self.assertEqual(b"private local content\n",local.read_bytes())
            self.assertEqual(old,head(f.local));self.assertEqual(before["index"],after["index"])
            self.assertEqual(working(before),working(after))
            self.assertEqual(target,head(f.local,"refs/remotes/origin/main"))

    def test_symbolic_fetch_destination_stops_before_unrelated_branch_write(self):
        with remote_fixture(self.root) as f:
            old=head(f.local);git(f.local,"branch","keep")
            git(f.local,"symbolic-ref","refs/remotes/origin/main","refs/heads/keep")
            target=commit(f.seed,"remote update");git(f.seed,"push","--","origin","main")
            before=snapshot_repository(f.local)
            result=fetch_selected(f)
            self.assertNotEqual(0,result.returncode)
            self.assertEqual(old,head(f.local,"refs/heads/keep"))
            self.assertEqual(before,snapshot_repository(f.local))
            self.assertEqual(target,head(f.remote,"refs/heads/main"))
