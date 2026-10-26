# Hosted Requests and Explicit Promotion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver independent hosted request management and explicitly authorized, source-guarded normal promotion.

**Architecture:** Instruction-first skills compose owned context and provider observations. Test-only provider fixtures expose documented GitHub/GitLab semantics, an operation ledger and a disposable transport; they are not installed runtime code. Entry routing and explicit dependency selection integrate the capabilities after both owners pass.

**Tech Stack:** Markdown/JSON catalog and existing manifests; Python unittest/development fixtures; Git 2.45+ for owned graph controls. No runtime SDK, interpreter, fixed plugin or live provider mutation.

**Spec:** [Approved hosted request/promotion design](../specs/2026-10-25-git-pr-promotion-design.md)

## Global Constraints

- Maintained sources/templates use English; user-facing prose follows explicit preference, request language, then English. Preserve identifiers/OIDs/status keys.
- Management depends only on git-working-directory-policy (two-folder closure). Promotion depends on management (three-folder closure including context). Entry hard foundation remains unchanged.
- Installed folders remain self-contained; no runtime root catalog/docs, helper interpreter, automatic installation or foreign dependency substitution.
- Proposal/inspect defaults use supplied/local evidence only. Explicit observation permits reads. Explicit create/update/merge permits only the selected operation and bounded verification.
- Management creates or edits selected title/body only. No implicit lifecycle/retarget/approval/reviewer/comment/label mutation, including provider-interpreted text effects.
- Promotion merges one existing request only when explicitly requested, with server-enforced source OID. Normal merge commit only; no squash/rebase/queue/admin override/source deletion or strict target-lock promise.
- No local Git writes, fetch/push, identity/credential/global config change, release or deployment from either capability. Hosted operations do not require a clean unrelated local worktree or local publish preflight.
- Tests/scenarios/fixtures/evaluations stay under root tests/, grouped by canonical owner and scope; helper fixtures are development-only.
- Advance existing manifests together to unpublished 0.1.0-preview.7; final inventory sixteen available/one planned across seventeen names. Historical release pages/tags/evaluations remain unchanged.
- Preserve local branch/worktree and commits after execution. No implementation push/PR/merge/release without a later user request.

## Review Focus

1. Provider-normalized unknown/paginated state must not become ready evidence: GitLab diff base is not live target, hypothetical merge SHA is not merged provenance, and empty checks are not passed checks (Tasks 1–2).
2. Same branch spelling across forks/hosts and incomplete request listings must not cause wrong-request edits or duplicate creation (Task 1).
3. GitLab draft markers and description quick actions must not expand a selected title/body write into lifecycle, approval or notification changes (Task 1).
4. Failed acknowledgment, source-precondition conflict and target advance/rewrite must preserve actual effects without a second mutation or invented containment (Tasks 1–2).
5. Method/queue/automatic-cleanup settings and stale policy/review/check scope must not bypass gates or expand an explicit normal merge; strict target conditions must stop when unsupported (Task 2).

## Execution and file ownership

Execute inline in the existing isolated worktree, in the user-approved order. The approved continuation covers plan and implementation; expose the plan and continue without another checkpoint. Fresh agents are behavioral tests, not task implementers; one final fresh whole-branch reviewer is the independent review gate.

- Shared `tests/support/hosted_provider_fixtures.py`: test-only canonical scope, provider-shaped records/normalization, owned state, request ledger and transport operations.
- Shared `tests/support/hosted_transport.py`: disposable CLI adapter over an owned fixture state (JSON input/output); no external HTTP, credentials or package installation.
- Task 1 owns `skills/git-manage-pull-request/{SKILL.md,references/requests.md,assets/pull-request.md}` and `tests/skills/git_manage_pull_request/{integration,fixtures,scenarios,evaluations}/`.
- Task 2 owns `skills/git-promote/{SKILL.md,references/promotion.md}` and corresponding owner tests/resources; extend shared fixture protocol only for promotion.
- Task 3 owns entry routes/reference, installation rows/full-set selection and current README/architecture/composition/compatibility/roadmap/unreleased changelog. Retain final evidence under `tests/integration/evaluations/2026-10-25-git-pr-promotion/`.

## Shared test interfaces

`provider_fixture(root: Path, provider: str = "github") -> context manager[HostedFixture]` initializes an owned state file and ledger with selected host/account, stable source/target project IDs, full refs/OIDs, request list, live target observation, template/diff coverage and explicit policy/review/check evidence. `HostedFixture` exposes `root: Path`, `state_path: Path`, `state: dict`, `events: list[dict]`, `save() -> None`, `read() -> dict`, `list_requests() -> dict`, `create(payload: dict) -> dict`, `update(request_id: int, payload: dict) -> dict`; Task 2 adds `merge(request_id: int, payload: dict) -> dict`. Fixtures may load/save state between transport invocations. Every operation records verb/payload/result, including actual effects before injected lost acknowledgment.

`normalize_request(provider: str, raw: dict, target: dict | None = None) -> dict` retains scope, request ID, lifecycle/draft, source_oid, separately observed target_oid, reported diff-base data, merge provenance and completeness/unknowns. GitHub's unmerged merge_commit_sha is hypothetical. GitLab target tip comes from target-branch evidence, not diff_refs.base_sha.

`ProviderFailure(status: int, message: str, effects: dict | None = None)` distinguishes rejection from failed receipt; it does not imply rollback. The transport accepts `python -B hosted_transport.py STATE ACTION` with JSON input on stdin for create/update/merge and emits JSON results. It exposes capabilities/read/list actions. Copy this development transport beside emulated applications, outside installed skill folders; actor resources do not include evaluator assertions or root catalog.

Task 2 consumes the exact fixture interfaces above. An owned real Git graph supplies full A/B/S/M/D OIDs and parent/ancestry evidence for merge/descendant/rewrite cases; provider state is still emulated. Test helpers may implement canonical recipe replays but their pass is not instruction-following or service-compatibility evidence.

### Task 1: Hosted request management

**Files:** Create owned skill/reference/template, owner package/integration/scenarios/actor-only fixtures/evaluations, shared fixture+transport; modify catalog availability/dependency, AGENTS bounded exception and both existing manifest versions.

**Interfaces:** Consumes context ownership and actual provider capability discovery; produces management scope, evidence coverage, selected fields, request identity, actual write/verification outcomes and limits. Exposes shared fixture interfaces above for Task 2. Intermediate inventory fifteen available/two planned; manifests preview.7.

- [x] **Step 1: Establish baseline and package RED.** Create five actor-only inputs: offline proposal; same branch across forks plus incomplete listing; explicit create with failed receipt; selected title/body update with concurrent old-field change; project template/language and GitLab interpreted text. Run fresh actors without the new instructions, retaining exact responses and baseline successes. Add `test_management_available_with_exact_two_skill_closure` and run while planned.
  Expected: package test fails for planned status; no fabricated model baseline failure and no actual hosting mutation.
- [x] **Step 2: Pin protocol controls before helpers.** Add `test_provider_profiles_preserve_identity_and_unknowns`, `test_incomplete_listing_is_not_confirmed_absence`, `test_fork_identity_disambiguates_equal_branch_names`, `test_create_update_roundtrip_preserves_other_fields`, `test_creation_lost_ack_preserves_one_created_request`, `test_title_and_description_can_have_gitlab_side_effects`, and `test_gitlab_diff_base_does_not_supply_live_target`. Assertions use actual fixture observations, exact request identities and unchanged unselected state; no keyword matching of skill prose. Observe missing helper RED once, then implement the minimal shared fixture/transport protocol.
  Expected: controls pass and explicitly demonstrate unsafe primitive effects rather than silently hiding them in a policy-enforcing emulator.
- [x] **Step 3: Write management instructions.** Keep entry body below 500 words; local reference defines exact identity/completeness, operation permissions, template/evidence/language, bounded create/update and verification. Supply local English Summary/Changes/Validation/Considerations template. Explicitly account for GitLab draft/body commands, source movement and lost acknowledgment. Mark available with context only and add bounded hosted-write exception; bump both manifests together.
  Run owner integration discovery, repository/distribution validators and complete-base whitespace.
  Expected: package RED→GREEN, fifteen available/two planned. The existing installation-guide test can remain temporarily mismatched until Task 3; it is not waived at final.
- [x] **Step 4: Test candidate and application.** Five fresh actors read exact management/context resources and identical actor-only facts; separately inspect outcomes against owner assertions. An actual copied-two-folder actor uses only an owned emulated transport for explicitly requested create/title-body update. Parent verifies one requested creation, only selected update fields, actual receipt reads, unchanged source/target/policy/reviews and local dirty Git snapshot, no extra files. Include missing/foreign/ambiguous dependency and provider-side text cases in a separate supplied-fact gap packet.
  Expected: bounded decisions and observed fixture effects, not live provider/native activation claims; preserve failures and calibration limits.
- [x] **Step 5: Commit and ledger.** Commit `feat: add hosted pull request management`. Complete Task 1 with `python -B -m unittest discover -s tests/skills/git_manage_pull_request/integration -p "test_*.py" -v` and record validators/behavior/application evidence.

### Task 2: Explicit normal promotion

**Files:** Create promotion skill/reference and owner package/integration/scenarios/inputs/evaluations; extend shared merge/graph controls and AGENTS/catalog bounded exception.

**Interfaces:** Consumes the available owned management/context closure and shared fixture observations; produces promotion mode/authorization, source/target scope, current policy/review/check gates, one guarded attempt, real-result provenance/containment, pending/partial/uncertain effects. Final inventory sixteen available/one planned; both manifests remain preview.7.

- [ ] **Step 1: Establish promotion baseline and package RED.** Five actor-only inputs cover approving text without merge request, stale/unknown review/check evidence, explicit merge with source movement, lost acknowledgment/pending receipt, and target/method/cleanup constraints. Run fresh no-new-guidance actors and retain successes. Add `test_promotion_available_with_exact_three_skill_closure` while planned.
  Expected: package failure for planned status, no live merge/approval side effect.
- [ ] **Step 2: Add focused protocol and graph controls.** Add `test_merge_uses_exact_source_precondition_and_normal_flags`, `test_source_conflict_does_not_mutate_or_retry`, `test_unknown_or_wrong_revision_gates_are_not_ready`, `test_already_merged_and_hypothetical_sha_are_distinct`, `test_lost_ack_or_pending_is_not_false_merged`, `test_strict_target_and_unsupported_method_or_cleanup_need_decision`, `test_actual_merge_graph_and_descendant_containment`, and `test_rewritten_target_does_not_claim_containment`. Pin full real Git OIDs/parents when graph behavior is asserted and use explicit provider policy facts for fixture mergeability. Observe merge/helper RED before implementation.
  Expected: provider source-CAS and effect records are correct; client readiness/unsupported-scope decisions remain behavioral tests rather than claims that the emulator is the installed skill.
- [ ] **Step 3: Write promotion instructions.** Keep body below 500 words, with local reference covering selected existing request, exact installed management observation, applicable policy and version-aware review/check gates, normal method, expected-head parameter, unsupported strict target guarantee, cleanup effects, one attempt and bounded post-reads. Return actual historical merge separately from mutable target and never infer deployment. Mark available requiring management only; update bounded AGENTS exception.
  Run owner integration discovery and validators.
  Expected: package RED→GREEN, standalone closure promotion/management/context only; no local publish safety preflight.
- [ ] **Step 4: Test candidate and application.** Five fresh actors follow exact promotion/management/context resources. An actual copied-three-folder actor merges one explicitly requested request through emulated transport with real graph OIDs and known current gates. Parent verifies one conditional normal merge call, exact identities/flags, no branch deletion/queue/other field effects, proper post-read provenance/target containment and preserved unrelated dirty local Git state. Gap cases cover branch cleanup, unknown/missing tools, strict target condition, stale comment, automatic queue, descendant and rewritten targets.
  Expected: candidate behavior and independently observed emulated effects pass; no authenticated GitHub/GitLab or native loader claim.
- [ ] **Step 5: Commit and ledger.** Commit `feat: add explicitly authorized hosted promotion`. Complete with owner unittest discovery and retain complete outcome/effect evidence before Task 3.

### Task 3: Compose, document and verify

**Files:** Modify entry SKILL/reference and owner scenarios/evaluations; README, architecture/composition/compatibility/roadmap, installation overview/individual rows/full-set selection and unreleased changelog. Create final evidence at the shared path above.

**Interfaces:** Consumes both closures and owner receipts. Produces optional owned routes, sixteen-name current source selection and one remaining planned git-publish-work. The foundation and historical preview.6 remain unchanged.

- [ ] **Step 1: Capture routing/installation RED.** Before entry edits, evaluate its existing unavailable PR/promotion routes with supplied complete owned discovery. Run `test_installation_selections_match_available_catalog_closures` and retain the missing new rows/full-set names.
  Expected: baseline lacks new routes, closure assertion fails until documentation updates.
- [ ] **Step 2: Add routes and current-source documentation.** Route management and promotion separately with exact owned identifiers and authorizations. Do not run local publish preflight for a selected hosted request. Test installed/absent/foreign/ambiguous/direct closure, default-offline, combined explicit actions and unrelated supplied-facts writing. Add two-/three-skill rows and all sixteen names. Keep preview.7 unpublished and default remote/pinned preview.6 inventories accurate; use development/candidate source until integrated. Mark both delivered in current roadmap, git-publish-work next, native/provider authenticated validation parallel and existing deferred scope unchanged.
  Run installation closure test and validators.
  Expected: documented dependency sets equal the catalog's actual transitive closures; sixteen available/one planned; no placeholders or historical probe rewriting.
- [ ] **Step 3: Run final gates and retain receipts.** Before the final source/evidence commit, run full unittest discovery, both validators, both new-skill quick validations, complete-base whitespace and changed-document local target checks. Retain exact pass/skip counts, baseline/candidate/application evidence and ledger. Then task-done runs the complete task verification command on the committed tree.
  Expected: all runnable tests pass, the existing Windows symlink privilege skip is explicit, and no intermediate installation mismatch remains.
- [ ] **Step 4: Commit and final review.** Commit `feat: compose request management and promotion`. Dispatch one fresh whole-branch reviewer with spec/plan, Review Focus verbatim and ledger rulings. Re-grade by user impact; one material fix pass with reproduced RED/GREEN and green suite, ledger minor deferrals/rulings. Preserve local branch/worktree; no implementation push/PR/merge/release.

## Self-review

Both capabilities share the hosted fixture identity/effect interfaces and promotion consumes management observations, so one ordered plan is appropriate. Task 1 introduces those interfaces and Task 2 extends the same names. Every Review Focus has named controls and actor cases. Management title/body scope, normal-merge-only limitation, provider-shaped unknowns and non-native evidence are explicit. Canonical instruction resources remain independent of development helpers and unavailable projects. Baseline 140/139/1 is observational; final counts come from executed gates rather than a preset target.
