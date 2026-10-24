# Git Analysis and Commit Planning Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver two read-only capabilities that explain local Git changes and propose evidence-based commits while preserving the index selection.

**Architecture:** Instruction-first analyzer with a local inspection/record reference; planner consumes that record and delegates messages to the existing formatter. Optional entry routes and explicit installation dependency closures package the same canonical folders.

**Tech Stack:** Markdown skills and references, JSON catalog/manifests, Python unittest development fixtures, local Git. No new runtime executable or dependency.

**Spec:** [Git analysis and planning design](../specs/2026-10-24-git-analysis-planning-design.md)

## Global Constraints

- Keep maintained source instructions, documentation, examples, and default templates in English. Resolve output language from explicit preference, then request language, then English; preserve technical identifiers and schema keys.
- Keep every installed skill self-contained. Declare dependencies in `catalog.json`; installed execution never requires that file or root documentation.
- Keep all automated tests, scenarios, fixtures, and retained evaluations under root `tests/`, grouped by canonical skill owner and scope.
- Perform no Git writes, network access, validation execution, credential changes, branch creation, staging, commits, publication, cleanup, or persisted analysis/plan output. Return records in the conversation.
- Do not introduce a runtime interpreter dependency, installer, hook, MCP service, coordinator placeholder, or new distribution mechanism.
- Native loading and authenticated invocation remain separate from manually following instructions. Existing preview.2 evidence describes its seven-skill payload and must remain historical.
- Product read-only boundaries above apply when users execute the delivered capabilities. Development fixture setup and commits of this implementation remain separate authorized work in the isolated feature worktree.

## Review Focus

1. Same-path staged/unstaged edits must never collapse into one selection or accidentally broaden a staged-only plan (Tasks 1–2).
2. Worktree changes with unchanged status codes or a stale supplied record must invalidate freshness; repeating status alone is insufficient (Tasks 1–2).
3. Configured external diff, textconv, clean/process filters, filesystem monitors and lazy fetch must not run during inspection (Task 1).
4. Filenames containing spaces, shell-looking text or pathspec magic and rename pairs must remain exact data; symlinks/submodules must not escape the selected scope (Task 1).
5. Missing/foreign dependency ownership must yield unavailable rather than emulation, while standalone closure and English/Spanish outputs remain supported (Tasks 2–3).

## File map

- Create analyzer `skills/git-analyze-changes/SKILL.md` and `references/inspection.md`.
- Create planner `skills/git-plan-commits/SKILL.md` and `references/planning.md`.
- Create owner-scoped scenarios, replay facts, evaluations and integration tests under `tests/skills/git_analyze_changes/` and `tests/skills/git_plan_commits/`; reuse `tests/support/git_fixtures.py`.
- Modify `catalog.json`, entry instructions/reference and owner-scoped entry scenarios/evaluation.
- Modify `README.md`, `docs/roadmap.md`, `docs/architecture.md`, `docs/composition.md`, `docs/compatibility.md`, current installation inventory/closures, `CHANGELOG.md`, and both plugin manifest versions. Historical release/evaluation documents retain their original inventory.

## Execution record

The design builder check reported “nothing important left”. The user requested spec, plan, remaining-roadmap documentation and then implementation in one continuous task. Execute inline with fresh-context behavioral actors and one final reviewer; do not request another planning approval. Retain genuine baseline successes and disclose evidence limits.

---

### Task 1: Analyze local changes

**Files:**
- Create: `skills/git-analyze-changes/SKILL.md`, `skills/git-analyze-changes/references/inspection.md`
- Create: `tests/skills/git_analyze_changes/{__init__.py,fixtures/analysis-facts.json,scenarios/analysis.md,evaluations/2026-10-24.md,integration/__init__.py,integration/test_inspection_recipes.py}`
- Modify: analyzer entry in `catalog.json`

**Interfaces:**
- Consumes: current `git-working-directory-policy` repository context.
- Produces: conversation analysis record with `outcome`, `repository`, `scope`, `snapshot`, `changes`, `constraints`, `unknowns`. Evidence entries have stable local IDs, exact paths, layer, kind, facts and coverage.

- [x] **Step 1: Define scenarios and baseline replay facts before skill authoring.**
  Cover mixed layers, content guard mutation with unchanged status, helper/filter safety, special paths/rename/deletion/binary/symlink/submodule, unborn/detached/conflict/missing identity and absent context dependency. Five fresh no-guidance replay controls establish the record-shaping baseline; retain verbatim outputs and failures without turning baseline successes into failures.
- [x] **Step 2: Write/run real Git fixture recipe tests.**
  In `test_inspection_recipes.py`, assert index/worktree evidence differs for a partially staged file, NUL names/rename pairs survive, disabling helpers leaves sentinels absent, content guard changes despite unchanged status, and full repository snapshots match before/after read recipes. Run `python -B -m unittest tests.skills.git_analyze_changes.integration.test_inspection_recipes -v`. These are command-semantic controls; they may already pass and must not be called missing-skill RED tests.
- [x] **Step 3: Author the minimal skill/reference from observed gaps and the specified contract.**
  Description starts `Use when...`; main instructions stay concise. Add the conservative filter gate, safe local Git prefix, NUL/literal path handling, bounded content coverage and before/after guards. Mark only the analyzer available, requiring repository context.
- [x] **Step 4: Repeat five fresh replay samples with full skill/local reference and test edge/gap scenarios.**
  Expected: complete or explicitly limited contract, layers and exact names preserved, freshness/support constraints explicit; no claim of native loading. Record actual deviations and rerun affected cases after necessary corrections.
- [x] **Step 5: Validate and commit the completed analyzer.**
  Run the Task 1 unittest command, `python -B scripts/validate_repository.py --root .`, and `git diff --check`. Expected: success. Commit `feat: add read-only Git change analysis` with owner-scoped tests/evidence.

### Task 2: Plan commits from evidence

**Files:**
- Create: `skills/git-plan-commits/SKILL.md`, `skills/git-plan-commits/references/planning.md`
- Create: `tests/skills/git_plan_commits/{__init__.py,fixtures/planning-facts.json,scenarios/planning.md,evaluations/2026-10-24.md,integration/__init__.py,integration/test_planning_fixtures.py}`
- Modify: planner entry in `catalog.json`

**Interfaces:**
- Consumes: Task 1 analysis record; installed `conventional-commits-style` supplied-facts message formatting.
- Produces: `outcome`, `analysis_snapshot`, `selection_policy`, `groups`, `excluded`, `decisions`, `limitations`. Groups have `id`, `intent`, `evidence`, `selection`, `depends_on`, `rationale`, `message`.

- [ ] **Step 1: Create planning scenarios and run five fresh baseline replay controls without planner instructions.**
  Cover staged-first default, same-path mixed intent, implementation/tests/docs belonging together, dependency order, explicit empty staged scope, missing formatter, stale record, blocked conflicts/active operation, ambiguous/binary coverage and language. Record raw outputs and score exact contract separately from sound general judgment.
- [ ] **Step 2: Write/run development fixture tests.**
  Assert real staged and worktree blobs represent different intents, a staged-only selection excludes untracked work, empty staged content does not imply clean repository, and changed index/content invalidates the captured facts. Run `python -B -m unittest tests.skills.git_plan_commits.integration.test_planning_fixtures -v`; expected: fixture controls pass without any mutation by inspected read recipes.
- [ ] **Step 3: Author skill/reference and mark the planner available.**
  Declare direct requirements `git-analyze-changes` and `conventional-commits-style`. Require context closure, freshness, intent groups, layer/hunk selections, exclusions and pending decisions. Reuse the formatter; do not silently repartition staged work or produce a complete plan when material facts are missing.
- [ ] **Step 4: Repeat five fresh replay samples with full instructions and dependencies, then edge/gap scenarios.**
  Expected: contract, staged selection, conditional proposals/blocked outcomes and formatter delegation match the spec; outputs follow request language. Retain manual evidence honestly.
- [ ] **Step 5: Validate and commit the completed planner.**
  Run the Task 2 unittest command, repository validator and `git diff --check`; expected: success. Commit `feat: add evidence-based commit planning`.

### Task 3: Compose and distribute the nine-skill candidate

**Files:**
- Modify: `skills/using-devcraft-toolkit/{SKILL.md,references/composition.md}`, `tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md`
- Create: `tests/skills/using_devcraft_toolkit/evaluations/git-preparation-composition.md`
- Modify: current documentation and manifest files from the File map; installation pages only where inventory or dependency closure changes.

**Interfaces:**
- Consumes: both available capabilities and declared dependency closures from Tasks 1–2.
- Produces: optional ownership-aware routes, nine available/eight planned entries, matching unpublished manifest version `0.1.0-preview.3`, current installation instructions and roadmap gates.

- [ ] **Step 1: Run entry composition baseline scenarios before changing instructions.**
  Cases: analysis installed in selected suite, planner absent despite foreign namespaced copy, required dependency missing, explicit standalone closure and unrelated formatter-only request. Expected missing new routing is retained as baseline evidence.
- [ ] **Step 2: Add optional routes and their dependency/result boundaries.**
  Preserve ownership-qualified identifiers and unavailable behavior; the foundation hard closure stays unchanged. Re-run fresh-context composition scenarios with both English and Spanish requests.
- [ ] **Step 3: Synchronize current documentation and candidate metadata.**
  Update inventory and explicit individual/full-set installation closures, scope/status of the new evidence, `Unreleased` changelog, and staged roadmap. Preserve preview.2's seven-skill historical evidence and release URLs. Leave authenticated native invocation gates open.
- [ ] **Step 4: Run complete verification.**
  Run `python -B -m unittest discover -s tests -p "test_*.py" -v`, `python -B scripts/validate_repository.py --root .`, `python -B -m scripts.validate_distribution --root .`, and `git diff --check`.
  Expected: all runnable tests pass (existing Windows symlink privilege skip is disclosed), both validators succeed, no whitespace errors.
- [ ] **Step 5: Commit and perform one fresh whole-branch review.**
  Commit `feat: compose Git analysis and planning in the toolkit`. Review the spec, plan, ledger rulings and branch diff. Re-grade findings by user impact; fix Important/Critical findings once with reproduced evidence and rerun affected/full checks. Record minor deferrals explicitly. Do not merge or publish a release in this increment.

## Self-review

All spec sections map to Tasks 1–3. Record contracts are identical at producer/consumer boundaries. Every Review Focus condition has owner-scoped scenarios and fixture/behavior evidence; structural checks do not substitute for skill invocation. The remaining roadmap work stays planned with no placeholder skills. Plan approval and implementation continuation were included in the user's current instruction.

