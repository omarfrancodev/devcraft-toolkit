# Commit Message Formatting Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver conventional-commits-style as a verified standalone capability with optional toolkit entry composition.

**Architecture:** Implement an instruction-first skill with bundled local resources and no hard skill dependencies. Validate its behavior before declaring it available, then integrate the optional entry route as a separate complete delivery.

**Tech Stack:** Markdown, YAML frontmatter, JSON catalog, Python 3.11+, PyYAML>=6.0,<7.0 and the existing unittest suite. Behavioral evaluation uses the actual supported harness rather than a fabricated test runner.

**Spec:** [Commit Message Formatting design](../specs/2026-10-22-commit-message-formatting-design.md).

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

## Review Focus

1. FMT-01: competing references and a later correction preserve the actual user decision. Task 1 owns the named case.
2. FMT-02: project-specific types, optional scope and requested bodies remain usable. Task 1 owns the named case.
3. FMT-03: breaking syntax is never inferred from a request alone. Task 1 owns the named case.
4. FMT-04: shell-looking message data is preserved without execution. Task 1 owns the named case.
5. FMT-05: no repository and language changes do not alter the requested formatting scope. Task 1 owns the named case.

---

## Evaluation procedure for instruction-first deliverables

The case data and assertions below are the tests. For baseline, provide only request/facts and actual permitted tools to the acting evaluator; assess its response separately against the assertions. For GREEN, use the same packet with the candidate skill supplied. Keep both observations. A missing file, skipped scenario, evaluator limitation or green baseline is not RED evidence.

Use supported fresh evaluation contexts when available, and record whether the invocation loaded the skill or followed it manually. If the required behavioral evaluation cannot run, leave the affected gate unresolved. Do not manufacture independence with an unapproved external CLI. Record results at the exact evaluation paths below, including actual run dates, tools and side effects.

Use the selected isolated worktree. Resolve the actual Python interpreter before commands; no test helper is an installed runtime dependency. Task steps leave all product implementation unexecuted until the written spec/plan have been reviewed and an execution method selected.

### Task 1: Deliver the verified standalone conventional-commits-style capability

**Files:**
- Create: `skills/conventional-commits-style/SKILL.md`
- Create: `skills/conventional-commits-style/references/message-format.md`
- Test: `tests/skills/conventional_commits_style/scenarios/formatting.md`
- Create: `tests/skills/conventional_commits_style/evaluations/standalone.md`.
- Modify: `catalog.json`
- Modify: `README.md`
- Modify: `docs/architecture.md`
- Modify: `docs/installation.md`
- Modify: `docs/compatibility.md`


**Interfaces:**
- Consumes: the request/evidence packets below, actual tool capabilities, resolved language and the spec's input contract.
- Produces: conventional-commits-style with the spec's result and side-effect boundaries, local resources, behavioral evidence and `requires: []`.
- No new callable product API or test-only keyword parser is introduced.
- Availability is committed atomically with the verified standalone implementation; existing unrelated catalog names/statuses remain unchanged.

- [ ] **Step 1: Write formatting.md as the behavior test**

Create `tests/skills/conventional_commits_style/scenarios/formatting.md` with canonical owner `conventional-commits-style` and the following case data. These are evaluation packets, not a new automated test engine. Keep assertions separate from the packet given to the acting evaluator.

~~~yaml
cases:
  - id: FMT-01
    name: ambiguous_reference_then_correction
    request: "Prepare a commit for the parser fix. Relevant issues may be TASK-12 or TASK-13. Do not choose one for me."
    facts: "The parser rejects an empty name with a clear error. Later response: Use TASK-13."
    assertions:
      - "Initial output asks which applicable issue to use and invents neither selection nor extra issue."
      - "After the explicit response, only TASK-13 is referenced and the decision is updated."
  - id: FMT-02
    name: project_specific_type_scope_and_body
    request: "Our project uses maintenance for internal cleanup. Draft a maintenance(parser) commit with a body."
    facts: "Consolidated duplicate parser checks; no user-visible behavior changed."
    assertions:
      - "Use the supplied maintenance type and parser scope; do not force feat or fix."
      - "The body describes the supplied cleanup without a fabricated functional change or test result."
  - id: FMT-03
    name: breaking_marker_requires_evidence
    request: "Draft a commit; add a breaking marker only if justified."
    facts: "An error message was clarified; no public input/output contract changed."
    assertions:
      - "No ! marker or BREAKING CHANGE footer is invented."
      - "Return a proposal without running Git."
  - id: FMT-04
    name: quoted_subject_is_data
    request: "Propose a subject that mentions the literal strings \"ready\", $HOME and $(touch marker). Do not execute anything."
    facts: "Logging preserves these literal values."
    assertions:
      - "Preserve the supplied literals as data; no shell command or file named marker is created."
      - "Do not drop useful wording merely to fit a future command-line quoting style."
  - id: FMT-05
    name: language_without_repository
    request: "Redacta un commit para corregir la validación de nombres vacíos; no hay repositorio disponible."
    facts: "The input rejects empty names. Repeat with an English request and with: Answer in French."
    assertions:
      - "Natural-language subject follows Spanish, English and the explicit French override respectively."
      - "Technical Conventional Commit tokens remain intact; no Git repository, ticket or validation result is invented."
  - id: FMT-06
    name: missing_intent
    request: "Write the commit."
    facts: "No change description, repository or evidence was provided."
    assertions:
      - "Ask for the change intent instead of producing a generic unsupported completion claim."
~~~

- [ ] **Step 2: Run baseline case FMT-01 without the candidate skill**

Use a supported fresh evaluation context with only the `FMT-01` request/facts from `tests/skills/conventional_commits_style/scenarios/formatting.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/conventional_commits_style/evaluations/standalone.md` under `FMT-01/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [ ] **Step 3: Run baseline case FMT-02 without the candidate skill**

Use a supported fresh evaluation context with only the `FMT-02` request/facts from `tests/skills/conventional_commits_style/scenarios/formatting.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/conventional_commits_style/evaluations/standalone.md` under `FMT-02/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [ ] **Step 4: Run baseline case FMT-03 without the candidate skill**

Use a supported fresh evaluation context with only the `FMT-03` request/facts from `tests/skills/conventional_commits_style/scenarios/formatting.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/conventional_commits_style/evaluations/standalone.md` under `FMT-03/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [ ] **Step 5: Run baseline case FMT-04 without the candidate skill**

Use a supported fresh evaluation context with only the `FMT-04` request/facts from `tests/skills/conventional_commits_style/scenarios/formatting.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/conventional_commits_style/evaluations/standalone.md` under `FMT-04/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [ ] **Step 6: Run baseline case FMT-05 without the candidate skill**

Use a supported fresh evaluation context with only the `FMT-05` request/facts from `tests/skills/conventional_commits_style/scenarios/formatting.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/conventional_commits_style/evaluations/standalone.md` under `FMT-05/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [ ] **Step 7: Run baseline case FMT-06 without the candidate skill**

Use a supported fresh evaluation context with only the `FMT-06` request/facts from `tests/skills/conventional_commits_style/scenarios/formatting.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/conventional_commits_style/evaluations/standalone.md` under `FMT-06/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [ ] **Step 8: Assess the baseline before authoring**

Identify which named assertion actually failed and why. If all cases pass, do not claim RED or write guidance merely to satisfy this plan: record the result and resolve whether an untested requirement or any need for the capability remains. Missing supported evaluation contexts or tools produce an explicit limitation; never manufacture independence or a failed baseline.

- [ ] **Step 9: Write the primary skill**

Create `skills/conventional-commits-style/SKILL.md` with `name: conventional-commits-style` and a concise description limited to when the skill applies. Implement the spec's request/result flow and boundaries, addressing the demonstrated baseline gap. The body carries essential behavior; substantial conditional detail goes in the listed local reference. No root-doc runtime dependency or hard skill dependency is added.

- [ ] **Step 10: Write the local reference**

Create `skills/conventional-commits-style/references/message-format.md` with the spec's domain decisions and the demonstrated edge cases. For each of `FMT-01`, `FMT-02`, `FMT-03`, `FMT-04`, `FMT-05`, `FMT-06`, an executor must be able to find the decision that governs its assertions. Do not copy the test packet into installed resources or replace behavior with a list of prohibitions unrelated to an observed failure.

- [ ] **Step 11: Run GREEN case FMT-01 with the skill**

Repeat the exact `FMT-01` request/facts and tool restrictions in a fresh supported context, now providing `skills/conventional-commits-style/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/conventional_commits_style/evaluations/standalone.md` under `FMT-01/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [ ] **Step 12: Run GREEN case FMT-02 with the skill**

Repeat the exact `FMT-02` request/facts and tool restrictions in a fresh supported context, now providing `skills/conventional-commits-style/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/conventional_commits_style/evaluations/standalone.md` under `FMT-02/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [ ] **Step 13: Run GREEN case FMT-03 with the skill**

Repeat the exact `FMT-03` request/facts and tool restrictions in a fresh supported context, now providing `skills/conventional-commits-style/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/conventional_commits_style/evaluations/standalone.md` under `FMT-03/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [ ] **Step 14: Run GREEN case FMT-04 with the skill**

Repeat the exact `FMT-04` request/facts and tool restrictions in a fresh supported context, now providing `skills/conventional-commits-style/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/conventional_commits_style/evaluations/standalone.md` under `FMT-04/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [ ] **Step 15: Run GREEN case FMT-05 with the skill**

Repeat the exact `FMT-05` request/facts and tool restrictions in a fresh supported context, now providing `skills/conventional-commits-style/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/conventional_commits_style/evaluations/standalone.md` under `FMT-05/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [ ] **Step 16: Run GREEN case FMT-06 with the skill**

Repeat the exact `FMT-06` request/facts and tool restrictions in a fresh supported context, now providing `skills/conventional-commits-style/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/conventional_commits_style/evaluations/standalone.md` under `FMT-06/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [ ] **Step 17: Refine only a demonstrated behavioral gap**

If a GREEN assertion fails, adjust only the responsible instruction/resource and state the observed reason in `tests/skills/conventional_commits_style/evaluations/standalone.md`. If no gap remains, record no change. Do not add unrelated policy or alter an expected assertion merely to turn a result green.

- [ ] **Step 18: Recheck the affected cases after refinement**

Run only affected `FMT-01`, `FMT-02`, `FMT-03`, `FMT-04`, `FMT-05`, `FMT-06` cases, plus an earlier passing case when the changed instruction can affect it. Expected: the recorded gap is fixed without losing a required behavior. An unrun material case remains an unmet availability gate.

- [ ] **Step 19: Publish the verified standalone catalog entry**

Only after principal behavioral cases are verified, modify the `conventional-commits-style` entry in `catalog.json` to `status: available` and keep `requires: []`. Preserve all other statuses. Until that evidence exists this task is incomplete; do not commit a discoverable skill together with a planned-placeholder violation.

- [ ] **Step 20: Update standalone availability documentation**

Modify `README.md`, `docs/architecture.md`, `docs/installation.md`, `docs/compatibility.md` to describe this standalone capability, its observed limits and its empty hard dependency list. Derive counts from the current catalog. Do not rewrite the historical foundation delivery count or advertise the entry route before Task 2.

- [ ] **Step 21: Run the existing automated suite**

Run: `python -m unittest discover -s tests -p "test_*.py" -v` from the selected worktree with an actual Python 3.11+ interpreter.
Expected: discovered tests pass, with observed environmental skips reported explicitly. This is structural/fixture regression evidence, not proof of the new skill's behavior.

- [ ] **Step 22: Run repository validation**

Run: `python scripts/validate_repository.py --root .`.
Expected: `Repository catalog is valid.` and exit 0. Fix source/catalog/resource disagreements before committing.

- [ ] **Step 23: Check the standalone diff**

Run: `git diff --check`.
Expected: exit 0 and no whitespace errors. Inspect that only Task 1 files and the named availability updates are changed.

- [ ] **Step 24: Commit the complete standalone delivery**

Inspect effective repository-local identity before the write. Stage exact owned files and commit the verified capability; do not stage a directory or unrelated work.

~~~sh
git add -- skills/conventional-commits-style/SKILL.md skills/conventional-commits-style/references/message-format.md tests/skills/conventional_commits_style/scenarios/formatting.md tests/skills/conventional_commits_style/evaluations/standalone.md catalog.json README.md docs/architecture.md docs/installation.md docs/compatibility.md
git commit -m "feat: add conventional-commits-style"
~~~
The message is an English source example; follow the active contribution-language instruction for execution. This task contains its own test/evaluation cycle and independently usable deliverable.

### Task 2: Deliver and verify optional toolkit composition

**Files:**
- Modify: `skills/using-devcraft-toolkit/SKILL.md`
- Modify: `skills/using-devcraft-toolkit/references/composition.md`
- Test: `tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md`
- Create: `tests/skills/using_devcraft_toolkit/evaluations/formatting-composition.md`
- Modify: `docs/composition.md`
- Modify: `docs/installation.md`
- Modify: `docs/compatibility.md`
- Modify: `docs/roadmap.md`

**Interfaces:**
- Consumes: Task 1's available standalone capability and its recorded evidence, plus the actual installed-state variants below.
- Produces: an optional route, truthful absent-installation behavior and recorded entry evidence; the entry's existing hard dependency group stays unchanged.
- A composition failure keeps this task incomplete; it does not silently redefine a verified standalone result.

- [ ] **Step 1: Write the entry-composition behavior cases**

Append an owned `conventional-commits-style` section to `tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md` with these cases; keep existing entry cases intact.

~~~yaml
cases:
  - id: FORMATTING-ENTRY-01
    name: direct_call
    request: "Invoke conventional-commits-style directly with its first owned scenario."
    facts: "The new standalone capability is installed; no repository root is supplied to the installed skill."
    assertions:
      - "The owned behavior is preserved; no development catalog or root docs are required at runtime."
  - id: FORMATTING-ENTRY-02
    name: optional_entry_route
    request: "Use Devcraft Toolkit for the commit message formatting request in the first owned scenario."
    facts: "The entry, its foundation dependencies and conventional-commits-style are actually installed."
    assertions:
      - "Route the requested operation to conventional-commits-style without running an unrelated Git preflight or another coordinator."
      - "Language and permission boundaries remain those of the owned scenario."
  - id: FORMATTING-ENTRY-03
    name: optional_skill_absent
    request: "Use Devcraft Toolkit for the same commit message formatting request."
    facts: "The entry and foundation group are installed, but conventional-commits-style is not."
    assertions:
      - "Report the missing capability honestly without emulation, automatic installation or an invented completed result."
~~~

- [ ] **Step 2: Evaluate the existing entry before changing its instructions**

Run `FORMATTING-ENTRY-01`, `FORMATTING-ENTRY-02`, `FORMATTING-ENTRY-03` against the current entry and the Task 1 standalone skill. Record actual responses and assertions in `tests/skills/using_devcraft_toolkit/evaluations/formatting-composition.md`. Expected: identify a concrete routing gap if one exists; do not assume the entry needs more text merely because a new skill exists.

- [ ] **Step 3: Implement only the demonstrated composition change**

If the baseline entry misses a named assertion, modify `skills/using-devcraft-toolkit/SKILL.md` and `skills/using-devcraft-toolkit/references/composition.md` to add the optional installed route and preserve missing-capability behavior. If it already meets every assertion, leave its instructions unchanged and record that decision. Do not add `conventional-commits-style` to the entry's hard `requires` array.

- [ ] **Step 4: Verify composition case FORMATTING-ENTRY-01**

Run the exact `FORMATTING-ENTRY-01` packet with the resulting entry and installed-state variant. Record observed behavior in `tests/skills/using_devcraft_toolkit/evaluations/formatting-composition.md`. Expected: every assertion for that case holds. If an optional tool/installation condition cannot be exercised, record the specific limitation rather than a pass.

- [ ] **Step 5: Verify composition case FORMATTING-ENTRY-02**

Run the exact `FORMATTING-ENTRY-02` packet with the resulting entry and installed-state variant. Record observed behavior in `tests/skills/using_devcraft_toolkit/evaluations/formatting-composition.md`. Expected: every assertion for that case holds. If an optional tool/installation condition cannot be exercised, record the specific limitation rather than a pass.

- [ ] **Step 6: Verify composition case FORMATTING-ENTRY-03**

Run the exact `FORMATTING-ENTRY-03` packet with the resulting entry and installed-state variant. Record observed behavior in `tests/skills/using_devcraft_toolkit/evaluations/formatting-composition.md`. Expected: every assertion for that case holds. If an optional tool/installation condition cannot be exercised, record the specific limitation rather than a pass.

- [ ] **Step 7: Update composition and installation documentation**

Modify `docs/composition.md`, `docs/installation.md`, `docs/compatibility.md`, `docs/roadmap.md` to describe direct versus optional entry use, actual evaluated coverage and current availability. Catalog status was established by Task 1; a routing issue does not invent failure or success of standalone behavior.

- [ ] **Step 8: Run the automated regression suite**

Run: `python -m unittest discover -s tests -p "test_*.py" -v`.
Expected: pass with actual environmental skips disclosed and a nonzero discovered test count.

- [ ] **Step 9: Validate the repository after composition**

Run: `python scripts/validate_repository.py --root .`.
Expected: exit 0 and `Repository catalog is valid.`. The catalog still has seventeen names and the entry's two hard dependencies.

- [ ] **Step 10: Inspect the composition diff**

Run: `git diff --check`.
Expected: exit 0. Confirm no unimplemented coordinator, CCR/Jira integration, plugin or extra runtime was introduced.

- [ ] **Step 11: Commit the complete composition delivery**

Stage only actually changed files from this exact owned list and the retained entry evaluation. Keep the successfully verified standalone declaration intact.

~~~sh
git add -- skills/using-devcraft-toolkit/SKILL.md skills/using-devcraft-toolkit/references/composition.md tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md tests/skills/using_devcraft_toolkit/evaluations/formatting-composition.md docs/composition.md docs/installation.md docs/compatibility.md docs/roadmap.md
git commit -m "feat: route conventional-commits-style through the toolkit"
~~~
Inspect local identity before the write. Branch publication, PR creation, merge and release require their own authorization.

## Self-review and execution handoff

- Spec coverage: Task 1 covers every owned `FMT-01`, `FMT-02`, `FMT-03`, `FMT-04`, `FMT-05`, `FMT-06` behavior; Task 2 covers direct, routed and absent-installation behavior.
- Step scan: each checkbox names one action, its exact file/case or command, and its observable result. Fixture preparation belongs to its capability delivery rather than a separate unreviewable scaffolding task.
- Contract consistency: canonical owner `conventional-commits-style`, normalized package `conventional_commits_style`, empty hard dependencies and retained evaluation paths match the spec and tasks.
- Review Focus: all five classes map to concrete owned cases before implementation; no missing-file failure or generic prose check substitutes for baseline behavior.
- Proportion: implementation bodies remain with the executor; literal test packets, source templates and fixture interfaces preserve the non-obvious decisions.

The spec is a draft for written review; this companion plan remains provisional until that spec is approved. After reviewing both, select Native or Subagent-driven execution. Native implementation with final independent review is the lower-overhead option for this small two-delivery increment; skill behavior still needs the real evaluation cycle described above. No approval, implementation or evaluation is implied by the presence of these files.
