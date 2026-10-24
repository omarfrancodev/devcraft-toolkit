# Scoped commit flow

## Inputs, language and progress

Keep the selected repository/index, actual authorization, operation mode, planner groups, evidence/guards, validations, commit receipts and remaining state in memory. Use the progress controller rather than duplicating its state machine; missing native tracker tools use its inline fallback. A named step is not execution permission.

Planning is the default. An explicit request to create commits authorizes the corresponding selected staging/commits and ordinary inspected local checks, not branch creation, history mutation, network or arbitrary side effects. Honor explicit preview-only or supplied-transcript requests without executing anything. Missing skill dependencies differ from missing tools; neither grants substitutes.

Resolve selected-installation ownership for the complete closure: builder, planner, stage, safety, validation, progress, analyzer, context and formatter. Preserve formatter decisions and language. Do not read a development catalog at runtime.

## Protected evidence and selection

Resolve root/Git metadata first; apply the analyzer's safe prefix/filter gate even during context and safety reads. Reuse current facts but refresh HEAD/index/content/inventory, attributes/config/effects, identity and operation markers before dependent writes. A prior timestamp, equal status code or ready preflight is not a lock.

Use the planner's exact paths/layers/hunks and staged-first within requested paths. Preserve existing selection/exclusions. Unknown target content, unsupported flags or transport remain limited/blocked. Missing identity or unclear inherited work/personal identity needs a decision; do not repair config. Before committing, inspect effective author and committer with protected `git var GIT_AUTHOR_IDENT` and `git var GIT_COMMITTER_IDENT`, including environment overrides; config names alone do not establish the actual identity. Compare the identity values to the authorized choice before writing, not only after creating a commit. Never clear overrides silently. Detached HEAD needs an explicit strategy before commit; do not create/switch branches for the user.

Before each group, the whole index must represent that group's intended complete tree, including unchanged base content. If unrelated staged changes would enter the commit, request a concrete temporary-deferral decision and use stage only for its approved reverse/forward cached transformations. Do not use alternate GIT_INDEX_FILE, commit --only/path arguments or commit -a to sidestep selection. Successful completion restores only expressly approved residual deferrals via fresh exact staging; failures preserve actual deferred state and stop, not automatic rollback.

For multiple groups, remember approved partition boundaries and deferred bytes/OIDs. Expected own index/HEAD transitions are reconciled with refreshed analysis after each commit; they do not make unrelated external changes acceptable or give old evidence IDs new meanings.

## Validation scope and effects

Delegate command discovery/assessment/execution to validation-discovery. Its evidence/effect rules and passed/failed/not_run/blocked/not_detected outcomes remain authoritative. Required failed, blocked or not_run checks stop affected downstream writes. A missing configured check is not_detected, not a pass; it is not a new gate unless the user/project requires one. Report every required check separately. Each receipt has command, source, working_directory, scope, exit/result and artifacts; retain unknown for unsupplied values. A selected repository root alone is not evidence of the check's actual working directory.

Disclose expected artifacts. Do not silently install, autofix, stash, clean, create another checkout or stage generated output to make validation work. Preserve unexpected changes and pause. Checks run on actual working content; if excluded edits differ from the selected index, explicitly report that scope. When exact selected-content validation is required, obtain real corresponding evidence through an authorized safe method or block; never claim a dirty-worktree pass validates another tree.

If allowed validation/hook artifacts changed guards, refresh the analyzer and approved target rather than reusing stale scope. Permission to run a check does not authorize additional source edits or their inclusion.

## Commit effects

Perform this effect gate before staging or any other mutation, not only before the commit command; refresh it again before each write. Explicitly inspect post-index-change and its helpers through effective/default hooksPath: both staging and commit preparation can write the index. The stage capability's pre-write gate also applies to every deferral/restoration. Unknown or out-of-contract effects block before writing; never bypass hooks to proceed.

Inspect effective core.hooksPath (or the resolved default hooks directory) and active commit hooks, including referenced helpers; sample/disabled hooks are not active. Resolve relative hook paths according to Git execution context. Inspect signing/editor settings and user/project conventions. No hook/signing bypass, --no-verify, key setup, configuration writes or network is implicit.

Known bounded local hooks within the request may run with their effects disclosed. Unknown, destructive, external or additional unapproved effects require the relevant decision. An autofixing hook is not automatically authorized just because it is a hook. Required signing/interaction that the harness cannot provide blocks the operation; do not disable it. Effective message transformations must be explicitly accounted for, not silently accepted.

After exact staging and fresh commit preflight, use the protected Git command with byte-safe message stdin, for example:

```text
commit --file=- --cleanup=verbatim
```

A safe literal argument API is an alternative; absent byte/argument-safe transport yields limited. Do not create temporary patch/message/output files as an undocumented fallback. Avoid shell interpolation of message data. Do not use -a, --only, path arguments, --amend, --allow-empty, rebase or any history-changing shortcut.

## Postconditions and failures

Capture actual exit/stdout/stderr during the command, not by rerunning it. Read new HEAD and its commit object: expected parent (none for initial commit), branch strategy, whole tree versus the approved manifest, final message and identity must match the authorized operation. Verify residual index, excluded worktree bytes/refs and configuration. Necessary commit/index/object/log metadata are expected; unexplained content/ref changes are not.

An exit-zero commit with an unexpected tree or message stops the flow and preserves the actual commit. A failing command may have effects or even advance HEAD; inspect before reporting. Never delete earlier commits or force success. Record actual SHAs and exact remaining groups; partial means some commits exist and work remains. An empty selected delta is no_op, never an empty forced commit.

Return semantic record fields from the main skill; prose/tables are sufficient. Verification covers an observed interval, not atomic concurrent mutation or native compatibility.

## Example

The index contains G1's rounding correction while the worktree also has excluded debug output. A passing worktree check is reported with that scope. With current preflight and explicit commit permission, an index-based commit must contain the correction only and leave the debug edit in the worktree. If G2 later fails its hook, report G1's actual SHA and G2's pending index state as partial; do not reset G1 or retry G2.

Official semantics: [commit](https://git-scm.com/docs/git-commit), [hooks](https://git-scm.com/docs/githooks).
