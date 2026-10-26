"""Disposable JSON/stdin transport over an owned emulated provider state."""
import json
from pathlib import Path
import sys
if __package__:
    from .hosted_provider_fixtures import HostedFixture,ProviderFailure
else:
    from hosted_provider_fixtures import HostedFixture,ProviderFailure

def main():
    # This disposable wire protocol is UTF-8 regardless of the Windows locale.
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    fixture=HostedFixture(Path(sys.argv[1]).resolve().parent);action=sys.argv[2]
    raw=sys.stdin.read() if not sys.stdin.isatty() and action in ["create","update","merge","read"] else ""
    payload=json.loads(raw) if raw.strip() else {}
    if action=="capabilities":result=fixture.capabilities()
    elif action=="read":
        if "request_id" in payload:fixture.state["selected_id"]=payload["request_id"]
        result=fixture.read()
    elif action=="list":result=fixture.list_requests()
    elif action=="create":result=fixture.create(payload)
    elif action=="update":result=fixture.update(payload.pop("request_id"),payload)
    elif action=="merge" and hasattr(fixture,"merge"):result=fixture.merge(payload.pop("request_id"),payload)
    else:raise ProviderFailure(400,"unsupported fixture operation")
    print(json.dumps(result,ensure_ascii=False))
if __name__=="__main__":
    try:main()
    except ProviderFailure as failure:
        print(json.dumps({"error":str(failure),"status":failure.status}));sys.exit(1)
