# Scoped Publication Reference

## Selected installation and request

Use the actual owned identifiers for publication/context/safety, with context+safety as the complete three-skill standalone closure. No entry, sync skill, commit builder or hosting-service API is required. Missing or foreign dependencies are unavailable, not invitations to manual imitation or installation; unresolved duplicate ownership needs one choice. Installed execution never reads root catalog or docs.

Resolve language from explicit preference, request language, then English. `inspect` is offline/cached assessment only, not a server-freshness check. `observe` needs explicit remote observation and permits only a selected advertisement. `publish` needs an explicit push request and covers one normal branch publication and bounded verification queries. No fetch, commit creation, branch switch/creation, PR, promotion or release follows from that permission. A ready preflight, plan, skill name or earlier sync grants no publication authorization.

Select the current named branch with existing full commit OID. Detached/unborn or another local source branch needs a branch strategy outside this contract. Clean index/worktree and no conflicts/active operation are required before writes. Missing commit identity alone does not block publication; network authentication is separate. Do not change identity, credentials, remotes, URLs, keys, login or global settings to proceed.

Use one explicit configured remote and full destination refs/heads ref. Otherwise require one unambiguous existing upstream with agreeing push routing. Inspect branch.pushRemote, remote.pushDefault, upstream and configured mappings; conflicting implicit choices need a decision. Explicit one-ref intent may override broad defaults through exact command operands; it does not approve mirror or unrequested push options. Do not guess origin, primary branch or a fork.

## Effective endpoint and protected effects

Use `remote get-url --push --all <remote>` as effective push endpoint evidence, separately from fetch URL inspection. Account for pushurl and URL rewrites rather than manually guessing their precedence. Require exactly one known SSH/scp-like, HTTPS, local or file endpoint; multiple URLs or unknown custom protocols/helpers/overrides block dependent execution. Keep raw comparison data in memory and redact credential userinfo, tokens/query values and secret helper output in receipts. Normal trusted transport/authentication can run within the requested operation; new authentication/configuration setup is separate. Server processing belongs to the selected push but is not evidence of deployment/release.

Use profile-free shells, explicit workdir and literal argument arrays. Git 2.45+ local inspection uses:

```text
git --no-pager --no-optional-locks --no-lazy-fetch --no-replace-objects
    -c core.fsmonitor=false -c maintenance.auto=false -c gc.auto=0
    -c log.showSignature=false
```

The display is an argument sequence, not an unescaped shell snippet. Unsupported controls block; do not drop them. Content queries disable external diff/textconv, colors/notes and signature display. Validate full ref names and OIDs, use supported end-of-options separators, and never evaluate names/messages/outputs as shell code. Preserve and inspect environment overrides rather than silently clearing them.

Obtain metadata/config before optional worktree scans. Inspect applicable clean/process filters/helpers before status/worktree diff/safety reads; unknown side effects block those reads. Then use the owned safety skill's publish preflight for fresh local gates. Before mutation recheck source branch/HEAD, index/content, operation markers, selected endpoint/config/mappings and effects. Observed guards are not locks.

Inspect effective/default hooksPath, active pre-push and reference-transaction hooks plus referenced helpers before pushing: an accepted remote update can be followed by a local tracking-ref transaction. Include signing, transport/credential commands and known required checks. Known bounded approved effects may run with disclosure; unknown/destructive/additional effects block. Do not bypass hooks/signing, use --no-verify or install tooling to force success. Inaccessible server-hook source alone is not a new approval gate.

Resolve configured mirror mode, push options (including effective list clearing), follow-tags, submodule publication, automatic setup and local fetch mappings. Reject configured mirror/unapproved options/custom commands or multiple/unsafe opportunistic tracking destinations before network mutation. One expected tracking update may occur under a safe mapping; preserve other local heads/tags/config. Symbolic pointers are compared by target, not their derived OIDs.

## Observe and publish exactly one ref

Under explicit observation/publication permission query only the selected branch at the selected effective **push** endpoint, for example with the safe prefix and:

```text
ls-remote --refs --exit-code -- <effective-push-endpoint> refs/heads/<destination>
```

Resolve the query operand through inspected effective transport/URL rewriting and verify it reaches the same endpoint as the push. A named remote in ls-remote normally selects its fetch URL; use it only when that endpoint is proven equal. Distinct fetch/push URLs must never cause before/after publication observations to query the fetch server. Unknown or unqueryable push-endpoint routing blocks verification rather than substituting the fetch endpoint.

Parse exact full ref/OID, status and complete output. Exit 2 is absence only after a successful selected-server query; connection/auth/other errors are not an absent branch. Multiple/malformed/truncated results remain unresolved. Cache or a supplied transcript is not a live advertisement.

For an existing remote OID, verify local object availability with no lazy fetch, then establish complete relevant ancestry. Missing target object requires a fetch/sync decision; never fetch silently. Unknown/shallow/missing evidence cannot prove fast-forward. Non-fast-forward is blocked. Equal means branch no_op without push; separately requested upstream setup may still follow verified equality. An explicit publication to a named branch may create it or update it normally; it does not create a remote repository.

A strict create-only or exact-old-OID condition is not an ordinary push promise. If the available normal transport cannot enforce it atomically, stop for a supported strategy instead of adding lease-force or silently weakening it. Server/concurrent ref state is mutable; do not advertise preflight observations as atomic locks.

After fresh guards, use only the pinned full source OID and one full branch destination:

```text
-c push.autoSetupRemote=false push --porcelain --no-follow-tags
   --recurse-submodules=no -- <remote> <source-full-OID>:refs/heads/<destination>
```

Apply the protected prefix and literal operands. Explicit refspec prevents matching/default push expansion; no-follow-tags and submodule=no suppress those automatic publications. autoSetupRemote=false is command-local and avoids implicit config writes. No force/lease-force, mirror, deletion, all/tags, push options, --no-verify or automatic retries. Respect required signing and known approved pre-push behavior. Do not use push dry-run as an offline inspection: it contacts the endpoint and may invoke helpers/hooks.

Capture the actual exit/stdout/stderr during that one attempt. Verify selected target through a separate bounded advertisement covered by publish permission. Confirm exact remote OID, same source HEAD/index/worktree/config and only expected tracking-ref effects. Do not rerun push to recover output. A nonzero exit may still have effects; unavailable acknowledgment or verification yields uncertainty. An unexpected new tip, config/ref/source change or partial effect stops downstream work without rollback/reset/cleanup/force. If the remote advances after the snapshot, disclose the actual observations instead of claiming current-tip equality.

## Explicit upstream setup

Only an explicit request permits repository-local `branch.<current>.remote` and `branch.<current>.merge` changes. Verify publication/equality, recheck the source/endpoint and inspect old effective values/origins. Conflicting command/worktree/include overrides that would prevent the requested local values from becoming effective need a decision before config writes; do not change another scope silently.

When permitted, set exactly:

```text
config --local --replace-all branch.<current>.remote <selected-remote>
config --local --replace-all branch.<current>.merge refs/heads/<destination>
```

Pass keys/values as separate arguments, verify both local and effective values/origins, and preserve every other key and global file. A pinned-OID push with -u is not evidence that a named local branch's tracking was configured. Do not use -u as that assumption. Already equal remote state satisfies the verified publication prerequisite for explicitly requested setup; no unnecessary push is run. Report configuration effects separately from branch no_op.

If one key fails after the other or source changes after push, preserve the successful push/actual key state and report partial; do not restore automatically or claim complete setup. Without explicit setup permission, config stays unchanged.

## Receipt and limits

Return outcome, requested mode/exact authorization, root/current branch/pinned source, selected remote/ref/redacted endpoint, remote-before/after OIDs, relation/effect checks, actual push exit and sanitized output, post-query/protected-state results, optional upstream results and remaining decisions/limits.

`planned` is offline; `observed` advertisement-only. `published` requires verified remote/local postconditions. `no_op` is an already equal branch and does not hide separately authorized config effects. `needs_decision` resolves ambiguity/strategy; `limited` means insufficient evidence; `blocked` unavailable safe operation; `stopped` stopped attempt; `partial` known effects with unfinished work; `uncertain` an unestablished outcome. Failed output is not proof of no mutation. Supplied transcripts remain reported, never claimed personal/live execution. Create no cache, receipt file or external post by default.
