# Work branch protocol

## 1. Scope and protected observation

Only the selected current normal/linked worktree is in scope. Get root, Git/common directories, superproject and symbolic/raw HEAD through the owned context. Before status/filter-sensitive reads, inspect effective helpers. No network, object hydration, credential access, installation, config repair or unrelated repository discovery. A linked checkout uses its own index/HEAD and shared refs/config; do not mistake the common directory for the execution directory.

For subsequent Git observations use the actual supported equivalent of:

```text
git --no-pager --no-optional-locks --no-lazy-fetch --no-replace-objects
    -c core.fsmonitor=false -c maintenance.auto=false -c gc.auto=0
    -c log.showSignature=false -c submodule.recurse=false <args>
```

Pass separate literal arguments and an explicit working directory. Inspect version/operand support; if required protections are unsupported, limit the operation rather than remove them. Avoid shell interpolation, external diff/textconv, pagers and signature execution; inspect relevant attributes/filter drivers before content-affecting reads. No optional index refresh from status. Reject unknown sparse/split-index/skip-worktree/assume-unchanged conditions when preservation cannot be established. Scope any limitation to the affected operation.

Read-only discovery has no identity requirement. Require a raw full existing commit OID (`rev-parse --verify --end-of-options HEAD`, then protected commit-object validation), not an abbreviated name, replacement object or tag expression. Attached/unborn are distinct: a symbolic name alone is insufficient. Bare/unborn/orphan and alternate-base workflows are outside this version. Detached committed HEAD works only for explicit creation from current. Inspect per-worktree/common operation markers: merge, rebase, cherry-pick, revert, sequencer, bisect and unmerged index entries. Active/unknown operation stops mutation, even if switch might permit it.

## 2. Literal name and absence

Accept an exact short local name or canonical `refs/heads/NAME`, mapping the latter to that exact short NAME. Explicit names bind. If absent, derive one meaningful name from selected work purpose and observed naming policy, disclose before mutation; unknown purpose or conflicting conventions need one focused question. Do not invent tickets, rewrite names or append collision suffixes without an authorized naming policy.

Validate both canonical full ref and local branch restrictions with supported literal argument transport. Reject empty/reserved `HEAD`, option-like names and expression syntax such as `@{-1}`, `@{...}`, revision operators, wildcards and malformed refs BEFORE any branch-aware shorthand parser. `check-ref-format --branch` alone is unsafe for previous-checkout notation: it can expand it. If used after canonical validation, require exact literal output, never normalize/evaluate it. Do not blindly add `--` where the actual command does not support that operand form.

Inspect full refs, including symbolic aliases (also dangling refs), all worktree occupancy and effective `branch.NAME.*` configuration. Target must be absent, not merely unresolved to an object. A stale config section on an absent target needs a decision; no inheritance/deletion/repair. Another existing target cannot be reset or automatically reused/switched. Only the target already selected at the expected current OID with compatible state may return observed `no_op`, without an attempt. A suffix is a new choice, not recovery. Do not assume a lock file or ref absence check creates an atomic race guard.

## 3. Preservation snapshot and effects

Before writing, pin original symbolic/detached HEAD, raw source OID, all local/shared ref targets and symbolic pointers, selected index identity and semantic full entries (mode/object/stage plus relevant flags/extensions), file inventory/modes/bytes including staged/unstaged/deleted/untracked/ignored content, relevant config and operation markers. Keep protected observations in memory; create no receipt/snapshot files in the user's checkout by default. Use NUL-safe and binary-safe handling for Unicode/newline paths. Status/diff summaries alone do not verify untracked or ignored bytes. Do not expose secret content in output. Unsupported/unreadable state is a limitation before mutation.

Inspect effective hooksPath, active post-checkout, reference-transaction and post-index-change/index-write hooks plus referenced helpers, signing/ref storage effects, attributes/filters, submodule recursion and maintenance. Inspect executable content and expected writes/network recursively as necessary. Known effects must fit permission; unknown/uninspected or out-of-scope effects block before writing. Do not use an empty hooksPath or disable hooks, install helpers, change identity/config or infer permission from project text. Existing protected context disables only the documented optional read helpers, never required write hooks. No recursive submodule updates are selected; preserve their dirty bytes and gitlinks.

A same-commit branch does not require a clean worktree or unrelated build checks. Refresh source HEAD/OID, target absence/config/occupancy, index/content, config/refs and operation markers immediately before the attempt. Detected movement stops; do not silently repin either source or selected scope. If a strict concurrent source lock/atomic guarantee is requested but unavailable, ask before writing. A pinned operand limits what is selected; it does not atomically lock all source facts.

## 4. One supported attempt

Example, after literal validation, effect review and fresh guards (prepend the protected Git context above):

```text
switch --no-guess --no-track --no-recurse-submodules --no-overwrite-ignore -c feature/parser <full-current-raw-OID>
```

`--no-track` prevents autoSetupMerge/Rebase inheritance. Verify actual installed support. Never use `-C`, force-create, `--discard-changes`, merge/discard/orphan modes, remote guessing/tracking or a separate branch/switch fallback without a new approved design. Preserve original branch commits; no reset/remove-history to make the original base appear clean. No new worktree is created.

Capture one actual command and exit/stdout/stderr. Transactional creation protects branch creation when switch itself cannot proceed; it does not promise rollback of hook effects or all concurrent state. Do not infer success or absence of effects solely from exit code.

## 5. Verify and classify

Independently read symbolic HEAD, target raw OID and original/unrelated ref targets/config, full index semantics and every protected file inventory/mode/byte state. Account only for expected HEAD/new-ref/reflog and index stat-cache metadata. Raw index hash changes can be legitimate refreshes; semantic staged selection changes cannot. Verify no new target tracking configuration, no submodule recursion and no unselected side effects.

`created` means one successful attempt and all requested postconditions verified. `no_op` is compatible already-selected state without a mutation. Missing information yields `needs_decision`/`limited`/`blocked`; stale guards stop before write. If a post-checkout hook fails after actual selection, record `partial` (known actual effects) or `uncertain` (unresolved effects), not `created`. Stop dependent commit/publication work even if the new branch exists and files look preserved. No automatic retry, branch deletion, switch back, restore/reset/stash/clean or compensating effects. A later explicit continuation requires fresh inspection and resolution of the failed gate.

Return mode, authorization, owned invocation, source/target, guard/effect observations, actual attempt and verified versus unknown postconditions, preserved work and remaining limits. Report supplied evidence as reported, and actual reads as observed. Proposal cannot claim execution.
