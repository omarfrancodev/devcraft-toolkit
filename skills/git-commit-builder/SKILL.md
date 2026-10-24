---
name: git-commit-builder
description: Use when local changes need a coordinated commit proposal or explicitly requested commit creation, including ordered groups, scoped validation and partial progress.
---

# Build Scoped Local Commits

Coordinate capabilities; preserve selection and progress. No branch creation, publication, history rewrite or automatic recovery is implied.

## Resolve mode and dependencies

Require `git-plan-commits`, `git-stage-changes`, `git-safety-check`, `validation-discovery` and `todo-workflow-controller`, including their analyzer/context/formatter closure. Resolve actual selected-installation identifiers and ownership. Missing dependencies are unavailable, never imitated, substituted or installed.

Use explicit language preference, then request language, then English; preserve technical keys/identifiers/statuses.

Plan unless the request explicitly asks to create commits. A skill name, plan or preflight grants no write permission. An explicit commit request covers its exact selected staging and inspected ordinary local checks; disclose expected effects without redundant confirmations. Material scope, partition, identity or additional effects need a focused decision.

Read [commit flow](references/commit-flow.md) before execution. Its protected dependency reads, validation scope, hook/signing inspection and postconditions are required.

## Coordinate the flow

1. Track steps/gates with the progress controller's native or inline mode. Obtain current analysis/context and intent-specific preflight.
2. Use the planner's evidenced ordered groups/messages. Narrow paths, retain staged-first and exclusions. Do not silently repartition the index.
3. Delegate discovery and requested checks to validation-discovery. Report each check's actual scope/result. Dirty-worktree success is not proof of different selected content; a required exact-index check must really cover it.
4. Before each authorized group's staging, inspect index/commit effects and refresh facts; delegate the exact index transformation. Account for every index entry before committing. Unrelated staged entries require an approved deferral/restore decision, not a path/alternate-index bypass.
5. Refresh commit preflight, identity, target and configured effects. Honor inspected hooks/signing; unknown or additional effects block the affected operation. Never force success by bypassing them.
6. Create only a normal new index-based commit with literal message transport. Capture exit/output once and verify actual SHA, parent/branch, complete tree, message, identity and residual state. Reconcile expected own transitions before the next group.

Stop on failure, unexpected mutations or stale evidence. Preserve earlier commits and remaining state; never reset, amend, clean, revert or retry automatically.

## Return the observed result

| Field | Content |
| --- | --- |
| `outcome` | `planned`, `committed`, `no_op`, `needs_decision`, `limited`, `blocked`, `stopped`, `partial` |
| `mode`, `authorization` | Requested mode and exact permitted effects |
| `groups` | Selection, messages, order and decisions |
| `validations` | Commands/source, observed working_directory (unknown if unsupplied), scope, exits/results and artifacts |
| `commits` | Actual verified SHAs/parents/trees/messages/identity |
| `remaining`, `state` | Unfinished groups, index/worktree and blockers |
| `limitations` | Evidence, transport and execution limits |

`committed` requires every requested group verified; `partial` means actual commits exist but the sequence is unfinished. Supplied transcripts must be identified as reported evidence, never personal/live execution. A failed command may still have created effects or a commit.

Common mistakes: committing all staged content for one named path, treating validation as broader than observed, or losing earlier progress when a later step fails.
