---
name: git-sync-branch
description: Use when a current local Git branch needs an upstream synchronization assessment or explicitly requested fetch and fast-forward synchronization.
---

# Synchronize One Branch

Refresh one selected remote-branch observation and fast-forward only the current local branch. Preserve divergence and actual partial effects; no merge commit, rebase or publication is implied.

## Resolve scope and permission

Require the selected installation's `git-working-directory-policy` and `git-safety-check`, with their exact discovered identifiers/ownership. Missing or foreign dependencies are unavailable; ambiguous ownership needs a choice. Never read a runtime root catalog, install or imitate a dependency.

Use explicit language preference, request language, then English. Preserve identifiers/statuses.

Default `inspect` is local/cached evidence only: no network, fetch or dry-run. Explicit `observe` permits only advertisement queries. An explicit sync request authorizes one scoped fetch and eligible fast-forward, not push or config changes. Skill names, plans and ready preflight do not authorize writes. Reuse existing authorization; ask only for material unresolved scope/effects.

Resolve one repository, current named committed branch, remote, remote branch and single effective fetch endpoint. Prefer an explicit selection, otherwise one unambiguous upstream. Do not guess origin, choose among URLs, use pushurl for fetching, create/switch branches or weaken a stricter request.

Read [synchronization.md](references/synchronization.md) before inspection/execution; its protected-read, transport, hook/filter and freshness gates are mandatory.

## Execute the scoped flow

1. Obtain metadata-only context, then inspect helper effects before worktree scans or safety reads. For writes require fresh clean/committed/named-branch preflight; its internal publish intent does not grant push permission.
2. Inspect effective endpoints, ref mapping, hooks and helpers. Refresh source/index/config/operation guards before each mutation. Unknown or unapproved effects block; never bypass hooks or signing.
3. Fetch exactly one branch into one approved remote-tracking ref with the reference's tag/prune/refmap/submodule/maintenance restrictions. Record actual object/ref effects, including after a failed command.
4. Pin the fetched commit and establish ancestry. Equal or local-ahead needs no branch movement. Divergent/unrelated history needs a decision; unknown ancestry stays limited. Do not infer ancestry from counts or stale refs.
5. For a verified behind branch, refresh guards and fast-forward that pinned commit only. Verify exact HEAD, expected index/worktree/tree and permitted ref/metadata transitions. Stop on failure or unexpected changes; preserve state, without stash/reset/cleanup/retry.

## Return

Report `outcome`, mode/authorization, scope/redacted endpoint, before/fetched/after OIDs, relation, preflight/effect evidence, command results, changed refs, remaining decisions and limitations. Outcomes are `planned`, `observed`, `synced`, `no_op`, `needs_decision`, `limited`, `blocked`, `stopped`, `partial` or `uncertain`.

`no_op` means no local branch advance; disclose fetch writes separately. `synced` requires verified fast-forward. A snapshot is not perpetual remote freshness. Supplied transcripts are reported evidence, never claimed live execution. Create no auxiliary files or external posts.
