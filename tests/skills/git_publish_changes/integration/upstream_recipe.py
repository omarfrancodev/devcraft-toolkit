"""Development-only replay of upstream setup, never installed runtime code.

Owned fixtures here have one positive fetch refspec. The maintained reference
also requires inspecting negative/ambiguous/custom mappings and effective scopes.
"""
from tests.support.remote_git_fixtures import git

def setup_upstream(repo, branch, remote, destination):
    local_ref=f"refs/heads/{branch}"
    # Ask Git to resolve the prospective mapping with command-local values only;
    # the fixture branches have no old merge values or conflicting overrides.
    probe=git(repo,"-c",f"branch.{branch}.remote={remote}",
              "-c",f"branch.{branch}.merge=refs/heads/{destination}",
              "for-each-ref","--format=%(refname)%00%(upstream)","--",local_ref,check=False)
    rows=[line.split(b"\0",1) for line in probe.stdout.splitlines()]
    mappings=[value.decode() for name,value in rows if name.decode()==local_ref and value]
    if probe.returncode or len(mappings)!=1:
        return {"outcome":"needs_decision","reason":"no usable fetch mapping"}
    tracking=mappings[0]
    if not tracking.startswith(f"refs/remotes/{remote}/"):
        return {"outcome":"needs_decision","reason":"unsafe tracking destination"}
    direct=git(repo,"symbolic-ref","--quiet","--no-recurse","--",tracking,check=False)
    commit=git(repo,"rev-parse","--verify","--end-of-options",tracking+"^{commit}",check=False)
    if direct.returncode!=1 or commit.returncode:
        return {"outcome":"needs_decision","reason":"tracking ref is symbolic or unavailable"}
    for key,value in ((f"branch.{branch}.remote",remote),(f"branch.{branch}.merge",f"refs/heads/{destination}")):
        result=git(repo,"config","--local","--replace-all",key,value,check=False)
        if result.returncode:return {"outcome":"partial","exit":result.returncode}
    resolved=git(repo,"rev-parse","--symbolic-full-name",f"{branch}@{{upstream}}",check=False)
    oid=git(repo,"rev-parse","--verify","--end-of-options",f"{branch}@{{upstream}}^{{commit}}",check=False)
    if resolved.returncode or resolved.stdout.decode().strip()!=tracking or oid.returncode:
        return {"outcome":"partial","reason":"upstream resolution failed after keys"}
    return {"outcome":"configured","tracking_ref":tracking,"tracking_oid":oid.stdout.decode().strip()}
