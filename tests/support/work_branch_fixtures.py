"""Owned primitive recipes and semantic snapshots; never installed runtime policy."""
from pathlib import Path
from tests.support.remote_git_fixtures import git, refs, head
from tests.support.git_fixtures import snapshot_repository


def branch_snapshot(repo: Path) -> dict:
    raw=snapshot_repository(repo)
    return {
        "head": raw["HEAD"], "symbolic": raw["symbolic-HEAD"], "refs": refs(repo),
        "index": git(repo,"ls-files","--stage","-z").stdout.hex(),
        "files": {k:v for k,v in raw.items() if k.startswith(("working:","working-mode:"))},
        "config": git(repo,"config","--local","--null","--list").stdout.hex(),
    }


def create_branch(repo: Path, name: str, source_oid: str):
    # Caller owns name validation, authorization, hook/effect review and fresh guards.
    # This deliberately exposes Git's actual partial effects, not a policy simulator.
    return git(repo,"switch","--no-guess","--no-track","--no-recurse-submodules",
               "--no-overwrite-ignore","-c",name,source_oid,check=False)
