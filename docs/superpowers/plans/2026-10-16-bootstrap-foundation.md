# Devcraft Toolkit Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** Establish a verifiable, portable repository foundation with three real skills and centralized tests, without migrating the full suite.

**Architecture:** A project-level catalog distinguishes available capabilities from future work. Skills remain instruction-first, with local references and explicit dependencies; Python tooling validates the repository but is not a hidden runtime dependency of installed skills.

**Tech Stack:** Markdown, YAML frontmatter, JSON, Git, Python 3.11+, PyYAML>=6.0,<7.0, and unittest.

**Spec:** ../specs/2026-10-16-bootstrap-foundation-design.md

**State:** Planning complete; implementation has not started. Review both documents before executing.
**Updated:** 2026-10-17 (CCR excluded; tests grouped by skill and scope).
**Execution checkout:** .worktrees/bootstrap-foundation, branch feat/bootstrap-foundation.
**Baseline:** README.md and .gitignore, with the foundation spec added on the planning branch.

## Global Constraints

- Project identity is Devcraft Toolkit; the repository slug is devcraft-toolkit.
- Source skill instructions, documentation, examples and default templates are written in English.
- User-facing language precedence is explicit user preference, then the language of the user's request, then English when neither can be determined.
- Resolve language once for an execution; an explicit later user instruction can update it.
- Translate natural-language content and visible template labels; preserve technical identifiers, schema keys and command syntax.
- All tests, scenarios, fixtures and evaluation records live under the repository-root tests/ directory, never under skills/<name>/.
- Group skill-owned tests by skill first, then by scope under tests/skills/<skill_package>/; reserve repository/ and shared directories for genuine infrastructure or cross-skill coverage.
- A skill's test package name is its canonical name with hyphens replaced by underscores; keep the canonical name in scenario/evaluation ownership.
- Every available skill is self-contained except for explicitly cataloged dependencies on other available skills.
- Planned skills have catalog entries but no discoverable SKILL.md placeholders.
- Instructions and catalog dependencies do not grant tools, permissions, user authorization or automatic installation.
- Repository identity is inspected locally before Git writes; never silently replace or infer user.name or user.email.
- Tool execution uses explicit working directories or git -C; terminal persistence is never assumed.
- Missing todo or structured-question tools alone must not prevent an otherwise safe workflow.
- Never fabricate execution, checks, review independence, compatibility or remote state.
- Milestone 1 performs no product Git writes, network operations or credential changes through its skills.
- Development tooling uses Python 3.11+ with PyYAML>=6.0,<7.0; unittest is the test runner.
- Git is required for Git-specific skills and integration fixtures, not for merely reading their instructions.
- Jira and CCR integration are outside the current scope; CCR has no catalog entry, dependency, routing hook, test folder or migration task in this project.
- Full coordinators, installable plugin manifests and release automation are deferred.

## Review Focus

1. Paths with spaces/Unicode or symlink escapes must preserve containment; Tasks 1-3 pin these cases.
2. Existing index selections and volatile repository state must survive preflight untouched; Task 4 owns the before/after scenarios.
3. A clean published branch and an unborn commit preparation require different verdicts; Tasks 3-4 own their fixtures and outcomes.
4. Spanish/other-language requests, explicit overrides and indeterminate inputs must share one language decision without translating identifiers; Task 5 owns these scenarios.
5. Planned/missing capabilities, dependency cycles and absent harness tools must yield honest limitations without accidental fallback execution; Tasks 1, 4 and 5 cover them.

## Task boundaries and execution rules

Complete each task's verification before its commit. Run all development commands from the isolated checkout; use an interpreter that actually resolves to Python 3.11+, not an unverified Windows app alias. For a local virtual environment, substitute its interpreter for python in the commands below.

Skill behavior is tested through real scenario execution, not substring assertions against SKILL.md. Automated fixture tests establish raw Git conditions; they do not prove a model follows a skill. Record execution limitations honestly.

Stage exact owned files only. Before any commit verify the repository-local identity still resolves to omarfrancodev <fofe2803@gmail.com>; if it differs, stop for the human's decision. Do not change global identity or bypass hooks. Commit examples use English source conventions; adapt subjects to an explicit/current user-language instruction when executing.

## Task 1: Establish the inventory and catalog validation

**Files:**
- Create: catalog.json, requirements-dev.txt, scripts/__init__.py, scripts/validate_repository.py.
- Create: tests/__init__.py, tests/repository/__init__.py, tests/repository/test_repository_validation.py.
- Create: AGENTS.md, CONTRIBUTING.md, docs/architecture.md.
- Modify: README.md.

**Interfaces:**
- Produces frozen ValidationIssue(code: str, path: str, message: str).
- Produces validate_repository(root: Path) -> list[ValidationIssue].
- Produces CLI: python scripts/validate_repository.py --root <path>, exits 0 when valid, 1 for invalid source or a missing dependency.
- Catalog schema and the exact seventeen names/roles come from the spec; all entries begin planned in this task. Paths are skills/<name>; initially requires=[].
- Stable issue codes introduced here: catalog-schema, duplicate-name, invalid-path, unknown-dependency, dependency-cycle, unavailable-dependency.

- [ ] **Step 1: Add temporary-root tests for catalog validity and rejection.** Test valid small catalogs and a separate accepted-inventory assertion for the project's seventeen names. Add tests named test_duplicate_name, test_absolute_or_parent_path, test_unknown_dependency, test_dependency_cycle, and test_available_requires_planned. Each asserts the corresponding issue code and offending relative path rather than an entire message.
- [ ] **Step 2: Run the focused suite and observe failure from the absent validator.** Command: python -m unittest discover -s tests/repository -p "test_*.py" -v. A missing implementation is the expected initial failure; fixture/setup errors must be corrected first.
- [ ] **Step 3: Implement catalog parsing and validation using JSON and safe path resolution.** Use PyYAML only for the later frontmatter task. Reject wrong container/field types without an uncaught traceback. Add the minimum requirements-dev.txt dependency. Missing yaml at CLI startup gives a useful install instruction.
- [ ] **Step 4: Write the catalog and development conventions.** Document English source/user-language output, root tests, explicit workdir, local identity inspection and no future placeholders. README lists the foundation as under development; it must not advertise all planned capabilities as usable.
- [ ] **Step 5: Verify and commit.** Install development requirements in an isolated environment when permitted, run the focused suite and the validator, inspect git diff --check, and commit the exact task files with subject chore: establish the toolkit catalog and validation base.

## Task 2: Validate actual skill resources and external test placement

**Files:**
- Modify: scripts/validate_repository.py, tests/repository/test_repository_validation.py.

**Interfaces:**
- Consumes Task 1 ValidationIssue and validate_repository without signature changes.
- Adds codes: skill-frontmatter, skill-body, missing-resource, resource-escape, skill-local-tests, planned-placeholder, unlisted-skill, test-ownership.
- Supported local-link surface: Markdown inline links outside inline/fenced code, optional anchors, and paths relative to the skill root. HTTP(S) URLs and fragment-only links are not local files. Do not crawl the network.

- [ ] **Step 1: Build temporary skill trees and add rejection tests.** Cover malformed YAML; missing/wrong name or description; name mismatch/limits; empty body; missing local resource; ../ escape; a skill-local symlink escaping its root; tests/ or test_*.py inside the skill; a planned entry with SKILL.md; and an uncataloged discoverable skill. Skip symlink creation only with a specific observed OS limitation.
- [ ] **Step 2: Add positive link/structure tests.** Include a linked local file with an anchor, a remote URL, code fences showing example links, inline code, and a root tests/ fixture. Add ownership cases for a correctly normalized skill package and an unknown skill package. Explicit repository/shared multi-skill tests are valid; reviewers assess whether a shared test genuinely belongs there instead of inferring semantic ownership through wording. These must not produce false missing-resource/skill-local-tests issues; ownership violations return test-ownership.
- [ ] **Step 3: Run the focused tests and observe the new failures, then implement safe frontmatter and resource validation.** Use yaml.safe_load and the spec's required metadata constraints. Resolve real paths for containment; do not infer runtime dependencies from arbitrary prose.
- [ ] **Step 4: Run all repository tests and the CLI against the current checkout.** The all-planned catalog is valid at this intermediate task. Tests must remain under the root tests/ directory; no source files are rewritten by validation.
- [ ] **Step 5: Commit the two exact files after git diff --check.** Suggested subject feat: validate skill resources and test boundaries.

## Task 3: Deliver portable repository-context discovery

**Files:**
- Create: skills/git-working-directory-policy/SKILL.md and references/context.md inside that skill.
- Create: tests/support/__init__.py, tests/support/git_fixtures.py, tests/skills/__init__.py.
- Create: tests/skills/git_working_directory_policy/__init__.py, tests/skills/git_working_directory_policy/integration/__init__.py, tests/skills/git_working_directory_policy/integration/test_context_fixtures.py.
- Create: tests/scenarios/README.md, tests/skills/git_working_directory_policy/scenarios/context.md.
- Modify: catalog.json.

**Interfaces:**
- Test-only context manager git_fixture(kind: str, root: Path, *, dirname: str = "repo") -> Iterator[Path].
- Supported kinds introduced here: normal, unborn, linked-worktree, detached.
- Test-only snapshot_repository(repo: Path) -> dict[str, str] captures refs, HEAD, index digest, pseudo-ref and other Git metadata outside the object database, plus working-file content digests and modes.
- Skill output follows the spec's repository-context contract; it is plain sourced information, not a callable Python API.
- Mark git-working-directory-policy available with requires=[] only after its scenarios are actually exercised.

- [ ] **Step 1: Write fixture tests for a repository whose path contains spaces and Unicode, an unborn main branch with one untracked README.md, a linked worktree and detached HEAD.** Assert fixture Git evidence directly, including differing Git/common directories for linked worktrees. All writes are confined to a temporary root; Git identity is configured locally inside fixtures.
- [ ] **Step 2: Run python -m unittest discover -s tests/skills/git_working_directory_policy/integration -p "test_*.py" -v and observe failures for missing helpers.** Implement only the fixture helpers, then rerun. Use subprocess argument lists, explicit cwd, checked return codes and local Git configuration; never interpolate a shell command.
- [ ] **Step 3: Define the behavioral scenarios before authoring the skill.** Cover separate terminal invocations, explicit workdir/git -C, missing Git, non-repository input, submodule versus worktree identity and missing/inherited Git identity. Expected evidence is correct context, unchanged fixture state and no invented identity.
- [ ] **Step 4: Author the skill and its local reference.** Remove persistent-terminal assumptions and mandatory approval for git -C. Resolve requested scope before inspecting unrelated repositories. Use the shared language rule but do not load unrelated toolkit skills.
- [ ] **Step 5: Execute the context scenarios with the actual available harness.** Follow the skill against raw fixtures, compare snapshots, and record actual tool/platform limitations. If retaining evaluation notes, use tests/skills/git_working_directory_policy/evaluations/<run>/; do not put them in the installed skill folder. Document which scenarios were run versus limited.
- [ ] **Step 6: Mark the skill available, rerun all tests and the validator, then commit the exact task files.** Suggested subject feat: add portable Git repository context.

## Task 4: Deliver intent-aware read-only Git preflight

**Files:**
- Create: skills/git-safety-check/SKILL.md and references/preflight.md inside that skill.
- Create: tests/skills/git_safety_check/__init__.py, tests/skills/git_safety_check/integration/__init__.py, tests/skills/git_safety_check/integration/test_preflight_fixtures.py.
- Create: tests/skills/git_safety_check/scenarios/preflight.md, tests/integration/scenarios/context-to-preflight.md.
- Modify: tests/support/git_fixtures.py, catalog.json. Context-skill tests remain under their own owner; shared fixture code is extended without copying it.

**Interfaces:**
- Extend git_fixture kinds with dirty, staged, conflicted and missing-identity.
- Preflight inputs: repository context plus intent inspect|commit|publish.
- Preflight outcomes: ready|no_op|blocked|needs_decision|limited, with observed evidence and affected intent.
- Mark git-safety-check available with requires=["git-working-directory-policy"] after behavioral verification.

- [ ] **Step 1: Add and run failing fixture tests in tests/skills/git_safety_check/integration/test_preflight_fixtures.py for staged, dirty, conflicted and missing-identity states.** Run python -m unittest discover -s tests/skills/git_safety_check/integration -p "test_*.py" -v. Extend the shared helpers without changing earlier fixture semantics. Identity-free fixtures must neutralize inherited global identity within the child process/fixture, not edit the developer's configuration.
- [ ] **Step 2: Define the scenario matrix and expected decisions.** Clean committed repository: publish ready, commit no_op. Unborn repository: inspect permitted, commit preparation permitted with a known identity, publish blocked. Conflicts: mutation blocked. Missing identity: inspect still permitted, future commit blocked. Detached HEAD: mutation needs a branch decision.
- [ ] **Step 3: Add preservation and tools scenarios.** Existing staged hunks remain intact; no stage/unstage/commit/switch/fetch/push/stash runs. Global work identity without a resolved personal/work choice requires clarification before a write. Missing todo/question tools do not imply safety failure; an unanswered material decision still pauses dependent work.
- [ ] **Step 4: Write the skill and reference, using read-only Git commands and optional locks disabled where supported.** Do not copy the legacy empty-worktree stop into every intent. A ready result permits only the requested preflight conclusion.
- [ ] **Step 5: Execute the scenarios and compare snapshots before/after.** The cross-skill scenario tests/integration/scenarios/context-to-preflight.md names both git-working-directory-policy and git-safety-check: change state after context discovery and require refreshed preflight evidence. Retain skill-only evaluation notes under tests/skills/git_safety_check/evaluations/<run>/ and joint evidence under tests/integration/evaluations/<run>/. Record limitations rather than declaring an unexecuted scenario passed.
- [ ] **Step 6: Mark the skill available, run the automated suites and repository validator, and commit the exact task files.** Suggested subject feat: add intent-aware Git safety checks.

## Task 5: Deliver the toolkit entry and language-aware composition

**Files:**
- Create: skills/using-devcraft-toolkit/SKILL.md and references/composition.md inside that skill.
- Create: docs/language.md, docs/composition.md, tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md.
- Modify: catalog.json.

**Interfaces:**
- Consumes the repository-context and preflight outputs from Tasks 3-4.
- Instructional run context preserves resolved language, its source, requested scope, decisions and actually available capabilities; do not introduce a runtime engine or persisted JSON state machine.
- Mark using-devcraft-toolkit available with requires=["git-working-directory-policy", "git-safety-check"].

- [ ] **Step 1: Define realistic routing and language scenarios.** Include English, Spanish, one additional language, explicit language override, an indeterminate request defaulting to English, and an explicit later language change. Check meaning and visible labels, while technical identifiers stay unchanged.
- [ ] **Step 2: Add missing-capability and scope scenarios.** Commit, publish and activity requests must report planned/not installed in this distribution. Do not add a CCR-specific route, fallback, dependency or integration test. An unrelated request must not force toolkit entry. Individually installed skills must not attempt to open catalog.json from an unavailable repository root.
- [ ] **Step 3: Author the entry and local composition reference.** Discover installed skills through the actual harness/catalog when available; do not imply the repository catalog is deployed with an individual skill. Use the catalog only for maintained development inventory. The dependency group is explicit, not auto-installed.
- [ ] **Step 4: Document language and composition once at suite level and embed concise applicable rules in each available skill.** Avoid links from installed skills to out-of-folder root docs. Reuse an already resolved context and refresh only facts that became stale.
- [ ] **Step 5: Evaluate the scenarios on the actual available harness and mark the entry available.** Preserve exact observed compatibility and missing-tool limitations. Retain skill-owned evidence under tests/skills/using_devcraft_toolkit/evaluations/<run>/. Structural tests are insufficient for a language/behavior claim.
- [ ] **Step 6: Run all suites and validation and commit exact task files.** Suggested subject feat: add toolkit entry and language-aware routing.

## Task 6: Document a usable foundation and verify the complete increment

**Files:**
- Create: docs/installation.md, docs/compatibility.md, docs/migration.md.
- Modify: README.md, CONTRIBUTING.md, docs/architecture.md.
- Modify validation/tests only if a newly evidenced defect requires it.

**Interfaces:**
- Final catalog contains exactly three available entries and fourteen planned entries from the spec.
- Installation documentation specifies the available three-skill dependency group and standalone context skill, plus explicit manual selection. It does not promise automatic dependency resolution or validated plugin installation.
- Compatibility records separate intended portability from observed harness/version/scenario execution.

- [ ] **Step 1: Document setup and real commands.** Use Python 3.11+ and install requirements-dev.txt in an isolated environment. Document these exact verification commands from the repository root:

~~~sh
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repository.py --root .
~~~
- [ ] **Step 2: Document selective installation and planned scope.** CCR remains exclusively in its separate project until its owner selects a stable version and authorizes a new integration design. It has no active catalog entry, planned migration task, routing hook or test subtree here. No license choice, empty future SKILL.md files, GitHub/GitLab/Jira credentials or generated vendor manifests enter this milestone.
- [ ] **Step 3: Run acceptance from a clean environment and confirm discovery actually finds the nested test suites.** Root, repository, skills, each Python skill package, its integration package and shared support __init__.py files make discovery/imports explicit on Python 3.11. Hyphens in canonical skill names map to underscores in test package names. Zero discovered tests is not a passing suite.
- [ ] **Step 4: Run repository validation, inspect git diff --check and review all retained behavioral results/limitations.** Confirm seventeen catalog entries, only three actual skills, all tests outside skill folders and assigned by skill/scope or explicitly shared ownership, and no false full-suite or cross-harness claims.
- [ ] **Step 5: Request final branch review under the chosen execution method, resolve material issues and commit the exact documentation files.** Suggested subject docs: document the verified toolkit foundation. Publish a branch or create a PR only when authorized; never merge or release as an implied documentation step.

## Spec coverage and self-review

| Spec requirement | Owning tasks |
| --- | --- |
| Seventeen names; planned/available distinction; dependency closure | 1, 2, 5, 6 |
| Root-only tests, skill/scope ownership and shared exceptions; self-contained resources; safe metadata | 1, 2, 3, 4, 5, 6 |
| Workdir portability, Git/worktree identity and local identity source | 3, 4 |
| Intent-sensitive preflight and unchanged repository state | 4 |
| Language precedence, honest routing, missing optional tools | 4, 5 |
| Actual compatibility evidence and selective installation | 3, 5, 6 |
| Excluded CCR/Jira; deferred plugin packaging and releases | 1, 5, 6 |

Self-review: all tasks have named files, inputs/outputs and observable checks. Test helpers remain test-only. Automated validator/fixture tests are separated from behavioral evaluation. All seventeen active names are fixed by the spec and exclude CCR; no task implements a deferred coordinator. Skill tests and evidence have explicit owners, with shared helpers and cross-skill coverage kept separate. No step in this planning request has executed product code, installed dependencies or claimed tests passing.

## Execution handoff

The human explicitly requested both spec and plan; this does not start implementation. Review both artifacts, then choose native execution or subagent-driven execution before beginning Task 1. Native execution is the lower-overhead recommendation for this small foundation with shared validator/fixture interfaces; independent final review still checks the whole branch under the selected method.
