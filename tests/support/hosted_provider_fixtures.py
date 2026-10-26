"""Owned provider emulation for development; not a live service/client SDK."""
from contextlib import contextmanager
from copy import deepcopy
from pathlib import Path
from urllib.parse import urlsplit
import json
import re

class ProviderFailure(Exception):
    def __init__(self,status,message,effects=None):
        super().__init__(message);self.status=status;self.effects=effects

def _ref(value):
    if value is None:return None
    return value if value.startswith("refs/heads/") else "refs/heads/"+value

def normalize_request(provider,raw,target=None):
    if provider=="github":
        head=raw.get("head") or {};base=raw.get("base") or {}
        source=(head.get("repo") or {}).get("id");dest=(base.get("repo") or {}).get("id")
        oid=head.get("sha");reported=base.get("sha");merged=raw.get("merged")
        values=(raw.get("number"),source,dest,_ref(head.get("ref")),_ref(base.get("ref")),raw.get("body"),raw.get("html_url"))
        state=raw.get("state");result=raw.get("merge_commit_sha")
    elif provider=="gitlab":
        diff=raw.get("diff_refs") or {};oid=raw.get("sha");reported=diff.get("base_sha")
        merged=True if raw.get("state")=="merged" else False if raw.get("state") in ["opened","closed"] else None
        values=(raw.get("iid"),raw.get("source_project_id"),raw.get("target_project_id"),_ref(raw.get("source_branch")),_ref(raw.get("target_branch")),raw.get("description"),raw.get("web_url"))
        state={"opened":"open"}.get(raw.get("state"),raw.get("state"));result=raw.get("merge_commit_sha")
    else:raise ProviderFailure(400,"unsupported emulated provider")
    ident,source,dest,source_ref,target_ref,body,url=values
    return {"provider":provider,"host":urlsplit(url).hostname if url else None,"id":ident,"global_id":raw.get("id"),"source_project":source,"target_project":dest,"source_ref":source_ref,"target_ref":target_ref,"source_oid":oid,"target_oid":target.get("oid") if target else None,"reported_base_oid":reported,"state":state,"draft":raw.get("draft"),"merged":merged,"mergeable":raw.get("mergeable"),"merge_oid":result if merged is True else None,"hypothetical_merge_oid":result if merged is not True else None,"title":raw.get("title"),"body":body,"url":url,"complete":raw.get("_complete")}

class HostedFixture:
    def __init__(self,root,state=None):
        self.root=Path(root).resolve();self.state_path=self.root/"state.json"
        self.state=state if state is not None else json.loads(self.state_path.read_text(encoding="utf-8"))
        assert self.state.get("fixture")=="devcraft-hosted-emulation"
    @property
    def events(self):return self.state["events"]
    def save(self):
        self.root.mkdir(parents=True,exist_ok=True)
        self.state_path.write_text(json.dumps(self.state,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    def _event(self,op,payload,result=None,status=200):
        self.events.append({"op":op,"payload":deepcopy(payload),"status":status,"result":deepcopy(result)})
        self.save()
    def capabilities(self):
        result={"emulated":True,"provider":self.state["provider"],"host":self.state["scope"]["host"],"account":self.state["account"],"operations":["capabilities","read","list","create","update","merge"],"atomic_target_oid":False,"merge_input":"request_id plus GitHub sha/merge_method=merge; GitLab sha/squash=false/auto_merge=false/should_remove_source_branch=false","input":"JSON stdin; writes carry scope/title/body or request_id plus selected fields","auth":"owned fixture only; no real account"}
        self._event("capabilities",{},result);return result
    def raw_request(self,request):
        s=request["scope"];common={"id":10000+request["id"],"title":request["title"],"draft":request["draft"],"mergeable":request.get("mergeable"),"merge_commit_sha":request.get("merge_oid") or "c"*40,"_complete":True}
        if self.state["provider"]=="github":
            return {**common,"number":request["id"],"head":{"repo":{"id":s["source_project"]},"ref":s["source_ref"].removeprefix("refs/heads/"),"sha":s["source_oid"]},"base":{"repo":{"id":s["target_project"]},"ref":s["target_ref"].removeprefix("refs/heads/"),"sha":s["target_oid"]},"body":request["body"],"state":"closed" if request["state"]=="merged" else request["state"],"merged":request["state"]=="merged","html_url":f"https://{s['host']}/org/repo/pull/{request['id']}"}
        return {**common,"iid":request["id"],"source_project_id":s["source_project"],"target_project_id":s["target_project"],"source_branch":s["source_ref"].removeprefix("refs/heads/"),"target_branch":s["target_ref"].removeprefix("refs/heads/"),"sha":s["source_oid"],"diff_refs":{"base_sha":s["target_oid"],"head_sha":s["source_oid"]},"description":request["body"],"state":"opened" if request["state"]=="open" else request["state"],"web_url":f"https://{s['host']}/org/repo/-/merge_requests/{request['id']}"}
    def _normalized(self,request):return normalize_request(self.state["provider"],self.raw_request(request),{"oid":self.state["scope"]["target_oid"]})
    def read(self):
        selected=next((q for q in self.state["requests"] if q["id"]==self.state["selected_id"]),None)
        result={"emulated":True,"provider":self.state["provider"],"account":self.state["account"],"scope":deepcopy(self.state["scope"]),"request":self._normalized(selected) if selected else None,"gates":deepcopy(self.state["gates"]),"template":self.state["template"],"compare":deepcopy(self.state["compare"]),"complete":self.state["observation_complete"]}
        graph=self.state.get("graph")
        if graph and selected and selected["state"]=="merged":
            result["commit_evidence"]={"source":"owned_real_git_graph_fixture","merge_oid":selected["merge_oid"],"parents":graph["merge_parents"],"observed_target_oid":self.state["scope"]["target_oid"],"target_contains_merge":graph["containment"].get(self.state["scope"]["target_oid"])}
        self._event("read",{"request_id":self.state["selected_id"]},{"id":selected["id"] if selected else None});return result
    def list_requests(self):
        result={"items":[self._normalized(q) for q in self.state["requests"]],"complete":self.state["listing_complete"],"next_cursor":None if self.state["listing_complete"] else "page-2"}
        self._event("list",{}, {"count":len(result["items"]),"complete":result["complete"]});return result
    def _apply_text(self,request,payload):
        if self.state["provider"]!="gitlab":return
        if "title" in payload:request["draft"]=bool(re.match(r"^(?:Draft:|\[Draft\]|\(Draft\))",request["title"],re.I))
        # Deliberately emulate unsafe primitive effects, not a client permission gate.
        if "body" in payload:
            if "/approve" in request["body"].splitlines():request["approvals"]+=1
            if "/close" in request["body"].splitlines():request["state"]="closed"
    def create(self,payload):
        s=self.state["scope"];wanted=payload.get("scope") or {}
        for key in ["provider","host","source_project","target_project","source_ref","target_ref"]:
            if wanted.get(key)!=s[key]:
                self._event("create",payload,status=422);raise ProviderFailure(422,"scope mismatch")
        same=lambda q:all(q["scope"][k]==s[k] for k in ["source_project","target_project","source_ref","target_ref"])
        if any(q["state"]=="open" and same(q) for q in self.state["requests"]):
            self._event("create",payload,status=422);raise ProviderFailure(422,"request already exists")
        q={"id":self.state["next_id"],"scope":deepcopy(s),"title":payload["title"],"body":payload["body"],"draft":payload.get("draft",False),"state":"open","mergeable":True,"merge_oid":None,"labels":["keep"],"reviewers":["existing-reviewer"],"approvals":0}
        self.state["next_id"]+=1;self._apply_text(q,payload);self.state["requests"].append(q);self.state["selected_id"]=q["id"]
        fault=self.state["faults"].pop("create",None);self._event("create",payload,{"id":q["id"]},0 if fault=="lost_ack" else 201)
        if fault=="lost_ack":raise ProviderFailure(0,"lost acknowledgment")
        return self._normalized(q)
    def update(self,request_id,payload):
        q=next((q for q in self.state["requests"] if q["id"]==request_id),None)
        if q is None:raise ProviderFailure(404,"request not found")
        if set(payload)-{"title","body","state","target_ref"}:raise ProviderFailure(422,"unsupported field")
        for key,value in payload.items():
            if key=="target_ref":q["scope"][key]=value
            else:q[key]=value
        self._apply_text(q,payload);self.state["selected_id"]=q["id"]
        fault=self.state["faults"].pop("update",None);self._event("update",{"request_id":request_id,**payload},{"id":q["id"]},0 if fault=="lost_ack" else 200)
        if fault=="lost_ack":raise ProviderFailure(0,"lost acknowledgment")
        return self._normalized(q)

    def merge(self,request_id,payload):
        q=next((q for q in self.state["requests"] if q["id"]==request_id),None)
        if q is None:raise ProviderFailure(404,"request not found")
        operand={"request_id":request_id,"operands":deepcopy(payload)}
        if payload.get("sha")!=self.state["scope"]["source_oid"]:
            self._event("merge",operand,status=409);raise ProviderFailure(409,"source precondition failed")
        expected=({"sha":payload["sha"],"merge_method":"merge"} if self.state["provider"]=="github" else {"sha":payload["sha"],"squash":False,"auto_merge":False,"should_remove_source_branch":False})
        if payload!=expected:
            self._event("merge",operand,status=422);raise ProviderFailure(422,"unsupported normal merge operands")
        if q["state"]!="open":
            self._event("merge",operand,status=409);raise ProviderFailure(409,"request not open")
        graph=self.state.get("graph")
        if not graph:raise ProviderFailure(422,"owned graph required")
        fault=self.state["faults"].pop("merge",None)
        if fault=="pending":
            self.state["pending"]=True;self._event("merge",operand,{"status":"pending"},202);return {"status":"pending"}
        q["state"]="merged";q["merge_oid"]=graph["M"];self.state["scope"]["target_oid"]=graph["M"]
        self._event("merge",operand,{"merged":True,"merge_oid":graph["M"]},0 if fault=="lost_ack" else 200)
        if fault=="lost_ack":raise ProviderFailure(0,"lost merge acknowledgment")
        return self._normalized(q)

@contextmanager
def provider_fixture(root,provider="github"):
    assert provider in ["github","gitlab"]
    source="a"*40;target="b"*40
    state={"fixture":"devcraft-hosted-emulation","provider":provider,"account":"fixture-user","scope":{"provider":provider,"host":provider+".fixture.invalid","source_project":42,"target_project":7,"source_ref":"refs/heads/feature/demo","target_ref":"refs/heads/main","source_oid":source,"target_oid":target},"requests":[],"selected_id":None,"next_id":7,"events":[],"faults":{},"listing_complete":True,"observation_complete":True,"template":None,"compare":{"complete":True,"source_oid":source,"target_oid":target,"changes":["Adds invoice totals"],"validation":"not_run"},"gates":{"merge_method":"merge","allow_merge_commit":True,"squash_required":False,"source_cleanup":False,"review":{"state":"not_required","source":"fixture_project_policy","head_oid":source},"checks":{"state":"satisfied","source":"fixture_project_policy","head_oid":source,"required":["unit"],"records":[{"name":"unit","head_oid":source,"status":"completed","conclusion":"success"}]}}}
    fixture=HostedFixture(root,state);fixture.save();yield fixture
