"""Owned local remotes for development tests; never an installed skill runtime."""
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
import os
import subprocess

SAFE=["--no-pager","--no-optional-locks","--no-lazy-fetch","--no-replace-objects",
      "-c","core.fsmonitor=false","-c","maintenance.auto=false","-c","gc.auto=0",
      "-c","log.showSignature=false","-c","submodule.recurse=false"]
FETCH=["fetch","--no-tags","--no-prune","--no-prune-tags","--no-recurse-submodules",
       "--no-write-fetch-head","--no-auto-maintenance","--no-write-commit-graph","--refmap=","--"]
PUSH=["-c","push.autoSetupRemote=false","push","--porcelain","--no-follow-tags","--recurse-submodules=no","--"]

@dataclass(frozen=True)
class RemoteFixture:
    root:Path
    remote:Path
    seed:Path
    local:Path

def git(repo:Path,*args:str,check:bool=True,env:dict|None=None)->subprocess.CompletedProcess[bytes]:
    repo=Path(repo).resolve()
    cfg=repo/".fixture-global-config"
    if not cfg.exists():cfg=repo.parent/".fixture-global-config"
    assert cfg.is_file(), cfg
    child={k:v for k,v in os.environ.items() if not k.upper().startswith("GIT_")}
    child.update(GIT_CONFIG_GLOBAL=str(cfg),GIT_CONFIG_NOSYSTEM="1")
    child.update(env or {})
    return subprocess.run(["git",*SAFE,*map(str,args)],cwd=repo,env=child,capture_output=True,check=check)

def head(repo:Path,ref:str="HEAD")->str:
    return git(repo,"rev-parse","--verify","--end-of-options",ref).stdout.decode("ascii").strip()

def refs(repo:Path)->dict[str,str]:
    # Preserve symbolic pointers, not their changing resolved object values.
    result={}
    for row in git(repo,"for-each-ref","--format=%(refname)%00%(objectname)%00%(symref)").stdout.decode("utf-8").splitlines():
        name,oid,symbolic=row.split("\0")
        result[name]="symref:"+symbolic if symbolic else oid
    return result

def commit(repo:Path,message:str,filename:str="work.txt")->str:
    p=Path(repo)/filename
    with p.open("a",encoding="utf-8") as f:f.write(message+"\n")
    git(repo,"add","--",filename)
    git(repo,"-c","commit.gpgsign=false","commit","-m",message)
    return head(repo)

@contextmanager
def remote_fixture(root:Path):
    root=Path(root).resolve();root.mkdir(parents=True,exist_ok=True)
    (root/".fixture-global-config").write_text("",encoding="utf-8")
    remote=root/"remote space.git";seed=root/"seed";local=root/"client"
    git(root,"init","--bare","--initial-branch=main",str(remote))
    git(root,"init","--initial-branch=main",str(seed))
    for name,value in (("user.name","Fixture User"),("user.email","fixture@example.invalid")):
        git(seed,"config","--local",name,value)
    commit(seed,"fixture: initial")
    git(seed,"remote","add","origin",str(remote))
    git(seed,"push","--","origin","HEAD:refs/heads/main")
    git(root,"clone",str(remote),str(local))
    for name,value in (("user.name","Fixture User"),("user.email","fixture@example.invalid")):
        git(local,"config","--local",name,value)
    yield RemoteFixture(root,remote,seed,local)

def _fixture_tracking_gate(repo:Path,remote:str,branch:str):
    # These owned fixtures use the conventional single tracking mapping. Runtime
    # instructions require inspecting every actual matching configured mapping.
    target=f"refs/remotes/{remote}/{branch}"
    result=git(repo,"symbolic-ref","--quiet","--no-recurse","--",target,check=False)
    if result.returncode==0:
        return subprocess.CompletedProcess(result.args,1,b"",b"symbolic tracking destination; stop before mutation")
    if result.returncode!=1:
        return result
    return None

def fetch_selected(f:RemoteFixture,branch:str="main"):
    blocked=_fixture_tracking_gate(f.local,"origin",branch)
    if blocked is not None:return blocked
    return git(f.local,*FETCH,"origin",f"refs/heads/{branch}:refs/remotes/origin/{branch}",check=False)

def fast_forward(repo:Path,oid:str):
    return git(repo,"merge","--ff-only","--no-overwrite-ignore","--no-autostash","--no-squash","--no-edit","--no-stat",oid,check=False)

def working(snapshot:dict)->dict:
    return {k:v for k,v in snapshot.items() if k.startswith(("working:","working-mode:"))}

def hook(repo:Path,name:str,body:str):
    text=git(repo,"rev-parse","--git-path","hooks").stdout.decode("utf-8").strip()
    directory=Path(text)
    if not directory.is_absolute():directory=repo/directory
    directory.mkdir(parents=True,exist_ok=True)
    target=directory/name
    target.write_bytes(("#!/bin/sh\n"+body+"\n").encode("utf-8"));target.chmod(0o755)
    return target

def advertise(repo:Path,remote:str="origin",branch:str="main"):
    endpoints=git(repo,"remote","get-url","--push","--all",remote).stdout.decode("utf-8").splitlines()
    assert len(endpoints)==1, "publication needs one effective push endpoint"
    return git(repo,"ls-remote","--refs","--exit-code","--",endpoints[0],"refs/heads/"+branch,check=False)

def push_pinned(f:RemoteFixture,oid:str,branch:str="main",remote:str="origin"):
    blocked=_fixture_tracking_gate(f.local,remote,branch)
    if blocked is not None:return blocked
    return git(f.local,*PUSH,remote,oid+":refs/heads/"+branch,check=False)
