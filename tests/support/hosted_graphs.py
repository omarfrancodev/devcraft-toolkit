"""Disposable real Git objects used only by emulated-provider controls."""
from pathlib import Path
from tests.support.git_fixtures import git_fixture,_git

def _run(graph,args,check=True):
    return _git(args,cwd=Path(graph["repository"]),env={"GIT_CONFIG_GLOBAL":graph["global_config"]},check=check)

def git_parents(graph,oid):return _run(graph,["show","-s","--format=%P",oid]).stdout.strip().split()
def git_ancestor(graph,ancestor,target):
    result=_run(graph,["merge-base","--is-ancestor",ancestor,target],check=False)
    if result.returncode not in [0,1]:raise RuntimeError(result.stderr)
    return result.returncode==0

def hosted_graph(root):
    root=Path(root).resolve()
    with git_fixture("normal",root) as repo:
        g={"repository":str(repo),"global_config":str(root/".fixture-global-config")}
        def run(*args):return _run(g,list(args)).stdout.strip()
        def commit(name,text):
            (repo/name).write_text(text,encoding="utf-8");run("add","--",name);run("commit","-m","fixture: "+name);return run("rev-parse","HEAD")
        g["A"]=run("rev-parse","HEAD")
        g["B"]=commit("target.txt","Target base.\n")
        run("switch","-c","feature/demo",g["A"]);g["S"]=commit("source.txt","Invoice totals.\n")
        run("switch","main");run("merge","--no-ff","feature/demo","-m","fixture: normal merge");g["M"]=run("rev-parse","HEAD")
        g["D"]=commit("descendant.txt","Later target commit.\n")
        run("switch","-c","rewritten",g["A"]);g["R"]=commit("rewritten.txt","Different target history.\n")
        g["merge_parents"]=git_parents(g,g["M"])
        g["containment"]={oid:git_ancestor(g,g["M"],oid) for oid in [g["M"],g["D"],g["R"]]}
        return g
