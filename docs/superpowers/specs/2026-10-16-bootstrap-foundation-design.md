# Devcraft Toolkit Foundation Design

Date: 2026-10-16
Updated: 2026-10-17
Status: Proposed for review; this document authorizes no implementation or release.
Scope: Milestone 1, the repository foundation and three usable entry/context/safety skills.

## Intent and approved direction

Devcraft Toolkit is a single maintained collection of composable capabilities for Git operations, code review, and activity reporting across coding harnesses. Users can invoke an individual capability or a coordinator. Platform-specific business integrations such as Jira remain outside the core.

The human has approved the suite identity, the seventeen-skill target inventory, the three coordinator names, language behavior, and centralized tests. The present request is to prepare a spec and implementation plan in an isolated worktree, starting with the basics. It is not an instruction to implement all seventeen skills, migrate CCR, or archive its repository now.

This is architectural work. The design and plan are prepared together at the human's explicit request; both remain reviewable drafts before implementation begins.

## Baseline

The repository initially contains README.md and .gitignore only. Main includes the initial README and the published ignore change. There is no application, dependency manifest, test runner, skill directory, or plugin manifest to validate yet.

The local repository identity is omarfrancodev <fofe2803@gmail.com>. The global work identity must remain unchanged. The planning checkout is .worktrees/bootstrap-foundation on feat/bootstrap-foundation; /.worktrees/ is ignored by the main checkout.

## Alternatives and selected increment

1. Implement all seventeen skills immediately: broad scope, coupled migrations, and no established validation boundary.
2. Add seventeen empty skill folders: misleading discoverability and no usable outcome.
3. Establish a small usable foundation, then extend it: selected.

Milestone 1 creates three real skills, a catalog that distinguishes available and planned capabilities, repository validation, centralized tests and behavioral evaluation instructions. It establishes the rules the later workflows will follow.

## Global constraints

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

## Target capability inventory

The catalog has exactly the following seventeen entries. Available below means the completed Milestone 1 target, not the current planning checkout.

| Name | Role | Milestone 1 status |
| --- | --- | --- |
| using-devcraft-toolkit | Entry and composition | available |
| git-commit-builder | Commit coordinator | planned |
| git-publish-work | Publication coordinator | planned |
| git-activity-report | Activity-report coordinator | planned |
| git-analyze-changes | Git capability | planned |
| git-plan-commits | Git capability | planned |
| git-stage-changes | Git capability | planned |
| git-sync-branch | Git capability | planned |
| git-publish-changes | Git capability | planned |
| git-manage-pull-request | Git capability | planned |
| git-promote | Git capability | planned |
| git-safety-check | Supporting capability | available |
| git-working-directory-policy | Supporting capability | available |
| conventional-commits-style | Supporting capability | planned |
| validation-discovery | Supporting capability | planned |
| natural-language-report-writer | Supporting capability | planned |
| todo-workflow-controller | Supporting capability | planned |

Milestone 1 declared dependencies:
- using-devcraft-toolkit requires git-working-directory-policy and git-safety-check.
- git-safety-check requires git-working-directory-policy.
- git-working-directory-policy has no skill dependencies.
- Planned entries have empty dependency lists until their own designs define and validate them.

CCR continues to evolve in its own project and is excluded from this project's active inventory and roadmap. Reconsider its integration only after the owner selects a stable version and authorizes a separate design. Archive the original repository only after that later integration has been completed and verified; no archival is scheduled now.

## Repository layout after implementation

~~~
devcraft-toolkit/
  README.md
  .gitignore
  AGENTS.md
  CONTRIBUTING.md
  catalog.json
  requirements-dev.txt
  docs/
    architecture.md
    installation.md
    composition.md
    language.md
    compatibility.md
    migration.md
    superpowers/specs/2026-10-16-bootstrap-foundation-design.md
    superpowers/plans/2026-10-16-bootstrap-foundation.md
  skills/
    using-devcraft-toolkit/SKILL.md
    using-devcraft-toolkit/references/composition.md
    git-working-directory-policy/SKILL.md
    git-working-directory-policy/references/context.md
    git-safety-check/SKILL.md
    git-safety-check/references/preflight.md
  scripts/
    __init__.py
    validate_repository.py
  tests/
    __init__.py
    repository/__init__.py
    repository/test_repository_validation.py
    skills/__init__.py
    skills/git_working_directory_policy/__init__.py
    skills/git_working_directory_policy/integration/__init__.py
    skills/git_working_directory_policy/integration/test_context_fixtures.py
    skills/git_working_directory_policy/scenarios/context.md
    skills/git_safety_check/__init__.py
    skills/git_safety_check/integration/__init__.py
    skills/git_safety_check/integration/test_preflight_fixtures.py
    skills/git_safety_check/scenarios/preflight.md
    skills/using_devcraft_toolkit/scenarios/routing-and-language.md
    integration/scenarios/context-to-preflight.md
    support/__init__.py
    support/git_fixtures.py
    scenarios/README.md
~~~

Create files only when their task needs them. Do not add empty future skills, .gitkeep files, copied vendor plugins or an installer/runtime framework. Do not choose a license on the human's behalf.

Skill resources stay inside the skill folder; root development tools and docs are not implicit runtime dependencies. Cross-skill references use declared skill names, not machine-specific paths.

Each skill owns a subtree tests/skills/<skill_package>/, with unit/, integration/, support/, scenarios/, fixtures/ and evaluations/ created only when needed. Python-compatible package names normalize hyphens to underscores (for example git-safety-check maps to git_safety_check); scenario/evaluation records state the canonical skill name.

tests/repository/ owns catalog, validator and repository-layout checks. tests/integration/ owns tests spanning multiple skills and must name all participating skills. tests/support/ and tests/fixtures/ contain only helpers/data genuinely reused by multiple owners; otherwise place them under the owning skill. tests/scenarios/README.md is the common evaluation protocol, not a container for unowned skill scenarios. Shared code has one maintained implementation, not a copied helper per skill. Retained evaluation evidence stays with its skill owner or the cross-skill integration suite.

The validator rejects a tests/skills/ package that does not map to a catalog name and test code placed in skills/<name>/. Reviewers check that files in shared groups genuinely cover repository infrastructure or multiple named skills; the validator must not guess semantic ownership by scanning test wording. A synthetic future package is not created merely because a capability is planned.

## Catalog and discovery contract

catalog.json is a project-level inventory, not a new Agent Skills or plugin standard.

The root object has schema_version=1, name="devcraft-toolkit" and a skills array. Each skill entry has:
- name: canonical lowercase hyphenated skill name.
- role: entry, coordinator, capability or support.
- status: planned or available.
- path: skills/<name>.
- requires: an array of canonical skill names.

Names and paths are unique. Paths are relative, contain no traversal, and resolve within the repository even through symlinks. Unknown dependencies and cycles fail validation. Available entries may depend only on available entries. Available entries require a substantive SKILL.md and linked resources. Planned entries must not expose SKILL.md.

A standalone installation must include its declared dependency closure; the catalog does not cause a third-party installer to do that. Document selection and dependency groups without claiming tested installation on an untested harness. Native plugin packaging is a later increment.

## Three foundation skills

### git-working-directory-policy

Discover a repository from the user-selected location using the terminal tool's working-directory parameter or git -C. Resolve the physical worktree root, Git directory and common Git directory; distinguish a normal checkout, linked worktree and submodule using Git evidence.

Return a compact repository context: root, Git/common directories, branch or detached state, unborn HEAD state, effective Git identity and its configuration origin, observed tool limitations and applicable execution directory. This is an instructional output contract, not a new runtime API.

Support spaces and Unicode paths and separately launched command calls. Do not switch branches, create a repository, change identity, install dependencies, write context files or request approval merely to use git -C. No Git repository produces an explicit limitation, not an invented root.

### git-safety-check

Consume or discover current repository context, plus requested intent: inspect, commit or publish. Refresh volatile facts before decisions; a context packet is not proof that Git has remained unchanged.

Inspect conflicts, in-progress Git operations, dirty/index state, branch/HEAD state and effective identity. Read-only inspection must not fail merely because Git identity is missing. A clean committed branch is valid for publication preflight. No changes for a commit intent returns no_op. An unborn HEAD is valid for initial-commit preparation, but not for publication.

For commit intent, preserve existing staged selections and exclusions. Ask only for a material unresolved decision. Missing/conflicting identity blocks a future commit; inherited global identity with unclear personal/work context requires clarification before a future write. Never change identity automatically.

For publish intent, require an existing commit and a clean worktree. Conflicts and unresolved operations block the affected mutation. Detached HEAD requires an explicit branch strategy before mutation. A ready preflight is not a merge authorization.

Return ready, no_op, blocked, needs_decision or limited with observed evidence and the affected intent. Use read-only Git operations with optional locks disabled where supported. Do not stage, commit, switch, fetch, push, stash or repair files.

### using-devcraft-toolkit

Route requests only within toolkit scope. Resolve language and actual installed capabilities. Do not auto-load this entry in unrelated conversations or require every capability on every request.

In Milestone 1, a repository-context or Git-preflight request can use the two available supporting skills. A request for committing, publication or activity generation must explicitly report that the target capability is planned/not installed in this distribution. It must not claim completion, silently emulate a missing coordinator or modify another installation.

The entry has no CCR-specific route, fallback or integration. It does not inspect or alter the independent CCR project.

Compose existing results without repeated repository-wide discovery. Refresh facts affected by changes. Structured questions and progress tools are optional adaptations; required unanswered decisions still wait for the user.

## Language and permission boundaries

Use the full explicit language preference where available, then the current request's language. Do not infer language from machine locale, Git identity or repository folder. Examples cover English, Spanish, another language and an indeterminate request. Preserve user-required output formats.

Commit subjects, future reports, MR/PR text and interactive questions follow the same precedence; technical Conventional Commit types remain unchanged. Language adaptation is not scope expansion or permission to write externally.

Docs default to English. Behavioral evaluation reports follow the evaluating user's language. Retain skill-owned reports only in tests/skills/<skill_package>/evaluations/<run>/; retain cross-skill reports in tests/integration/evaluations/<run>/. They are not installed resources.

## Repository validation

scripts/validate_repository.py exposes validate_repository(root: Path) -> list[ValidationIssue], where ValidationIssue has code, path and message strings. The CLI accepts --root <path>, prints actionable issues and returns 0 for no issues or 1 for invalid content. Missing tooling dependencies produce a clear diagnostic and nonzero exit.

Validate catalog shape, canonical names/roles/statuses/paths, uniqueness, dependency closure/cycles, available/planned folder agreement, required frontmatter and a nonempty instruction body. Parse YAML using yaml.safe_load; never execute constructors. Check the Agent Skills name/description limits and directory-name agreement.

Reject test directories/test modules inside available skill folders and skill-local symlinks that escape their root. Validate test ownership and normalized skill packages using the root test-layout contract; README documentation does not replace that check. Validate explicit local Markdown links to skill resources; distinguish URLs, fragment-only links and declared cross-skill dependencies. Ignore inline/fenced code examples instead of treating them as links; support relative resource links and file anchors. Reject linked files outside the skill or missing linked files. This is scoped repository validation, not a claim of implementing a complete Markdown parser or the full Agent Skills standard.

Validation reports source problems without modifying files, fetching URLs or loading a harness. Structural success does not prove behavioral correctness, language quality or model compliance.

## Validation and acceptance

1. Run real unittest cases over temporary repository copies for valid content, broken YAML, missing descriptions/body/resources, duplicate names, path escape, dependency cycles, planned placeholders and skill-local tests.
2. Git fixture helpers create temporary repositories only, using fixture-local identity and no network. Exercise ordinary, unborn, linked-worktree, detached and conflicted states; use spaces/Unicode paths. They must not mutate the developer's Git configuration.
3. Behavioral scenarios instruct an evaluator to invoke the skills against those raw fixtures and record evidence of scope, language, decisions and side effects. Expected outcomes are behavior, not exact wording or regex matches against instructions.
4. Compare refs, index and working files before/after preflight. The skills must not change them.
5. Missing tools or unsupported symlink facilities are explicit limitations/skips, not passed coverage.
6. A maintainer can run python -m unittest discover -s tests -p "test_*.py" -v and python scripts/validate_repository.py --root . after installing requirements-dev.txt.
7. Document actual executed harness/version and scenario results before claiming compatibility. A single-harness smoke check does not prove every harness.
8. End state: exactly three available skills, fourteen planned entries, all tests centralized and grouped by owner and scope, documented dependency groups, and no misleading full-suite/plugin installation claim.

## Follow-on increments

- Shared capabilities: commit formatting, natural-language reports, safe project-check discovery and portable progress.
- Commit workflow: analysis, plan, staging and git-commit-builder, preserving user-selected hunks and decisions.
- Activity workflow: date/timezone/author selection and verified translated templates.
- Publication workflow: synchronize, review exact versions, push, MR/PR lifecycle and promotion with separate authorizations.
- Harness distribution: validated manifests, selective bundles, CI and releases after selecting supported interfaces.

Each increment gets its own bounded design/plan as needed. This spec is a target map and a foundation implementation contract, not a hidden seventeen-skill implementation plan.

## Sources and review notes

- Human decisions in the current Devcraft Toolkit conversation through 2026-10-17, including CCR exclusion and per-skill test ownership.
- https://agentskills.io/specification (consulted 2026-10-16): SKILL.md metadata, resource structure and relative references.
- Existing README.md and .gitignore at the repository baseline.
- Existing Git helper skills and original agents informed the compatibility corrections; they are not runtime dependencies.

Self-review: seventeen active names exclude CCR; tests are external and grouped by skill and scope; Spanish-only rules are removed; clean-publication and unborn-commit cases are distinct; no global identity mutation, empty skill advertisement, automatic dependency installation or unverified harness compatibility is promised.
