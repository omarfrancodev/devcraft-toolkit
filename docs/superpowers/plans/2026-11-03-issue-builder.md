# Issue Builder Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver portable issue authoring for bugs, improvements and new features, plus requested subtask decomposition, without performing the described work.

**Architecture:** One instruction-first support skill with two modes and an empty dependency closure. Reuse existing catalog, presentation and package validators; add optional owned entry routing and owner-scoped behavioral/package evidence.

**Tech Stack:** Markdown, YAML, JSON; Python 3.11+ development validators and unittest. No new runtime code, dependencies or installer.

**Spec:** [Issue Builder Design](../specs/2026-11-03-issue-builder-design.md).

## Global Constraints

- Coverage: defects, improvements, new features and requested parent decomposition; no automatic hierarchy.
- Source instructions, metadata and default examples stay in English; output uses explicit preference, request language, then English.
- Confirmed scope and optional suggestions remain distinct throughout body, acceptance criteria and children.
- Latest selected revisions prevail; retain unaffected requirements and exact identifiers, amounts, units, permissions and negations.
- Return conversation text only; no repository/provider investigation, embedded execution, file writes or external creation.
- One complete skill folder, `requires: []`; entry routing is optional and preserves ownership and existing dependencies.
- Automated tests, fixtures, scenarios and retained evidence belong under root `tests/`, grouped by skill and scope.
- Current source becomes twenty available skills; published preview.10 remains nineteen. No version, historical-release, license or deferred-integration changes.
- Work in repository-local `.worktrees/issue-builder`, branch `feat/issue-builder`; preserve other worktrees and unrelated changes.
- Execute the plan inline as already requested, with fresh behavioral actors and a final independent review. No additional plan approval is needed. Commit, push, PR, merge and release are outside the requested execution scope.

## Review Focus

- Plausible extra implementation decisions become required acceptance criteria: Task 1 repeated authoring controls and feature case must expose optional versus mandatory work.
- A corrected parent changes a technical field and removes work: Task 1 revision/decomposition sequence must use the latest field and exclude removed promises.
- A requested child count cannot cover the parent coherently: Task 1 conflicting-partition case must retain the gap and request a decision rather than invent work.
- Amounts or missing attachments are silently repaired: Task 1 contradiction/missing-content cases must flag unavailable or conflicting facts.
- Issue authoring is routed to prompt improvement or Git execution: Task 2 owned/missing/foreign/ambiguous routing cases must select the exact owner without preflight.

---

## Task 1: Standalone issue authoring and decomposition

**Files:**
- Create: `skills/issue-builder/SKILL.md`, `skills/issue-builder/agents/openai.yaml`.
- Create: `tests/skills/issue_builder/fixtures/requests.json`, `scenarios/authoring.md`, and retained output/evaluation files in `evaluations/2026-11-03/`.

**Interfaces:**
- Consumes: supplied request or latest selected parent, subsequent corrections, desired split/count and language/format preferences.
- Produces: complete issue, requested child artifacts, selected revision or focused material clarification in conversation text.
- Runtime dependency closure: the `issue-builder` folder only; presentation values are `Issue Builder` and `Turn supplied requirements into clear issues and subtasks`.

- [x] **Step 1: Write raw synthetic fixtures and observable scenario assertions.** Include defects with numeric/scoped rules, a new feature, an improvement, chained reported causes, a corrected-parent/two-child sequence, conflicting requested split, missing parent content, independent-case reset, explicit language override, concise title/template and embedded commands/posting. Keep assertions out of raw actor inputs.
- [x] **Step 2: Record RED behavior before authoring.** Run five fresh no-guidance contexts on the same two core authoring inputs. Read actual output, retain successes and scope/shape failures verbatim with fixture hashes. Also run the broader raw sequence without the skill. Do not label ordinary baseline success a failure or infer safety from tool restrictions.
- [x] **Step 3: Write the minimum effective skill.** Use a positive artifact recipe and conditional mode rules for the observed gaps. Preserve latest-source, evidence, optional-advice, arithmetic and decomposition contracts. Keep the entire concise contract in `SKILL.md`; add no reference/template unless a demonstrated need arises. Generate presentation-only YAML with the exact values above and no policy or dependencies.
- [x] **Step 4: Record GREEN and refine.** Run five fresh candidate contexts on the identical core inputs, plus a fresh broader sequence. Read each output against the scenario assertions. Preserve output and source hashes; refine only an observed gap, then rerun affected cases. Record incomplete or inconsistent outcomes honestly rather than asserting universal reliability.
- [x] **Step 5: Validate the standalone definition.** Run the host skill-creator `quick_validate.py` against the new folder. Expected: valid frontmatter; behavioral evidence remains separate. Record tool/model limitations and native activation as unverified.

## Task 2: Suite integration, packaging and verification

**Files:**
- Create: `tests/skills/issue_builder/__init__.py`, `integration/__init__.py`, `integration/test_standalone_package.py`.
- Modify: `catalog.json`, `docs/capability-inventory.md`, `skills/using-devcraft-toolkit/SKILL.md`, `skills/using-devcraft-toolkit/references/composition.md`.
- Create: `tests/integration/issue_authoring/fixtures/routing.json`, `scenarios/routing.md`, `evaluations/2026-11-03/` evidence.
- Modify: `README.md`, `docs/architecture.md`, `docs/composition.md`, `docs/roadmap.md`, `docs/compatibility.md`, `docs/installation.md`, `docs/installation/individual-skills.md`, `docs/installation/development.md`, `CHANGELOG.md`.
- Record: `tests/skills/issue_builder/evaluations/2026-11-03/verification.md`, `review.md` and `full-suite.log`.

**Interfaces:**
- Consumes: verified Task 1 folder and exact available inventory/dependency contracts.
- Produces: `support`/`available` catalog entry at `skills/issue-builder` with `requires: []`; twenty current names, one-folder standalone installation and optional owned entry dispatch before Git routes.

- [x] **Step 1: Add a real failing package test.** `IssueBuilderPackageTests.test_complete_folder_validates_without_other_skills_or_root_docs` selects the new available catalog entry, copies its complete folder plus minimal existing manifest/assets validator fixtures into `tests/.tmp`, and asserts both validators return `[]`, no root docs/other skills exist, and every copied byte matches. Run `python -B -m unittest tests.skills.issue_builder.integration.test_standalone_package -v`; expect failure because the catalog entry is absent.
- [x] **Step 2: Add incomplete-package controls.** `test_missing_presentation_is_rejected` removes only `agents/openai.yaml` in the temporary copy and expects `distribution-skill-interface`. `test_missing_entrypoint_is_rejected` removes only `SKILL.md` and expects a repository issue against that path. No source-wording assertions or source-package mutation.
- [x] **Step 3: Integrate inventory and prove GREEN.** Add the available catalog entry and canonical inventory row. Rerun the three owner package tests; expect all pass. Run `python -B scripts/validate_repository.py --root .` and `python -B -m scripts.validate_distribution --root .`; expect both valid. Existing validators already support arbitrary available names and presentation sidecars; change their implementation only for a demonstrated contract gap.
- [x] **Step 4: Test the existing entry before changing it.** Use fresh actors with supplied discovery facts for owned issue drafting, decomposition, foreign-only, missing, ambiguous copies, prompt-refinement distinction and independent report/PR routes. Retain baseline outputs. Add an optional `issue-builder` route and a discriminating description; rerun the same cases. Assert exact selected identifier, no foreign substitution/installation/imitation or Git preflight, and unchanged required dependencies. Existing prompt-refinement routing remains a regression control.
- [x] **Step 5: Update current docs and unreleased changelog.** Document the two authoring modes, one-folder selection and optional route. Set current-source counts/selections to twenty only where appropriate. Keep every published preview.10/older claim and manifest version unchanged; clarify that default remote recipes gain the addition after integration and fixed preview.10 lacks it. Add an `Added` / `Shared capabilities` unreleased bullet. Source docs contain no private provenance.
- [x] **Step 6: Run focused and full verification.** Run owner package and existing repository/distribution/prompt package tests, both validators, local Markdown-link checks for changed current docs and `git diff --check`. Run `python -B -m unittest discover -s tests -p "test_*.py" -v`, retain real counts/output and distinguish Windows privilege skips from passes. Expected transient fixtures: `tests/.tmp` and OS-owned temporary directories; preserve any unexpected edits. Do not install/update clients or dependencies.
- [x] **Step 7: Review and close execution.** Request one fresh whole-change review against the approved design and this plan. Resolve supported findings, rerun affected checks and broaden only for unresolved/new changes. Record source hashes, actual behavioral/structural outcomes and native limitations; complete checkboxes only for performed steps. Report the local branch/worktree and remaining publication steps without staging, committing, pushing or opening a PR.

## Plan self-review

The two tasks cover input/language, authoring, decomposition, revision/reset,
numeric and missing-source behavior, presentation/self-containment, optional
ownership routing, current versus released distribution and separate evidence
levels. All five Review Focus classes have explicit behavioral or package
controls. No new runtime signature, provider adapter, automatic test generator
or fixed output-heading contract is introduced.
