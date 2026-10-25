---
name: git-publish-changes
description: Use when a current committed Git branch needs a publication assessment or explicitly requested normal single-branch push, optionally with requested upstream setup.
---

# Publish One Branch Snapshot

Publish one pinned current-branch commit to one selected remote branch. Preserve local work and actual partial/uncertain effects; no synchronization, commit construction, PR, promotion or release is implied.

## Resolve ownership, scope and permission

Require the selected installation's `git-working-directory-policy` and `git-safety-check` through their exact discovered identifiers and ownership. No sync skill or hosting connector is required. Missing/foreign dependencies are unavailable; unresolved ownership needs a choice. Do not install, imitate or read a runtime catalog.

Use explicit language preference, request language, then English. Preserve identifiers/statuses and redact secrets.

Default `inspect` is local/cached evidence only: no network, fetch or push dry-run. Explicit `observe` permits selected advertisement queries. An explicit publish request authorizes its normal single-branch push and bounded verification, never an implicit fetch or upstream change. Only an explicit upstream request authorizes two local branch-key writes. Reuse existing permission; ask only for material unresolved choices.

Read [publication.md](references/publication.md) before inspection/execution. Its protected reads, endpoint/effect gates, exact commands and receipts are mandatory.

## Execute one publication

1. Obtain metadata-only context and inspect helpers before status/preflight reads. Require a current named committed branch, fresh clean worktree/index and no active operation; use safety's read-only publish gate. Commit identity does not establish authentication or authorize changes.
2. Resolve one explicit remote/destination, otherwise an unambiguous agreeing upstream/push route. Inspect effective pushurl/rewrite, endpoint, mappings, options, hooks/helpers and signing. Do not guess origin, choose multiple URLs or bypass required checks.
3. Pin full source OID. Observe the selected remote branch under publication permission. Unknown local target objects require a fetch decision, not automatic fetch. Non-fast-forward is blocked. Stricter create-only/exact-old conditions must not be weakened.
4. Refresh guards; push only the full pinned source to the full branch ref, suppressing tag/submodule/default expansion and automatic setup as documented. Never force, mirror, delete, use all/tags or skip hooks. Capture the actual result once.
5. Independently verify the remote OID and preserved local guards/expected tracking effects. Failed or unavailable acknowledgment is not proof of no effects; preserve state without retry, rollback or cleanup.
6. Only for explicitly requested upstream setup, after verified publication/equality and unchanged source, write/read back the two repository-local branch keys. Preserve other/global config and actual partial failure. An already equal target needs no push; requested configuration remains a separate result.

## Return

Report outcome/mode/authorization, scope/redacted endpoint, pinned source and observed remote OIDs, relation/effect checks, actual command/verification results, optional upstream result, remaining state and limits. Outcomes: `planned`, `observed`, `published`, `no_op`, `needs_decision`, `limited`, `blocked`, `stopped`, `partial`, `uncertain`.

`published` requires verified postconditions. `no_op` describes an equal branch, not absence of requested configuration effects. Keep supplied transcripts identified as reported evidence. Create no auxiliary files or external posts.
