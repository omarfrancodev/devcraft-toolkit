# Git Activity Reporting Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a local-history report coordinator with explicit date, identity, coverage and output boundaries.

**Architecture:** An instruction-first coordinator obtains context through `git-working-directory-policy`, inspects a pinned local history snapshot using safe Git recipes, and delegates supplied evidence to `natural-language-report-writer`. Optional entry routing and explicit three-skill installation expose the same canonical resources.

**Tech Stack:** Markdown, JSON catalog/existing manifests, Python unittest development fixtures and Git 2.45+. No runtime interpreter, collector or network dependency.

**Spec:** [Approved Git activity reporting design](../specs/2026-10-24-git-activity-report-design.md)

## Global Constraints

- Source skills, documentation, examples and default templates use English. User-facing content follows an explicit language instruction, then the request language, then English.
- Runtime resources are self-contained under `skills/git-activity-report/`; no Python runtime, root catalog, repository docs or network is required by an installed skill.
- Runtime Git inspection is read-only. No staging, commits, branch/config changes, fetching, lazy fetching, installs, validation execution or external posting.
- A requested saved report delegates the report writer's existing one-file permission: explicit user-selected destination, existing-parent requirement, replacement authorization and matching readback. Do not create companion evidence files.
- Automated tests, fixtures, scenarios and retained evaluations live under root `tests/`, grouped by owning skill and scope.
- Do not add runtime collectors, installers, release automation, a license or new manifests. CCR remains deferred.
- Existing published preview.4 remains an eleven-skill snapshot. This increment is an unpublished twelve-skill candidate; five capabilities remain planned. Both existing manifests advance together to `0.1.0-preview.5` before the inventory becomes available.
- Defaults: pinned HEAD, today in known user/session timezone, author timestamp, configured exact raw author email, exclude merge records while traversing all parents, 1,000 examined commits plus one truncation probe.
- Development fixture setup and local implementation commits are authorized work in the isolated feature worktree. Runtime read-only restrictions apply to delivered skill use.

## Review Focus

1. Non-monotonic author/committer times and DST days must not drop matching ancestors or use a fixed 24-hour interval (Task 1 controls and behavior).
2. Literal author identities, alias/mailmap/co-author text and duplicate messages must not broaden selection or collapse distinct OIDs (Task 1).
3. Zero matches in shallow, missing-object, truncated or budget-exceeded history must remain `limited`, never a complete `no_op` (Task 1).
4. Hostile commit content, hooks/helpers, moving refs and failed output writes must not redirect execution or imply an up-to-date/saved report (Tasks 1–2).
5. Standalone ownership and missing/foreign copies must not cause a catalog read, automatic installation or manual emulation (Task 2).

## File map and execution

The approved request authorizes spec, plan and implementation in order. Execute inline using the established method, without another approval checkpoint. Use fresh behavioral actors as tests and one final reviewer, not per-task implementers.

- Create `skills/git-activity-report/SKILL.md`, `references/history.md`.
- Create `tests/skills/git_activity_report/{__init__.py,integration/,scenarios/,fixtures/,evaluations/}` and `integration/test_history_recipes.py`; test-only helpers remain in that owner directory.
- Modify `catalog.json`, both existing manifest versions and entry instructions/reference.
- Add entry-owner scenarios/evaluation in `tests/skills/using_devcraft_toolkit/`.
- Update current README/architecture/composition/compatibility/roadmap, installation inventory/closures and `CHANGELOG.md` unreleased; preserve historical releases/probes/evaluations.

### Task 1: Deliver verified history reporting

**Files:** Create the coordinator/resources and owner-scoped fixtures, scenarios, evaluations, integration tests; modify catalog availability/dependencies and both existing manifest versions.

**Interfaces:**
- Consumes installed context root/HEAD/identity and writer's supplied-fact/language/output contract.
- Produces `status`, `scope`, `coverage`, `commits`, `report`, `output` as defined in the spec. Direct closure: `git-activity-report git-working-directory-policy natural-language-report-writer`.
- Test-only `history(repo: Path, *, start: int, end: int, emails: set[str] | None, basis: str = "author", budget: int = 1000, include_merges: bool = False, revision: str = "HEAD") -> dict`: runs real safe Git commands and returns pinned OID, inspected records and completeness. It verifies the recipe, not skill invocation.

- [x] **Step 1: Record RED behavior before writing skill resources.** Create at least five concrete raw-fact requests for author/committer divergence, exact identity, incomplete empty history, hostile text and language/file output. Run fresh no-guidance samples and retain their actual responses under `evaluations/`; assess successes and omissions explicitly. Create a package-closure test asserting the new available entry, exact dependencies, local self-contained resources and candidate manifest agreement; run it before availability changes.
  Expected: package closure fails because reporting is planned; behavioral baseline results are recorded without invented failures.
- [x] **Step 2: Write real Git recipe controls.** Implement owner-scoped tests named `test_author_date_and_nonmonotonic_ancestors`, `test_half_open_boundaries_and_committer_basis`, `test_exact_email_ignores_aliases_and_regex`, `test_merge_traversal_and_duplicate_messages`, `test_budget_and_shallow_zero_matches_are_limited`, `test_missing_objects_are_not_empty_history`, `test_unborn_invalid_and_detached_revisions`, `test_helpers_and_dirty_state_are_preserved`, `test_pinned_snapshot_survives_ref_movement`, and `test_calendar_boundaries_include_dst_days`. Use `tests/support/git_fixtures.py` snapshots and an isolated global config. Avoid executing untrusted message text or external helpers.
  Run: `python -B -m unittest discover -s tests/skills/git_activity_report/integration -p "test_*.py" -v`.
  Expected: every recipe assertion passes; before/after snapshots remain equal for inspections. The package availability test stays RED until Step 3.
- [x] **Step 3: Write minimal coordinator and local history reference.** Keep SKILL body below 500 words, description beginning `Use when`, complete local metadata/selection/output contract, and one concrete safe recipe. Require exact UTC intervals, safe flags and finite coverage. Mark catalog available with the two declared dependencies and advance both manifests to `0.1.0-preview.5`.
  Run owner integration checks and both repository/distribution validators.
  Expected: package closure GREEN and safe recipes pass. No runtime script or sibling/root resource link is introduced.
- [x] **Step 4: Run candidate behavior and actual application.** Repeat the five raw-fact requests with complete candidate resources in fresh contexts. Correct only observed defects and retain raw results. In an owned fixture, have a fresh actor manually load only the three-skill closure, read real commits, request one explicit saved report and verify the written/read-back content plus independent repository snapshots. Assess language, exact IDs, limits, source attribution and absence of extra files. Disclose native loading was not exercised.
  Expected: candidate results satisfy the scenario assertions; failures remain visible and are corrected/retested. No blanket compliance claim from one sample.
- [x] **Step 5: Commit.** Commit skill, owner tests/evidence, catalog/manifests and task progress as `feat: add verified local Git activity reports`.
  Task verification: owner integration command from Step 2, both validators and `git diff --check 613ffebe3f15a7d0e42e55330d5742ad8f96bb4d` all pass.

### Task 2: Route installed history reporting

**Files:** Modify entry SKILL/reference and owner scenarios; create `tests/skills/using_devcraft_toolkit/evaluations/git-activity-report-composition.md`.

**Interfaces:**
- Consumes Task 1's available coordinator and exact three-skill standalone closure.
- Produces an optional route using selected-installation discovered identifiers, without changing entry hard dependencies. Supplied-fact requests continue directly to the writer.

- [ ] **Step 1: Record routing RED.** Evaluate the unchanged entry for a history report with reporting/context/writer installed in the selected package. Also evaluate absent, foreign/ambiguous and direct standalone conditions using supplied discovery metadata.
  Expected: unchanged entry calls the coordinator planned/unavailable; distinguish that expected limitation from any baseline successes.
- [ ] **Step 2: Add the optional route.** Replace only stale activity-planned text and retain publication-planned boundaries. Delegate dependency ownership, history evidence and writer output; no safety preflight solely for reporting. Record the same dependency/result boundaries in the local composition reference.
- [ ] **Step 3: Re-evaluate routing.** Fresh supplied-metadata cases cover installed, absent, foreign/ambiguous, direct three-skill closure and supplied-facts writing.
  Expected: exact owned identifiers selected, absent dependencies unavailable, ambiguity pauses dependent invocation, no catalog read or automatic install, supplied facts still use writer directly.
- [ ] **Step 4: Verify and commit.** Run both validators and owner integration checks; retain exact outcomes and limitations. Commit `feat: route installed Git history reporting`.

### Task 3: Align distribution and retained evidence

**Files:** Modify README, current architecture/composition/compatibility/roadmap, `docs/installation.md`, `docs/installation/individual-skills.md`, other current full-set recipes if found and unreleased changelog. Create final integration evaluation under `tests/integration/evaluations/2026-10-24-git-activity-report/`.

**Interfaces:**
- Consumes Tasks 1–2's twelve available/five planned catalog, three-skill report closure and actual verification evidence.
- Produces consistent current-source inventory and explicit unpublished-candidate guidance; older preview.4 pinned sources remain eleven skills.

- [ ] **Step 1: Check installation closure against catalog.** Extend the owner package test to parse the individual-install table and complete `$toolkitSkills` list; compare sets to transitive catalog closures and available inventory rather than matching prose.
  Expected RED: current guide lacks the report closure and still lists eleven skills.
- [ ] **Step 2: Update current docs and changelog.** Add report defaults/limits, file permission delegation, explicit dependency selection and version-specific source inventory. Roadmap marks activity reporting available in the candidate and makes remote publication the next increment, with native invocation parallel. Preserve old release files and historical evaluation wording.
- [ ] **Step 3: Verify the full branch.** Run `python -B -m unittest discover -s tests -p "test_*.py" -v`, both validators, `git diff --check 613ffebe3f15a7d0e42e55330d5742ad8f96bb4d`, and changed-document local-link checks. Record exact discovered/passed/skipped counts and fixture/behavior distinctions.
  Expected: all runnable tests pass, existing Windows symlink privilege skip disclosed; validators and links pass.
- [ ] **Step 4: Commit and request one fresh whole-branch review.** Commit `docs: document activity reporting and remaining roadmap`. Review the approved spec/plan, branch diff and ledger rulings. Re-grade findings by user impact; one fix pass for Important/Critical findings with reproduced RED/GREEN evidence, then affected/full checks. Record any minor deferrals explicitly. Preserve the branch/worktree; no push, PR, merge, tag or release is requested.

## Self-review

Each spec requirement maps to Task 1's coordinator/evidence, Task 2's ownership route or Task 3's distribution boundary. Producer/consumer field names and closures agree. Review Focus conditions have real Git controls or behavioral applications, with native activation explicitly separate. No task introduces a new executable runtime, source provenance dependency or external side effect.
