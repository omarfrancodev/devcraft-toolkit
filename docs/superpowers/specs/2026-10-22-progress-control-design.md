# Portable Progress Control Design

Date: 2026-10-22
Status: Proposed; product implementation has not started.
Capability: todo-workflow-controller

## Product goal

Track a multi-step task and its required gates without binding task execution to a particular harness tool.

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

Inputs are the requested workflow, ordered steps/dependencies, required gates, observed evidence, user decisions and available progress tools. Keep only the amount of tracking useful for the task; a small one-step request does not need a generated process.

Use native task/todo tracking when suitable and available. If unavailable or it fails, continue with concise inline status and in-memory state when the work can otherwise proceed safely. Absence of the tracking tool does not imply absence of execution capability.

## State and evidence

Step states are pending, in_progress, completed, blocked and skipped. A skipped optional step carries its reason. A required step is not satisfied by marking it skipped; it needs completion evidence or an explicit applicable user change to the requirement. Such a change is recorded as a decision, not a fabricated successful check.

The default sequential flow has one in_progress step at a time. Explicitly independent parallel tasks may each be in progress; track the real tasks rather than claiming a single active step while several run. Do not introduce delegation or parallel execution solely to satisfy tracking.

Advance only after the dependencies relevant to that step are met. A blocked branch need not stop independent permitted work. An unanswered required decision stays pending; silence or elapsed time is not approval.

Completion is based on observed results, not a task tool's checkbox. Preserve blockers and unsatisfied required gates across a tool failure or context handoff. Report completed, remaining and blocked work accurately without replaying the entire tool transcript.

## Scope and persistence

Progress control grants no permission to perform Git writes, send messages, deploy, install software or modify business records. Native progress adapters use only tools actually exposed by the harness. No hardcoded tool name, mandatory tool-presence gate, external scheduler or durable state-machine framework is introduced.

Keep progress in ordinary working context unless the user explicitly requests a saved task artifact or an existing project plan is the agreed tracking artifact. Do not create extra files simply because a todo tool is absent.

## Boundaries and acceptance

No required skill dependencies, Git repository or network access is needed. This skill tracks work; it does not replace verification or execute another capability by itself.

Scenarios cover native tracking, no tracking tool, mid-run tool failure, sequential dependencies, an optional skipped step, a failed required gate, a user-adjusted requirement, a blocked branch with independent work, explicitly parallel work and resuming from incomplete evidence. Verify observable ordering, decisions and final claims, not exact status wording. Missing tool cases must retain the same safety and evidence standards as native-tool cases.

## Files and test ownership

- skills/todo-workflow-controller/SKILL.md
- skills/todo-workflow-controller/references/progress-states.md
- tests/skills/todo_workflow_controller/scenarios/progress.md
- tests/skills/todo_workflow_controller/evaluations/<run>.md when explicitly retained

Tests use the canonical owner todo-workflow-controller; the Python-compatible test package is todo_workflow_controller. Introduce unit/integration test code only for a real executable contract, not to check whether instructions contain a chosen sentence. Scenario fixtures and evidence remain outside the installed skill folder.

## Catalog, routing and documentation

After actual verification, mark only todo-workflow-controller available and leave requires=[] in catalog.json. Add its installed-capability route to using-devcraft-toolkit without widening the entry's hard dependency group. Route only when the skill is actually installed; a missing optional capability remains a visible limitation.

Update README.md, docs/architecture.md, docs/composition.md, docs/installation.md, docs/compatibility.md and docs/roadmap.md to match observed availability. Derive current counts from catalog.json instead of assuming that other increments have already landed. Keep the foundation spec's historical three-skill delivery record intact.

Foundation context/preflight stay read-only. If this capability allows explicit file output or check execution, document those effects precisely in AGENTS.md and the scenario protocol; do not change the permissions of unrelated skills.

## Acceptance and evidence

Run the existing repository suite and structural validator. Execute the owned behavioral scenarios on the actual available harness; use the common protocol and record executed/limited outcomes. Structural success alone is not a behavioral pass. A manually followed skill is recorded as a self-evaluation, not a dynamically loaded or independent evaluation.

No network connection, unrelated source tree or tool absent from the environment is needed to understand the requirements. A limited scenario remains limited and must not become a blanket compatibility claim. Leave future coordinators planned.

## References

- [Skill composition](../../composition.md), [language behavior](../../language.md) and [scenario protocol](../../../tests/scenarios/README.md): existing project contracts.

The maintained implementation requirements are fully stated above. References explain standards or existing project contracts; they do not substitute for missing product decisions.
