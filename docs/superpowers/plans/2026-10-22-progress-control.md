# Portable Progress Control Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) tracking.

**Goal:** Deliver todo-workflow-controller as an independently usable capability with recorded evidence.
**Architecture:** Instruction-first skill with local resources, no required skill dependencies and externally owned behavioral tests. Reuse the existing repository validator and language/composition contracts.
**Tech Stack:** Markdown, YAML frontmatter, existing JSON catalog, Python 3.11+/PyYAML development checks; no new runtime framework.
**Spec:** [Portable Progress Control design](../specs/2026-10-22-progress-control-design.md).
**Status:** Proposed for review; implementation has not started.

## Global Constraints

- Source instructions, documentation, examples and default templates are English; user-facing output uses explicit user preference, then request language, then English when indeterminate.
- Technical identifiers, schema keys, command syntax and supplied data identifiers remain unchanged by translation.
- Tests, fixtures, scenarios and retained evaluations live under tests/skills/<normalized_skill_name>/; root tests/integration/ is only for multiple named skills.
- Installed skills use only their bundled resources and explicitly declared skill dependencies; repository tooling and catalog.json are development resources.
- Implementation must be understandable from repository-local requirements and accessible official technical references, without private conversations, personal paths or unavailable files.
- Catalog status stays planned until structural checks and actual behavioral evaluation justify available; record unexecuted cases as limitations.
- No new coordinator, CCR/Jira integration, plugin manifest, installer, release automation or runtime orchestration engine is included.
- Use Python 3.11+ and the existing PyYAML>=6.0,<7.0 development setup; add no dependencies or helpers without a demonstrated need.

## Review Focus

1. A failed required gate cannot become completed via a checkbox or a skip.
2. Missing or failed task tools must retain blockers while allowing safe independent work.
3. An unanswered user decision is never implied approval.
4. Actual parallel work must be tracked honestly rather than forced into one active step.
5. Progress tracking must not create files or expand operation permissions.

## Task 1: Define executable behavioral evaluation packets

**Files:**
- tests/skills/todo_workflow_controller/scenarios/progress.md

**Interfaces:**
- Canonical owner: todo-workflow-controller; normalized package: todo_workflow_controller.
- Test inputs: A workflow with dependency/required-gate information, actual progress evidence, decisions and exposed tracking tools.
- Expected result: Accurate step states, unresolved gates and a truthful final progress summary, with no extra artifact by default.
- Scenario protocol: tests/scenarios/README.md. Behavioral evaluation is not a keyword check against instructions.

- [ ] **Step 1: Write the owned scenarios before the skill.** Include the exact input facts/state and the expected decisions for these cases:
  - progress.md: A sequential workflow starts a dependent step only after its prerequisite has evidence; an optional skip has a reason.
  - progress.md: No todo tool or a mid-run tool failure uses inline tracking without writing an extra artifact or losing a blocker.
  - progress.md: A failed required validation or unanswered decision prevents a completed claim; a user waiver remains a waiver.
  - progress.md: A blocked branch does not stop independent authorized tasks; explicitly parallel tasks are represented accurately.
  - progress.md: Language follows the user and a context handoff preserves what remains unverified without inventing executed work.
- [ ] **Step 2: Prepare the smallest self-contained fixture/evidence packets.** Use small supplied task/evidence packets, not a synthetic runtime. Include sequential, independent-branch, parallel and interrupted runs. Evaluate native-tool and no-tool cases only when the harness actually supports the scenario, or record a simulation/limitation explicitly.
- [ ] **Step 3: Establish the initial unmet acceptance result.** The skill is currently planned and absent. Record that its invocation cannot yet satisfy these cases; do not invent a failing executable test or claim a model ran an unavailable skill. The evaluation packets are the behavioral contract for the following task.
- [ ] **Step 4: Verify ownership and fixture safety.** Every case is under tests/skills/todo_workflow_controller/; no runtime resource links to it. Do not run blocked command variants or touch production resources. Keep current catalog status planned.
- [ ] **Step 5: Commit only the owned scenario/fixture files after git diff --check.** Suggested subject: test: define todo-workflow-controller behavior. Adapt the natural-language subject to the active contribution-language instruction.

## Task 2: Implement the capability and verify actual behavior

**Files:**
- Modify: catalog.json, README.md, docs/architecture.md, docs/installation.md and docs/compatibility.md after actual standalone verification.
- skills/todo-workflow-controller/SKILL.md
- skills/todo-workflow-controller/references/progress-states.md


**Interfaces:**
- Consumes the Task 1 request/evidence packets.
- Produces the skill/reference contracts defined in the spec, with requires=[].
- No script/API signature is invented when the product is an instructional capability.
- Modify catalog.json and standalone availability documentation only after the principal behavioral cases have actually been verified.

- [ ] **Step 1: Author the smallest complete skill and its actual local resources.** Author the state/transition and tool-adaptation rules. Keep tracking in working context, allowing concise inline fallback. Do not hardcode a harness tool name or make a missing progress tool a universal blocker. Preserve required decisions and evidence through tool failures. Do not add a scheduler, persistent state framework or automatic delegation.
- [ ] **Step 2: Evaluate progress.md against the implemented skill in the actual harness.** Record whether it was discovered/loaded or followed manually. Supply raw facts/fixtures and the request; do not feed an evaluator the intended diagnosis as evidence. Retain optional notes under tests/skills/todo_workflow_controller/evaluations/<run>.md with actual outcomes and limitations.
- [ ] **Step 3: Check side effects, language and negative cases.** Compare fixture files/state before and after; distinguish expected scoped effects from unauthorized or unexpected changes. Check claims against input facts and actual command results. Cases not dynamically exercised remain limited.
- [ ] **Step 4: Fix demonstrated discrepancies and rerun only affected cases.** Do not change the acceptance rule merely to make a result pass. Add an executable test only if a real helper/contract has been introduced and the test verifies its behavior.
- [ ] **Step 5: Verify local resources and commit exact owned files after git diff --check.** After evidence review, mark only this verified standalone capability available with requires=[] and update README.md, docs/architecture.md, docs/installation.md and docs/compatibility.md to match its actual availability. Run the repository tests and validator before committing. If a material acceptance gate remains unmet, this task remains incomplete: do not commit or merge a discoverable skill advertised as planned. Suggested subject: feat: add todo-workflow-controller.

## Task 3: Integrate honest availability and close the increment

**Files:**
- Modify: catalog.json.
- Modify: skills/using-devcraft-toolkit/SKILL.md and skills/using-devcraft-toolkit/references/composition.md only for the new optional installed-capability route.
- Modify: tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md.
- Modify: README.md, docs/architecture.md, docs/composition.md, docs/installation.md, docs/compatibility.md and docs/roadmap.md.
- Add cross-skill scenarios/evidence under tests/integration/ only when a case truly involves multiple named skills.

**Interfaces:**
- Change only todo-workflow-controller to available with requires=[] after checking actual structural and behavioral evidence.
- The standalone capability was verified and made available by Task 2. Recheck that evidence before entry composition; do not change other capabilities' statuses.
- Entry routing uses actual installed capability availability; it does not add this optional capability to its existing hard requires group.
- Derive availability counts from the catalog at execution time; other independent increments may already be present.

- [ ] **Step 1: Recheck standalone evidence before composition.** The principal intended behavior must have been exercised. If a material required scenario is blocked, keep the candidate unadvertised/planned and describe the unmet gate rather than inventing a pass. Do not merge discoverable candidate files while they violate planned-placeholder validation.
- [ ] **Step 2: Update the catalog and optional route together with their documentation.** Preserve missing-capability behavior and leave all other unimplemented coordinators planned. A standalone invocation needs no repository-root documentation or development catalog.
- [ ] **Step 3: Exercise direct invocation, entry composition and missing optional installation.** Record actual results and recheck the foundation context/preflight boundaries. Do not claim compatibility for an untested harness or an isolated installer that was not run.
- [ ] **Step 4: Run the repository checks from the selected worktree using an actual Python interpreter.**
~~~sh
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repository.py --root .
git diff --check
~~~
Expected: discovered tests pass with explicitly explained environmental skips; repository validation is valid; no whitespace errors. Baseline count is not a hardcoded future expected total.
- [ ] **Step 5: Review and commit exact owned files.** Verify the effective repository-local Git identity before any write; do not change global identity. Suggested subject: feat: expose todo-workflow-controller in the toolkit. Publishing, PR creation, merging and release remain separate authorized operations.

## Coverage and handoff

Task 1 defines every Review Focus case, Task 2 implements and evaluates its decisions, and Task 3 verifies composition and honest catalog status. Preserve actual limitations and source-local resource containment. The spec and test packets contain the implementation requirements; no external private material is required.

Review this plan with its in-repository spec before implementation. Native execution is suitable for a small instruction-first increment; subagent-driven execution is also possible if selected. These documents do not record product execution or change catalog availability.
