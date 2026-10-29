"""Development-only hosting bridge over actual owned bare Git publication."""
import json
import os
from pathlib import Path
import subprocess
import sys
try:
    from hosted_provider_fixtures import HostedFixture, ProviderFailure
except ModuleNotFoundError:
    sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
    from tests.support.hosted_provider_fixtures import HostedFixture, ProviderFailure


def refresh(f):
    binding=f.state["publication"];repo=Path(binding["repository"])
    env={k:v for k,v in os.environ.items() if not k.upper().startswith("GIT_")}
    env.update(GIT_CONFIG_GLOBAL=binding["global_config"],GIT_CONFIG_NOSYSTEM="1")
    def git(*args):
        return subprocess.run(["git","--no-pager","--no-optional-locks","--no-lazy-fetch","--no-replace-objects","-c","core.fsmonitor=false","-c","maintenance.auto=false","-c","gc.auto=0",*args],cwd=repo,env=env,capture_output=True)
    scope=f.state["scope"]
    for role in ("source","target"):
        result=git("rev-parse","--verify","--end-of-options",scope[role+"_ref"])
        scope[role+"_oid"]=result.stdout.decode("ascii").strip() if result.returncode==0 else None
    complete=all(scope[k] for k in ("source_oid","target_oid"))
    changes=[]
    if complete:
        result=git("diff","--no-ext-diff","--no-textconv","--name-only","-z",scope["target_oid"],scope["source_oid"],"--")
        if result.returncode:raise ProviderFailure(502,"owned comparison failed")
        changes=result.stdout.decode("utf-8").rstrip("\0").split("\0") if result.stdout else []
    f.state["compare"]={"complete":complete,"source_oid":scope["source_oid"],"target_oid":scope["target_oid"],"changes":changes,"validation":"not_run"}
    f.save()


def main():
    sys.stdin.reconfigure(encoding="utf-8");sys.stdout.reconfigure(encoding="utf-8")
    f=HostedFixture(Path(sys.argv[1]).resolve().parent);action=sys.argv[2]
    payload=json.loads(sys.stdin.read() or "{}") if action in ("read","create","update") else {}
    if action=="capabilities":
        result=f.capabilities();result["operations"]=["capabilities","read","list","create","update"]
    else:
        refresh(f)
        if action=="read":result=f.read()
        elif action=="list":result=f.list_requests()
        elif action=="create":
            if not f.state["scope"]["source_oid"]:raise ProviderFailure(422,"source branch absent")
            result=f.create(payload)
        elif action=="update":result=f.update(payload.pop("request_id"),payload)
        else:raise ProviderFailure(400,"unsupported bridge action")
    print(json.dumps(result,ensure_ascii=False))
if __name__=="__main__":
    try:main()
    except ProviderFailure as exc:print(json.dumps({"error":str(exc),"status":exc.status}));sys.exit(1)
