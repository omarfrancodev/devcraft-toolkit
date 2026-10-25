"""Real normal-push controls using local bare endpoints; no skill-loader claim."""
from pathlib import Path
import hashlib
import tempfile
import unittest
from tests.support.git_fixtures import snapshot_repository
from tests.support.remote_git_fixtures import remote_fixture,git,head,refs,commit,hook,advertise,push_pinned,working

class PublishRecipeTests(unittest.TestCase):
    def setUp(self):
        p=Path(__file__).resolve().parents[3]/".tmp";p.mkdir(parents=True,exist_ok=True)
        self.temp=tempfile.TemporaryDirectory(dir=p);self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)

    def assert_local_content_preserved(self,before,after):
        for key in ("HEAD","symbolic-HEAD","index","git:common/config"):
            self.assertEqual(before[key],after[key],key)
        self.assertEqual(working(before),working(after))

    def test_pinned_single_ref_overrides_matching_and_follow_tags(self):
        with remote_fixture(self.root) as f:
            old=head(f.local);git(f.seed,"branch","other");git(f.seed,"push","--","origin","other")
            selected=commit(f.local,"selected publication");git(f.local,"branch","other")
            git(f.local,"-c","tag.gpgSign=false","tag","-a","release-label","-m","fixture tag")
            for key,value in (("push.default","matching"),("remote.origin.push","refs/heads/*:refs/heads/*"),("push.followTags","true"),("push.recurseSubmodules","on-demand"),("push.autoSetupRemote","true")):
                git(f.local,"config","--local",key,value)
            before=snapshot_repository(f.local);prior=refs(f.remote)
            result=push_pinned(f,selected);self.assertEqual(0,result.returncode,result.stderr)
            expected=dict(prior);expected['refs/heads/main']=selected
            self.assertEqual(expected,refs(f.remote));self.assertEqual(old,head(f.remote,"refs/heads/other"))
            self.assertNotIn("refs/tags/release-label",refs(f.remote))
            self.assert_local_content_preserved(before,snapshot_repository(f.local))
            self.assertEqual(selected,head(f.local,"refs/remotes/origin/main"))

    def test_normal_push_rejects_non_fast_forward(self):
        with remote_fixture(self.root) as f:
            local=commit(f.local,"local work");remote=commit(f.seed,"remote work");git(f.seed,"push","--","origin","main")
            prior=refs(f.remote);before=snapshot_repository(f.local)
            result=push_pinned(f,local)
            self.assertNotEqual(0,result.returncode);self.assertEqual(prior,refs(f.remote))
            self.assertEqual(remote,head(f.remote,"refs/heads/main"));self.assert_local_content_preserved(before,snapshot_repository(f.local))

    def test_unknown_remote_oid_requires_fetch_decision(self):
        with remote_fixture(self.root) as f:
            remote=commit(f.seed,"unknown remote work");git(f.seed,"push","--","origin","main")
            before=snapshot_repository(f.local)
            advertised=advertise(f.local);self.assertEqual(0,advertised.returncode)
            self.assertEqual(remote,advertised.stdout.decode("ascii").split()[0])
            self.assertNotEqual(0,git(f.local,"cat-file","-e",remote+"^{commit}",check=False).returncode)
            self.assertEqual(before,snapshot_repository(f.local))

    def test_pushurl_and_rewrite_select_effective_endpoint(self):
        with remote_fixture(self.root) as f:
            other=f.root/"push.git";git(f.root,"init","--bare","--initial-branch=main",str(other))
            selected=commit(f.local,"push to different endpoint")
            git(f.local,"config","--local","remote.origin.pushurl","fixture-alias:push.git")
            git(f.local,"config","--local","url."+f.root.as_posix()+"/.insteadOf","fixture-alias:")
            fetched=git(f.local,"remote","get-url","--all","origin").stdout.decode("utf-8").strip()
            pushed=git(f.local,"remote","get-url","--push","--all","origin").stdout.decode("utf-8").strip()
            self.assertEqual(str(f.remote),fetched);self.assertEqual(other.as_posix(),pushed)
            # Publication observation must query the push endpoint, not fetch origin.
            self.assertEqual(2,advertise(f.local).returncode)
            old=refs(f.remote);r=push_pinned(f,selected)
            self.assertEqual(0,r.returncode,r.stderr);self.assertEqual(selected,head(other,"refs/heads/main"));self.assertEqual(old,refs(f.remote))
            self.assertEqual(selected,advertise(f.local).stdout.decode("ascii").split()[0])

    def test_multiple_endpoints_and_mirror_require_decision(self):
        with remote_fixture(self.root/"multiple") as f:
            git(f.local,"config","--add","remote.origin.pushurl",str(f.remote))
            git(f.local,"config","--add","remote.origin.pushurl",str(f.root/"other.git"))
            before=snapshot_repository(f.local)
            self.assertEqual(2,len(git(f.local,"remote","get-url","--push","--all","origin").stdout.splitlines()))
            self.assertEqual(before,snapshot_repository(f.local))
            # No raw multi-endpoint push is attempted.
        with remote_fixture(self.root/"mirror") as f:
            git(f.local,"config","--local","remote.origin.mirror","true")
            prior=refs(f.remote)
            self.assertEqual(b"true\n",git(f.local,"config","--bool","--get","remote.origin.mirror").stdout)
            r=push_pinned(f,head(f.local))
            self.assertNotEqual(0,r.returncode);self.assertEqual(prior,refs(f.remote))

    def test_pre_push_and_reference_hooks_are_not_bypassed(self):
        with remote_fixture(self.root) as f:
            selected=commit(f.local,"hook test");prior=refs(f.remote)
            pre=hook(f.local,"pre-push","echo pre > prepush-marker\nexit 1")
            r=push_pinned(f,selected)
            self.assertNotEqual(0,r.returncode);self.assertEqual(prior,refs(f.remote));self.assertTrue((f.local/"prepush-marker").exists())
            pre.unlink();(f.local/"prepush-marker").unlink()
            hook(f.local,"reference-transaction","echo ref >> ref-marker")
            r=push_pinned(f,selected);self.assertEqual(0,r.returncode,r.stderr)
            self.assertTrue((f.local/"ref-marker").exists());self.assertEqual(selected,head(f.remote,"refs/heads/main"))
            # Primitive controls show why known effects need approval before publication.

    def test_source_movement_does_not_publish_new_tip(self):
        with remote_fixture(self.root) as f:
            pinned=commit(f.local,"approved snapshot");new=commit(f.local,"new local work")
            before=snapshot_repository(f.local)
            self.assertNotEqual(pinned,new)
            r=push_pinned(f,pinned);self.assertEqual(0,r.returncode,r.stderr)
            self.assertEqual(pinned,head(f.remote,"refs/heads/main"));self.assertEqual(new,head(f.local))
            self.assert_local_content_preserved(before,snapshot_repository(f.local))
            # If movement is detected before the write, the skill must stop; this
            # raw control only proves a pinned operand cannot silently send new.

    def test_rejection_or_lost_ack_requires_actual_observation(self):
        with remote_fixture(self.root) as f:
            selected=commit(f.local,"verify actual remote")
            reject=hook(f.remote,"pre-receive","exit 1")
            before=head(f.remote,"refs/heads/main")
            r=push_pinned(f,selected);self.assertNotEqual(0,r.returncode)
            self.assertEqual(before,advertise(f.local).stdout.decode("ascii").split()[0])
            reject.unlink()
            push_pinned(f,selected)  # Deliberately discard the acknowledgment.
            observed=advertise(f.local)
            self.assertEqual(0,observed.returncode)
            self.assertEqual(selected,observed.stdout.decode("ascii").split()[0])
            # Discarded receipt is an observation-gap control, not a simulated
            # broken transport or evidence that every failed push has effects.

    def test_explicit_upstream_changes_only_two_local_keys(self):
        with remote_fixture(self.root) as f:
            git(f.local,"switch","-c","feature/demo");selected=commit(f.local,"new branch")
            git(f.local,"config","--local","push.autoSetupRemote","true")
            git(f.local,"config","--local","branch.other.remote","backup")
            cfg=f.root/".fixture-global-config";global_before=hashlib.sha256(cfg.read_bytes()).hexdigest()
            before=git(f.local,"config","--local","--list").stdout.splitlines()
            self.assertEqual(2,advertise(f.local,branch="feature/demo").returncode)
            r=push_pinned(f,selected,"feature/demo");self.assertEqual(0,r.returncode,r.stderr)
            self.assertEqual(selected,advertise(f.local,branch="feature/demo").stdout.decode("ascii").split()[0])
            self.assertEqual(1,git(f.local,"config","--get","branch.feature/demo.remote",check=False).returncode)
            git(f.local,"config","--local","--replace-all","branch.feature/demo.remote","origin")
            git(f.local,"config","--local","--replace-all","branch.feature/demo.merge","refs/heads/feature/demo")
            after=git(f.local,"config","--local","--list").stdout.splitlines()
            self.assertEqual(set(before)|{b"branch.feature/demo.remote=origin",b"branch.feature/demo.merge=refs/heads/feature/demo"},set(after))
            self.assertEqual(global_before,hashlib.sha256(cfg.read_bytes()).hexdigest())
            self.assertEqual(b"backup\n",git(f.local,"config","--get","branch.other.remote").stdout)

    def test_upstream_failure_preserves_verified_push_and_partial_keys(self):
        with remote_fixture(self.root) as f:
            git(f.local,"switch","-c","feature/demo");selected=commit(f.local,"partial configuration")
            self.assertEqual(0,push_pinned(f,selected,"feature/demo").returncode)
            git(f.local,"config","--local","--replace-all","branch.feature/demo.remote","origin")
            lock=f.local/".git/config.lock";lock.write_text("owned fault injection\n",encoding="utf-8")
            r=git(f.local,"config","--local","--replace-all","branch.feature/demo.merge","refs/heads/feature/demo",check=False)
            self.assertNotEqual(0,r.returncode)
            self.assertEqual(selected,head(f.remote,"refs/heads/feature/demo"))
            self.assertEqual(b"origin\n",git(f.local,"config","--get","branch.feature/demo.remote").stdout)
            self.assertEqual(1,git(f.local,"config","--get","branch.feature/demo.merge",check=False).returncode)

    def test_equal_remote_allows_requested_upstream_without_push(self):
        with remote_fixture(self.root) as f:
            git(f.local,"config","--local","--unset","branch.main.remote")
            git(f.local,"config","--local","--unset","branch.main.merge")
            hook(f.local,"pre-push","echo unexpected > push-marker\nexit 99")
            before=refs(f.remote);source=head(f.local)
            observed=advertise(f.local)
            self.assertEqual(source,observed.stdout.decode("ascii").split()[0])
            git(f.local,"config","--local","--replace-all","branch.main.remote","origin")
            git(f.local,"config","--local","--replace-all","branch.main.merge","refs/heads/main")
            self.assertEqual(before,refs(f.remote));self.assertFalse((f.local/"push-marker").exists())
            self.assertEqual(b"origin\n",git(f.local,"config","--get","branch.main.remote").stdout)
            self.assertEqual(b"refs/heads/main\n",git(f.local,"config","--get","branch.main.merge").stdout)
