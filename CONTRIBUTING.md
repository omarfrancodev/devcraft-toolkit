# Contributing

## Development setup

Use Python 3.11 or newer. Create an isolated environment and install the development dependency:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

On Windows, activate with `.venv\\Scripts\\Activate.ps1`.

## Checks

Run commands from the repository root with an explicit terminal working directory:

```sh
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repository.py --root .
git diff --check
```

Tests stay under `tests/`, grouped by skill and scope. Python test package names replace canonical skill-name hyphens with underscores. Keep fixtures local to the tests that own them unless multiple suites genuinely share them.

Before any Git write, inspect the repository-local `user.name` and `user.email`. Do not silently change global or local identity. The foundation skills themselves only inspect Git state and do not stage or commit changes.
