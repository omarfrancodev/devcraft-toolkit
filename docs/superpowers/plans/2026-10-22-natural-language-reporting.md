# Natural-Language Reporting Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver natural-language-report-writer as a verified standalone capability with optional toolkit entry composition.

**Architecture:** Implement an instruction-first skill with bundled local resources and no hard skill dependencies. Validate its behavior before declaring it available, then integrate the optional entry route as a separate complete delivery.

**Tech Stack:** Markdown, YAML frontmatter, JSON catalog, Python 3.11+, PyYAML>=6.0,<7.0 and the existing unittest suite. Behavioral evaluation uses the actual supported harness rather than a fabricated test runner.

**Spec:** [Natural-Language Reporting design](../specs/2026-10-22-natural-language-reporting-design.md).

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

1. RPT-01: several related facts consolidate without invented completion or impact. Task 1 owns the named case.
2. RPT-02: empty/conflicting evidence remains explicit instead of producing filler. Task 1 owns the named case.
3. RPT-03: translated headings preserve dates, numbers and identifiers. Task 1 owns the named case.
4. RPT-04: a technical audience and custom format override the starter template. Task 1 owns the named case.
5. RPT-05: content-only and explicit local-file output have different side-effect boundaries. Task 1 owns the named case.

---

## Evaluation procedure for instruction-first deliverables

The case data and assertions below are the tests. For baseline, provide only request/facts and actual permitted tools to the acting evaluator; assess its response separately against the assertions. For GREEN, use the same packet with the candidate skill supplied. Keep both observations. A missing file, skipped scenario, evaluator limitation or green baseline is not RED evidence.

Use supported fresh evaluation contexts when available, and record whether the invocation loaded the skill or followed it manually. If the required behavioral evaluation cannot run, leave the affected gate unresolved. Do not manufacture independence with an unapproved external CLI. Record results at the exact evaluation paths below, including actual run dates, tools and side effects.

Use the selected isolated worktree. Resolve the actual Python interpreter before commands; no test helper is an installed runtime dependency. Task steps leave all product implementation unexecuted until the written spec/plan have been reviewed and an execution method selected.

### Task 1: Deliver the verified standalone natural-language-report-writer capability

**Files:**
- Create: `skills/natural-language-report-writer/SKILL.md`
- Create: `skills/natural-language-report-writer/references/report-quality.md`
- Create: `skills/natural-language-report-writer/assets/report.md`
- Test: `tests/skills/natural_language_report_writer/scenarios/reporting.md`
- Test: `tests/skills/natural_language_report_writer/fixtures/report-facts.json`
- Create: `tests/skills/natural_language_report_writer/evaluations/standalone.md`.
- Modify: `catalog.json`
- Modify: `README.md`
- Modify: `docs/architecture.md`
- Modify: `docs/installation.md`
- Modify: `docs/compatibility.md`
- Modify: `AGENTS.md` and `tests/scenarios/README.md` for only the explicitly defined side effects.

**Interfaces:**
- Consumes: the request/evidence packets below, actual tool capabilities, resolved language and the spec's input contract.
- Produces: natural-language-report-writer with the spec's result and side-effect boundaries, local resources, behavioral evidence and `requires: []`.
- No new callable product API or test-only keyword parser is introduced.
- Availability is committed atomically with the verified standalone implementation; existing unrelated catalog names/statuses remain unchanged.

- [x] **Step 1: Write reporting.md as the behavior test**

Create `tests/skills/natural_language_report_writer/scenarios/reporting.md` with canonical owner `natural-language-report-writer` and the following case data. These are evaluation packets, not a new automated test engine. Keep assertions separate from the packet given to the acting evaluator.

~~~yaml
cases:
  - id: RPT-01
    name: consolidation_and_numeric_fidelity
    request: "Summarize these facts as an activity report in Spanish."
    facts: "Date: 2026-10-20. Empty-name validation was added. A clear error for missing names was added. Search rendering is pending. Twelve fixture cases passed."
    assertions:
      - "Consolidate the two related validation facts without losing their meaning."
      - "Keep search rendering unfinished and preserve the date and count 12."
      - "Do not invent business gains, deployment, authorship or additional tests."
  - id: RPT-02
    name: empty_and_conflicting_evidence
    request: "Prepare the report."
    facts: "Variant A: no facts. Variant B: one supplied note says search is complete; another says the same search work is pending."
    assertions:
      - "Variant A identifies insufficient evidence without filler activities."
      - "Variant B preserves or clarifies the conflict; it does not arbitrarily choose completed."
  - id: RPT-03
    name: translation_preserves_data
    request: "Use the default template in French. Then repeat in English with an explicit instruction to answer in Spanish."
    facts: "Date 2026-10-20; count 12; identifier ORDER-7."
    assertions:
      - "Translate visible headings and prose to the resolved language."
      - "Preserve 2026-10-20, 12 and ORDER-7 exactly; do not translate placeholder keys in the source template."
  - id: RPT-04
    name: technical_audience_and_custom_format
    request: "Use exactly two sections, Findings and Evidence. Include the filename and identifier."
    facts: "parser.py now rejects an empty name; reference ORDER-7; no deployment information."
    assertions:
      - "Use the requested sections, with labels translated only if requested."
      - "Preserve supplied technical detail rather than forcing an outcome-only template."
      - "Do not add unsupported deployment or test claims."
  - id: RPT-05
    name: content_only_then_requested_file
    request: "First provide report content only. In a separate request, save that content to the selected temporary report.md."
    facts: "Use the supplied fact fixture. The evaluator provides the actual temporary destination only in the second request."
    assertions:
      - "The first request creates no file."
      - "The second request writes only the selected report.md and verifies it by reading it back."
      - "Unrelated files and the input fixture remain unchanged."
~~~

- [x] **Step 2: Write the data-only fact fixture**

Create `tests/skills/natural_language_report_writer/fixtures/report-facts.json` with these exact values; scenarios use a copy of this data.

~~~json
{
  "date": "2026-10-20",
  "facts": [
    "Empty-name validation was added.",
    "A clear error for missing names was added.",
    "Search rendering is pending.",
    "Twelve fixture cases passed."
  ],
  "count": 12,
  "identifier": "ORDER-7"
}
~~~

- [x] **Step 3: Run baseline case RPT-01 without the candidate skill**

Use a supported fresh evaluation context with only the `RPT-01` request/facts from `tests/skills/natural_language_report_writer/scenarios/reporting.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/natural_language_report_writer/evaluations/standalone.md` under `RPT-01/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [x] **Step 4: Run baseline case RPT-02 without the candidate skill**

Use a supported fresh evaluation context with only the `RPT-02` request/facts from `tests/skills/natural_language_report_writer/scenarios/reporting.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/natural_language_report_writer/evaluations/standalone.md` under `RPT-02/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [x] **Step 5: Run baseline case RPT-03 without the candidate skill**

Use a supported fresh evaluation context with only the `RPT-03` request/facts from `tests/skills/natural_language_report_writer/scenarios/reporting.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/natural_language_report_writer/evaluations/standalone.md` under `RPT-03/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [x] **Step 6: Run baseline case RPT-04 without the candidate skill**

Use a supported fresh evaluation context with only the `RPT-04` request/facts from `tests/skills/natural_language_report_writer/scenarios/reporting.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/natural_language_report_writer/evaluations/standalone.md` under `RPT-04/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [x] **Step 7: Run baseline case RPT-05 without the candidate skill**

Use a supported fresh evaluation context with only the `RPT-05` request/facts from `tests/skills/natural_language_report_writer/scenarios/reporting.md` and the actual permitted tools. Omit candidate instructions and assertions from the actor packet. Record its response, tool effects and each assertion outcome in `tests/skills/natural_language_report_writer/evaluations/standalone.md` under `RPT-05/baseline`. Expected RED evidence is a specific observed violated assertion; absence of the skill alone is not a failure.

- [x] **Step 8: Assess the baseline before authoring**

Identify which named assertion actually failed and why. If all cases pass, do not claim RED or write guidance merely to satisfy this plan: record the result and resolve whether an untested requirement or any need for the capability remains. Missing supported evaluation contexts or tools produce an explicit limitation; never manufacture independence or a failed baseline.

- [x] **Step 9: Write the primary skill**

Create `skills/natural-language-report-writer/SKILL.md` with `name: natural-language-report-writer` and a concise description limited to when the skill applies. Implement the spec's request/result flow and boundaries, addressing the demonstrated baseline gap. The body carries essential behavior; substantial conditional detail goes in the listed local reference. No root-doc runtime dependency or hard skill dependency is added.

- [x] **Step 10: Write the local reference**

Create `skills/natural-language-report-writer/references/report-quality.md` with the spec's domain decisions and the demonstrated edge cases. For each of `RPT-01`, `RPT-02`, `RPT-03`, `RPT-04`, `RPT-05`, an executor must be able to find the decision that governs its assertions. Do not copy the test packet into installed resources or replace behavior with a list of prohibitions unrelated to an observed failure.

- [x] **Step 11: Write the English starter template**

Create `skills/natural-language-report-writer/assets/report.md` with this source structure. The skill translates visible headings, honors an explicitly requested format first, and removes an unused optional Open items section; placeholder keys remain unchanged.

~~~markdown
# {{title}}

## Summary
{{summary}}

## Activities
{{activities}}

## Open items
{{open_items}}
~~~

- [x] **Step 12: Declare only the capability's permitted effects**

Modify `AGENTS.md` and `tests/scenarios/README.md` to distinguish this capability's expressly requested single local report file with readback from read-only foundation context/preflight. Retain all unrelated permission boundaries; the scenario itself must name its allowed effects.

- [x] **Step 13: Run GREEN case RPT-01 with the skill**

Repeat the exact `RPT-01` request/facts and tool restrictions in a fresh supported context, now providing `skills/natural-language-report-writer/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/natural_language_report_writer/evaluations/standalone.md` under `RPT-01/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [x] **Step 14: Run GREEN case RPT-02 with the skill**

Repeat the exact `RPT-02` request/facts and tool restrictions in a fresh supported context, now providing `skills/natural-language-report-writer/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/natural_language_report_writer/evaluations/standalone.md` under `RPT-02/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [x] **Step 15: Run GREEN case RPT-03 with the skill**

Repeat the exact `RPT-03` request/facts and tool restrictions in a fresh supported context, now providing `skills/natural-language-report-writer/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/natural_language_report_writer/evaluations/standalone.md` under `RPT-03/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [x] **Step 16: Run GREEN case RPT-04 with the skill**

Repeat the exact `RPT-04` request/facts and tool restrictions in a fresh supported context, now providing `skills/natural-language-report-writer/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/natural_language_report_writer/evaluations/standalone.md` under `RPT-04/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [x] **Step 17: Run GREEN case RPT-05 with the skill**

Repeat the exact `RPT-05` request/facts and tool restrictions in a fresh supported context, now providing `skills/natural-language-report-writer/SKILL.md` and its accessible local resources. Record actual behavior and assertions in `tests/skills/natural_language_report_writer/evaluations/standalone.md` under `RPT-05/green`. Expected: all stated assertions hold. Record manual following or unavailable variants accurately; neither is silently relabeled as independent loaded-skill success.

- [x] **Step 18: Refine only a demonstrated behavioral gap**

If a GREEN assertion fails, adjust only the responsible instruction/resource and state the observed reason in `tests/skills/natural_language_report_writer/evaluations/standalone.md`. If no gap remains, record no change. Do not add unrelated policy or alter an expected assertion merely to turn a result green.

- [x] **Step 19: Recheck the affected cases after refinement**

Run only affected `RPT-01`, `RPT-02`, `RPT-03`, `RPT-04`, `RPT-05` cases, plus an earlier passing case when the changed instruction can affect it. Expected: the recorded gap is fixed without losing a required behavior. An unrun material case remains an unmet availability gate.

**Result:** The five GREEN cases passed without a demonstrated gap, so no instruction refinement or follow-up case run was needed.

- [x] **Step 20: Publish the verified standalone catalog entry**

Only after principal behavioral cases are verified, modify the `natural-language-report-writer` entry in `catalog.json` to `status: available` and keep `requires: []`. Preserve all other statuses. Until that evidence exists this task is incomplete; do not commit a discoverable skill together with a planned-placeholder violation.

- [x] **Step 21: Update standalone availability documentation**

Modify `README.md`, `docs/architecture.md`, `docs/installation.md`, `docs/compatibility.md` to describe this standalone capability, its observed limits and its empty hard dependency list. Derive counts from the current catalog. Do not rewrite the historical foundation delivery count or advertise the entry route before Task 2.

- [x] **Step 22: Run the existing automated suite**

Run: `python -m unittest discover -s tests -p "test_*.py" -v` from the selected worktree with an actual Python 3.11+ interpreter.
Expected: discovered tests pass, with observed environmental skips reported explicitly. This is structural/fixture regression evidence, not proof of the new skill's behavior.

- [x] **Step 23: Run repository validation**

Run: `python scripts/validate_repository.py --root .`.
Expected: `Repository catalog is valid.` and exit 0. Fix source/catalog/resource disagreements before committing.

- [x] **Step 24: Check the standalone diff**

Run: `git diff --check`.
Expected: exit 0 and no whitespace errors. Inspect that only Task 1 files and the named availability updates are changed.

- [x] **Step 25: Commit the complete standalone delivery**

Inspect effective repository-local identity before the write. Stage exact owned files and commit the verified capability; do not stage a directory or unrelated work.

~~~sh
git add -- skills/natural-language-report-writer/SKILL.md skills/natural-language-report-writer/references/report-quality.md skills/natural-language-report-writer/assets/report.md tests/skills/natural_language_report_writer/scenarios/reporting.md tests/skills/natural_language_report_writer/fixtures/report-facts.json tests/skills/natural_language_report_writer/evaluations/standalone.md catalog.json README.md docs/architecture.md docs/installation.md docs/compatibility.md AGENTS.md tests/scenarios/README.md
git commit -m "feat: add natural-language-report-writer"
~~~

**Result:** Committed locally as `e6abfa1` on `feat/capability-design` using the repository-local Git identity. No push was performed.

The message is an English source example; follow the active contribution-language instruction for execution. This task contains its own test/evaluation cycle and independently usable deliverable.

### Task 2: Deliver and verify optional toolkit composition

**Files:**
- Modify: `skills/using-devcraft-toolkit/SKILL.md`
- Modify: `skills/using-devcraft-toolkit/references/composition.md`
- Test: `tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md`
- Create: `tests/skills/using_devcraft_toolkit/evaluations/reporting-composition.md`
- Modify: `docs/composition.md`
- Modify: `docs/installation.md`
- Modify: `docs/compatibility.md`
- Modify: `docs/roadmap.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: Task 1's available standalone capability and its recorded evidence, plus the actual installed-state variants below.
- Produces: an optional route, truthful absent-installation behavior and recorded entry evidence; the entry's existing hard dependency group stays unchanged.
- A composition failure keeps this task incomplete; it does not silently redefine a verified standalone result.

- [x] **Step 1: Write the entry-composition behavior cases**

Append an owned `natural-language-report-writer` section to `tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md` with these cases; keep existing entry cases intact.

~~~yaml
cases:
  - id: REPORTING-ENTRY-01
    name: direct_call
    request: "Invoke natural-language-report-writer directly with its first owned scenario."
    facts: "The new standalone capability is installed; no repository root is supplied to the installed skill."
    assertions:
      - "The owned behavior is preserved; no development catalog or root docs are required at runtime."
  - id: REPORTING-ENTRY-02
    name: optional_entry_route
    request: "Use Devcraft Toolkit for the natural-language reporting request in the first owned scenario."
    facts: "The entry, its foundation dependencies and natural-language-report-writer are actually installed."
    assertions:
      - "Route the requested operation to natural-language-report-writer without running an unrelated Git preflight or another coordinator."
      - "Language and permission boundaries remain those of the owned scenario."
  - id: REPORTING-ENTRY-03
    name: optional_skill_absent
    request: "Use Devcraft Toolkit for the same natural-language reporting request."
    facts: "The entry and foundation group are installed, but natural-language-report-writer is not."
    assertions:
      - "Report the missing capability honestly without emulation, automatic installation or an invented completed result."
~~~

- [x] **Step 2: Evaluate the existing entry before changing its instructions**

Run `REPORTING-ENTRY-01`, `REPORTING-ENTRY-02`, `REPORTING-ENTRY-03` against the current entry and the Task 1 standalone skill. Record actual responses and assertions in `tests/skills/using_devcraft_toolkit/evaluations/reporting-composition.md`. Expected: identify a concrete routing gap if one exists; do not assume the entry needs more text merely because a new skill exists.

- [x] **Step 3: Implement only the demonstrated composition change**

If the baseline entry misses a named assertion, modify `skills/using-devcraft-toolkit/SKILL.md` and `skills/using-devcraft-toolkit/references/composition.md` to add the optional installed route and preserve missing-capability behavior. If it already meets every assertion, leave its instructions unchanged and record that decision. Do not add `natural-language-report-writer` to the entry's hard `requires` array.

- [x] **Step 4: Verify composition case REPORTING-ENTRY-01**

Run the exact `REPORTING-ENTRY-01` packet with the resulting entry and installed-state variant. Record observed behavior in `tests/skills/using_devcraft_toolkit/evaluations/reporting-composition.md`. Expected: every assertion for that case holds. If an optional tool/installation condition cannot be exercised, record the specific limitation rather than a pass.

- [x] **Step 5: Verify composition case REPORTING-ENTRY-02**

Run the exact `REPORTING-ENTRY-02` packet with the resulting entry and installed-state variant. Record observed behavior in `tests/skills/using_devcraft_toolkit/evaluations/reporting-composition.md`. Expected: every assertion for that case holds. If an optional tool/installation condition cannot be exercised, record the specific limitation rather than a pass.

- [x] **Step 6: Verify composition case REPORTING-ENTRY-03**

Run the exact `REPORTING-ENTRY-03` packet with the resulting entry and installed-state variant. Record observed behavior in `tests/skills/using_devcraft_toolkit/evaluations/reporting-composition.md`. Expected: every assertion for that case holds. If an optional tool/installation condition cannot be exercised, record the specific limitation rather than a pass.

- [x] **Step 7: Update composition and installation documentation**

Modify `README.md`, `docs/composition.md`, `docs/installation.md`, `docs/compatibility.md`, and `docs/roadmap.md` to describe direct versus optional entry use, actual evaluated coverage and current availability. Catalog status was established by Task 1; a routing issue does not invent failure or success of standalone behavior.

- [x] **Step 8: Run the automated regression suite**

Run: `python -m unittest discover -s tests -p "test_*.py" -v`.
Expected: pass with actual environmental skips disclosed and a nonzero discovered test count.

- [x] **Step 9: Validate the repository after composition**

Run: `python scripts/validate_repository.py --root .`.
Expected: exit 0 and `Repository catalog is valid.`. The catalog still has seventeen names and the entry's two hard dependencies.

- [x] **Step 10: Inspect the composition diff**

Run: `git diff --check`.
Expected: exit 0. Confirm no unimplemented coordinator, CCR/Jira integration, plugin or extra runtime was introduced.

- [x] **Step 11: Commit the complete composition delivery**

Stage only actually changed files from this exact owned list and the retained entry evaluation. Keep the successfully verified standalone declaration intact.

~~~sh
git add -- skills/using-devcraft-toolkit/SKILL.md skills/using-devcraft-toolkit/references/composition.md tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md tests/skills/using_devcraft_toolkit/evaluations/reporting-composition.md docs/composition.md docs/installation.md docs/compatibility.md docs/roadmap.md README.md docs/superpowers/plans/2026-10-22-natural-language-reporting.md
git commit -m "feat: route natural-language-report-writer through the toolkit"
~~~

**Result:** Committed locally on `feat/capability-design` using the repository-local identity. No push was performed.

Inspect local identity before the write. Branch publication, PR creation, merge and release require their own authorization.

## Self-review and execution handoff

- Spec coverage: Task 1 covers every owned `RPT-01`, `RPT-02`, `RPT-03`, `RPT-04`, `RPT-05` behavior; Task 2 covers direct, routed and absent-installation behavior.
- Step scan: each checkbox names one action, its exact file/case or command, and its observable result. Fixture preparation belongs to its capability delivery rather than a separate unreviewable scaffolding task.
- Contract consistency: canonical owner `natural-language-report-writer`, normalized package `natural_language_report_writer`, empty hard dependencies and retained evaluation paths match the spec and tasks.
- Review Focus: all five classes map to concrete owned cases before implementation; no missing-file failure or generic prose check substitutes for baseline behavior.
- Proportion: implementation bodies remain with the executor; literal test packets, source templates and fixture interfaces preserve the non-obvious decisions.

The spec is a draft for written review; this companion plan remains provisional until that spec is approved. After reviewing both, select Native or Subagent-driven execution. Native implementation with final independent review is the lower-overhead option for this small two-delivery increment; skill behavior still needs the real evaluation cycle described above. No approval, implementation or evaluation is implied by the presence of these files.
