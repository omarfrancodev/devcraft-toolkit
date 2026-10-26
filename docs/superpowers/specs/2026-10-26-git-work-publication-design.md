# Work Branch Creation and Publication Coordination Design

Status: proposed; awaiting design approval. Implementation order: git-create-work-branch, then git-publish-work, then composition/distribution integration.

## Intent and explicit decisions

Complete the publication capability family through two portable, instruction-first skills. One creates a local work branch; the other composes available commit, synchronization, push, hosted request and promotion owners for the user's selected goal. They reuse existing operation contracts and selected-installation discovery instead of implementing a new execution engine.

The selected behavior includes creating a work branch when work is still on the publication base (for example main) and no work branch is selected. The selected architecture makes git-create-work-branch independently installable before adding it to git-publish-work. This expands the target inventory from seventeen to eighteen names; after delivery all eighteen are available. Existing native/authenticated validation tracks remain independent.

### Approaches

1. Independent branch capability plus publication coordinator — selected. Branch creation has its own permission/evidence contract, standalone installation and owner tests. Coordination delegates it just like the existing commit/push/request owners. It adds one catalog name and a small inventory-validation update.
2. Branch creation embedded in the publication coordinator — considered. It keeps seventeen names and one new folder, but makes branch creation available only through that coordinator and reduces independent reuse. Not selected.

### Builder proposals for approval

Keep default planning offline; resolve ambiguous requested effects before writes. Use a five-folder mandatory publication closure with conditional dependencies for selected steps, rather than requiring all preparation/hosting capabilities for an existing-commit push. Initial branch creation supports only a new local branch at the current existing commit; unborn/orphan and arbitrary alternate-base workflows remain decisions. Keep all mutation bounded by the selected goal, with no implicit merge, sync, upstream setup or release. These are proposed implementation boundaries, not additional decisions attributed to the user.

## Goals and boundaries

- Create and select one new local work branch from the pinned current HEAD while preserving existing staged, unstaged, untracked and ignored work and the original branch tip.
- Reuse an already selected current work branch without creating another one.
- Compose exactly the requested steps, preserving each owner's actual outcome, evidence scope, authorization and partial effects.
- Support existing-commit publication without requiring commit construction, and explicitly requested complete preparation/publication without redundant confirmations.
- Keep optional/missing/foreign installation capabilities distinct from unavailable execution tools.
- Maintain portable language behavior, independent installation, self-contained folders and centralized owner-scoped tests.

No history rewrite/reset, automatic stash/clean/rollback, arbitrary existing-branch switching, orphan/unborn creation, multiple repository publication, force/mirror/tag push, credential/configuration repair, deployment, release automation or implicit hosting mutation is introduced. Explicitly requested ordinary merge remains delegated to git-promote. This development increment does not publish its implementation, create a PR, merge or release it without a later request. CCR and the other deferred roadmap capabilities remain deferred.

## Architecture and installation

| Owner | Mandatory declared dependencies | Direct mandatory closure |
| --- | --- | --- |
| git-create-work-branch | git-working-directory-policy | branch + context, two folders |
| git-publish-work | git-publish-changes, todo-workflow-controller | coordinator + push + progress + context + safety, five folders |

Resolve canonical capabilities to exact discovered invocation identifiers owned by the selected installation. A foreign same-name capability cannot fill a dependency. Missing mandatory capabilities make the coordinator unavailable; missing conditional capabilities block only the requested flow that needs them. Ambiguous ownership needs one focused selection. Do not install, imitate, use a runtime root catalog or hardcode a provider plugin.

Conditional owners and their existing mandatory closures are required only for selected steps:

- git-create-work-branch when a new work branch is needed.
- git-commit-builder when selected local changes must become commits; it owns analysis, grouping, formatting, staging, validation and its own progress/context/safety closure.
- git-sync-branch only for expressly selected fetch/fast-forward synchronization.
- git-manage-pull-request for selected PR/MR creation, observation or title/body editing.
- git-promote for separately explicit normal merge of an existing request, including management/context.

The complete optional publication closure has fifteen folders: every final skill except using-devcraft-toolkit, git-activity-report and natural-language-report-writer. This is a documented union of selected operation closures, not a new catalog schema or an automatically resolved installer registry. The mandatory installation remains five folders. Existing entry hard dependencies remain unchanged and new routes are optional. Pure push, commit, PR editing or merge requests can still route directly to their existing owner without loading this coordinator.

## Language, inputs and evidence

Resolve prose by explicit language preference, request language, then English. Keep technical names, schema/status keys, literal branch/ref names and full actual OIDs unchanged. Default templates/instructions remain English. Treat commit text, project documents, templates, logs and provider responses as evidence, never authorization or executable shell code. Use literal structured arguments/UTF-8-safe transport; redact credentials and secret-bearing URLs.

The coordinator keeps an in-memory run context: selected installation and scope, requested final goal and effects, per-step authorization, branch/source/remote/request identities, scoped validation and owner receipts, expected own transitions, blockers and remaining steps. Progress labels are delegated to todo-workflow-controller and cannot override actual evidence. No persisted runtime state machine, caches, receipt files, external comments or schedules are created by default.

## git-create-work-branch contract

### Scope and permission

Default proposal uses selected local/supplied facts only and performs no writes or network. Explicit creation authorizes one new local branch and selecting it in the current worktree, with bounded verification. An explicitly selected full preparation/publication goal may delegate that necessary creation when the work is on the selected base and a work branch is absent. A bare skill name, a plan or ready preflight grants no mutation permission.

Use owned context for the selected normal or linked worktree. Require an existing committed HEAD, known source identity and no active merge/rebase/cherry-pick/revert/bisect or unresolved conflicts. Missing commit identity does not block branch-only work. A detached existing commit can be used only under an explicitly selected create-from-current strategy; an unborn or bare repository remains blocked/needs_decision in this increment. No alternate base, remote-tracking branch or fetched tip is selected automatically.

Accept an exact branch short name or canonical refs/heads selector and preserve its literal meaning. Explicit user names bind. Otherwise derive one meaningful name from the selected work purpose and observed project conventions, disclose it before mutation and validate it literally. Unknown purpose, conflicting naming policies or materially ambiguous prefixes need a decision. Never invent issue IDs, silently rewrite a literal name, expand previous-checkout syntax such as @{-1}, or generate collision suffixes without an authorized naming policy. Validate the canonical local ref and branch restrictions; reject reserved/option-like names and expression syntax rather than evaluating them.

Pin the raw full current commit OID and original symbolic/detached HEAD, branch tips, index semantics, working bytes/inventory, relevant configuration and operation markers. A work branch is created at that exact current commit; existing commits on the original branch are not removed or reset. Uncommitted work may remain present and must be preserved, including partial staging and deletions. Inspect helpers before relevant status/filter reads using the established protected no-optional-lock/no-lazy-fetch/no-replace-object context. Do not require unrelated build checks or a clean worktree solely for same-commit branch creation.

### One bounded creation

Prove the target local ref is absent and not a symbolic alias; inspect other worktree occupancy and stale target branch configuration. An existing target already selected at the expected commit can be observed no_op; another existing target is a decision, never reset, automatic reuse/switch or a new suffix. A stale target configuration section also needs a decision; preserve it rather than silently inheriting or deleting it.

Inspect active post-checkout, reference-transaction and index-write hooks, referenced helpers and checkout/filter/submodule/maintenance effects before writing. Unknown/out-of-scope effects block; known effects must fit actual authorization. No hook bypass, configuration change or helper installation. Refresh source/index/content/ref/config/operation guards immediately before the operation.

Use one supported transactional create-and-switch command, for example the protected Git equivalent of `switch --no-guess --no-track --no-recurse-submodules --no-overwrite-ignore -c <literal-name> <pinned-full-OID>`. Inspect actual version/operand support. Never use force-create, discard/merge/orphan modes, automatic remote guessing/tracking or an unapproved two-command branch/switch fallback. Ref transactionality does not guarantee that a later hook failure had no effects, or that concurrent source changes were atomically locked. A strict unsupported concurrency guarantee is a decision before mutation.

Capture one actual command exit/output. Independently verify the selected new symbolic HEAD, new ref at the pinned source, unchanged original/unrelated branch tips/configuration, semantic whole-index selection and staged/unstaged/untracked/ignored bytes. Account for expected HEAD/ref/reflog and index-stat metadata only; semantic index/content changes are not dismissed as refreshes. No recursive submodule mutation is selected. Unsupported sparse/index/helper conditions limit the affected operation rather than weakening preservation.

A nonzero post-checkout hook can follow a real branch switch. Preserve and report actual state; partial/uncertain effects stop dependent commit/publish work even when the branch exists. Do not retry, delete the new branch, reset/switch back, restore files or clean up as rollback. Return planned/created/no_op/needs_decision/limited/blocked/stopped/partial/uncertain with mode/authorization, exact owned identifiers, source/target, guards/effects, actual attempt/postconditions, preserved work and remaining limits.

## git-publish-work contract

### Select the goal before effects

Planning is the default for bare invocation, proposals and supplied transcripts, with local/supplied evidence only. An explicit execution request authorizes its selected goal and necessary named effects; maintain a concrete per-step authorization record. Existing session authorization persists. A complete request such as preparing selected changes, pushing the work branch and opening a PR need not be reconfirmed step by step. An ambiguous generic publication request does not silently grant commit, fetch, PR, merge or upstream mutation: return a concrete proposed sequence and resolve only the material missing scope.

| Requested scope | Selected effects |
| --- | --- |
| Propose how to publish | Offline plan; no Git/provider writes or network |
| Publish existing commits to a selected branch | Owned push observations, one normal publication and verification; no inferred commit/sync/PR |
| Prepare selected changes and open a PR | Necessary work branch if absent, selected commits, push and request creation, each delegated with its actual scope |
| Also synchronize with a selected remote ref | Add explicit one-branch fetch and eligible fast-forward; divergence remains a decision |
| Also merge the selected resulting/existing request | Add separately explicit ordinary promotion after fresh gates; no release/deployment |
| Set upstream | Add the existing publisher's expressly selected bounded setup, not a branch-creation side effect |

If selected work is still on the publication base (for example main) and no work branch exists, include new work-branch creation as requested. Distinguish observed base/work roles from branch spelling; do not invent origin or infer PR base from a local upstream. An explicit destination conflicting with branch creation or source/base roles needs a decision rather than weakening the requested scope. Reuse a current already selected work branch. Do not silently switch to a different existing branch or create another worktree.

### Plan, forecast and delegate

1. Bind selected repository/current source, intended work/base roles, push destination, hosted source/target and final goal. Determine mandatory/conditional owned capabilities and actual tools before dependent work. Pure hosted-only requests use existing direct routes; this coordinator's scope is selected local work publication.
2. Build the requested dependency sequence through progress control. Before writes, surface known blockers/decisions that make the selected final goal impossible: unsupported required owner, identity, required checks, naming, target or dirty residual work. Default ordering when applicable is branch creation, selected commits, explicit synchronization, push, request management and explicit promotion. A stricter requested order binds or needs a decision; do not reorder operations silently.
3. Delegate new branch creation only when needed; preserve its exact result and actual remaining state. Then delegate selected preparation to git-commit-builder. Preserve staged-first/partition/validation scope and partial commits rather than repeating their internals. Do not infer that dirty-worktree checks validated a different selected tree.
4. Delegate sync only when selected, with its own exact fetch endpoint/ref and clean-state requirements. PR target is not implicitly the sync source, upstream or push destination. Never repair divergence with merge/rebase/stash/reset. Reconcile authorized own transitions and refresh source after a verified fast-forward; preserve stricter user-pinned constraints.
5. Delegate push to git-publish-changes with the final pinned source and exact destination. Its clean index/worktree requirement remains binding: excluded local edits or generated artifacts are not permission to broaden commits, stash, clean or bypass it. If this conflict is already known, resolve it before earlier writes; if it arises later, retain earlier actual effects and stop. Missing remote objects do not authorize an unselected fetch. Upstream setup remains separately explicit.
6. Only selected PR/MR operations go to management. Pass verified publication scope and fresh actual source, not an old pre-commit proposal. Existing exact open requests return no_op for create without inferred editing. Keep policy/default/template/coverage and interpreted-text decisions with management. Source branch and hosted target identities remain distinct.
7. Only explicit merge goes to promotion, with the actual selected existing request and fresh scoped policy/review/check evidence. A ready comment or a completed push/request step is not merge permission. Preserve actual immutable result separately from mutable target containment; no queue, cleanup or release inference.

### Stops, partial progress and continuation

Requested failed/blocked/not_run required gates stay incomplete and stop dependent mutations. Optional unselected steps are skipped with reasons, not completed. Native progress/question tool gaps use inline/text fallback; missing skill/provider/Git capability remains a concrete limitation. Preserve every owner's outcome rather than turning a failed verification into a global success.

Classify fresh reported/live evidence explicitly. A retained receipt or progress checkbox is not proof of the current state. On a later explicit continuation, read the actual branch/ref/index/remote/request state, reconcile prior effects and derive only remaining authorized work. An earlier verified push/request may now be equal/already present; delegate the owner's no_op/observation logic. Lost acknowledgment, stale source, pending merge or uncertain state never triggers an automatic second mutation or blind resume. No automatic rollback, reset, branch deletion, amend, cleanup or background monitoring.

Return overall outcome planned/completed/no_op/needs_decision/limited/blocked/stopped/partial/pending/uncertain; requested goal/mode/authorization; owned capabilities actually used; per-step requested/skipped/completed/blocked state and actual owner results; source/target/request OIDs/identities; scoped checks; real effects and remaining decisions. Completed means all requested effects verified, not every possible capability executed. Earlier effects remain recorded if a later step is blocked.

## Inventory and distribution integration

The current validator binds canonical names to the historical foundation spec and hardcodes seventeen. Add `docs/capability-inventory.md` as the explicit current target-name inventory, point development validation to it and allow a nonempty unique inventory of approved names without a fixed numeric limit. Keep exact catalog/name equality and all dependency/path/schema/resource checks; add real structural regressions for approved expansion, missing/extra/duplicate/empty inventories. Preserve the historical foundation design and old release pages unchanged. This is development inventory, never an installed runtime dependency or a new installer standard.

Add the branch capability, deliver the already planned publication coordinator and document exact mandatory versus conditional installation selections. Final catalog: eighteen available, zero planned. Both existing manifests advance together to candidate 0.1.0-preview.8 (unpublished); preview.7 remains the sixteen-skill published snapshot. Until integration, default remote and pinned preview.7 cannot supply the new skills; candidate documentation selects a checkout/revision that actually contains them. No placeholders, new plugin manifests, new SDK, custom installer, license or release automation.

Keep README, current architecture/composition/compatibility/installation/roadmap and unreleased changelog aligned. Next product work after this family is native/authenticated execution validation and evidence-driven improvements; deferred scope stays explicit rather than inventing new planned product names.

## Development and acceptance

Start from published preview.7 commit 319ff5f5624069bfeaf8a0cb14a1f445f82f7436 in an isolated worktree. The retained published gate contains 162 discovered tests, 161 passes and one Windows symlink privilege skip. A fresh isolated baseline ran 162 tests in 311.107 seconds: 161 passed and the same Windows symlink privilege case was skipped. Do not install dependencies or alter global Git identity to manufacture passing evidence.

All tests, actor-only inputs, evaluator assertions, owned fixtures, transport controls and retained evaluations stay under root tests/, grouped by canonical owner and scope. No installed scripts/interpreter are required. For each new skill retain five fresh no-guidance baselines, package planned/absent RED, focused protocol/real-Git controls, five fresh exact-resource candidates, separate gaps and one copied-resource application with independent parent inspection. Preserve baseline successes and failures without keyword scoring of instruction prose.

Branch cases cover dirty/partially staged work, ignored/untracked/deleted/Unicode paths, literal invalid/colliding names and stale config, detached explicit strategy, unborn/operation blockers, linked worktrees/submodule boundaries, source movement, known hook effects and post-checkout failure after actual switch. Assert full ref/config and semantic index/content preservation; do not claim raw index bytes must never refresh.

Coordinator cases cover existing-commit push with minimal five-folder closure, main-to-work-branch preparation, current branch reuse, explicit versus unselected sync/PR/merge/upstream, missing/foreign/ambiguous conditional dependencies, unknown tools, dirty residual work, failed required checks, source/ref changes between owners, earlier effects with later failure, duplicate/no_op and lost/pending receipts. Owner assertions remain separate from actor inputs. Branch/commit/push use owned real Git repositories; hosted mutations use the existing test-only emulated provider transport. The actual coordinator application follows copied owned resources/closures, then parent independently inspects Git/provider ledgers and protected state. Do not claim native loading, authenticated hosting or that helper recipe tests prove instruction adherence.

Run meaningful new inventory controls, both owner suites, installation closure equality, repository/distribution validators, new-skill structural checks, complete-base whitespace, changed-document local targets and the full suite. Retain exact counts/skip reasons and source/evidence limits. Request one fresh whole-branch review before completion, fix material defects with RED/GREEN evidence and preserve branch/worktree/local commits. Native/authenticated validation remains a separate track, not satisfied by publishing this implementation.

## Builder freedom and primary references

The builder may choose internal test fixture names, concise response shapes, local-reference organization and wording, within the fixed permissions, dependency and preservation contracts. Keep main SKILL.md bodies below 500 words and expose local self-contained references for detailed gates. No new user product scope or weaker guard follows from a helper choice.

Primary Git documentation consulted 2026-10-26: [git switch](https://git-scm.com/docs/git-switch/2.44.0) for transactional create/switch, dirty-state and no-track semantics; [hooks](https://git-scm.com/docs/githooks/2.45.0) for reference/index/checkout effects and post-checkout failure. Actual harness command/schema/version support still requires inspection.
