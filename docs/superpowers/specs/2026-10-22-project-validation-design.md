# Project Validation Discovery Design

Date: 2026-10-22
Status: Proposed; product implementation has not started.
Capability: validation-discovery

## Product goal

Find project-defined validation commands, assess their effects, and execute only the checks actually requested and permitted.

This increment is independently deliverable. It extends the current seventeen-capability catalog without changing any other planned capability into an available implementation.

## Global constraints

- Source instructions, documentation, examples and default templates are English; user-facing output uses explicit user preference, then request language, then English when indeterminate.
- Technical identifiers, schema keys, command syntax and supplied data identifiers remain unchanged by translation.
- Tests, fixtures, scenarios and retained evaluations live under tests/skills/<normalized_skill_name>/; root tests/integration/ is only for multiple named skills.
- Installed skills use only their bundled resources and explicitly declared skill dependencies; repository tooling and catalog.json are development resources.
- Implementation must be understandable from repository-local requirements and accessible official technical references, without private conversations, personal paths or unavailable files.
- Catalog status stays planned until structural checks and actual behavioral evaluation justify available; record unexecuted cases as limitations.
- No new coordinator, CCR/Jira integration, plugin manifest, installer, release automation or runtime orchestration engine is included.
- Use Python 3.11+ and the existing PyYAML>=6.0,<7.0 development setup; add no dependencies or helpers without a demonstrated need.

## Architecture and dependencies

Use instruction-first SKILL.md content, with only the local reference or asset files listed below. The skill has requires=[] and must work independently of the toolkit entry. Reuse the language resolved by a caller, or resolve it using the project precedence when invoked alone.

Existing repository context and evidence may be consumed when provided; they are not required Git or platform dependencies. No new callable runtime API, schema version, installed root catalog dependency or orchestration service is introduced.

## Inputs and output

Inputs are the selected project root, requested scope, mode discover or run, optional explicit command, project instructions and resolved language. Git is optional; reuse already supplied repository context when applicable.

Discover is the default: inspect project definitions and return candidates without executing them. Run applies when the user or an authorized composing operation requests validation. A command found in configuration is not by itself permission to run it.

Return candidates with source location, exact command/working directory, intended check, expected effects and decision; execution results include actual command, exit status, evidence and limitations. Distinguish passed, failed, not_run, blocked and not_detected. Missing or skipped checks never count as passed. These are instructional results, not a new mandatory data file.

## Discovery and safety decisions

Start with an explicit user command, then relevant project instructions and package.json, Makefile, pyproject.toml, composer.json, solution/project files or task-runner definitions actually present. Inspect only the applicable project/subproject. Configuration alone does not imply an executable command: report absent definitions instead of inventing one.

Inspect the body of wrapper commands and relevant hooks, dependencies, environment and output locations. A friendly name such as test or lint does not prove safety. Shell operators are a reason to inspect the entire composition, not a universal rejection rule. A fully understood project-defined local composite may run in run mode when its effects are authorized.

Autofix, installation/update, cleanup, database migration, deployment, publication, destructive commands and external business mutations are outside ordinary validation. Do not run them merely because a wrapper includes them. Unknown or material unapproved effects block the affected candidate or require a precise decision; continue independent in-scope checks when safe.

Expected local build/test artifacts can be permitted when scoped to an owned worktree or temporary directory and disclosed. Unexpected source/index/working-file changes are a material result: preserve them, report them and pause affected downstream writes. Do not silently repair, reset, clean or stage anything.

## Execution behavior

Use the actual supported terminal working-directory parameter or git -C where appropriate; use the project's documented subproject root. Do not assume a persistent shell or manufacture an unavailable tool.

Inspect then execute the selected checks only. Respect required project gates; a first successful command does not establish all required gates. Bounded checks that already passed are not rerun without changed inputs, an uncovered required scenario or unreliable evidence. Retry only for an observed transient cause, once, and retain the first failure. Do not interpret a confirmed user waiver as an executed success.

## Boundaries and acceptance

No required skill dependencies and no new execution framework/helper are included. A non-Git directory can be a valid project. CCR, credentials, network installation and remote publication are not prerequisites.

Use temporary self-contained project fixtures. Cases cover discover mode with no execution, a safe requested local check, a failing check, unavailable execution, no command definitions, a wrapper hiding autofix/install, a permitted inspected composite, missing dependency, a subproject path with spaces, required multi-check coverage and unexpected writes. Unsafe fixtures use harmless markers and must not be executed. Preserve the preexisting repository snapshot and never use production/shared databases in a scenario.

## Files and test ownership

- skills/validation-discovery/SKILL.md
- skills/validation-discovery/references/check-selection.md
- tests/skills/validation_discovery/scenarios/discovery.md
- tests/skills/validation_discovery/scenarios/execution.md
- tests/skills/validation_discovery/fixtures/local-project/check.py
- tests/skills/validation_discovery/fixtures/local-project/package.json
- tests/skills/validation_discovery/evaluations/<run>.md when explicitly retained

Tests use the canonical owner validation-discovery; the Python-compatible test package is validation_discovery. Introduce unit/integration test code only for a real executable contract, not to check whether instructions contain a chosen sentence. Scenario fixtures and evidence remain outside the installed skill folder.

## Catalog, routing and documentation

After actual verification, mark only validation-discovery available and leave requires=[] in catalog.json. Add its installed-capability route to using-devcraft-toolkit without widening the entry's hard dependency group. Route only when the skill is actually installed; a missing optional capability remains a visible limitation.

Update README.md, docs/architecture.md, docs/composition.md, docs/installation.md, docs/compatibility.md and docs/roadmap.md to match observed availability. Derive current counts from catalog.json instead of assuming that other increments have already landed. Keep the foundation spec's historical three-skill delivery record intact.

Foundation context/preflight stay read-only. If this capability allows explicit file output or check execution, document those effects precisely in AGENTS.md and the scenario protocol; do not change the permissions of unrelated skills.

## Acceptance and evidence

Run the existing repository suite and structural validator. Execute the owned behavioral scenarios on the actual available harness; use the common protocol and record executed/limited outcomes. Structural success alone is not a behavioral pass. A manually followed skill is recorded as a self-evaluation, not a dynamically loaded or independent evaluation.

No network connection, unrelated source tree or tool absent from the environment is needed to understand the requirements. A limited scenario remains limited and must not become a blanket compatibility claim. Leave future coordinators planned.

## References

- [Repository architecture](../../architecture.md), [composition](../../composition.md) and [scenario protocol](../../../tests/scenarios/README.md): project boundaries and evidence requirements.

The maintained implementation requirements are fully stated above. References explain standards or existing project contracts; they do not substitute for missing product decisions.
