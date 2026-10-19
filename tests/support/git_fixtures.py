"""Git repositories for isolated integration tests; never used by skills."""

from __future__ import annotations

import hashlib
import os
import stat
import subprocess
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


def _git(args: list[str], *, cwd: Path, env: dict[str, str] | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    child_env = os.environ.copy()
    for key in tuple(child_env):
        if key.startswith("GIT_CONFIG_") or key in {
            "GIT_AUTHOR_NAME", "GIT_AUTHOR_EMAIL", "GIT_COMMITTER_NAME", "GIT_COMMITTER_EMAIL",
        }:
            child_env.pop(key, None)
    child_env["GIT_CONFIG_NOSYSTEM"] = "1"
    if env:
        child_env.update(env)
    return subprocess.run(["git", *args], cwd=cwd, env=child_env, check=check, capture_output=True, text=True, encoding="utf-8")


def _init_repository(path: Path, root: Path, env: dict[str, str]) -> None:
    _git(["init", str(path)], cwd=root, env=env)
    _git(["symbolic-ref", "HEAD", "refs/heads/main"], cwd=path, env=env)
    _git(["config", "--local", "user.name", "Fixture User"], cwd=path, env=env)
    _git(["config", "--local", "user.email", "fixture@example.invalid"], cwd=path, env=env)


def _commit_readme(path: Path, env: dict[str, str]) -> None:
    (path / "README.md").write_text("Fixture repository.\n", encoding="utf-8")
    _git(["add", "--", "README.md"], cwd=path, env=env)
    _git(["commit", "-m", "fixture: create repository"], cwd=path, env=env)


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
    fixture_env = {"GIT_CONFIG_GLOBAL": str(global_config), "GIT_CONFIG_NOSYSTEM": "1"}
    repository = root / dirname
    if kind == "linked-worktree":
        source = root / f"{dirname}-source"
        _init_repository(source, root, fixture_env)
        _commit_readme(source, fixture_env)
        _git(["worktree", "add", "-b", "fixture-linked", str(repository)], cwd=source, env=fixture_env)
    else:
        _init_repository(repository, root, fixture_env)
        if kind != "unborn":
            _commit_readme(repository, fixture_env)
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


def snapshot_repository(repo: Path) -> dict[str, str]:
    """Capture Git metadata and working-file contents and modes without reading objects."""
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

    git_dir = Path(_git(["rev-parse", "--absolute-git-dir"], cwd=repo).stdout.strip()).resolve()
    common_text = _git(["rev-parse", "--git-common-dir"], cwd=repo).stdout.strip()
    common_dir = Path(common_text)
    if not common_dir.is_absolute():
        common_dir = (repo / common_dir).resolve()
    roots = [("common", common_dir)] if common_dir == git_dir else [("worktree", git_dir), ("common", common_dir)]
    for scope, git_root in roots:
        snapshot[f"git:{scope}/"] = "<directory>"
        for current, directories, files in os.walk(git_root):
            current_path = Path(current)
            relative_dir = current_path.relative_to(git_root)
            directories[:] = [name for name in directories if name != "objects"]
            for directory in directories:
                directory_path = current_path / directory
                relative = (relative_dir / directory).as_posix()
                snapshot[f"git:{scope}/{relative}/"] = "<directory>"
            for filename in files:
                path = current_path / filename
                relative = (relative_dir / filename).as_posix()
                try:
                    file_stat = path.lstat()
                    snapshot[f"git-mode:{scope}/{relative}"] = str(stat.S_IMODE(file_stat.st_mode))
                    contents = os.readlink(path).encode("utf-8") if path.is_symlink() else path.read_bytes()
                    snapshot[f"git:{scope}/{relative}"] = hashlib.sha256(contents).hexdigest()
                except OSError:
                    snapshot[f"git:{scope}/{relative}"] = "<unreadable>"

    for current, directories, files in os.walk(repo):
        current_path = Path(current)
        directories[:] = [name for name in directories if name != ".git"]
        for filename in files:
            path = current_path / filename
            relative = path.relative_to(repo)
            try:
                file_stat = path.lstat()
                snapshot[f"working-mode:{relative.as_posix()}"] = str(stat.S_IMODE(file_stat.st_mode))
                contents = os.readlink(path).encode("utf-8") if path.is_symlink() else path.read_bytes()
                snapshot[f"working:{relative.as_posix()}"] = hashlib.sha256(contents).hexdigest()
            except OSError:
                snapshot[f"working:{relative.as_posix()}"] = "<unreadable>"
    return snapshot
