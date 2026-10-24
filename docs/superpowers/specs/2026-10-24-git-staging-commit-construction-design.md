# Scoped Staging and Commit Construction Design

**Date:** 2026-10-24
**Status:** Scope authorized; sequential implementation requested
**Increment:** Explicit local Git writes

## Intent and approach

Complete the local commit flow with two composable instruction-first skills: `git-stage-changes` changes an exact approved index selection; `git-commit-builder` coordinates existing analysis, planning, formatting, progress and validation to create requested commits. Implement and verify staging before building the coordinator.

Keep the established Markdown/reference approach. A monolithic coordinator would duplicate independently usable staging; a runtime executable would introduce an unnecessary dependency and separate source of policy. These choices are implementation judgments within the requested scope.

## Global constraints

- Maintain source skills, documentation, examples and default formats in English. Resolve output language from explicit preference, then request language, then English; preserve technical identifiers and schema keys.
- Keep installed skills self-contained, with local references and declared catalog dependencies. Runtime never requires the root catalog, docs or development Python tools.
- Keep tests, scenarios, fixtures and retained evaluations under root `tests/`, grouped by skill owner and scope.
- Preserve excluded worktree content, unrelated index entries, configuration and other repositories. No automatic branch creation/switching, stash, reset, cleanup, amend, history rewrite, network, publication or credential changes.
- Authorization is scoped to the user's requested operation and exact selected changes. A plan, discovered command, ready preflight or skill invocation alone grants no write permission.
- Capture process exit status during the operation. Stop on unexpected changes or failures, preserve all observed state, and never retry, roll back or hide effects automatically.
- Test writes occur only in owned disposable repositories. Native client loading remains separate from instruction-following and Git recipe evidence.
- Preserve published preview.3 and historical evidence. Use matching development manifest version `0.1.0-preview.4`, unpublished; do not merge, create a PR or release in this increment.

Update project instructions to distinguish the existing read-only milestone from these bounded write exceptions.

## Dependencies and installation

`git-stage-changes` requires `git-analyze-changes` and `git-safety-check`; their closure includes repository context.
`git-commit-builder` requires `git-plan-commits`, `git-stage-changes`, `git-safety-check`, `validation-discovery` and `todo-workflow-controller`. Its transitive closure also includes the analyzer, context and formatter: nine skills including the coordinator itself.

The entry keeps its existing hard foundation. Add optional installed-only staging and commit-coordination routes; check selected-installation ownership for every required dependency. Missing dependencies are unavailable, never silently imitated, substituted or installed. Message-only requests continue to use the formatter without Git operations.

The catalog becomes eleven available and six planned across the same seventeen names. Current individual/full-set documentation describes the new closure and distinguishes the unpublished eleven-skill checkout from published preview.3's nine skills.

## Shared operation context

Reuse current repository context and an analyzer record, preserving exact paths, evidence IDs, layer/hunk boundaries, scope and limitations. Refresh HEAD/index/content/inventory and operation/configuration facts before each dependent write. Narrow paths before applying explicit layers or the staged-first default within those paths.

The mutation request records `mode`, `repository`, `authorization` (actual user instruction and approved scope), `analysis_snapshot`, `selection`, `expected_index` and `exclusions`. `expected_index` is a complete stage-zero index manifest (exact path, mode and blob OID), with missing entries representing approved deletions; it is not just a list of filenames. Capture raw selected/excluded content guards and effective attributes/configuration affecting normalization.

Read protections apply while resolving context/preflight, not only afterward. Resolve location/Git metadata first, then use the analyzer's protective options and external-filter gate before any dependency status/worktree hashing. Do not silently clear GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE or bypass a different selected repository/index. An unresolved override needs a decision.

Unmerged entries or active operations block writes. Unsupported intent-to-add, sparse/skip-worktree selections, unobserved modes or binary hunk splitting return limited/blocked for affected selections without changing flags. Missing identity does not block index-only staging; commit creation needs a known unambiguous identity and resolved branch strategy through the existing preflight. Do not set local/global identity automatically.

## Staging skill

Inputs are the shared context plus an exact target selection, from a reviewed planner group or direct user selection. A bare invocation or request to propose staging is preview-only and returns `planned`; a clear “stage these changes” request authorizes the matching index mutation without a redundant confirmation. Changed or materially ambiguous scope needs one focused decision before the affected write.

The default preserves current staged content. Full-path staging is allowed only when the complete working version of every selected path is approved. A partially staged path with excluded later edits requires an exact index-only patch; never replace that selection by add-all or whole-file staging. Explicit multi-commit repartition may remove/defer only approved index hunks while preserving their worktree content. Record deferred selections; no implicit unstage or reset.

Supported recipes:
- Exact whole-path add/update/delete with literal pathspecs and argument-safe paths, using NUL stdin where supported.
- Exact approved text patches with `git apply --cached --check` before `git apply --cached`; approved reverse cached patches may defer selected staged hunks during an explicit repartition. Never use worktree apply, three-way fallback, whitespace fixing or unsafe paths.
- No write if the current index already equals the approved target; return `no_op`.

Obtain expected normalized blob OIDs without writing objects (Git hash-object without -w, only after the external-filter gate), using complete approved target bytes and observed modes. For partial patches, construct/verify complete target content in memory with available harness capabilities; absent exact content is limited, not permission to guess. Reject patch paths/changes outside the approved manifest before applying. Built-in normalization follows effective configuration; external clean/process filters retain the analyzer's conservative unsupported worktree fallback rather than running arbitrary helpers.

Before writing, verify exact target, authorization, safety, fresh guards and mutation effects. Resolve effective/default hooksPath and inspect post-index-change plus referenced helpers before any index write, including deferral/restoration and commit preparation. Unknown or out-of-contract effects block before mutation; never disable or bypass hooks. Afterward compare the entire index manifest to the expected manifest, HEAD/refs and worktree guards to their prior values, and report actual exit/output and any discrepancy. Necessary Git blob/index writes are allowed; repository files and branch/HEAD changes are not.

Staging result fields: `outcome` (`planned`, `staged`, `no_op`, `needs_decision`, `limited`, `blocked`, `stopped`), `repository`, `authorization`, `selection`, `before`, `after`, `checks`, `deferred`, `limitations`. An unexpected postcondition is stopped even if the command returned zero.

## Commit coordinator

Use progress tracking with its documented inline fallback. Default to planning unless the request explicitly asks to create commits; a supplied plan/skill name alone does not authorize execution. A clear commit request authorizes necessary selected staging and inspected ordinary local checks, with expected artifacts disclosed. Ask only for unresolved material scope, repartition, identity or effect decisions.

Sequence:
1. Resolve ownership, operation mode and scope; reuse analyzer/context and run intent-specific preflight. Inspect index-write and commit effects before any mutation, then refresh them before each write. Explain actual planned effects.
2. Obtain the planner's ordered groups/messages. Respect staged-first, path scope, exclusions and pending decisions. An existing multi-intent index is not silently repartitioned; explicit execution approval must cover the concrete partition. Unrelated staged entries outside a requested group require an explicit deferral decision before they can be temporarily removed; do not bypass the approved index through path-only commit or an alternate index. After successful requested commits, restore only the expressly approved deferred entries through exact staging and verify their intended residual selection. A failure stops before automatic restoration/rollback and reports the actual deferred state.
3. Discover checks through validation-discovery and inspect the selected commands/hooks/artifacts. Required failed, blocked or not_run checks stop dependent writes. No detected check is not a pass; absence alone is not a new gate unless required by user/project. Do not invent a command or install dependencies.
4. Run only authorized checks through that skill. Evidence about a dirty working tree is not proof of a different selected index: report the actual validation scope. If an exact selected-content check is required and unavailable, block rather than silently stash, build another checkout or claim a pass. Preserve unexpected artifacts and never stage generated files automatically.
5. For each group, refresh facts and delegate only its approved index transformation to staging. Verify the entire index contains precisely that commit group's expected tree, with approved deferrals and unrelated entries accounted for; never commit all staged content merely because the group names one path.
6. Recheck preflight, identity, operation state, selected index and commit effects. Inspect effective hooksPath/default active hooks, referenced helpers, signing/editor configuration and relevant message transformations. Honor configured checks/signing; never disable hooks/signing or use no-verify to force success. Known bounded local hooks within the commit request can run; unknown, external, destructive or additional unapproved effects need a specific decision. Unavailable signer/interaction blocks execution without changing config.
7. Create a normal new commit with literal message transport, preferably `git commit --file=- --cleanup=verbatim` through byte-safe stdin. Never use -a, path arguments that bypass the approved index, --amend, --allow-empty or history mutation.
8. Capture exit/output once; verify actual new HEAD, parent (or initial commit), branch, complete committed tree, message, effective identity, residual index and worktree. Record each actual commit SHA and only continue after expected own transitions are reconciled with refreshed evidence. A failing hook or later group failure preserves earlier commits and all remaining state; no automatic reset, amend, revert, cleanup or retry.

A changed HEAD after a failing command is an observed effect, not proof that nothing happened. Unknown/unapproved hook changes to committed tree/message/index/worktree stop the flow and are reported with actual commits preserved. The observation is guarded, not an atomic concurrency guarantee.

Coordinator result fields: `outcome` (`planned`, `committed`, `no_op`, `needs_decision`, `limited`, `blocked`, `stopped`, `partial`), `mode`, `authorization`, `groups`, `validations`, `commits`, `remaining`, `state`, `limitations`. `partial` means some actual commits exist but the authorized sequence did not finish; include the blocker and remaining groups. `committed` requires verified postconditions for every requested group. No outcome implies publication.

## Acceptance and evidence

Before each skill is written, define owner-scoped application, pressure, variation and gap scenarios; use fresh baseline controls without the candidate instructions and then complete-instruction actors. Preserve successes and failures honestly. Record-shaping micro-tests use five fresh samples per arm; targeted application regressions do not establish universal reliability.

Use real disposable Git recipe tests for partial staging, exact filenames/deletions, stale patch rejection, approved repartition, unborn staging/commits, commit messages as data, excluded dirty content, hooks failing or altering the selection, and partial multi-commit progress. Snapshots distinguish allowed index/objects/commits from unexpected worktree/config/ref effects. Automated recipe tests prove command semantics, not assistant judgment or native loading.

Test selected-installation dependency absence, stage-only identity absence, required validation failure/unavailable tools, path-only staged-first, normalization, sparse/intent-to-add fallbacks, hooks/signing boundaries, and no implicit branch/network operations through application/gap cases. Keep progress/validation behavior delegated rather than duplicated.

A fresh builder check precedes the plan; implement staging completely before the coordinator. Use one independent whole-branch review and a bounded verified fix pass. Builder choices left open: concise record presentation/ID spelling, owner-scoped fixture decomposition and safe transport APIs available in each harness. Unsupported transport yields limited rather than unsafe shell interpolation.

## References

- [Git add](https://git-scm.com/docs/git-add): selected pathspecs, staging and normalization.
- [Git apply](https://git-scm.com/docs/git-apply): cached/check/reverse patch behavior.
- [Git commit](https://git-scm.com/docs/git-commit): index-based commits and message input.
- [Git hooks](https://git-scm.com/docs/githooks): hook execution and failure effects.

## Release integration amendment — 2026-10-24

The implementation record above retains its original development-candidate scope. After the approving review of `38d376648fdbb067721f12eea5ced1eb835825d2`, publication of `v0.1.0-preview.4` is authorized through PR #6. Changelog and consumer release preparation are included in that PR before merging. The release tag and verified ZIP/checksum assets must use its exact merge commit; no subsequent source-preparation commit is required. Native activation gates remain open, and this amendment adds no runtime behavior or release automation.
