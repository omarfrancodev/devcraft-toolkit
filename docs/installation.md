# Installation

## Preview distribution

Download `devcraft-toolkit-v0.1.0-preview.1.zip` and `SHA256SUMS.txt` from the [v0.1.0-preview.1 release](https://github.com/omarfrancodev/devcraft-toolkit/releases/tag/v0.1.0-preview.1). Verify the ZIP's SHA-256 against that file before extracting it.

The ZIP contains the versioned source repository under `devcraft-toolkit-v0.1.0-preview.1/`. Install only the selected complete folders under `skills/`, including their `references/` and `assets/` directories when present, and include all required skill dependencies listed below. The repository's development scripts and tests do not need to be installed with a skill.

This is an experimental pre-release. Package integrity and resource containment checks do not verify a harness's native skill discovery or loading. See [compatibility evidence and limits](compatibility.md).

## Available skills

This distribution contains seven usable skills:

- `using-devcraft-toolkit` — entry and composition; requires the two supporting skills below.
- `git-working-directory-policy` — standalone repository and worktree context discovery.
- `git-safety-check` — read-only `inspect`, `commit`, or `publish` preflight; requires `git-working-directory-policy`.
- `conventional-commits-style` — standalone Conventional Commit message drafting and review; has no skill dependencies and does not require a Git repository.
- `todo-workflow-controller` — portable multi-step progress tracking with required gates, blockers, and handoffs; has no skill dependencies or mandatory tracking-tool requirement.
- `natural-language-report-writer` — evidence-based reports using the user's language and requested format; it has no skill dependencies and writes a local file only when the user selects a destination.
- `validation-discovery` — project check discovery and explicitly requested local validation; it has no skill dependencies.

For the composed entry, install the full dependency group: `using-devcraft-toolkit`, `git-working-directory-policy`, and `git-safety-check`. For repository context only, install `git-working-directory-policy` by itself. Install `conventional-commits-style` alone for commit-message formatting, or alongside the entry and its foundation group to enable optional routing. Install `todo-workflow-controller` alone for portable progress tracking, or alongside the entry and foundation group to enable optional routing. Install `natural-language-report-writer` alone for evidence-based reporting, or alongside the entry and foundation group to enable optional reporting routes. It has no hard dependency on the entry. None of these optional skills is a hard dependency of the entry. If the entry is installed without an optional capability, it reports that capability as unavailable. Select each skill explicitly in the target harness.

Select `validation-discovery` directly in the target harness to discover or run project checks, or install it alongside the entry to enable optional routing. Its `references/` folder is part of the standalone installation. It may be installed without the toolkit entry or any other skill; it is not a hard entry dependency.

Copy the chosen complete skill folder, including its local `references/` and `assets/` when present, into the skill location supported by the target harness. Consult that harness's current documentation for its skill discovery location. The repository catalog does not install or resolve dependencies, and the entry skill does not require the repository root at runtime.

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
