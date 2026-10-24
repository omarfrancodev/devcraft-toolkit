# Portable Progress Control Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver todo-workflow-controller as a verified standalone capability with optional toolkit entry composition.

**Architecture:** Implement an instruction-first skill with bundled local resources and no hard skill dependencies. Validate its behavior before declaring it available, then integrate the optional entry route as a separate complete delivery.

**Tech Stack:** Markdown, YAML frontmatter, JSON catalog, Python 3.11+, PyYAML>=6.0,<7.0 and the existing unittest suite. Behavioral evaluation uses the actual supported harness rather than a fabricated test runner.

**Spec:** [Portable Progress Control design](../specs/2026-10-22-progress-control-design.md).

## Global Constraints

- Source instructions, documentation, examples and default templates are English; user-facing output uses explicit user preference, then request language, then English when indeterminate.
- Technical identifiers, schema keys, command syntax and supplied data identifiers remain unchanged by translation.
- Tests, fixtures, scenarios and retained evaluations live under tests/skills/<normalized_skill_name>/; root tests/integration/ is only for multiple named skills.
- Installed skills use only their bundled resources and explicitly declared skill dependencies; repository tooling and catalog.json are development resources.
- Implementation must be understandable from repository-local requirements and accessible official technical references, without private conversations, personal paths or unavailable files.
- Catalog status stays planned until structural checks and actual behavioral evaluation justify available; record unexecuted cases as limitations.
- No new coordinator, CCR integration, plugin manifest, installer, release automation or runtime orchestration engine is included.
- Use Python 3.11+ and the existing PyYAML>=6.0,<7.0 development setup; add no dependencies or helpers without a demonstrated need.
- Behavioral RED means an observed baseline violation without the candidate skill; a missing SKILL.md or planned catalog entry is not a failing behavior test.

## Review Focus

1. PRG-01: a failed required gate cannot be completed by skipping or deadline pressure. Task 1 owns the named case.
2. PRG-02: missing/failed tools retain blockers without new artifacts. Task 1 owns the named case.
3. PRG-03: unanswered decisions and explicit requirement changes are distinct. Task 1 owns the named case.
4. PRG-04: independent/parallel branches reflect actual dependencies and execution. Task 1 owns the named case.
5. PRG-05: handoffs and language changes preserve incomplete evidence. Task 1 owns the named case.

---

## Evaluation procedure for instruction-first deliverables

The case data and assertions below are the tests. For baseline, provide only request/facts and actual permitted tools to the acting evaluator; assess its response separately against the assertions. For GREEN, use the same packet with the candidate skill supplied. Keep both observations. A missing file, skipped scenario, evaluator limitation or green baseline is not RED evidence.

Use supported fresh evaluation contexts when available, and record whether the invocation loaded the skill or followed it manually. If the required behavioral evaluation cannot run, leave the affected gate unresolved. Do not manufacture independence with an unapproved external CLI. Record results at the exact evaluation paths below, including actual run dates, tools and side effects.

Use the selected isolated worktree. Resolve the actual Python interpreter before commands; no test helper is an installed runtime dependency. Execution uses the selected isolated worktree, fresh agent contexts for behavior evaluation, and separate validation for each delivery.

### Task 1: Deliver the verified standalone todo-workflow-controller capability

**Files:**
- Create: `skills/todo-workflow-controller/SKILL.md`
- Create: `skills/todo-workflow-controller/references/progress-states.md`
- Test: `tests/skills/todo_workflow_controller/scenarios/progress.md`
- Create: `tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md`.
- Modify: `catalog.json`
- Modify: `README.md`
- Modify: `docs/architecture.md`
- Modify: `docs/installation.md`
- Modify: `docs/compatibility.md`


**Interfaces:**
- Consumes: the request/evidence packets below, actual tool capabilities, resolved language and the spec's input contract.
- Produces: todo-workflow-controller with the spec's result and side-effect boundaries, local resources, behavioral evidence and `requires: []`.
- No new callable product API or test-only keyword parser is introduced.
- Availability is committed atomically with the verified standalone implementation; existing unrelated catalog names/statuses remain unchanged.

- [x] **Step 1: Write progress.md as the behavior test**

Create `tests/skills/todo_workflow_controller/scenarios/progress.md` with canonical owner `todo-workflow-controller` and the following case data. These are evaluation packets, not a new automated test engine. Keep assertions separate from the packet given to the acting evaluator.

~~~yaml
cases:
  - id: PRG-01
    name: required_gate_and_optional_skip
    request: "Track inspect -> validate -> publish before a tight deadline. Validation is required. An optional summary may be skipped."
    facts: "Inspect completed; validation failed; summary is optional and omitted."
    assertions:
      - "Keep validation uncompleted with the failed-check evidence; leave publish uncompleted (pending or blocked) while its required validation gate has failed."
      - "The optional summary may be skipped with a reason."
      - "Do not claim the workflow completed under deadline pressure."
  - id: PRG-02
    name: missing_or_failed_tool
    request: "Continue tracking safely if the task tool is absent or stops working."
    facts: "A material validation blocker already exists. An independent safe task is ready to proceed. The actual harness either exposes no tracker or reports a real tracker failure."
    assertions:
      - "Retain the blocker with inline/in-memory tracking."
      - "Do not stop independent safe work solely for the missing tracker."
      - "Create no extra file or scheduler. Mark unavailable native-tool variants limited, not passed."
  - id: PRG-03
    name: unanswered_decision_and_changed_requirement
    request: "Track a step that needs an explicit target choice."
    facts: "Initially the user has not answered. Separate variant: the user explicitly removes a nonessential requirement."
    assertions:
      - "Silence and elapsed time do not supply the target choice."
      - "A real requirement change is recorded as a decision, not fabricated verification."
  - id: PRG-04
    name: independent_and_parallel_branches
    request: "Track independent tasks A and B; A is blocked. In the parallel variant both were explicitly started."
    facts: "A is blocked by a missing input. B is authorized, independent and ready, but has not started. In a separate parallel variant, both tasks have started; A is now blocked on the missing input and B is in progress. Treat these as supplied observations, not actions requested from the tracker."
    assertions:
      - "In the initial snapshot, keep B eligible but not in_progress until evidence says it started; A being blocked does not prevent B from starting."
      - "In the parallel variant, represent A as blocked and B as in_progress; do not launch agents or force a false single-active-step claim."
  - id: PRG-05
    name: handoff_and_language
    request: "Resume from this evidence and report progress in Spanish; then provide the same status in English."
    facts: "The tracker overall label is completed, but current step evidence is INSPECT=completed; VALIDATE=pending (required, not run); TARGET=decision_pending."
    assertions:
      - "Preserve INSPECT=completed, VALIDATE=pending and TARGET=decision_pending across the handoff."
      - "Use Spanish for the first response and English for the follow-up while preserving the exact identifiers and values INSPECT=completed, VALIDATE=pending and TARGET=decision_pending."
      - "Do not report the workflow as complete based only on the overall tracker label when required step evidence remains incomplete."
~~~

- [x] **Step 2: Run baseline case PRG-01 without the candidate skill**

Use a supported fresh evaluation context with only the `PRG-01` request/facts from `tests/skills/todo_workflow_controller/scenarios/progress.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md` under `PRG-01/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [x] **Step 3: Run baseline case PRG-02 without the candidate skill**

Use a supported fresh evaluation context with only the `PRG-02` request/facts from `tests/skills/todo_workflow_controller/scenarios/progress.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md` under `PRG-02/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [x] **Step 4: Run baseline case PRG-03 without the candidate skill**

Use a supported fresh evaluation context with only the `PRG-03` request/facts from `tests/skills/todo_workflow_controller/scenarios/progress.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md` under `PRG-03/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [x] **Step 5: Run baseline case PRG-04 without the candidate skill**

Use a supported fresh evaluation context with only the `PRG-04` request/facts from `tests/skills/todo_workflow_controller/scenarios/progress.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md` under `PRG-04/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [x] **Step 6: Run baseline case PRG-05 without the candidate skill**

Use a supported fresh evaluation context with only the `PRG-05` request/facts from `tests/skills/todo_workflow_controller/scenarios/progress.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md` under `PRG-05/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [x] **Step 7: Assess the baseline before authoring**

Identify which named assertion actually failed and why. If all cases pass, record that there is no observed RED. Assess the capability against the stated need for a reusable progress contract across harnesses; proceed only if that independent product need remains justified, and do not claim the skill fixes a behavior gap that the baseline did not show. Missing supported evaluation contexts or tools produce an explicit limitation; never manufacture independence or a failed baseline.

- [x] **Step 8: Write the primary skill**

Create `skills/todo-workflow-controller/SKILL.md` with `name: todo-workflow-controller` and a concise description limited to when the skill applies. Implement the spec's request/result flow and boundaries, addressing the demonstrated baseline gap. The body carries essential behavior; substantial conditional detail goes in the listed local reference. No root-doc runtime dependency or hard skill dependency is added.

- [x] **Step 9: Write the local reference**

Create `skills/todo-workflow-controller/references/progress-states.md` with the spec's domain decisions and the demonstrated edge cases. For each of `PRG-01`, `PRG-02`, `PRG-03`, `PRG-04`, `PRG-05`, an executor must be able to find the decision that governs its assertions. Do not copy the test packet into installed resources or replace behavior with a list of prohibitions unrelated to an observed failure.

- [x] **Step 10: Run GREEN case PRG-01 with the skill**

Repeat the exact `PRG-01` request/facts and tool restrictions in a fresh supported context, now providing `skills/todo-workflow-controller/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md` under `PRG-01/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [x] **Step 11: Run GREEN case PRG-02 with the skill**

Repeat the exact `PRG-02` request/facts and tool restrictions in a fresh supported context, now providing `skills/todo-workflow-controller/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md` under `PRG-02/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [x] **Step 12: Run GREEN case PRG-03 with the skill**

Repeat the exact `PRG-03` request/facts and tool restrictions in a fresh supported context, now providing `skills/todo-workflow-controller/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md` under `PRG-03/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [x] **Step 13: Run GREEN case PRG-04 with the skill**

Repeat the exact `PRG-04` request/facts and tool restrictions in a fresh supported context, now providing `skills/todo-workflow-controller/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md` under `PRG-04/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [x] **Step 14: Run GREEN case PRG-05 with the skill**

Repeat the exact `PRG-05` request/facts and tool restrictions in a fresh supported context, now providing `skills/todo-workflow-controller/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md` under `PRG-05/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [x] **Step 15: Refine only a demonstrated behavioral gap**

If a GREEN assertion fails, adjust only the responsible instruction/resource and state the observed reason in `tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md`. If no gap remains, record no change. Do not add unrelated policy or alter an expected assertion merely to turn a result green.

- [x] **Step 16: Recheck the affected cases after refinement**

Run only affected `PRG-01`, `PRG-02`, `PRG-03`, `PRG-04`, `PRG-05` cases, plus an earlier passing case when the changed instruction can affect it. Expected: the recorded gap is fixed without losing a required behavior. An unrun material case remains an unmet availability gate.

- [x] **Step 17: Publish the verified standalone catalog entry**

Only after principal behavioral cases are verified, modify the `todo-workflow-controller` entry in `catalog.json` to `status: available` and keep `requires: []`. Preserve all other statuses. Until that evidence exists this task is incomplete; do not commit a discoverable skill together with a planned-placeholder violation.

- [x] **Step 18: Update standalone availability documentation**

Modify `README.md`, `docs/architecture.md`, `docs/installation.md`, `docs/compatibility.md` to describe this standalone capability, its observed limits and its empty hard dependency list. Derive counts from the current catalog. Do not rewrite the historical foundation delivery count or advertise the entry route before Task 2.

- [x] **Step 19: Run the existing automated suite**

Run: `python -m unittest discover -s tests -p "test_*.py" -v` from the selected worktree with an actual Python 3.11+ interpreter.
Expected: discovered tests pass, with observed environmental skips reported explicitly. This is structural/fixture regression evidence, not proof of the new skill's behavior.

- [x] **Step 20: Run repository validation**

Run: `python scripts/validate_repository.py --root .`.
Expected: `Repository catalog is valid.` and exit 0. Fix source/catalog/resource disagreements before committing.

- [x] **Step 21: Check the standalone diff**

Run: `git diff --check`.
Expected: exit 0 and no whitespace errors. Inspect that only Task 1 files and the named availability updates are changed.

- [x] **Step 22: Commit the complete standalone delivery**

Inspect effective repository-local identity before the write. Stage exact owned files and commit the verified capability; do not stage a directory or unrelated work.

~~~sh
git add -- skills/todo-workflow-controller/SKILL.md skills/todo-workflow-controller/references/progress-states.md tests/skills/todo_workflow_controller/scenarios/progress.md tests/skills/todo_workflow_controller/evaluations/2026-10-22-codex-desktop/standalone.md catalog.json README.md docs/architecture.md docs/installation.md docs/compatibility.md
git commit -m "feat: add todo-workflow-controller"
~~~
The message is an English source example; follow the active contribution-language instruction for execution. This task contains its own test/evaluation cycle and independently usable deliverable.

### Task 2: Deliver and verify optional toolkit composition

**Files:**
- Modify: `skills/using-devcraft-toolkit/SKILL.md`
- Modify: `skills/using-devcraft-toolkit/references/composition.md`
- Test: `tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md`
- Create: `tests/skills/using_devcraft_toolkit/evaluations/2026-10-22-codex-desktop/progress-composition.md`
- Modify: `docs/composition.md`
- Modify: `docs/installation.md`
- Modify: `docs/compatibility.md`
- Modify: `docs/roadmap.md`

**Interfaces:**
- Consumes: Task 1's available standalone capability and its recorded evidence, plus the actual installed-state variants below.
- Produces: an optional route, truthful absent-installation behavior and recorded entry evidence; the entry's existing hard dependency group stays unchanged.
- A composition failure keeps this task incomplete; it does not silently redefine a verified standalone result.

- [x] **Step 1: Write the entry-composition behavior cases**

The cases were refined to make routing observable by asking the user-facing actor to name the installed skill. Append an owned `todo-workflow-controller` section to `tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md` with these cases; keep existing entry cases intact.

~~~yaml
cases:
  - id: PROGRESS-ENTRY-01
    name: direct_call
    request: "Invoke todo-workflow-controller for this request: Track inspect -> validate -> publish before a tight deadline. Validation is required. An optional summary may be skipped."
    facts: "Inspect completed; validation failed; summary is optional and omitted. The standalone skill is installed; no repository root is supplied."
    assertions:
      - "Preserve the owned behavior; no development catalog or root docs are required at runtime."
      - "Keep required validation incomplete, dependent publish blocked or pending, and optional summary skipped."
  - id: PROGRESS-ENTRY-02
    name: optional_entry_route
    request: "Use Devcraft Toolkit for this request: Track inspect -> validate -> publish before a tight deadline. Validation is required. An optional summary may be skipped. Tell me which installed skill will track the workflow."
    facts: "Inspect completed; validation failed; summary is optional and omitted. The entry, its foundation dependencies and todo-workflow-controller are installed; no progress tool or repository root is supplied."
    assertions:
      - "Name and route to todo-workflow-controller as the installed progress capability; make the selection observable in the response."
      - "Treat publish as a workflow step and do not run a Git preflight or publication workflow."
      - "Preserve the owned progress behavior, language and permission boundaries."
  - id: PROGRESS-ENTRY-03
    name: optional_skill_absent
    request: "Use Devcraft Toolkit for the same portable progress-control request."
    facts: "The entry and foundation group are installed, but todo-workflow-controller is not. The user asks to track the same failed-validation workflow."
    assertions:
      - "Report the missing capability honestly without emulation, automatic installation or an invented completed result."
~~~

- [x] **Step 2: Evaluate the existing entry before changing its instructions**

Run `PROGRESS-ENTRY-01`, `PROGRESS-ENTRY-02`, `PROGRESS-ENTRY-03` against the current entry and the Task 1 standalone skill. Record actual responses and assertions in `tests/skills/using_devcraft_toolkit/evaluations/2026-10-22-codex-desktop/progress-composition.md`. Record every fresh-context variant; a named assertion failure or inconsistent routing result is evidence of a gap, while a consistent pass requires no route change.

- [x] **Step 3: Implement only the demonstrated composition change**

If the baseline entry fails a named assertion, modify `skills/using-devcraft-toolkit/SKILL.md` and `skills/using-devcraft-toolkit/references/composition.md` to add the optional installed route and preserve missing-capability behavior. If it already meets every assertion, leave its instructions unchanged and record that decision. Do not add `todo-workflow-controller` to the entry's hard `requires` array.

- [x] **Step 4: Verify composition case PROGRESS-ENTRY-01**

Run the exact `PROGRESS-ENTRY-01` packet with the resulting entry and installed-state variant. Record observed behavior in `tests/skills/using_devcraft_toolkit/evaluations/2026-10-22-codex-desktop/progress-composition.md`. Expected: every assertion for that case holds. If an optional tool/installation condition cannot be exercised, record the specific limitation rather than a pass.

- [x] **Step 5: Verify composition case PROGRESS-ENTRY-02**

Run the exact `PROGRESS-ENTRY-02` packet with the resulting entry and installed-state variant. Record observed behavior in `tests/skills/using_devcraft_toolkit/evaluations/2026-10-22-codex-desktop/progress-composition.md`. Expected: every assertion for that case holds. If an optional tool/installation condition cannot be exercised, record the specific limitation rather than a pass.

- [x] **Step 6: Verify composition case PROGRESS-ENTRY-03**

Run the exact `PROGRESS-ENTRY-03` packet with the resulting entry and installed-state variant. Record observed behavior in `tests/skills/using_devcraft_toolkit/evaluations/2026-10-22-codex-desktop/progress-composition.md`. Expected: every assertion for that case holds. If an optional tool/installation condition cannot be exercised, record the specific limitation rather than a pass.

- [x] **Step 7: Update composition and installation documentation**

Modify `docs/composition.md`, `docs/installation.md`, `docs/compatibility.md`, `docs/roadmap.md` to describe direct versus optional entry use, actual evaluated coverage and current availability. Catalog status was established by Task 1; a routing issue does not invent failure or success of standalone behavior.

- [ ] **Step 8: Run the automated regression suite**

Run: `python -m unittest discover -s tests -p "test_*.py" -v`.
Expected: pass with actual environmental skips disclosed and a nonzero discovered test count.

- [ ] **Step 9: Validate the repository after composition**

Run: `python scripts/validate_repository.py --root .`.
Expected: exit 0 and `Repository catalog is valid.`. The catalog still has seventeen names and the entry's two hard dependencies.

- [ ] **Step 10: Inspect the composition diff**

Run: `git diff --check`.
Expected: exit 0. Confirm no unimplemented coordinator, CCR integration, plugin or extra runtime was introduced.

- [ ] **Step 11: Commit the complete composition delivery**

Stage only actually changed files from this exact owned list and the retained entry evaluation. Keep the successfully verified standalone declaration intact.

~~~sh
git add -- skills/using-devcraft-toolkit/SKILL.md skills/using-devcraft-toolkit/references/composition.md tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md tests/skills/using_devcraft_toolkit/evaluations/2026-10-22-codex-desktop/progress-composition.md docs/composition.md docs/installation.md docs/compatibility.md docs/roadmap.md
git commit -m "feat: route todo-workflow-controller through the toolkit"
~~~
Inspect local identity before the write. Branch publication, PR creation, merge and release require their own authorization.

## Self-review and execution record

- Spec coverage: Task 1 covers every owned `PRG-01`, `PRG-02`, `PRG-03`, `PRG-04`, `PRG-05` behavior; Task 2 covers direct, routed and absent-installation behavior.
- Step scan: each checkbox names one action, its exact file/case or command, and its observable result. Fixture preparation belongs to its capability delivery rather than a separate unreviewable scaffolding task.
- Contract consistency: canonical owner `todo-workflow-controller`, normalized package `todo_workflow_controller`, empty hard dependencies and retained evaluation paths match the spec and tasks.
- Review Focus: all five classes map to concrete owned cases before implementation; no missing-file failure or generic prose check substitutes for baseline behavior.
- Proportion: implementation bodies remain with the executor; literal test packets, source templates and fixture interfaces preserve the non-obvious decisions.
- Task 1 execution: all five baseline and manual GREEN cases are recorded; the baseline showed no valid RED. The portable contract remains a product requirement, while native loading and other harnesses remain unverified. The full suite passed (57 tests, one Windows symlink-permission skip), the repository validator passed, and `git diff --check` passed.
- Task 2 execution: direct, routed, and absent-installation cases were evaluated in fresh manual contexts. The refined baseline showed that the entry did not invoke the matching installed capability and could imitate it when absent; all three GREEN cases passed after the explicit optional route was added. The route does not alter the entry hard dependencies. Native loading and actual harness-managed installed-state discovery remain unverified.

Execution selection: Native implementation in the isolated worktree with fresh-agent behavior evaluations. The user authorized implementation in roadmap order; the current shared-capability sequence is formatting, progress control, reporting and validation. Each delivery requires its recorded behavior checks and repository validation. Branch publication, pull requests and releases are outside this plan.
