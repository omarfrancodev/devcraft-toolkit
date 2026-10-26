# Scoped Branch Synchronization and Publication Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver independent scoped fetch/fast-forward and normal single-branch push capabilities.

**Architecture:** Two self-contained instruction-first skills compose context and read-only safety preflight, then execute only the requested operation after destination/effect/freshness checks. Shared local bare-repository fixtures test Git recipes; optional entry routes and explicit three-skill closures integrate the canonical resources.

**Tech Stack:** Markdown, JSON catalog/existing manifests, Python unittest development fixtures and Git 2.45+. No runtime collector, interpreter or hosting-service API dependency.

**Spec:** [Approved sync/publication design](../specs/2026-10-25-git-sync-publish-design.md)

## Global Constraints

- Maintained skills, documentation, examples and default templates use English. User-facing content follows explicit preference, then request language, then English.
- Installed resources remain self-contained, with no runtime root catalog/docs, interpreter dependency or automatic installer.
- All tests, scenarios, fixtures and retained evaluations belong under root `tests/`, grouped by canonical skill owner and scope; shared fixture infrastructure may live in `tests/support/`.
- Default invocation is local inspection/proposal only. It performs no network, fetch, push, config or worktree mutation. Explicit remote observation permits advertisement queries only; it does not authorize fetch or push.
- Explicit sync permission covers one selected fetch and a verified fast-forward of the current branch. Explicit publish permission covers one selected normal branch push and bounded verification queries. A ready preflight, skill name, plan or prior successful operation grants no mutation permission.
- No force/lease-force push, mirror/all-ref/tag publication, pruning, deletion, stash, reset, cleanup, branch switching/creation, merge commit, rebase or automatic rollback/retry.
- Do not change remotes, URLs, credentials, identities, global configuration or authentication setup. Only explicitly requested upstream configuration may change the selected branch's two repository-local tracking keys after verified publication/equality.
- Testing uses owned local bare repositories and disposable clones, never live publication to the project's real origin. No push, PR, merge, tag or release of this implementation is part of this increment unless later requested.
- Keep preview.5 and its twelve-skill historical evidence unchanged. Advance both existing manifests together to unpublished `0.1.0-preview.6`; final candidate inventory is fourteen available and three planned entries across seventeen names.
- Both standalone closures are capability+context+safety. Entry hard dependencies remain unchanged; publication does not require synchronization as an installed dependency.

## Review Focus

1. Fetch defaults/refmaps/pruning/tags and push defaults/pushurls/follow-tags must not widen the approved one-branch destination (Tasks 1–2).
2. Unknown hook/filter/transport effects, including reference-transaction and index hooks, must block before mutation or protected preflight reads (Tasks 1–2).
3. Divergence, missing ancestry, source/endpoint movement and failed acknowledgment must preserve partial/uncertain effects without reset, merge/rebase, force or retry (Tasks 1–2).
4. Publication without upstream must not create config implicitly; explicit upstream setup must touch only two local branch keys after verified publication (Task 2).
5. Offline inspection and missing/foreign/ambiguous ownership must not trigger network, runtime catalog reads or imitation (Tasks 1–3).

## File map and execution

Execute inline following the user's approved spec/implementation continuation. Use fresh behavior actors as tests, real owned local remotes for applications and one fresh whole-branch reviewer. Do not pause between tasks for another approval.

- Shared test-only `tests/support/remote_git_fixtures.py` owns local bare remote, seed and client repositories; no toolkit runtime imports it.
- Create each skill's `SKILL.md` and `references/synchronization.md` or `references/publication.md`.
- Create owner-scoped `tests/skills/git_sync_branch/` and `tests/skills/git_publish_changes/` with integration tests, scenarios, actor-only fixture inputs and raw evaluations.
- Modify bounded AGENTS exceptions, catalog status/dependencies, both existing manifest versions, entry instructions/reference and entry-owner scenarios/evidence.
- Update current README/architecture/composition/compatibility/roadmap, installation overview/closures and unreleased changelog. Preserve historical release pages and evaluation snapshots.

## Shared test interfaces

`RemoteFixture` exposes `root: Path`, `remote: Path` (bare), `seed: Path` and `local: Path`. `remote_fixture(root: Path)` creates these inside the owned test root with isolated global configuration and an initial tracked main branch. `git(repo: Path, *args: str, check: bool = True, env: dict | None = None) -> subprocess.CompletedProcess[bytes]` runs literal arguments with protected flags; fixture setup writes are distinct from runtime recipe authorization. `head(repo: Path, ref: str = "HEAD") -> str`, `refs(repo: Path) -> dict[str,str]`, and `commit(repo: Path, message: str, filename: str = "work.txt") -> str` support concrete assertions. Existing `snapshot_repository` guards client metadata/working files; bare refs/config are captured separately.

### Task 1: Scoped synchronization

**Files:** Create shared fixture helper, `skills/git-sync-branch/{SKILL.md,references/synchronization.md}`, owner integration tests/evidence/scenarios; modify AGENTS, catalog and both manifests.

**Interfaces:** Consumes owned context/safety with local publish preflight and separate sync authorization. Produces spec outcome/mode/authorization, selected scope/endpoints, before/fetched/after OIDs, relation, effects/command receipts and remaining state. Candidate availability initially becomes thirteen available/four planned at version preview.6; final installation docs follow Task 3.

- [x] **Step 1: Record baseline and structural RED.** Create five actor-only requests: default offline check; explicit behind sync; divergence after fetch; unknown hook/filter; ambiguous endpoint/upstream. Run one fresh no-guidance sample per request and retain actual output, including successes. Add owner package test `test_sync_available_with_exact_three_skill_closure`; run while entry is planned.
  Expected: structural failure because sync remains planned; no expected assertions exposed to actors.
- [x] **Step 2: Exercise real Git controls.** Implement `test_exact_fetch_ignores_tags_prune_and_extra_refmaps`, `test_fast_forward_moves_only_current_branch`, `test_equal_ahead_and_diverged_are_not_reset`, `test_unrelated_and_missing_history_do_not_fast_forward`, `test_dirty_conflicted_unborn_detached_write_gates`, `test_reference_and_index_hooks_execute_in_real_recipes`, `test_ref_and_endpoint_movement_invalidate_snapshot`, and `test_literal_remote_paths_and_refs`. Use owned fixtures and real snapshots, not Markdown string assertions. Run `python -B -m unittest tests.skills.git_sync_branch.integration.test_sync_recipes -v`.
  Expected: finite scoped recipe controls pass or expose a concrete command/fixture defect to correct without weakening assertions.
- [x] **Step 3: Write and activate sync.** Keep body below 500 words with local reference, exact protected-read/effect gates, explicit refspec/fetch controls, guarded fast-forward, no-op fetch disclosure and partial/uncertain receipts. Add bounded AGENTS exception, mark catalog available with context+safety, and set both manifests to preview.6.
  Run owner discovery, both validators and complete-base whitespace against `36a224dbb05d35810e5e94fb4be4adbddb46508e`.
  Expected: owner package RED→GREEN; no runtime scripts or unrelated contract changes.
- [x] **Step 4: Verify candidate behavior and actual application.** Repeat the same five requests in fresh contexts reading only installed-style closure resources. Run one real actor application from a three-folder copy against an owned bare remote/client, then independently verify exact HEAD/index/worktree/refs/config effects and no extra files. Retain procedure limitations; native activation is not claimed.
  Expected: assertions and exact postconditions pass; observed defects corrected/retested. No live project-origin network mutation.
- [x] **Step 5: Commit and ledger.** Commit `feat: add scoped fast-forward branch synchronization`. Task verification: owner integration discovery (same directory, `-p test_*.py -v`) and both validators pass. Record command/result and any rulings before Task 2.

### Task 2: Scoped publication

**Files:** Create `skills/git-publish-changes/{SKILL.md,references/publication.md}`, owner tests/scenarios/evidence; reuse shared fixtures; modify bounded AGENTS exception/catalog availability.

**Interfaces:** Consumes context+safety and independent publish authorization, not a required sync skill. Produces pinned source/destination, before/after advertisement evidence, push result, protected local state, optional two-key upstream result, partial/uncertain effects and limits. Inventory becomes fourteen available/three planned; both manifests remain preview.6.

- [x] **Step 1: Record baseline and structural RED.** Five actor-only requests cover offline/dry-run confusion, exact push despite configured defaults/tags, unknown remote OID without fetch permission, a failed push with possible effects, and explicit versus absent upstream setup. Fresh no-guidance actors see only inputs. Add package test `test_publish_available_with_exact_three_skill_closure`; run while planned.
  Expected: package test fails for planned status; retain baseline successes without fabricated failures.
- [x] **Step 2: Exercise publication controls.** Implement `test_pinned_single_ref_overrides_matching_and_follow_tags`, `test_normal_push_rejects_non_fast_forward`, `test_unknown_remote_oid_requires_fetch_decision`, `test_pushurl_and_rewrite_select_effective_endpoint`, `test_multiple_endpoints_and_mirror_require_decision`, `test_pre_push_and_reference_hooks_are_not_bypassed`, `test_source_movement_does_not_publish_new_tip`, `test_rejection_or_lost_ack_requires_actual_observation`, and `test_explicit_upstream_changes_only_two_local_keys`. Include missing/detached/dirty gates and literal names through shared controls; no force flags. Run owner recipe tests with real bare endpoints.
  Expected: exact selected remote refs and client protected state match expected effects; default no config update and explicit local tracking setup are distinct.
- [x] **Step 3: Write and activate publication.** Keep body below 500 words and local reference covering exact one-ref push/verification, effective destinations, hooks/signing, no silent fetch, source/race guards, redaction, no bypass/retry and optional exact upstream writes. Add AGENTS exception and mark available with context+safety.
  Run owner integration discovery, both validators and complete-base whitespace.
  Expected: package RED→GREEN; sync remains independently installable and existing source behavior remains bounded.
- [x] **Step 4: Verify candidate behavior and actual application.** Five fresh candidate samples plus a real three-folder actor publication to an owned local bare repo, with explicit requested upstream setup. Independently verify the exact remote OID, preserved other refs/tags/source/index/worktree/global config, only two local config changes and no extra files. Retain output/effect evidence and uncertainty; do not treat a porcelain message alone as success.
  Expected: scoped publication verified without live external push or native activation claims.
- [x] **Step 5: Commit and ledger.** Commit `feat: add exact single-branch publication`. Task verification: owner integration discovery and both validators pass; record outcomes before Task 3.

### Task 3: Integrate routes, installation and roadmap

**Files:** Modify entry SKILL/local composition reference and owner routing scenarios/evidence, README, current architecture/composition/compatibility/roadmap, installation overview/individual selection and unreleased changelog. Create final evaluation under `tests/integration/evaluations/2026-10-25-git-sync-publish/`.

**Interfaces:** Consumes both three-skill closures and actual results from Tasks 1–2; produces optional independent routes and coherent fourteen-name source inventory. Existing entry foundation and historical preview.5 payload remain unchanged.

- [x] **Step 1: Record routing/installation RED.** Evaluate unchanged entry for explicit sync/push with complete selected closures; record planned/unavailable routing before edits. Run existing `test_installation_selections_match_available_catalog_closures`, which detects missing new rows/full-set names.
  Expected: unavailable-route samples and installation-set mismatch; no native discovery claim.
- [x] **Step 2: Add optional routes and docs.** Route exact owned identifiers, honor inspect/observe/write authorization and separate sync/push from commit/PR/promotion/release requests. Cases cover installed, absent, foreign, ambiguous, direct standalone and supplied-facts requests. Update two dependency rows/full fourteen-name selection and all current-source counts; preview.6 remains unpublished. Roadmap makes PR management and promotion next, then coordinator; native validation remains parallel.
  Run existing installation closure test and validators.
  Expected: documented selections equal real transitive catalog closures, fourteen available/three planned, no placeholder skills.
- [x] **Step 3: Final verification.** Run full `python -B -m unittest discover -s tests -p "test_*.py" -v`, both validators, new-skill quick validation, complete-base whitespace and changed-document local links. Retain exact pass/skip counts, raw owner outcomes, application verification and ledger. Current intermediate installation mismatch is resolved here, not ignored as a final failure.
  Expected: all runnable tests pass, existing Windows symlink privilege skip disclosed, validators/links/closures pass.
- [x] **Step 4: Commit and review.** Commit `feat: compose synchronization and publication capabilities`. Request one fresh read-only whole-branch review with this spec/plan/Review Focus and ledger. Re-grade by user impact; one Important/Critical fix pass with reproduced RED/GREEN and affected/full checks. Record any minor deferrals. Preserve branch/worktree without push/PR/merge/release.

## Self-review

Shared field names and both dependency closures agree across tasks. Every Review Focus item has real Git controls or explicit behavioral cases. Recipe tests do not prove instruction following, and manual copied-resource applications do not establish native activation. No implementation relies on unavailable projects or historical migration provenance.

## Review follow-up: usable upstream

Add real single-branch and absent-tracking controls for the upstream postcondition, retaining their RED/GREEN outcomes. Verify normal publication still succeeds independently, safe mapped setup resolves the correct ref/commit, missing setup prerequisites preserve keys/publication, and no implicit fetch or mapping repair occurs. Retain fresh supplied-fact behavior and rerun the full suite/validators before updating the same PR.

Follow-up completed: both new regressions failed before the correction and passed afterward; successful setup cases also resolve the correct upstream ref/commit. Fresh full verification: 140 tests, 139 passed, one existing Windows skip; validators passed.
