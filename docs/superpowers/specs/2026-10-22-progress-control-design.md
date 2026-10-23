# Portable Progress Control Design

Date: 2026-10-22
Status: Implementation in progress.
Capability: todo-workflow-controller

## Goal

Track a multi-step task and its required gates without binding task execution to a particular harness tool.

## Scope and non-goals

Deliver one independently usable instruction-first capability. Keep requires=[]; the toolkit entry is an optional consumer, not a prerequisite. Do not implement another planned capability or change catalog availability by writing this design.

The capability's persistence and execution boundaries are stated below. CCR/Jira, coordinators, native plugin packaging and releases are outside scope.

## Approaches considered

| Approach | Tradeoff and decision |
| --- | --- |
| Mandatory native todo tool | Simple adapter contract, but blocks safe tasks solely because the harness lacks that tool. |
| Persisted workflow engine | Durable state, but introduces unnecessary files, runtime and lifecycle ownership. |
| Native tracking with in-memory/inline fallback | Selected: preserves evidence and dependencies while adapting to actual harness tools. |

## Architecture and components

| Component | Responsibility |
| --- | --- |
| SKILL.md | When tracking helps, task flow, optional adapters and scope boundary. |
| references/progress-states.md | State transitions, required/optional gates, parallel branches and truthful completion. |

Installed resources are local to skills/todo-workflow-controller/. Tests and fixtures are owned by tests/skills/todo_workflow_controller/. Root validation tooling is not an installed runtime dependency.

## Data flow and contracts

Requested steps and dependencies -> choose actual native tracking or inline fallback -> update states from observed evidence -> preserve blockers/decisions -> advance eligible work -> report completed and remaining work without creating an unsolicited artifact.

The interfaces are request/evidence/result records interpreted by the assistant; no callable runtime API or persisted state schema is introduced. The implementation plan supplies exact test packets, source paths and execution checks.

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

## Error handling and authorization

Missing or failed tracking tools use fallback; they do not erase blockers. A failed required gate cannot become completed through a checkbox or skip. An unanswered decision remains unresolved. A caller-provided requirement change is recorded as a decision rather than an executed check. Parallel work is represented as observed, not manufactured.

No progress status, formatting result, drafted report or discovered command is authorization for another operation. Preserve unknown facts, unresolved choices and limitations. Do not mutate unrelated files or claim work was executed without evidence.

## Testing strategy and acceptance criteria

Use the following exact request/evidence packets as behavioral cases. The baseline evaluator sees only the request, supplied facts and actual permitted tools, without the candidate skill or expected answer. A separate assessment compares the observed behavior with the assertions below. The same inputs and tool restrictions are used for GREEN with the candidate skill supplied.

Use a fresh supported evaluation context when available; record whether execution was independent, manual or limited. Missing evaluation capability is a limitation, not invented independence. An absent skill is not a RED result. If the baseline meets all cases, inspect the unproven requirement or necessity of the capability; do not force a failure by changing expectations after seeing results.

### PRG-01: required_gate_and_optional_skip

- Request: Track inspect -> validate -> publish before a tight deadline. Validation is required. An optional summary may be skipped.
- Supplied evidence: Inspect completed; validation failed; summary is optional and omitted.
- Assertions:
  - Keep validation uncompleted with the failed-check evidence; leave publish uncompleted (pending or blocked) while its required validation gate has failed.
  - The optional summary may be skipped with a reason.
  - Do not claim the workflow completed under deadline pressure.

### PRG-02: missing_or_failed_tool

- Request: Continue tracking safely if the task tool is absent or stops working.
- Supplied evidence: A material validation blocker already exists. An independent safe task is ready to proceed. The actual harness either exposes no tracker or reports a real tracker failure.
- Assertions:
  - Retain the blocker with inline/in-memory tracking.
  - Do not stop independent safe work solely for the missing tracker.
  - Create no extra file or scheduler. Mark unavailable native-tool variants limited, not passed.

### PRG-03: unanswered_decision_and_changed_requirement

- Request: Track a step that needs an explicit target choice.
- Supplied evidence: Initially the user has not answered. Separate variant: the user explicitly removes a nonessential requirement.
- Assertions:
  - Silence and elapsed time do not supply the target choice.
  - A real requirement change is recorded as a decision, not fabricated verification.

### PRG-04: independent_and_parallel_branches

- Request: Track independent tasks A and B; A is blocked. In the parallel variant both were explicitly started.
- Supplied evidence: A is blocked by a missing input. B is authorized, independent and ready, but has not started. In a separate parallel variant, both tasks have started; A is now blocked on the missing input and B is in progress. Treat these as supplied observations, not actions requested from the tracker.
- Assertions:
  - In the initial snapshot, keep B eligible but not in_progress until evidence says it started; A being blocked does not prevent B from starting.
  - In the parallel variant, represent A as blocked and B as in_progress; do not launch agents or force a false single-active-step claim.

### PRG-05: handoff_and_language

- Request: Resume from this evidence and report progress in Spanish; then provide the same status in English.
- Supplied evidence: The tracker overall label is completed, but current step evidence is INSPECT=completed; VALIDATE=pending (required, not run); TARGET=decision_pending.
- Assertions:
  - Preserve INSPECT=completed, VALIDATE=pending and TARGET=decision_pending across the handoff.
  - Use Spanish for the first response and English for the follow-up while preserving the exact identifiers and values INSPECT=completed, VALIDATE=pending and TARGET=decision_pending.
  - Do not report the workflow as complete based only on the overall tracker label when required step evidence remains incomplete.

Capture actual observations and assertion outcomes in tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md. Where a required evaluation could not run, record the limitation and leave the availability decision open. No new script is required merely to turn prose into keyword tests.

## File structure

- skills/todo-workflow-controller/SKILL.md
- skills/todo-workflow-controller/references/progress-states.md
- tests/skills/todo_workflow_controller/scenarios/progress.md
- tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md

Create optional directories only when an actual file needs them. Python packages normalize hyphens to underscores, while scenario ownership retains the canonical skill name.

## Catalog and composition

After principal behavior and structural validation succeed, change only todo-workflow-controller to available with requires=[] in the same complete standalone delivery. Update its availability documentation from the actual catalog counts. The other independently delivered capabilities may or may not already be available.

A separate complete task adds the optional installed-capability route to using-devcraft-toolkit and verifies direct, composed and absent-installation cases. It does not widen the entry's hard dependency group or emulate an absent skill. Standalone capability failure and entry-composition failure remain separate results.

Preserve the read-only foundation context/preflight contracts. A report's explicit file output or a requested validation execution needs its exact side-effect policy in AGENTS.md and tests/scenarios/README.md; that exception does not grant writes to other skills.

## Global Constraints

- Source instructions, documentation, examples and default templates are English; user-facing output uses explicit user preference, then request language, then English when indeterminate.
- Technical identifiers, schema keys, command syntax and supplied data identifiers remain unchanged by translation.
- Tests, fixtures, scenarios and retained evaluations live under tests/skills/<normalized_skill_name>/; root tests/integration/ is only for multiple named skills.
- Installed skills use only their bundled resources and explicitly declared skill dependencies; repository tooling and catalog.json are development resources.
- Implementation must be understandable from repository-local requirements and accessible official technical references, without private conversations, personal paths or unavailable files.
- Catalog status stays planned until structural checks and actual behavioral evaluation justify available; record unexecuted cases as limitations.
- No new coordinator, CCR/Jira integration, plugin manifest, installer, release automation or runtime orchestration engine is included.
- Use Python 3.11+ and the existing PyYAML>=6.0,<7.0 development setup; add no dependencies or helpers without a demonstrated need.
- Behavioral RED means an observed baseline violation without the candidate skill; a missing SKILL.md or planned catalog entry is not a failing behavior test.

## Risks and review focus

1. PRG-01: a failed required gate cannot be completed by skipping or deadline pressure.
2. PRG-02: missing/failed tools retain blockers without new artifacts.
3. PRG-03: unanswered decisions and explicit requirement changes are distinct.
4. PRG-04: independent/parallel branches reflect actual dependencies and execution.
5. PRG-05: handoffs and language changes preserve incomplete evidence.

The implementation plan maps every item above to a named case and a concrete task. Source/content checks do not replace observed behavior. Limited harness coverage remains explicitly limited.

## References

- [Skill composition](../../composition.md), [language behavior](../../language.md) and [scenario protocol](../../../tests/scenarios/README.md): existing project contracts.

Project requirements are stated in this document; links provide accessible standards or in-repository contracts. This spec is the behavioral contract for the companion implementation plan.
