# Contributing

## Development setup

Use Python 3.11 or newer. Create an isolated environment and install the development dependency:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

On Windows, activate with `.venv\Scripts\Activate.ps1`.

## Checks

Run commands from the repository root with an explicit terminal working directory:

```sh
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repository.py --root .
git diff --check
```

Tests stay under `tests/`, grouped by skill and scope. Python test package names replace canonical skill-name hyphens with underscores. Keep fixtures local to the tests that own them unless multiple suites genuinely share them.

Behavioral scenarios also stay under the owning skill's subtree in `tests/skills/`; cross-skill scenarios belong under `tests/integration/`. Record the actual harness, version, evidence, and limitations. Structural validation alone does not prove that an assistant follows a skill or that a harness is compatible. See [the evaluation protocol](tests/scenarios/README.md) and [compatibility notes](docs/compatibility.md).

Before any Git write, inspect the repository-local `user.name` and `user.email`. Do not silently change global or local identity. The foundation skills themselves only inspect Git state and do not stage or commit changes.

For the available skill group and standalone installation choices, see [installation](docs/installation.md). Do not add empty planned skills, harness manifests, or integrations outside an approved design.
