"""Git repositories for isolated integration tests; never used by skills."""

from __future__ import annotations

import hashlib
import os
import subprocess
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


def _git(args: list[str], *, cwd: Path, env: dict[str, str] | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    child_env = os.environ.copy()
    child_env["GIT_CONFIG_NOSYSTEM"] = "1"
    if env:
        child_env.update(env)
    return subprocess.run(["git", *args], cwd=cwd, env=child_env, check=check, capture_output=True, text=True, encoding="utf-8")


def _init_repository(path: Path, root: Path) -> None:
    _git(["init", "--initial-branch=main", str(path)], cwd=root)
    _git(["config", "--local", "user.name", "Fixture User"], cwd=path)
    _git(["config", "--local", "user.email", "fixture@example.invalid"], cwd=path)


def _commit_readme(path: Path) -> None:
    (path / "README.md").write_text("Fixture repository.\n", encoding="utf-8")
    _git(["add", "--", "README.md"], cwd=path)
    _git(["commit", "-m", "fixture: create repository"], cwd=path)


@contextmanager
def git_fixture(kind: str, root: Path, *, dirname: str = "repo") -> Iterator[Path]:
    """Create an isolated Git fixture for context or preflight scenarios."""
    kinds = {"normal", "unborn", "linked-worktree", "detached", "dirty", "staged", "conflicted", "missing-identity"}
    if kind not in kinds:
        raise ValueError(f"Unsupported fixture kind: {kind}")
    root = Path(root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    global_config = root / ".fixture-global-config"
    global_config.write_text("", encoding="utf-8")
    env_keys = ("GIT_CONFIG_GLOBAL", "GIT_CONFIG_NOSYSTEM", "GIT_AUTHOR_NAME", "GIT_AUTHOR_EMAIL", "GIT_COMMITTER_NAME", "GIT_COMMITTER_EMAIL")
    prior_env = {key: os.environ.get(key) for key in env_keys}
    os.environ["GIT_CONFIG_GLOBAL"] = str(global_config)
    os.environ["GIT_CONFIG_NOSYSTEM"] = "1"
    for key in env_keys[2:]:
        os.environ.pop(key, None)
    repository = root / dirname
    try:
        if kind == "linked-worktree":
            source = root / f"{dirname}-source"
            _init_repository(source, root)
            _commit_readme(source)
            _git(["worktree", "add", "-b", "fixture-linked", str(repository)], cwd=source)
        else:
            _init_repository(repository, root)
            if kind != "unborn":
                _commit_readme(repository)
            if kind == "unborn":
                (repository / "README.md").write_text("Untracked fixture.\n", encoding="utf-8")
            elif kind == "detached":
                _git(["checkout", "--detach", "HEAD"], cwd=repository)
            elif kind == "dirty":
                with (repository / "README.md").open("a", encoding="utf-8") as readme:
                    readme.write("Unstaged change.\n")
            elif kind == "staged":
                (repository / "staged.txt").write_text("Staged selection.\n", encoding="utf-8")
                _git(["add", "--", "staged.txt"], cwd=repository)
            elif kind == "conflicted":
                _git(["switch", "-c", "fixture-conflict"], cwd=repository)
                (repository / "README.md").write_text("Conflict branch.\n", encoding="utf-8")
                _git(["commit", "-am", "fixture: conflicting branch"], cwd=repository)
                _git(["switch", "main"], cwd=repository)
                (repository / "README.md").write_text("Main branch conflict.\n", encoding="utf-8")
                _git(["commit", "-am", "fixture: main conflict"], cwd=repository)
                merge = _git(["merge", "fixture-conflict"], cwd=repository, check=False)
                if merge.returncode == 0:
                    raise RuntimeError("Conflict fixture merge unexpectedly succeeded.")
            elif kind == "missing-identity":
                _git(["config", "--local", "--unset", "user.name"], cwd=repository)
                _git(["config", "--local", "--unset", "user.email"], cwd=repository)
        yield repository
    finally:
        for key, value in prior_env.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def snapshot_repository(repo: Path) -> dict[str, str]:
    """Capture refs, HEAD, index bytes, and working-file digests."""
    repo = Path(repo).resolve()
    refs = _git(["for-each-ref", "--format=%(refname) %(objectname)"], cwd=repo).stdout.strip()
    head_result = _git(["rev-parse", "--verify", "HEAD"], cwd=repo, check=False)
    head = head_result.stdout.strip() if head_result.returncode == 0 else "<unborn>"
    symbolic_head_result = _git(["symbolic-ref", "-q", "HEAD"], cwd=repo, check=False)
    symbolic_head = symbolic_head_result.stdout.strip() if symbolic_head_result.returncode == 0 else "<detached>"
    index_result = _git(["rev-parse", "--git-path", "index"], cwd=repo)
    index = Path(index_result.stdout.strip())
    if not index.is_absolute():
        index = repo / index
    snapshot = {
        "refs": refs,
        "HEAD": head,
        "symbolic-HEAD": symbolic_head,
        "index": hashlib.sha256(index.read_bytes()).hexdigest() if index.is_file() else "<missing>",
    }
    for path in sorted(repo.rglob("*")):
        relative = path.relative_to(repo)
        if ".git" in relative.parts or not path.is_file():
            continue
        try:
            snapshot[f"working:{relative.as_posix()}"] = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError:
            snapshot[f"working:{relative.as_posix()}"] = "<unreadable>"
    return snapshot
