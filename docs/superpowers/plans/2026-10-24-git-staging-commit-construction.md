# Scoped Staging and Commit Construction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver exact approved index changes and a coordinator that creates requested local commits without broadening scope.

**Architecture:** Two self-contained instruction-first skills reuse current analysis/preflight/planning, formatter, validation and progress contracts. Real disposable Git fixtures establish recipe semantics; fresh actor controls and candidate applications establish observed instruction following.

**Tech Stack:** Markdown skills/references, JSON catalog/manifests, Python unittest development fixtures, Git. No new runtime interpreter dependency.

**Spec:** [Scoped staging and commit construction](../specs/2026-10-24-git-staging-commit-construction-design.md)

## Global Constraints

- Maintain source skills, documentation, examples and default formats in English. Resolve output language from explicit preference, then request language, then English; preserve technical identifiers and schema keys.
- Keep installed skills self-contained, with local references and declared catalog dependencies. Runtime never requires the root catalog, docs or development Python tools.
- Keep tests, scenarios, fixtures and retained evaluations under root `tests/`, grouped by skill owner and scope.
- Preserve excluded worktree content, unrelated index entries, configuration and other repositories. No automatic branch creation/switching, stash, reset, cleanup, amend, history rewrite, network, publication or credential changes.
- Authorization is scoped to the user's requested operation and exact selected changes. A plan, discovered command, ready preflight or skill invocation alone grants no write permission.
- Capture process exit status during the operation. Stop on unexpected changes or failures, preserve all observed state, and never retry, roll back or hide effects automatically.
- Test writes occur only in owned disposable repositories. Native client loading remains separate from instruction-following and Git recipe evidence.
- Preserve published preview.3 and historical evidence. Use matching development manifest version `0.1.0-preview.4`, unpublished; do not merge, create a PR or release in this increment.

## Review Focus

1. Partial staging and path-only scope must not stage or commit excluded later edits or unrelated index entries (Tasks 1–2).
2. Authorization, stale guards and normalization must match the complete index target, not just filenames or a ready preflight (Task 1).
3. Failed commands, mutation by hooks/checks and a later-group failure must preserve actual state and earlier commits without retries/reset (Task 2).
4. Helpers, signing, overrides, unsupported index flags and missing dependencies must not be bypassed to force success (Tasks 1–3).
5. Validation of a dirty worktree must not be reported as validation of different selected index content; installed-only ownership and language behavior must remain intact (Tasks 2–3).

## File map

- Create `skills/git-stage-changes/{SKILL.md,references/index-operations.md}`.
- Create `skills/git-commit-builder/{SKILL.md,references/commit-flow.md}`.
- Create root owner-scoped `tests/skills/git_stage_changes/` and `tests/skills/git_commit_builder/` scenarios, replay facts, evaluations and integration modules.
- Reuse `tests/support/git_fixtures.py`; add only owner-scoped helpers when needed.
- Modify catalog, AGENTS.md bounded write exceptions, optional entry routes/reference and entry scenarios/evidence.
- Modify current README, architecture, composition, roadmap, compatibility, installation inventory/closures, unreleased changelog and both manifest versions. Preserve historical releases/evaluations.

## Execution

The user requested spec, plan and then sequential implementation in one task. Use inline execution, fresh test actors and one whole-branch reviewer; do not ask for redundant continuation approval. The fresh design builder check reported “Nothing important left.” Ordinary implementation judgments are recorded in the design, not attributed to the user.

---

### Task 1: Exact scoped staging

**Files:** Create analyzer-owner peer `tests/skills/git_stage_changes/{__init__.py,fixtures/staging-facts.json,scenarios/staging.md,evaluations/2026-10-24.md,integration/__init__.py,integration/test_index_operations.py}`; create staging SKILL/reference; modify stage catalog entry and AGENTS.md.

**Interfaces:**
- Consumes: analyzer record and safety inspect context; exact `mode,repository,authorization,analysis_snapshot,selection,expected_index,exclusions`.
- Produces: `outcome,repository,authorization,selection,before,after,checks,deferred,limitations`; current whole-index manifest plus observed effects.

- [x] **Step 1: Define scenarios and run five fresh baseline record/application controls without candidate instructions.**
  Fixture: selected text hunk, existing partial staging, excluded debug and unrelated staged entry, explicit stage authorization, complete current target manifest and no active helpers. Cover preview/authorization gaps, stale content, foreign dependencies, identity absence, unsupported flags and literal paths. Retain actual responses; score factual successes separately from missing result fields.
- [x] **Step 2: Write and run Git recipe fixture controls.**
  `IndexOperationTests` methods: `test_cached_patch_stages_only_selected_hunk`, `test_stale_patch_check_writes_nothing`, `test_literal_paths_deletion_and_unborn_stage`, `test_authorized_reverse_patch_defers_only_selected_index_hunk`. Assert complete index manifests, excluded file/index guards and no HEAD/worktree/config changes. Run `python -B -m unittest tests.skills.git_stage_changes.integration.test_index_operations -v`. These command-semantic controls may pass before skill authoring; do not label that as behavioral RED.
- [x] **Step 3: Implement the skill/reference, catalog dependency and project write boundary.**
  Concise Use-when metadata; preview versus stage mode; exact manifest/hash normalization; cached patch check/apply and scoped approved reverse; before/after verification; no automatic recovery. Available stage requires analyzer+safety. Missing exact target or unsupported effects blocks/limits, not whole-file fallback.
- [x] **Step 4: Run five fresh candidate samples with complete instructions/dependencies, then independent edge/gap cases.**
  Expected: semantic result fields, exact selected target, preserved exclusions, explicit replay limits and no invented execution. Execute actual Git recipes only in owned fixtures; record that these are not native loading.
- [x] **Step 5: Verify and commit staging before starting the coordinator.**
  Run Task 1 unittest, repository validator and full-base diff whitespace check. Expected success. Commit `feat: add exact scoped Git staging`.

### Task 2: Commit construction coordinator

**Files:** Create `tests/skills/git_commit_builder/{__init__.py,fixtures/commit-facts.json,scenarios/commits.md,evaluations/2026-10-24.md,integration/__init__.py,integration/test_commit_flow.py}`; create coordinator SKILL/reference; modify builder catalog entry.

**Interfaces:**
- Consumes: planner groups/messages and current analysis; Task 1 exact staging result; safety commit preflight; per-check validation results; progress gates.
- Produces: `outcome,mode,authorization,groups,validations,commits,remaining,state,limitations`, including actual commit SHA/tree/message/identity or explicit unexecuted states.

- [ ] **Step 1: Define scenarios and run five fresh baseline controls before coordinator authoring.**
  Explicit commit request, prepared G1 and excluded later same-path edit, known identity, inspected passing check with actual worktree scope, no hooks/signing effects. Include preview-only, exact-scope validation, missing identity/dependency, unknown hooks, two groups/approved deferral, failure after first commit and exit-zero unexpected changes.
- [ ] **Step 2: Write and run real commit fixture controls.**
  `CommitFlowTests`: `test_commit_uses_selected_index_and_literal_message`, `test_unborn_commit_has_no_parent`, `test_failing_hook_preserves_pending_state`, `test_hook_added_content_is_detectably_outside_expected_tree`, `test_second_group_failure_preserves_first_commit`. Compare actual committed trees/parents/message/identity and residual state; fixtures intentionally configure owned hooks before the observed operation. Run `python -B -m unittest tests.skills.git_commit_builder.integration.test_commit_flow -v`; expected recipe controls pass.
- [ ] **Step 3: Implement coordinator/reference and dependencies.**
  Use progress -> analysis/preflight -> plan -> scoped validation -> per-group staging -> fresh commit preflight -> normal new commit -> postconditions. Explicit commit authorization covers necessary selected staging and ordinary inspected checks; unresolved scope/repartition/effects pause dependent writes. Unrelated staged entries require an approved deferral/restore decision rather than alternate-index/path bypass. Preserve state after every failure and report partial progress. Declare planner, stage, safety, validation and progress dependencies.
- [ ] **Step 4: Repeat five fresh complete-instruction samples and independent edge/gap cases.**
  Expected: delegation, record completeness, no inferred validation of selected content, hook/signing/authorization gates, known own-transition freshness and partial failure semantics. English/Spanish variants preserve identifiers. No simulated command gets reported as executed.
- [ ] **Step 5: Verify and commit the coordinator.**
  Run Task 2 unittest, repository validator and full-base whitespace check; expected success. Commit `feat: coordinate scoped local commit construction`.

### Task 3: Compose and document the eleven-skill candidate

**Files:** Modify entry SKILL/reference, catalog, current documentation/installation selections and both manifests. Add `tests/skills/using_devcraft_toolkit/evaluations/staging-commit-composition.md` and matching scenario packets; retain final verification under `tests/integration/evaluations/2026-10-24-git-staging-commits/`.

**Interfaces:**
- Consumes: available stage/builder contracts, owned dependency closure and existing installed-only routing.
- Produces: optional routes, eleven available/six planned, exact individual/full-set selection closures and unpublished preview.4 metadata. Entry hard foundation unchanged.

- [ ] **Step 1: Run entry routing controls before editing it.**
  Cases: owned staging/builder present; absent capability despite foreign copy; missing transitive dependency; message-only request; explicit standalone builder closure. Retain baseline gaps and successes.
- [ ] **Step 2: Add optional routes and verify fresh candidate routing.**
  Preserve mode/authorization boundaries, actual discovered namespaces and no emulation. Delegate defaults and decisions to installed capabilities; do not duplicate their execution.
- [ ] **Step 3: Update current docs/catalog metadata.**
  Explain write exceptions, eleven-skill dependency closures, preview.4 candidate versus published preview.3, roadmap completion and native evidence limits. No change to prior release tags, historical payload counts or native gates.
- [ ] **Step 4: Run full checks and commit integration.**
  Run `python -B -m unittest discover -s tests -p "test_*.py" -v`, repository/distribution validators and `git diff --check <base>` (then `<base>..HEAD` after commit). Expected all runnable tests pass; disclose the existing Windows symlink privilege skip. Commit `feat: compose staging and commit construction capabilities`.
- [ ] **Step 5: One fresh whole-branch review and bounded fix pass.**
  Give reviewer the spec/plan, range, ledger rulings and Review Focus. Re-grade by actual impact, reproduce important findings before fixes and rerun affected/full checks. Preserve branch/worktree and report completion; no PR/merge/release unless subsequently requested.

## Self-review

Contracts match across Tasks 1–3; all five Review Focus classes have owner-scoped recipe/application coverage. Preview.4 is development metadata only. The design is the authority for edge conditions, not a guarantee of atomicity or native compatibility.
