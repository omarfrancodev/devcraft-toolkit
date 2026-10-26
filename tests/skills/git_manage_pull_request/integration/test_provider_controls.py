"""Owned emulation controls; passing them is not live service/skill evidence."""
from copy import deepcopy
from pathlib import Path
import tempfile
import unittest
import subprocess
import sys
import json
from tests.support.hosted_provider_fixtures import provider_fixture,normalize_request,ProviderFailure

class ProviderControls(unittest.TestCase):
    def setUp(self):
        parent=Path(__file__).resolve().parents[3]/".tmp";parent.mkdir(exist_ok=True)
        self.tmp=tempfile.TemporaryDirectory(dir=parent);self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
    def payload(self,f):return {"scope":deepcopy(f.state["scope"]),"title":"Invoice totals","body":"Tests not run.","draft":False}
    def test_provider_profiles_preserve_identity_and_unknowns(self):
        for provider in ["github","gitlab"]:
            with self.subTest(provider=provider),provider_fixture(self.root/provider,provider) as f:
                created=f.create(self.payload(f));f.state["requests"][0]["mergeable"]=None
                raw=f.raw_request(f.state["requests"][0]);result=normalize_request(provider,raw)
                self.assertEqual(created["id"],result["id"]);self.assertEqual(42,result["source_project"])
                self.assertEqual(7,result["target_project"]);self.assertIsNone(result["mergeable"])
                self.assertIsNone(result["target_oid"]);self.assertIsNone(result["merge_oid"])
    def test_incomplete_listing_is_not_confirmed_absence(self):
        with provider_fixture(self.root) as f:
            f.state["listing_complete"]=False
            found=f.list_requests()
            self.assertFalse(found["complete"]);self.assertEqual([],found["items"])
            self.assertEqual([],f.state["requests"])
    def test_fork_identity_disambiguates_equal_branch_names(self):
        with provider_fixture(self.root) as f:
            foreign=f.create(self.payload(f));f.state["requests"][0]["scope"]["source_project"]=99
            own=f.create(self.payload(f));found=f.list_requests()
            exact=[x for x in found["items"] if x["source_project"]==42 and x["target_project"]==7]
            self.assertEqual([own["id"]],[x["id"] for x in exact]);self.assertNotEqual(foreign["id"],own["id"])
    def test_create_update_roundtrip_preserves_other_fields(self):
        for provider in ["github","gitlab"]:
            with self.subTest(provider=provider),provider_fixture(self.root/provider,provider) as f:
                created=f.create(self.payload(f));before=deepcopy(f.state["requests"][0]);gates=deepcopy(f.state["gates"])
                updated=f.update(created["id"],{"body":"Verified supplied summary; validation not run."})
                after=deepcopy(f.state["requests"][0]);self.assertEqual(after.pop("body"),updated["body"])
                before.pop("body");self.assertEqual(before,after);self.assertEqual(gates,f.state["gates"])
                self.assertEqual(updated["id"],f.read()["request"]["id"])
    def test_creation_lost_ack_preserves_one_created_request(self):
        with provider_fixture(self.root) as f:
            f.state["faults"]["create"]="lost_ack"
            with self.assertRaises(ProviderFailure):f.create(self.payload(f))
            self.assertEqual(1,len(f.state["requests"]))
            self.assertEqual(1,len([e for e in f.events if e["op"]=="create"]))
            self.assertEqual(1,len(f.list_requests()["items"]))
    def test_title_and_description_can_have_gitlab_side_effects(self):
        with provider_fixture(self.root,"gitlab") as f:
            payload=self.payload(f);payload.update(title="Draft: Invoice totals",draft=True)
            created=f.create(payload)
            f.update(created["id"],{"title":"Invoice totals","body":"Summary\n/approve\n"})
            self.assertFalse(f.state["requests"][0]["draft"])
            self.assertEqual(1,f.state["requests"][0]["approvals"])
    def test_gitlab_diff_base_does_not_supply_live_target(self):
        with provider_fixture(self.root,"gitlab") as f:
            f.create(self.payload(f));raw=f.raw_request(f.state["requests"][0]);raw["diff_refs"]["base_sha"]="c"*40
            self.assertIsNone(normalize_request("gitlab",raw)["target_oid"])
            normalized=normalize_request("gitlab",raw,{"oid":"d"*40})
            self.assertEqual("d"*40,normalized["target_oid"])
            self.assertEqual("c"*40,normalized["reported_base_oid"])

    def test_cli_read_without_stdin_returns_observation(self):
        with provider_fixture(self.root) as f:
            driver=Path(__file__).resolve().parents[3]/"support/hosted_transport.py"
            result=subprocess.run([sys.executable,"-B",str(driver),str(f.state_path),"read"],input=b"",capture_output=True)
            self.assertEqual(0,result.returncode,result.stderr.decode())
            self.assertTrue(json.loads(result.stdout)["emulated"])

    def test_cli_preserves_utf8_request_text(self):
        with provider_fixture(self.root) as f:
            driver=Path(__file__).resolve().parents[3]/"support/hosted_transport.py"
            payload=self.payload(f);payload["body"]="Se añadió el total ☑"
            result=subprocess.run([sys.executable,"-B",str(driver),str(f.state_path),"create"],input=json.dumps(payload,ensure_ascii=False).encode("utf-8"),capture_output=True)
            self.assertEqual(0,result.returncode,result.stderr.decode(errors="replace"))
            self.assertEqual(payload["body"],json.loads(result.stdout)["body"])

    def test_cli_utf8_protocol_overrides_windows_stdio_locale(self):
        import os
        with provider_fixture(self.root) as f:
            driver=Path(__file__).resolve().parents[3]/"support/hosted_transport.py"
            payload=self.payload(f);payload["body"]="Se a\u00f1adi\u00f3 el total"
            child=os.environ.copy();child["PYTHONIOENCODING"]="cp1252"
            result=subprocess.run([sys.executable,"-B",str(driver),str(f.state_path),"create"],input=json.dumps(payload,ensure_ascii=False).encode("utf-8"),capture_output=True,env=child)
            self.assertEqual(0,result.returncode,result.stderr.decode(errors="replace"))
            saved=json.loads(f.state_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["body"],saved["requests"][0]["body"])
            self.assertEqual(payload["body"],json.loads(result.stdout)["body"])
