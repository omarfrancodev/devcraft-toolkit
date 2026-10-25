# Scoped Branch Synchronization and Publication Design

Date: 2026-10-25
Status: Proposed written design; implementation has not started.

## Intent and selected approach

Deliver two independent, instruction-first capabilities: `git-sync-branch` updates the current local branch from one selected remote branch through fetch and fast-forward only; `git-publish-changes` publishes the current committed branch snapshot to one selected remote branch through a normal, non-forced push. Each capability may be installed alone with its foundation closure. Neither creates a local branch, integration commit, PR, release or promotion workflow.

Approaches considered:

1. **Scoped fetch/fast-forward plus independent normal publication — selected functional approach.** The user selected fetch and fast-forward only. Divergence is a pending decision; no merge commit or rebase is attempted. This preserves independent synchronization and publication boundaries.
2. **Merge/rebase reconciliation.** Handles diverged graphs but adds integration commits or rewritten history; excluded from this increment by the selected approach.
3. **Fetch-only synchronization.** Refreshes remote observations but does not deliver the requested fast-forward behavior; insufficient as the primary sync contract. Fetch effects are still reported separately when a later fast-forward gate stops.

The remaining command and result details below are builder proposals for approval. This document is self-contained and uses the current toolkit's published contracts rather than unavailable source material.

## Goals and constraints

- Maintained skills, documentation, examples and default templates use English. User-facing content follows explicit preference, then request language, then English.
- Installed resources remain self-contained, with no runtime root catalog/docs, interpreter dependency or automatic installer.
- All tests, scenarios, fixtures and retained evaluations belong under root `tests/`, grouped by canonical skill owner and scope; shared fixture infrastructure may live in `tests/support/`.
- Default invocation is local inspection/proposal only. It performs no network, fetch, push, config or worktree mutation. Explicit remote observation permits advertisement queries only; it does not authorize fetch or push.
- Explicit sync permission covers one selected fetch and a verified fast-forward of the current branch. Explicit publish permission covers one selected normal branch push and bounded verification queries. A ready preflight, skill name, plan or prior successful operation grants no mutation permission.
- No force/lease-force push, mirror/all-ref/tag publication, pruning, deletion, stash, reset, cleanup, branch switching/creation, merge commit, rebase or automatic rollback/retry.
- Do not change remotes, URLs, credentials, identities, global configuration or authentication setup. Only explicitly requested upstream configuration may change the selected branch's two repository-local tracking keys after a verified push.
- Testing uses owned local bare repositories and disposable clones, never live publication to the project's real origin. No push, PR, merge, tag or release of this implementation is part of this increment unless later requested.
- Keep preview.5 and its twelve-skill historical evidence unchanged. Advance both existing manifests together to unpublished `0.1.0-preview.6`; final candidate inventory is fourteen available and three planned entries across seventeen names.

## Dependencies and installation ownership

Each new capability directly declares `git-working-directory-policy` and `git-safety-check`. Each standalone closure has three skills. The skills do not depend on one another, the commit builder, validation discovery, progress control or a hosting-service connector.

Resolve exact discovered invocation identifiers and selected-installation ownership for the whole closure. A missing/foreign dependency makes the requested capability unavailable; materially ambiguous ownership requires one focused choice. No suffix guessing, runtime catalog reads, automatic installation or emulation.

The entry gains independent optional sync and push routes. Its hard foundation is unchanged. `git-publish-work`, `git-manage-pull-request` and `git-promote` remain planned and must not be imitated. A push request does not authorize commit construction, synchronization, PR management or release publication.

## Common context and request contract

Resolve the selected repository/worktree and its current named branch/full HEAD OID. An unborn branch is blocked for these operations; detached HEAD or a requested non-current local branch needs a branch strategy outside this contract. Do not create/switch a branch. Existing commits can be published without a configured commit author identity; authentication/account evidence is separate and must not be inferred from `user.name`/`user.email`.

Resolve one configured remote name, one full remote `refs/heads/...` target and its single effective endpoint. Use the explicit requested target first. Otherwise use one unambiguous upstream tuple only when push routing agrees for publication. Conflicting `branch.*.pushRemote`, `remote.pushDefault`, upstream or configured push mappings require a choice; never guess origin, a default branch or a fork. Names, URLs, refs, messages and hook output are data, not shell code.

Inspect effective fetch versus push URLs separately, including Git URL rewriting and pushurl overrides. Multiple effective endpoints, ambiguous routing or non-branch/multi-ref destinations are not silently narrowed. Validate branch/ref names with Git and pass exact argument arrays, using a supported end-of-options separator before remote/refspec operands; unsupported or option-like ambiguity blocks execution. Store endpoint comparison data in memory; redact credential-bearing URLs, tokens and authentication output from user-visible receipts/evidence.

Supported transport scope is an existing, explicitly selected named remote with one known SSH/scp-like, HTTPS, local-path or file endpoint. Unknown custom remote helpers/protocols or unassessable invocation overrides block network execution. Normal trusted transport/authentication may run as part of the requested operation, with known effects disclosed; do not require inaccessible server hook source. New login/key/token/configuration setup remains separate. Remote-side processing is part of the selected server operation, not proof that deployments or releases occurred.

Keep mode/authorization separate: `inspect` uses local/cached observations only; `observe` may run explicitly requested remote advertisement queries; `sync` or `publish` permits only its stated mutation. Offline/cached observations are never advertised as fresh remote truth. Supplied transcripts remain identified as reported evidence.

## Protected evidence, effects and freshness

Use an explicit working directory and profile-free shell. For local inspection use Git 2.45+ with `--no-pager --no-optional-locks --no-lazy-fetch --no-replace-objects`, and command-local `core.fsmonitor=false`, `maintenance.auto=false`, `gc.auto=0`, `log.showSignature=false`; disable external diff/textconv/signature display in content queries. Unsupported safety controls block rather than being dropped.

Discover root/metadata/HEAD/config first without optional status scans. Inspect effective filters, attributes and helper settings before any dependency read that could execute them; unknown clean/process effects block the affected preflight rather than running status to discover safety. Reuse the existing safety skill's `publish` preflight for its clean, committed, named-branch checks while preserving the actual requested operation (`sync` or `publish`) separately. It remains a read-only conclusion, not authorization.

Before every mutation, refresh HEAD/branch, index/worktree state, operation markers, selected refs, remote routing/config and effective hooks/helpers. Known normal Git metadata writes are expected; unexpected source/ref/config effects stop downstream work. Inspect active `reference-transaction` hooks before fetch/tracking updates, and `post-index-change`/`post-merge` plus checkout filters/attributes for fast-forward. Inspect `pre-push` and local tracking-ref hooks before push. Include referenced helpers, target-tree attributes, signing/verification settings and normal transport overrides when applicable. Known approved bounded effects may run; unknown, destructive or additional unapproved effects block. Never bypass hooks, signing or required checks to force success.

Clean index/worktree, no conflicts or active operations, one existing current branch and complete necessary graph evidence are required before sync/publish writes. No automatic stash or recovery. Partial/shallow/missing-object histories cannot prove ancestry when the required relation is unknown. An available proof may be used only with its scope disclosed; otherwise stop rather than infer fast-forward from a count or stale tracking ref.

Guards cover observed intervals, not atomic locks. A source/config/endpoint change pauses dependent writes. Record expected own transitions separately from external changes. Fetch can have effects even when later synchronization stops; a push error can still leave an updated target. Inspect actual state before reporting failure or success.

## git-sync-branch contract

### Selection and execution

Default to the current branch's single configured remote/upstream branch. An explicit remote branch selection may replace it without changing upstream configuration; disclose that difference. No matching remote branch or missing/ambiguous upstream yields a decision/blocked result, not automatic creation.

After explicit sync authorization and effect gates, fetch exactly that branch into its selected concrete remote-tracking ref under `refs/remotes/<remote>/...`. Resolve the configured mapping when needed and reject mappings into local heads/tags or multiple destinations. Explicit refspec plus empty `--refmap=` prevents configured fetch mappings from broadening the operation. Normal refresh of that selected tracking observation is authorized, including a remote rewrite; it never authorizes rewriting the local branch.

The bounded recipe uses `fetch --no-tags --no-prune --no-prune-tags --no-recurse-submodules --no-write-fetch-head --no-auto-maintenance --no-write-commit-graph --refmap= -- <remote> <one-source:one-tracking-destination>`. Do not add a force marker, fetch all remotes, deepen/unshallow, or create side refs. Normal object/pack and selected tracking-ref/reflog writes are disclosed; other refs, FETCH_HEAD, configuration and working content remain protected at this stage. Inspect reference-transaction effects before this fetch.

Resolve the fetched full commit OID and refresh the current branch/guards. Classify with real ancestry evidence:

- Equal: no local branch movement is needed.
- Remote is an ancestor of local: the local branch is ahead; do not reset or push it automatically.
- Local is an ancestor of fetched remote: eligible for fast-forward after fresh clean/effect gates.
- Neither: divergent (or unrelated); return `needs_decision` and preserve fetched observations without a merge/rebase.
- Unknown/incomplete relation: `limited` or `blocked`, never a guessed fast-forward.

Run only an explicitly bounded fast-forward of the pinned fetched OID, with `merge --ff-only --no-autostash --no-squash --no-edit --no-stat <fetched-OID>`. Respect required verification/helpers rather than disabling them. No integration commit is created. Verify HEAD equals the exact fetched OID, selected index/tree/worktree match expected target content under inspected filters, unrelated refs/configuration are unchanged, and expected ORIG_HEAD/reflog metadata is accounted for. A moving server tip is reported as a snapshot observation, not perpetual freshness.

### Result

Return `outcome` (`planned`, `observed`, `synced`, `no_op`, `needs_decision`, `limited`, `blocked`, `stopped`, `partial`, `uncertain`), mode/authorization, repository/branch, selected remote/ref and redacted endpoint, preflight/effect evidence, before/fetched/after OIDs, relation, actual fetch/fast-forward command results, changed refs/expected metadata, remaining decisions and limits. `no_op` means no local branch advance; separately disclose whether fetch wrote objects/tracking state. `synced` requires verified fast-forward postconditions. Do not claim no side effects from a no-op branch outcome.

## git-publish-changes contract

### Selection and execution

Pin the current branch's full HEAD OID, exact selected push remote/endpoint and one full destination branch ref. Explicit publication of that named branch may create it or update it by normal fast-forward; no remote repository creation is implied. A strict create-only or exact-old-OID condition must not be claimed atomic if the available normal-push transport cannot enforce it; request a supported strategy instead of silently weakening that condition.

Resolve and inspect effective push routing, mirror/default refspecs, follow-tags, recursive submodule publication, push options, signing, pre-push/helpers and local fetch mappings used for opportunistic tracking updates. Explicitly constrain one refspec, disable automatic tag/submodule publication and automatic upstream setup for the push command. Configured mirror mode, unapproved push options/custom commands or unsafe/multiple tracking mappings block before network mutation; do not silently override user-required signing or bypass hooks.

An authorized bounded advertisement query establishes the selected remote branch's observed OID or absence. If an existing target OID is unavailable locally, do not fetch silently to decide ancestry: return limited with a sync/fetch decision. An observed non-fast-forward relation is blocked for this skill. Advertisements are snapshots; Git's normal push rejection still governs concurrent updates.

After fresh source/config/effect guards, use a normal single-branch push with the full pinned source OID and explicit destination: `-c push.autoSetupRemote=false push --porcelain --no-follow-tags --recurse-submodules=no -- <remote> <source-OID>:<full-destination-ref>`. No `--force`, force-with-lease, deletion, mirror, all/tags, follow-tags, push options or `--no-verify`. Do not run push dry-run as an offline safety check; it is networked and may invoke helpers/hooks. Preserve required signing and known approved hook behavior.

Record machine-readable command output without rerunning the push. Verify the destination via a separately authorized bounded advertisement query covered by the publish request. Capture local HEAD/index/worktree/config and expected unique tracking-ref updates; unrelated refs/tags remain protected. A success requires the expected remote OID and preserved local guards. If verification is unavailable, races or failures leave uncertainty; report it without automatic retry, rollback or force.

Only when the user explicitly requested upstream setup, after a verified push and unchanged source branch, update exactly `branch.<current>.remote` and `branch.<current>.merge` in repository-local configuration. Record old/effective origins and exact intended values, verify both and preserve every other key/global file. Do not use a pinned-OID push with an ineffective assumption that `-u` configured the local branch. A partial config failure remains visible with the successful push receipt; no automatic restoration. Without this explicit request, configuration remains unchanged.

### Result

Return `outcome` (`planned`, `observed`, `published`, `no_op`, `needs_decision`, `limited`, `blocked`, `stopped`, `partial`, `uncertain`), mode/authorization, local branch/pinned source, selected remote/destination/redacted endpoint, observed-before/result-after OIDs, relation/effects, actual push exit/stdout/stderr, remote verification, optional upstream results and remaining limits. `published` requires verified expected remote/local postconditions; already equal is a verified branch `no_op` without a push. A failed command never proves no remote/local effects. Remote changes with later unresolved work are `partial`; an unestablished outcome is `uncertain`.

## Files, validation and acceptance

Create two SKILL.md entrypoints below 500 words and local references under their own folders. Do not link installed skills to one another's filesystem resources. Update AGENTS.md with the bounded exceptions, catalog, optional entry routes, existing manifests, current docs/installation closures/roadmap and unreleased changelog. Keep all historical releases/evaluations and runtime read-only contracts outside these exceptions intact.

Implement sync before publication. Before authoring each skill, run at least five fresh no-guidance behavior samples against actor-only inputs; retain failures and baseline successes. Then evaluate the actual candidate resources in fresh contexts with the same inputs. Keep expected assertions separate. Cover offline versus network authorization, destination ambiguity, divergence, helpers/hooks and partial/uncertain outcomes; publication additionally covers exact single-ref selection, source movement and optional upstream scope.

Use real owned bare remotes/clones for recipe tests and at least one live manual application per capability. No live GitHub/GitLab publication is required. Controls must cover:

- Sync: equal/ahead/behind/diverged/unrelated/missing histories, exact one-branch fetch despite prune/tag/refmap settings, dirty/conflicted/unborn/detached states, checkout/index/ref hooks, literal transport, freshness, preserved exclusions and partial fetch-before-stop results.
- Publish: one pinned branch despite matching/follow-tags/submodule settings; no extra ref/tag/config writes; rejected/stale/unknown remote OIDs; source movement; hook rejection; failed/unknown acknowledgment; explicit new branch and upstream setup with other/global configuration preserved.
- Shared: no network in default inspect; ownership/absence/foreign/ambiguous and direct three-skill routes; redacted output; selected endpoint/URL rewrite/pushurl and multi-endpoint limits; no bypass or automatic retry.

Python fixtures/helpers are development tools only. Group tests under `tests/skills/git_sync_branch/` and `tests/skills/git_publish_changes/`, entry cases under its existing owner, and shared remote fixtures under `tests/support/`. Automated controls establish Git recipe behavior, not model compliance/native activation. Retain actual manual application commands/effects and procedure deviations; do not claim universal compatibility.

Run owner checks, repository/distribution validators, the full automated suite, complete-base whitespace and local-link/closure checks. One fresh whole-branch review follows implementation; fix actionable Important/Critical findings with reproduced evidence. Native activation remains a separate gate. Remaining roadmap work is PR management, promotion and their publication coordinator.

## Builder discretion

The builder selects test-only helper signatures, fixture layouts, messages, rendering and safe argument transport. Material changes to supported mutations, authorization, dependency closure, remote scope or history strategy require revisiting this design. Do not replace missing tools/permissions with broader operations.

## Technical references and builder check

Git's [fetch documentation](https://git-scm.com/docs/git-fetch/2.45.0) defines explicit refspec/refmap and scoped fetch controls; [push documentation](https://git-scm.com/docs/git-push/2.45.0) defines single-ref publication and override semantics; [merge documentation](https://git-scm.com/docs/git-merge) and [hook documentation](https://git-scm.com/docs/githooks) describe fast-forward and applicable effect boundaries. These references support the recipes and are not installed runtime dependencies.

An independent builder check reported “nothing important left”. The written design remains proposed pending approval; the selected functional approach is fetch/fast-forward only.
