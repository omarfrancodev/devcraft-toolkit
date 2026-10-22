# Project Validation Discovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) tracking.

**Goal:** Deliver validation-discovery as an independently usable capability with recorded evidence.
**Architecture:** Instruction-first skill with local resources, no required skill dependencies and externally owned behavioral tests. Reuse the existing repository validator and language/composition contracts.
**Tech Stack:** Markdown, YAML frontmatter, existing JSON catalog, Python 3.11+/PyYAML development checks; no new runtime framework.
**Spec:** [Project Validation Discovery design](../specs/2026-10-22-project-validation-design.md).
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

1. A name such as lint or test must not conceal hooks, autofix or installation.
2. Discover mode and missing execution tools must not become an executed pass.
3. An inspected local composite can be valid without relaxing authorization for unknown effects.
4. All required checks need outcomes; the first passing check is insufficient.
5. Exit 0 with unexpected writes must preserve evidence and block affected downstream work.

## Task 1: Define executable behavioral evaluation packets

**Files:**
- tests/skills/validation_discovery/scenarios/discovery.md
- tests/skills/validation_discovery/scenarios/execution.md
- tests/skills/validation_discovery/fixtures/local-project/check.py
- tests/skills/validation_discovery/fixtures/local-project/package.json

**Interfaces:**
- Canonical owner: validation-discovery; normalized package: validation_discovery.
- Test inputs: Selected project root, discover|run mode, requested checks, project instructions/configuration and optional supplied context.
- Expected result: Sourced candidate decisions and actual execution records with return codes, side effects and required-gate coverage.
- Scenario protocol: tests/scenarios/README.md. Behavioral evaluation is not a keyword check against instructions.

- [ ] **Step 1: Write the owned scenarios before the skill.** Include the exact input facts/state and the expected decisions for these cases:
  - discovery.md: Discover a command without running it; absent project-defined commands return not_detected and do not trigger guessed execution.
  - discovery.md: Inspect a wrapper and hooks: autofix/install or unknown external effects block the candidate; an understood local composite is not rejected solely for its operator.
  - execution.md: A requested harmless local Python check is executed in a temporary non-Git project with spaces in its path; preserve its exact return code and output.
  - execution.md: A failed check, missing tool or missing dependency remains failed/blocked/not_run; a retry requires an observed transient cause.
  - execution.md: All required checks are accounted for; unexpected file changes are preserved and reported, not cleaned or marked as passed.
- [ ] **Step 2: Prepare the smallest self-contained fixture/evidence packets.** Create a temporary-copy fixture from local-project/check.py and package.json. check.py accepts pass (stdout 'check ok', exit 0), fail (stderr 'check failed', exit 3) and unexpected-write (create unexpected.txt, exit 0). The package fixture declares a local check wrapper; scenarios also supply harmless blocked wrapper variants. Run only copied fixtures, never these tracked files or a real business service.
- [ ] **Step 3: Establish the initial unmet acceptance result.** The skill is currently planned and absent. Record that its invocation cannot yet satisfy these cases; do not invent a failing executable test or claim a model ran an unavailable skill. The evaluation packets are the behavioral contract for the following task.
- [ ] **Step 4: Verify ownership and fixture safety.** Every case is under tests/skills/validation_discovery/; no runtime resource links to it. Do not run blocked command variants or touch production resources. Keep current catalog status planned.
- [ ] **Step 5: Commit only the owned scenario/fixture files after git diff --check.** Suggested subject: test: define validation-discovery behavior. Adapt the natural-language subject to the active contribution-language instruction.

## Task 2: Implement the capability and verify actual behavior

**Files:**
- Modify: catalog.json, README.md, docs/architecture.md, docs/installation.md and docs/compatibility.md after actual standalone verification.
- skills/validation-discovery/SKILL.md
- skills/validation-discovery/references/check-selection.md
- Modify: AGENTS.md and tests/scenarios/README.md only for the precise side effects defined by this spec.

**Interfaces:**
- Consumes the Task 1 request/evidence packets.
- Produces the skill/reference contracts defined in the spec, with requires=[].
- No script/API signature is invented when the product is an instructional capability.
- Modify catalog.json and standalone availability documentation only after the principal behavioral cases have actually been verified.

- [ ] **Step 1: Author the smallest complete skill and its actual local resources.** Author command selection, full-wrapper inspection, side-effect assessment, execution evidence and retry boundaries in the skill/reference. No general-purpose command parser, runner framework or product helper is needed. Update AGENTS.md and the common scenario protocol to permit only this capability's explicitly requested safe local checks and owned temporary artifacts; foundation context/preflight remain read-only.
- [ ] **Step 2: Evaluate discovery.md, execution.md against the implemented skill in the actual harness.** Record whether it was discovered/loaded or followed manually. Supply raw facts/fixtures and the request; do not feed an evaluator the intended diagnosis as evidence. Retain optional notes under tests/skills/validation_discovery/evaluations/<run>.md with actual outcomes and limitations.
- [ ] **Step 3: Check side effects, language and negative cases.** Compare fixture files/state before and after; distinguish expected scoped effects from unauthorized or unexpected changes. Check claims against input facts and actual command results. Cases not dynamically exercised remain limited.
- [ ] **Step 4: Fix demonstrated discrepancies and rerun only affected cases.** Do not change the acceptance rule merely to make a result pass. Add an executable test only if a real helper/contract has been introduced and the test verifies its behavior.
- [ ] **Step 5: Verify local resources and commit exact owned files after git diff --check.** After evidence review, mark only this verified standalone capability available with requires=[] and update README.md, docs/architecture.md, docs/installation.md and docs/compatibility.md to match its actual availability. Run the repository tests and validator before committing. If a material acceptance gate remains unmet, this task remains incomplete: do not commit or merge a discoverable skill advertised as planned. Suggested subject: feat: add validation-discovery.

## Task 3: Integrate honest availability and close the increment

**Files:**
- Modify: catalog.json.
- Modify: skills/using-devcraft-toolkit/SKILL.md and skills/using-devcraft-toolkit/references/composition.md only for the new optional installed-capability route.
- Modify: tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md.
- Modify: README.md, docs/architecture.md, docs/composition.md, docs/installation.md, docs/compatibility.md and docs/roadmap.md.
- Add cross-skill scenarios/evidence under tests/integration/ only when a case truly involves multiple named skills.

**Interfaces:**
- Change only validation-discovery to available with requires=[] after checking actual structural and behavioral evidence.
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
- [ ] **Step 5: Review and commit exact owned files.** Verify the effective repository-local Git identity before any write; do not change global identity. Suggested subject: feat: expose validation-discovery in the toolkit. Publishing, PR creation, merging and release remain separate authorized operations.

## Coverage and handoff

Task 1 defines every Review Focus case, Task 2 implements and evaluates its decisions, and Task 3 verifies composition and honest catalog status. Preserve actual limitations and source-local resource containment. The spec and test packets contain the implementation requirements; no external private material is required.

Review this plan with its in-repository spec before implementation. Native execution is suitable for a small instruction-first increment; subagent-driven execution is also possible if selected. These documents do not record product execution or change catalog availability.
