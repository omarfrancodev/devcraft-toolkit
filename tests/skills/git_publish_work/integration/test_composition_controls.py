"""Owned primitive compositions; no policy engine or instruction-loader claim."""
from copy import deepcopy
from pathlib import Path
import tempfile
import subprocess
import sys
import json
import unittest
from tests.support.remote_git_fixtures import remote_fixture, git, refs, head, commit, push_pinned, advertise
from tests.support.work_branch_fixtures import create_branch, branch_snapshot
from tests.support.hosted_provider_fixtures import provider_fixture, ProviderFailure
from tests.support.hosted_graphs import hosted_graph

class PublicationControls(unittest.TestCase):
    def setUp(self):
        root=Path(__file__).resolve().parents[3]/".tmp";root.mkdir(parents=True,exist_ok=True)
        t=tempfile.TemporaryDirectory(dir=root);self.addCleanup(t.cleanup);self.root=Path(t.name)

    def test_branch_commit_push_uses_final_source_preserving_main_and_config(self):
        with remote_fixture(self.root) as f:
            original=head(f.local);before=branch_snapshot(f.local);remote_before=refs(f.remote)
            self.assertEqual(0,create_branch(f.local,"feature/demo",original).returncode)
            source=commit(f.local,"feat: add parser");self.assertNotEqual(original,source)
            self.assertEqual(0,push_pinned(f,source,"feature/demo").returncode)
            self.assertEqual(source,head(f.remote,"refs/heads/feature/demo"));self.assertEqual(original,head(f.local,"refs/heads/main"))
            self.assertEqual(remote_before|{"refs/heads/feature/demo":source},refs(f.remote))
            self.assertEqual(before["config"],branch_snapshot(f.local)["config"])
            self.assertEqual(b"",git(f.local,"status","--porcelain").stdout)

    def test_existing_commit_publication_does_not_create_commit_or_tracking_config(self):
        with remote_fixture(self.root) as f:
            git(f.local,"switch","--no-track","-c","feature/demo");source=commit(f.local,"feat: existing work")
            before=branch_snapshot(f.local)
            self.assertEqual(0,push_pinned(f,source,"feature/demo").returncode)
            after=branch_snapshot(f.local)
            for key in ("head","symbolic","index","files","config"):self.assertEqual(before[key],after[key],key)
            self.assertEqual(source,head(f.remote,"refs/heads/feature/demo"))
            self.assertNotIn("refs/heads/extra",refs(f.local))

    def test_rejected_push_keeps_earlier_branch_and_commit(self):
        with remote_fixture(self.root) as f:
            original=head(f.local);create_branch(f.local,"feature/demo",original);selected=commit(f.local,"selected work")
            git(f.seed,"switch","--no-track","-c","feature/demo");other=commit(f.seed,"conflicting remote work")
            git(f.seed,"push","--","origin","HEAD:refs/heads/feature/demo")
            before=branch_snapshot(f.local);remote_before=refs(f.remote)
            result=push_pinned(f,selected,"feature/demo");self.assertNotEqual(0,result.returncode)
            self.assertEqual(before,branch_snapshot(f.local));self.assertEqual(remote_before,refs(f.remote))
            self.assertEqual(selected,head(f.local));self.assertEqual(original,head(f.local,"refs/heads/main"));self.assertEqual(other,head(f.remote,"refs/heads/feature/demo"))

    def test_lost_push_receipt_is_resolved_by_observation_not_second_write(self):
        with remote_fixture(self.root) as f:
            source=commit(f.local,"publish once");push_pinned(f,source)  # receipt deliberately discarded
            observed=advertise(f.local);self.assertEqual(0,observed.returncode)
            self.assertEqual(source,observed.stdout.decode("ascii").split()[0]);self.assertEqual(source,head(f.local))
            # Observation establishes equality; this control does not perform a recovery push.

    def test_duplicate_and_lost_creation_preserve_exact_request_identity(self):
        with provider_fixture(self.root) as f:
            payload={"scope":deepcopy(f.state["scope"]),"title":"Parser","body":"Validation not run."}
            f.state["faults"]["create"]="lost_ack"
            with self.assertRaises(ProviderFailure):f.create(payload)
            listing=f.list_requests();self.assertTrue(listing["complete"]);self.assertEqual(1,len(listing["items"]))
            q=listing["items"][0];self.assertEqual(f.state["scope"]["source_ref"],q["source_ref"])
            self.assertEqual(f.state["scope"]["source_project"],q["source_project"])
            self.assertEqual(1,sum(e["op"]=="create" for e in f.events))
            self.assertFalse(any(e["op"] in ("update","merge") for e in f.events))
            f.state["listing_complete"]=False;self.assertFalse(f.list_requests()["complete"])

    def test_pending_promotion_has_no_merged_receipt(self):
        with provider_fixture(self.root) as f:
            graph=hosted_graph(self.root/"graph");f.state["graph"]=graph
            f.state["scope"].update(source_oid=graph["S"],target_oid=graph["B"])
            q=f.create({"scope":deepcopy(f.state["scope"]),"title":"Parser","body":"Test fixture."})
            f.state["faults"]["merge"]="pending"
            result=f.merge(q["id"],{"sha":graph["S"],"merge_method":"merge"})
            self.assertEqual("pending",result["status"]);self.assertFalse(f.read()["request"]["merged"])
            self.assertEqual(graph["B"],f.state["scope"]["target_oid"])
            self.assertEqual(1,sum(e["op"]=="merge" for e in f.events))

    def test_emulated_transport_observes_actual_published_tip(self):
        with remote_fixture(self.root/"git") as f,provider_fixture(self.root/"provider") as hosted:
            hosted.state["scope"].update(source_ref="refs/heads/feature/parser",source_oid=None,target_oid=head(f.remote))
            hosted.state["publication"]={"repository":str(f.remote),"global_config":str(f.root/".fixture-global-config")};hosted.save()
            transport=Path(__file__).with_name("publication_transport.py")
            def read():
                r=subprocess.run([sys.executable,"-B",str(transport),str(hosted.state_path),"read"],input="",capture_output=True,text=True,encoding="utf-8")
                self.assertEqual(0,r.returncode,r.stderr)
                return json.loads(r.stdout)
            self.assertIsNone(read()["scope"]["source_oid"])
            create_branch(f.local,"feature/parser",head(f.local));source=commit(f.local,"feat: parser")
            self.assertEqual(0,push_pinned(f,source,"feature/parser").returncode)
            observed=read();self.assertEqual(source,observed["scope"]["source_oid"])
            self.assertEqual(source,observed["compare"]["source_oid"])
            self.assertEqual(["work.txt"],observed["compare"]["changes"])
