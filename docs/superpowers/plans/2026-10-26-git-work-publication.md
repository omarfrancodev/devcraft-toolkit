# Work Branch Creation and Publication Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver independent, preserving work-branch creation followed by a publication coordinator that delegates only selected effects.

**Architecture:** Two instruction-first portable skills compose exact owned capabilities. Development-only real Git controls, copied-resource applications and supplied-fact behavioral evaluations establish bounded evidence; no runtime interpreter or root registry is installed. Integration follows both owner gates.

**Tech Stack:** Markdown, JSON, existing plugin manifests, Python unittest/PyYAML, owned Git 2.45 repositories and existing emulated hosted transport.

**Spec:** [Approved design](../specs/2026-10-26-git-work-publication-design.md)

## Global Constraints

- Maintained sources/templates use English; prose follows explicit language, request language, then English. Preserve literal identifiers and full raw OIDs.
- Branch requires only git-working-directory-policy (two folders). Publication requires git-publish-changes and todo-workflow-controller (five-folder transitive closure). Conditional selected owners retain their existing closures; complete optional union is fifteen folders.
- Proposal defaults are offline/read-only. Creation permits one local create-and-switch at current committed HEAD; selected publication effects require actual authorization. No inferred fetch, commit, PR, merge or upstream setup.
- Preserve staged/unstaged/deleted/untracked/ignored work and unrelated refs/config. No reset, rollback, cleanup, force, hook bypass, automatic retry, alternate-base/unborn branch creation or new worktree from installed skills.
- Inspect hooks/helpers/effects, refresh guards, capture one attempt and independently verify actual state. Nonzero hooks can follow successful effects; preserve partial/uncertain state.
- Installed skills are self-contained, below 500 words in main bodies, with local references. Missing/foreign/ambiguous owners and unknown capabilities cannot be imitated or auto-installed.
- Tests/scenarios/fixtures/evaluations remain under root tests/, grouped by owner and scope; no installed scripts or new manifests, runtime catalog, SDK, license or release automation.
- Final inventory eighteen available/zero planned. Existing manifests advance together to unpublished candidate 0.1.0-preview.8. Preserve historical specs/releases and preview.7 evidence.
- Preserve this worktree and local commits. No implementation push, PR, merge or release without a later request.

## Review Focus

1. Literal branch operands and stale target configuration must not expand checkout expressions, silently reuse refs or inherit remote tracking (Task 1).
2. Dirty partial staging, linked worktrees and post-checkout failure must retain semantic index/files and actual branch effects rather than being called rollback-safe (Task 1).
3. Known excluded dirty work or missing conditional owners must stop an impossible selected goal before earlier branch/commit writes (Task 2).
4. Own commit/fast-forward transitions versus unexpected source movement, lost acknowledgment and pending promotion must not cause stale publication or automatic repeats (Task 2).
5. Growing approved inventory must retain exact catalog equality and nonempty/unique enforcement, while candidate installation sets distinguish mandatory and conditional owners (Task 3).

## Execution and file ownership

Execute inline in the existing isolated worktree, in the requested order. User approval expressly covers plan then implementation; link the plan and continue without another approval. Fresh agents are instruction-consumption tests, not task implementers. One final fresh whole-branch reviewer supplies independent review.

- Task 1: `skills/git-create-work-branch/{SKILL.md,references/branch.md}`, `tests/skills/git_create_work_branch/{integration,fixtures,scenarios,evaluations}/`, test-only `tests/support/work_branch_fixtures.py`, catalog/AGENTS and existing manifests.
- Task 2: `skills/git-publish-work/{SKILL.md,references/publication.md}`, `tests/skills/git_publish_work/{integration,fixtures,scenarios,evaluations}/`, catalog/AGENTS. Reuse owned Git and hosted fixtures; no test interpreter pretending to be the installed coordinator.
- Task 3: `docs/capability-inventory.md`, development validator and repository/distribution tests, entry routes, current README/architecture/composition/compatibility/roadmap/install docs/unreleased changelog. Retain final ledger, commands and review under `tests/integration/evaluations/2026-10-26-git-work-publication/`.

## Shared interfaces

Branch outcome carries mode/authorization, selected owned context, original symbolic/detached source and full OID, literal target ref, guards, actual attempt/exit, independently observed new HEAD/ref, preserved index/files/config/other refs and limits. Outcomes: planned/created/no_op/needs_decision/limited/blocked/stopped/partial/uncertain. Publication consumes this outcome, never a boolean branch-exists signal.

Publication selects owners conditionally: branch when needed; git-commit-builder for selected changes; git-sync-branch for explicit sync; git-publish-changes for push; git-manage-pull-request for selected management; git-promote for explicit merge. In-memory receipts carry current source/target identities, requested/skipped/blocked/completed steps, scoped checks and actual effects. Overall completed requires every requested step verified; pending/lost/partial receipts stop dependent mutations. No persisted runtime state or new catalog schema.

Test-only `branch_snapshot(repo: Path) -> dict` returns semantic whole-index entries, working-byte inventory, branch/ref and local config observations using existing protected fixture Git. `create_branch(repo: Path, name: str, source_oid: str) -> CompletedProcess` is the exact bounded primitive recipe, not policy enforcement. Primitive controls deliberately demonstrate failure effects; consumer actors establish instruction adherence. Reuse `git_fixture`, `remote_fixture`, `snapshot_repository` and hosted transport without weakening their isolation.

### Task 1: Independent work-branch creation

**Files:** Create branch skill/reference, owner test package, actor-only facts and retained evaluations; add test-only snapshot/recipe helper; modify catalog and AGENTS bounded exception, existing manifest versions.

**Interfaces:** Consumes owned context; produces the branch outcome above. Intermediate catalog seventeen available/one planned, with eighteen target names pending Task 3 inventory integration.

- [x] **Step 1: Baseline and availability RED.** Create five actor-only packets: dirty partial index on main; exact invalid/colliding/stale-config target; explicit detached versus unborn; hook failure after switch/source movement; linked worktree/submodule/missing identity. Run five fresh actors without new guidance, retain verbatim responses and successes. Add `test_branch_available_with_two_folder_closure`; assert an available branch entry requiring only context and a copied valid two-folder package. Run while absent.
  Run: `python -B -m unittest discover -s tests/skills/git_create_work_branch/integration -p 'test_*.py' -v`.
  Expected: availability fails because branch is absent, not a syntax/import error.
- [x] **Step 2: Pin primitive controls.** Add meaningful real Git controls named `test_dirty_partial_index_and_all_working_bytes_survive`, `test_literal_names_and_existing_refs_do_not_expand_or_reset`, `test_no_tracking_even_with_auto_setup_config`, `test_detached_and_missing_identity_do_not_need_commits`, `test_post_checkout_failure_can_leave_new_branch_selected`, `test_linked_worktree_preserves_other_worktree`, `test_pinned_operand_does_not_follow_source_movement`, `test_unborn_and_operation_markers_are_observable`, `test_reference_hook_effects_are_not_hidden` and `test_submodule_work_is_not_recursed`. Verify missing helper RED, then implement snapshot and bounded recipe. Assert original/unrelated refs and configuration independently; semantic index equality, all file bytes including ignored/untracked Unicode/deletions. Do not infer that primitive Git enforces policy gates.
  Expected: controls pass and expose effects/limits, including a failed post-checkout exit after real branch selection.
- [x] **Step 3: Write branch resources.** Provide concise main skill and self-contained local reference for every approved source/name/effect/guard/attempt/verification/stop rule. Use literal structured operands and one supported protected `switch --no-guess --no-track --no-recurse-submodules --no-overwrite-ignore -c NAME OID`. Mark available, require context only, update AGENTS and both manifests to preview.8. Record the known temporary canonical-inventory mismatch until Task 3; do not rewrite historical spec.
  Expected: package RED becomes GREEN; new main body under 500 words and local links resolve.
- [x] **Step 4: Candidate and application.** Run five fresh exact-resource actors on identical facts and separate gap cases (missing/foreign/ambiguous context, unknown helpers/sparse/concurrency). Manually assess against separate assertions. Run one copied-two-folder actor on an owned dirty repository; parent inspects real OIDs, ref/config/index/files and exact attempt, retaining observations outside installed folders. No native loader claim.
  Expected: bounded decisions and independently verified preservation, no invented baseline failure.
- [x] **Step 5: Commit and ledger.** Commit `feat: add preserving work branch creation`. Complete using owner unittest discovery above; retain precise behavioral limits and task verification.

### Task 2: Publication coordinator

**Files:** Create coordinator resources and owner test package/packets/evaluations; modify catalog and AGENTS bounded composition permission. Existing primitive owners remain authoritative.

**Interfaces:** Consumes Task 1 outcome and existing owner receipts; produces selected plan/authorization, actual per-step outcomes, final source/destination/request identities and remaining work. Eighteen available/zero planned; five-folder mandatory closure.

- [x] **Step 1: Baseline and availability RED.** Five fresh no-guidance packets cover minimal existing-commit push; main-to-work-branch preparation/PR; known dirty residual/missing owner/checks; source transitions/strict order; lost receipt/pending merge/explicit continuation. Retain successes. Add `test_publication_available_with_five_folder_closure` and optional-union closure checks; run while planned.
  Run: `python -B -m unittest discover -s tests/skills/git_publish_work/integration -p 'test_*.py' -v`.
  Expected: planned availability fails; baseline does not mutate hosting.
- [x] **Step 2: Establish real composition controls.** Use existing remote Git and hosted fixtures to demonstrate branch->selected commit->exact push with unchanged original main and upstream, fresh final source; existing-commit push without new branch/commit/fetch; normal rejection preserving earlier commits; exact duplicate-request no_op observations and lost/pending effects. Assert full remote refs, actual local source/index/config and provider operation ledger. Keep helper replay evidence separate from actor behavior.
  Expected: controls exercise owned real Git/emulated hosting only; no live/authenticated claims or policy interpreter.
- [x] **Step 3: Write coordinator resources.** Define mandatory/conditional resolution, authorization matrix, offline default, role/destination selection, blocker forecast, selected ordering, whole-owner delegation, clean-push conflict, fresh source handling and bounded stops/continuation. Give one concrete complete-goal example and a compact result shape. Mark available requiring only publisher and progress; no added hard optional dependencies.
  Expected: owner package GREEN, main body below 500 words; no stale planned entry/folder mismatch except pending inventory source change.
- [x] **Step 4: Candidate, gaps and application.** Five fresh actors use exact copied resources/selected closures and the same packets. Separate gaps cover minimal closure versus missing/foreign/ambiguous conditional owners, no native question/progress tools, unknown provider/Git capabilities, failed checks, excluded dirty work, explicit/unselected sync/PR/merge/upstream, source movement and prior effects. An actual copied-resource actor executes selected branch/commit/push/request creation against owned Git/emulated transport. Parent independently inspects exact operation order, final source/remote/request identities, original refs, config and no extra effects. No bare read/recipe test is counted as instruction application.
  Expected: all requested actual effects verified or clearly stopped; preserved actual partial/pending state and no automatic second mutation.
- [x] **Step 5: Commit and ledger.** Commit `feat: coordinate selected work publication`. Complete with owner discovery above, retaining actor and parent evidence before integration.

### Task 3: Inventory, composition and final verification

**Files:** Current capability inventory, validator/repository fixtures, entry resources/owner evaluations, current docs/install guides and changelog; final evidence folder.

**Interfaces:** Consumes both available skills/closures. Produces eighteen-name exact approved inventory without fixed numeric ceiling; branch two-folder and coordinator five-folder mandatory installs, documented fifteen-folder optional union; historical preview.7 remains sixteen skills.

- [x] **Step 1: Inventory and installation RED.** Add full-project-root regressions for approved expansion beyond seventeen, missing/extra catalog names, duplicate and empty inventory. Assert `catalog-inventory` diagnostics and acceptance using literal independent expected names; existing schema/path/dependency checks remain enabled. Update fixture source-copy path in distribution tests. Run before validator change and retain actual failure. Run existing installation closure test to expose missing branch/coordinator rows. Evaluate old entry against complete owned discovery before editing.
  Expected: expansion acceptance and installation fail for the intended missing support, not test harness errors.
- [x] **Step 2: Implement integration.** Add `docs/capability-inventory.md` with eighteen current names; point validator to it and replace exactly-seventeen condition with nonempty+unique. Keep exact catalog equality. Add optional entry routes: direct branch, multi-step publication, existing direct single-owner routes. Align current docs, AGENTS, installation rows/full list/candidate revision guidance, roadmap delivery and next native/authenticated validation. Add unreleased changelog only; no tag/release publication or historical evidence rewrite.
  Run: `python -B -m unittest discover -s tests/repository -p 'test_*.py' -v`; `python -B -m scripts.validate_repository --root .`; `python -B -m scripts.validate_distribution --root .`.
  Expected: structural and closure checks pass; eighteen available/zero planned, manifests agree at preview.8 candidate.
- [x] **Step 3: Full final gates and record.** Run `python -B -m unittest discover -s tests -p 'test_*.py' -v`, both validators, skill-creator quick validation on both new folders, complete-base `git diff --check 319ff5f5624069bfeaf8a0cb14a1f445f82f7436`, and resolve changed Markdown local targets with existing validation helpers. Retain exact test counts/skips, behavioral assessments, commands and ledger. Record fresh entry-routing consumer outcomes including direct/conditional/foreign scope.
  Expected: every runnable test passes; existing Windows symlink privilege skip remains explicit. Evidence distinguishes recipe, supplied-fact actors, actual copied applications and missing native/authenticated coverage.
- [x] **Step 4: Commit, task-done and whole-branch review.** Commit `feat: integrate work publication into toolkit`. Task-done runs full unittest discovery on committed tree. Dispatch one fresh whole-branch reviewer on the most capable available model with spec, plan, Review Focus verbatim and ledger rulings. Re-grade findings; one material RED/GREEN fix pass with green full suite, record minor deferrals/rulings. Retain review/ledger under tests before safely deleting this plan's scratch only. Preserve worktree/commits.

## Self-review

All approved behavior maps to an owner task and every Review Focus has real controls plus consumer cases. Branch results feed coordinator state directly; Task 3 consumes catalog closures and adds no runtime schema. The approved source inventory expands only at integration, with a documented intermediate validator mismatch. Baseline 162 discovered/161 passed/one Windows symlink skip is already recorded in the spec; no redundant initial rerun or dependency installation is planned. Plan and implementation are explicitly authorized in sequence.
