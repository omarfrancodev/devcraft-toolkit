---
name: git-stage-changes
description: Use when local Git changes need an exact staging selection, partial hunks must be preserved, or an explicitly approved index partition is needed.
---

# Stage an Exact Selection

Change only the approved index target and necessary Git objects. Preserve HEAD, refs, worktree content, configuration and excluded index entries.

## Resolve scope and permission

Require installed `git-analyze-changes` and `git-safety-check`, including repository context. Use the selected installation's actual identifiers/ownership. Missing dependencies are unavailable; do not imitate, install or substitute foreign copies.

Use explicit language preference, then request language, then English. Preserve technical keys, identifiers and status values.

A bare invocation or proposed staging request is preview-only. An explicit stage request authorizes its exact selection without redundant confirmation. A plan or ready preflight alone grants no write permission. Ask one focused question for a material scope or partition decision.

Read the local [index operations reference](references/index-operations.md) before execution. Apply its protective setup during dependency reads too. Use current analysis and inspect preflight; missing identity does not block index-only staging. Conflicts/active operations block writes. Inspect index-write hooks before each mutation; unknown or unauthorized effects block execution.

## Establish the exact target

Keep `mode`, `repository`, actual `authorization`, `analysis_snapshot`, `selection`, complete `expected_index` and `exclusions` in memory. The target includes exact paths, modes and normalized blob OIDs for the whole index, preserving unrelated entries. Deletions are explicit absences.

Stage a whole path only when its complete working version is selected. For partial files use an exact approved index-only patch. A repartition may defer only expressly approved staged hunks; it is not an implicit unstage permission. Unknown target content/modes, unsupported flags or transport yield limited/blocked rather than broader staging.

Refresh guards before each write. If already at the exact target, return `no_op`. Otherwise check the patch or exact path operation, then execute only the authorized transformation.

## Verify and report

Capture exit/output once. Compare the entire resulting index with the expected target, and HEAD/refs/worktree/configuration guards with the prior state. Stop on any mismatch or failure, preserve observed effects and never retry, reset, clean or roll back automatically.

Return these semantic fields in conversation tables/prose:

| Field | Content |
| --- | --- |
| `outcome` | `planned`, `staged`, `no_op`, `needs_decision`, `limited`, `blocked`, `stopped` |
| `repository` | Selected root/index and HEAD |
| `authorization` | Actual request, permitted effects and mode |
| `selection` | Exact evidence/layers/hunks and target |
| `before`, `after` | Index manifests and protected guards |
| `checks` | Commands, actual exit/output and postconditions |
| `deferred` | Approved deferred selections or none |
| `limitations` | Missing coverage, transport or execution evidence |

`staged` requires verified expected effects; exit zero alone is insufficient. If reporting a supplied executor transcript, identify its source and distinguish reported results from operations performed by this assistant. Never invent execution or rerun solely to produce a report.

Common mistakes: whole-file/add-all fallback, dropping existing staged work, trusting stale evidence, or treating a stage result as commit permission.
