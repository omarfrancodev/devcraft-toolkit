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

## Proposing changes

Use the project's [change description template](docs/contribution-template.md) when preparing a proposed change. Write the title in Spanish using `type(scope): concrete outcome`, or `type: concrete outcome` when no useful scope applies. Do not invent tickets or versions, or repeat the title in the description.

Keep the sections in the template's order. Include compatibility and integration details when contracts, consumers, migrations, or follow-up steps matter to reviewers; include references only when they point to existing, accessible material. Remove optional sections that do not apply and all drafting comments before submitting.

Match the validation claims to the evidence. For documentation-only changes, a concise summary and checks for links and consistency are enough; do not invent behavioral test results. State which checks ran, their observed results, and relevant omissions, failures, or blockers. Do not describe an unpublished release or unverified external compatibility as complete.

Keep the description focused on the change. Exclude local absolute paths, credentials, private logs, artifacts from unrelated projects, and internal agent details. References should help reviewers without duplicating the linked content.

Use the same finalized description whether submitting through a web interface, CLI, API, or an agent. Provide the body explicitly instead of assuming the submission tool will fill it in, then verify that the published description matches. The template organizes the explanation; it does not validate claims or authorize publication, approval, or merging. Follow the authorization rules for each action.
