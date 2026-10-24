# Scoped staging and commit construction: final verification

Date: 2026-10-24.
Owners: `git-stage-changes`, `git-commit-builder`, `using-devcraft-toolkit`.
Branch: `feat/git-stage-commit-builder`, based on main at `c6a27b128d6fdec640c02f41984d487287086fbd`.
Inventory: eleven available, six planned; matching unpublished `0.1.0-preview.4` manifests.

## Delivery and evidence

The spec and plan precede implementation commits; staging was completed/tested before the coordinator. Owner-scoped controls used five fresh no-guidance and five complete-instruction samples per new record, with factual baseline successes retained. The coordinator's missing-cwd precision failure was corrected and separately verified instead of being silently scored as a pass.

Real manually loaded actors performed an exact staging operation and one selected commit in owned repositories. Independent parent checks compared exact blob/tree/message/identity/parent and protected state. These are real Git operations through source instructions; they do not establish native plugin loading.

The first complete suite found two existing distribution tests that assumed git-commit-builder was permanently planned. Explicit planned-status fixture setup fixed the stale assumptions while preserving rejection assertions. [Initial failure](initial-suite-failure.log) retains the diagnostics with personal paths/trailing whitespace normalized. Actual validators were not weakened.

## Independent review and single fix pass

A fresh gpt-6-astra high-effort reviewer inspected `c6a27b1..3930ba3`, the complete spec/plan, ledger and evidence. It reported one Important finding, no Critical/Minor findings and no declined behaviors.

The staging recipe omitted a pre-write post-index-change hook gate. A pinned pre-fix live actor staged the exact target and obtained exit0, but the hook rewrote an excluded protected file. Postcondition checks correctly stopped afterward; they could not prevent that effect. This is the observed RED failure, not an invented hypothetical.

The fix inspects effective/default index-write hooks and referenced helpers before every index mutation, including cached apply, add, deferral/restoration and commit preparation. Unknown or out-of-contract effects block without disabling hooks. The coordinator inspects these effects before staging, not only before commit.

A different fresh actor on an identical fixture blocked before mutation, with every parent-verified guard unchanged. A Git recipe control reproduced hook execution for both add/cached apply and default/custom hook paths. The [staging evaluation](../../../skills/git_stage_changes/evaluations/2026-10-24.md) retains both baseline and corrected results.

Additional builder controls blocked an unsafe index hook when the index was already prepared. One actor over-read development catalog contrary to the existing runtime contract; it was not used as ownership evidence. A separate nine-folder-only application had no missing package input but recorded two runner invocation errors; independent parent status/diff calls from the explicit fixture root returned zero. [Coordinator evidence](../../../skills/git_commit_builder/evaluations/2026-10-24.md) retains these limitations rather than claiming perfect compliance/native activation.

No second code review was used to substitute for the bounded fix pass and its regressions.

## Final checks

- `python -B -m unittest discover -s tests -p "test_*.py" -v`: 100 discovered, 99 passed, one existing Windows symlink privilege skip; exit0 after the hook fix. See [verification.log](verification.log).
- The eleven staging/commit recipe tests passed, including hook/effective-identity/failure controls.
- Repository and distribution validators passed, without claiming native loading.
- Complete-base and staged/committed-range whitespace checks passed.
- Installation selections exactly match catalog closures: stage four, builder nine; complete set eleven.
- Changed tracked documentation local targets: 93 checked before final report additions.
- Both new SKILL.md files remain below 500 words with self-contained local references.
- Published preview.3, historical release documentation and main remain untouched by this increment.

## Ruling and remaining limits

The executor made one plan ruling: construct an explicitly planned distribution fixture instead of assuming the builder remains planned forever. Existing rejection assertions remain unchanged. Cost if wrong: the fixture could misrepresent planned-status rejection; both targeted cases and the final suite passed.

No deferred code-review minors or unresolved Critical/Important findings remain. Native client activation/lifecycle, unsupported index cases and universal model adherence are not claimed; observation guards are not atomic concurrency locks.

The branch and worktree are preserved for review. No push, PR, merge, tag or release is part of this implementation increment.
