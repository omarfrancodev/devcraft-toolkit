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
    output_encoding = "mbcs" if os.name == "nt" else "utf-8"
    return subprocess.run(["git", *args], cwd=cwd, env=child_env, check=check, capture_output=True, text=True, encoding=output_encoding)


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
    """Create a normal, unborn, linked-worktree, or detached Git fixture."""
    if kind not in {"normal", "unborn", "linked-worktree", "detached"}:
        raise ValueError(f"Unsupported fixture kind: {kind}")
    root = Path(root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    repository = root / dirname
    if kind == "linked-worktree":
        source = root / f"{dirname}-source"
        _init_repository(source, root)
        _commit_readme(source)
        _git(["worktree", "add", "-b", "fixture-linked", str(repository)], cwd=source)
        return_value = repository
    else:
        _init_repository(repository, root)
        if kind in {"normal", "detached"}:
            _commit_readme(repository)
        if kind == "detached":
            _git(["checkout", "--detach", "HEAD"], cwd=repository)
        elif kind == "unborn":
            (repository / "README.md").write_text("Untracked fixture.\n", encoding="utf-8")
        return_value = repository
    yield return_value


def snapshot_repository(repo: Path) -> dict[str, str]:
    """Capture refs, HEAD, index bytes, and working-file digests."""
    repo = Path(repo).resolve()
    refs = _git(["for-each-ref", "--format=%(refname) %(objectname)"], cwd=repo).stdout.strip()
    head_result = _git(["rev-parse", "--verify", "HEAD"], cwd=repo, check=False)
    head = head_result.stdout.strip() if head_result.returncode == 0 else "<unborn>"
    index_result = _git(["rev-parse", "--git-path", "index"], cwd=repo)
    index = Path(index_result.stdout.strip())
    if not index.is_absolute():
        index = repo / index
    snapshot = {
        "refs": refs,
        "HEAD": head,
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
