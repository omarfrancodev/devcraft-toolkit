# Scoped Synchronization Reference

## Scope, ownership and modes

Require installed context+safety from the selected package or explicitly selected standalone closure. Invoke actual discovered identifiers without prefix guessing. No hosting connector, commit builder, validation or progress skill is required. Missing skills are distinct from missing execution tools; neither permits imitation or installation.

`inspect` is a local proposal using cached observations, not a remote-freshness check. Do not run fetch, ls-remote, pull or networked dry-run to complete it. `observe` requires an explicit remote-observation request and may advertise only the selected branch. `sync` requires an explicit synchronization request and covers its single fetch plus eligible fast-forward and verification. A plain skill invocation, preflight or proposed next step is not permission. A user-selected stricter scope remains binding.

Select the current named branch with an existing commit, exact remote name and full `refs/heads/...` remote branch. Use an explicit request, otherwise a single configured upstream. No upstream or conflicting/multiple endpoint/mapping evidence needs a decision; do not assume origin or a primary branch. Detached/unborn or a different local branch cannot be repaired through checkout/creation. Explicit remote-branch overrides do not change upstream configuration.

Inspect effective `remote get-url --all <remote>` fetch URLs, rewriting and relevant invocation overrides before network. Fetch and push endpoints differ: pushurl is not a fetch source. Require one supported known SSH/scp-like, HTTPS, local or file endpoint. Unknown custom protocols/helpers or unverifiable overrides block. Do not print credential-bearing URL components, token/query values or secret helper output. Keep comparison data in memory and redact presentation.

Normal trusted transport/authentication can run within the selected network request; new login/key/token/credential or remote setup is separate. Known server processing belongs to the selected operation and is not proof of deployment. Do not demand inaccessible server-hook source or change authentication to force a connection.

## Protected reads and preconditions

Use a profile-free shell, explicit working directory and separate literal arguments. Local reads use this Git 2.45+ prefix:

```text
git --no-pager --no-optional-locks --no-lazy-fetch --no-replace-objects
    -c core.fsmonitor=false -c maintenance.auto=false -c gc.auto=0
    -c log.showSignature=false
```

This is an argument sequence, not shell code to paste across unescaped lines. Unsupported controls block; do not remove them. Content queries disable external diff/textconv, notes/colors and signature display. Preserve user environment overrides rather than silently clearing them; account for their effects. Do not evaluate untrusted names/content as commands.

First obtain root/Git/common directories, branch/HEAD and configuration without optional status scans. Inspect clean/process filters and applicable attributes before status, worktree diff or safety reads that could execute them. Unknown helper effects block those reads; metadata-only findings may still be returned as limited. Then invoke the owned safety skill's publish preflight for its local clean/committed/named-branch gate, retaining `operation=sync` and separate authorization. Missing commit identity alone does not block this operation; no new commit is created.

Before each write require clean index/worktree, no conflicts/merge/rebase/other active operation and the same branch, HEAD, selected refs, endpoint/config and effect guards. A prior ready result is not a lock. Inspect effective core.hooksPath/default hooks and referenced helpers: reference-transaction before fetch/ref writes; post-index-change and post-merge before fast-forward; attributes/checkout filters in current and target trees; required signature verification and transport commands as applicable. Sample/disabled hooks are not active. Known approved bounded effects may run with expected changes disclosed; unknown/out-of-contract effects block before mutation. Never bypass hooks, signing or required checks.

## Fetch exactly one observation

Resolve one concrete source branch and one tracking destination beneath `refs/remotes/<remote>/...`. Reject multiple destinations, local-head/tag mappings and unresolved custom upstream mappings. Before fetch inspect the selected destination itself with protected `symbolic-ref --quiet --no-recurse -- <tracking-ref>` (or equivalent direct-ref metadata). Exit 0 means symbolic: stop before fetch, even if its printed pointer would remain unchanged; fetch dereferences it and could move an unrelated branch. Distinguish confirmed direct/absent state from query errors. Require a direct or absent destination and refresh that guard immediately before writing. Do not delete/replace a symbolic ref to proceed. Comparing unrelated symbolic aliases by pointer does not permit a symbolic write destination.

Use the explicit refspec with empty refmap so configured fetch mappings cannot widen it:

```text
fetch --no-tags --no-prune --no-prune-tags --no-recurse-submodules
      --no-write-fetch-head --no-auto-maintenance --no-write-commit-graph
      --refmap= -- <remote> refs/heads/<branch>:refs/remotes/<remote>/<branch>
```

Apply the protected prefix and safe argument transport. No force marker, all-remotes, tags, pruning, recursive submodules, deepen/unshallow, side refs or implicit config writes. Necessary fetched objects/packs and selected tracking-ref/reflog updates are expected; preserve other refs/configuration, FETCH_HEAD, local HEAD/index and working content. Tracking refresh may reflect a rewritten remote, but does not authorize local history rewriting. Guard actual symbolic pointers rather than mistaking their derived object values for independent ref writes.

Capture exit/stdout/stderr once and inspect actual state. A failed fetch may have written objects or a ref; report those effects, not an assumed rollback. Do not repeat a mutating command to recover its output.

## Decide and fast-forward

Resolve the fetched tracking value as a full commit OID. Recheck local guards after fetch; observed own transitions are reconciled explicitly. `merge-base --is-ancestor` provides relation evidence, with errors distinct from false and incomplete/shallow/missing data disclosed:

| Evidence | Action |
| --- | --- |
| Local equals fetched | No branch movement; disclose any fetch effects |
| Fetched ancestor of local | Local ahead; no reset or automatic push |
| Local ancestor of fetched | Eligible pinned fast-forward after fresh gates |
| Neither with complete evidence | Diverged/unrelated: needs_decision, preserve fetch effects |
| Relation not established | limited/blocked, no inferred fast-forward |

Use only:

```text
merge --ff-only --no-overwrite-ignore --no-autostash --no-squash --no-edit --no-stat <fetched-full-OID>
```

`--no-overwrite-ignore` is mandatory: a clean status omits ignored files and does not permit overwriting them when the target newly tracks their paths. A collision stops the fast-forward with original bytes/HEAD/index preserved; disclose earlier fetch and any merge metadata effects as partial, without deleting/moving the ignored content or retrying.

No pull default, stash, reset, merge commit, rebase or branch switch. Respect required verification and known approved helpers rather than disabling them. Before checkout inspect target attributes/helper effects, not only the old tree's settings.

Afterward verify exact HEAD equals the fetched OID, index/expected target tree and working content agree under inspected filters, config and unrelated refs are unchanged, and ORIG_HEAD/reflog/index metadata match expected own changes. Remote tip movement does not change the pinned operation silently; report the observed snapshot and any freshness limit. Stop and preserve actual state on changed guards, failure or unexplained effects. No rollback, cleanup or automatic retry.

## Receipt

Return outcome/mode/authorization, repository/current branch, exact selected ref and redacted endpoint, before/fetched/after OIDs and relation, preflight/effect checks, actual command exits and sanitized output, expected/observed ref/metadata changes, remaining state and limitations.

`planned` is offline proposal; `observed` is authorized advertisement evidence. `synced` requires verified FF. `no_op` describes no branch advance and must still disclose fetch/object/tracking writes. `needs_decision` covers unresolved scope/divergence; `limited` insufficient evidence; `blocked` unavailable safe operation; `stopped` a stopped attempt; `partial` known earlier effects with unfinished work; `uncertain` unestablished effects. Do not claim complete absence or no mutation from missing output. Supplied transcripts stay identified as reported evidence. No receipt file/cache/post is created by default.

Example: L and R diverge after a successful scoped fetch. Keep local L, record tracking R and fetched objects, and stop for a decision. The earlier successful fetch is not authorization for rebase, merge or publication.
