# Installation

## Available skills

This distribution contains four usable skills:

- `using-devcraft-toolkit` — entry and composition; requires the two supporting skills below.
- `git-working-directory-policy` — standalone repository and worktree context discovery.
- `git-safety-check` — read-only `inspect`, `commit`, or `publish` preflight; requires `git-working-directory-policy`.
- `conventional-commits-style` — standalone Conventional Commit message drafting and review; has no skill dependencies and does not require a Git repository.

For the composed entry, install the full dependency group: `using-devcraft-toolkit`, `git-working-directory-policy`, and `git-safety-check`. For repository context only, install `git-working-directory-policy` by itself. Install `conventional-commits-style` alone for commit-message formatting, or alongside the entry and its foundation group to enable optional routing. The formatter is not a hard dependency of the entry. Select each skill explicitly in the target harness.

Copy the chosen complete skill folder, including its local `references/`, into the skill location supported by the target harness. Consult that harness's current documentation for its skill discovery location. The repository catalog does not install or resolve dependencies, and the entry skill does not require the repository root at runtime.

No automatic installer or native plugin manifest is included. Standalone installation must include the declared dependency closure. Compatibility with a harness is documented only when that harness and its version have actually been exercised; see [compatibility](compatibility.md).

## Development tools

The repository validator and test suite are development tools, not dependencies of installed skills. Use Python 3.11+ and install `requirements-dev.txt` in an isolated environment:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

On Windows, activate with `.venv\Scripts\Activate.ps1`. From the repository root, run:

```sh
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repository.py --root .
```

These commands validate maintained source and fixtures. They do not establish behavior on every assistant harness.
