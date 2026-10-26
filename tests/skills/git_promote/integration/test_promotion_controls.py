"""Owned protocol/real-Git controls, not instruction or real-provider validation."""
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from tests.support.hosted_provider_fixtures import provider_fixture,ProviderFailure
from tests.support.hosted_graphs import hosted_graph,git_ancestor,git_parents

class PromotionControls(unittest.TestCase):
    def setUp(self):
        parent=Path(__file__).resolve().parents[3]/".tmp";parent.mkdir(exist_ok=True)
        self.tmp=tempfile.TemporaryDirectory(dir=parent);self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
    def prepare(self,f):
        graph=hosted_graph(f.root/"graph")
        f.state["graph"]=graph
        f.state["scope"].update(source_oid=graph["S"],target_oid=graph["B"])
        for name in ["review","checks"]:f.state["gates"][name]["head_oid"]=graph["S"]
        f.state["gates"]["checks"]["records"][0]["head_oid"]=graph["S"]
        return f.create({"scope":deepcopy(f.state["scope"]),"title":"Totals","body":"Checks supplied.","draft":False})
    def args(self,f):
        if f.state["provider"]=="github":return {"sha":f.state["scope"]["source_oid"],"merge_method":"merge"}
        return {"sha":f.state["scope"]["source_oid"],"squash":False,"auto_merge":False,"should_remove_source_branch":False}
    def test_merge_uses_exact_source_precondition_and_normal_flags(self):
        for provider in ["github","gitlab"]:
            with self.subTest(provider=provider),provider_fixture(self.root/provider,provider) as f:
                q=self.prepare(f);before=deepcopy(f.state);args=self.args(f);result=f.merge(q["id"],args)
                self.assertTrue(result["merged"]);self.assertEqual(args,f.events[-1]["payload"]["operands"])
                self.assertEqual(before["scope"]["source_oid"],f.state["scope"]["source_oid"])
                after=f.state["requests"][0];original=before["requests"][0]
                for key in ["title","body","labels","reviewers","approvals","draft"]:self.assertEqual(original[key],after[key])
                self.assertFalse(f.state.get("source_deleted",False));self.assertFalse(f.state.get("queued",False))
    def test_source_conflict_does_not_mutate_or_retry(self):
        with provider_fixture(self.root) as f:
            q=self.prepare(f);args=self.args(f);f.state["scope"]["source_oid"]="f"*40;before=deepcopy(f.state["requests"])
            with self.assertRaises(ProviderFailure) as caught:f.merge(q["id"],args)
            self.assertEqual(409,caught.exception.status);self.assertEqual(before,f.state["requests"])
            self.assertEqual(1,sum(e["op"]=="merge" for e in f.events))
    def test_unknown_or_wrong_revision_gates_are_not_ready(self):
        with provider_fixture(self.root) as f:
            self.prepare(f);f.state["gates"]["review"]={"state":"unknown","source":None,"head_oid":None}
            f.state["gates"]["checks"]={"state":"unknown","required":None,"records":[]}
            f.state["requests"][0]["mergeable"]=None
            read=f.read();self.assertIsNone(read["request"]["mergeable"]);self.assertEqual("unknown",read["gates"]["review"]["state"])
            self.assertIsNone(read["gates"]["checks"]["required"])
            f.state["gates"]["review"]={"state":"satisfied","head_oid":"e"*40}
            self.assertNotEqual(f.read()["request"]["source_oid"],f.read()["gates"]["review"]["head_oid"])
            self.assertFalse(any(e["op"]=="merge" for e in f.events))
    def test_already_merged_and_hypothetical_sha_are_distinct(self):
        with provider_fixture(self.root) as f:
            q=self.prepare(f);observed=f.read()["request"]
            self.assertFalse(observed["merged"]);self.assertIsNone(observed["merge_oid"]);self.assertIsNotNone(observed["hypothetical_merge_oid"])
            result=f.merge(q["id"],self.args(f));self.assertTrue(result["merged"]);self.assertEqual(f.state["graph"]["M"],f.read()["request"]["merge_oid"])
            self.assertIsNone(f.read()["request"]["hypothetical_merge_oid"])
    def test_lost_ack_or_pending_is_not_false_merged(self):
        for fault in ["lost_ack","pending"]:
            with self.subTest(fault=fault),provider_fixture(self.root/fault) as f:
                q=self.prepare(f);f.state["faults"]["merge"]=fault
                if fault=="lost_ack":
                    with self.assertRaises(ProviderFailure):f.merge(q["id"],self.args(f))
                    self.assertTrue(f.read()["request"]["merged"])
                else:
                    result=f.merge(q["id"],self.args(f));self.assertEqual("pending",result["status"])
                    self.assertFalse(f.read()["request"]["merged"]);self.assertIsNone(f.read()["request"]["merge_oid"])
                self.assertEqual(1,sum(e["op"]=="merge" for e in f.events))
    def test_strict_target_and_unsupported_method_or_cleanup_need_decision(self):
        with provider_fixture(self.root,"gitlab") as f:
            self.prepare(f);f.state["gates"].update(merge_method="ff",squash_required=True,source_cleanup=True)
            caps=f.capabilities();observed=f.read()
            self.assertFalse(caps["atomic_target_oid"]);self.assertEqual("ff",observed["gates"]["merge_method"])
            self.assertTrue(observed["gates"]["source_cleanup"]);self.assertTrue(observed["gates"]["squash_required"])
            self.assertFalse(any(e["op"]=="merge" for e in f.events))
    def test_actual_merge_graph_and_descendant_containment(self):
        with provider_fixture(self.root) as f:
            q=self.prepare(f);g=f.state["graph"];self.assertEqual([g["B"],g["S"]],git_parents(g,g["M"]))
            f.merge(q["id"],self.args(f));f.state["scope"]["target_oid"]=g["D"]
            result=f.read();self.assertEqual(g["M"],result["request"]["merge_oid"])
            self.assertTrue(git_ancestor(g,g["M"],g["D"]));self.assertTrue(result["commit_evidence"]["target_contains_merge"])
            self.assertEqual(g["D"],result["request"]["target_oid"])
    def test_rewritten_target_does_not_claim_containment(self):
        with provider_fixture(self.root) as f:
            q=self.prepare(f);g=f.state["graph"];f.merge(q["id"],self.args(f));f.state["scope"]["target_oid"]=g["R"]
            self.assertFalse(git_ancestor(g,g["M"],g["R"]))
            result=f.read();self.assertTrue(result["request"]["merged"]);self.assertFalse(result["commit_evidence"]["target_contains_merge"])
