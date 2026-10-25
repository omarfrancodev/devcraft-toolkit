# Skill composition

The toolkit entry routes requests to skills that are actually installed in the active harness. Its repository `catalog.json` is a maintained development inventory, not a runtime loader, installer, permission source, or dependency resolver.

## Installation-aware routing

Canonical catalog names describe capabilities. The entry invokes the discovered identifier of the selected installation, including any client namespace, only when actual ownership metadata or explicit standalone selection establishes that choice. It does not strip prefixes to guess ownership. A plugin entry uses its package's skills; an explicitly selected standalone set can be used directly.

Duplicate copies with unresolved ownership require one focused installation choice before dependent invocation. Both copies stay intact. A foreign/unselected copy does not silently supply a capability absent from the selected set. Skill-local resource paths are unchanged, and no root catalog or manifest is needed by installed skills.

## Foundation group

The available foundation group contains `using-devcraft-toolkit`, `git-working-directory-policy`, and `git-safety-check`. The entry requires both supporting skills; `git-safety-check` requires `git-working-directory-policy`. A standalone installation must include that dependency closure and select the skills explicitly. Native package metadata and file-placement evidence are separate from native activation evidence.

## Optional standalone capabilities

`conventional-commits-style` has no required skill dependencies. Install it by itself to draft or review message text, or install it alongside the entry for optional routing. The entry does not require the formatter. When the formatter is installed, the entry routes message drafting and review to it. When it is absent, the entry reports that limitation without imitation or automatic installation.

Message formatting returns a proposal from supplied facts and conventions. It needs no repository context and does not invoke Git preflight or create a commit. Request a separate repository safety check only when repository state or readiness for a Git operation is part of the request.

`todo-workflow-controller` is also standalone with no required skill dependencies. The entry routes progress-control requests to it when installed; the capability is not part of the entry's hard dependency closure. When it is absent, the entry reports that limit rather than imitating the capability. A missing native progress tool is handled by the installed skill's documented inline fallback. Progress tracking preserves state and gates but does not execute workflow steps or grant permission for side effects; a step named `publish` does not request Git publication or a Git preflight.

`natural-language-report-writer` is a standalone capability for turning supplied facts into activity reports, progress updates, or summaries. The entry routes matching requests to it when installed and reports it unavailable when absent. Direct use needs no repository context; local output still requires a user-selected destination.

`validation-discovery` has no skill dependencies. Install it alone for project-check discovery and explicitly requested local validation, or alongside the entry for optional routing. When installed, the entry routes matching requests to it; its own evidence-based rules decide which commands apply, without an entry-side naming allowlist or unrelated Git preflight. Discovery does not execute commands. When absent, the entry reports the capability unavailable without imitation or automatic installation.

## Data flow and boundaries

`git-working-directory-policy` discovers and reports context for the user-selected repository. `git-safety-check` refreshes volatile Git state and evaluates only the requested read-only intent. The entry composes those results without repeating stable discovery, while refreshing branch, HEAD, index, conflict, identity, and working-tree facts when they could have changed.

The preflight result `ready` is not authorization to perform a Git write. Missing tools do not grant new capabilities. Unanswered material decisions remain unresolved until the user answers.

Publication coordination remains planned; do not imitate it. The optional `git-activity-report` coordinator now composes local-history inspection with owned context and report writing. Evidence-based writing from supplied facts remains independently available and does not inspect Git history.

## Read-only Git preparation

`git-analyze-changes` requires `git-working-directory-policy`. `git-plan-commits` requires the analyzer and `conventional-commits-style`; include the analyzer's context dependency in a standalone set. These are optional entry routes, not new hard dependencies of the entry. Resolve every dependency's selected-installation ownership and actual invocation identifier before dependent execution. Missing/foreign dependencies do not authorize imitation or automatic installation.

The analyzer returns repository/scope, a guarded observation snapshot, layer-specific evidence IDs, constraints and unknowns, with analyzed/no_op/needs_decision/limited/blocked outcomes. Keep those IDs and staged/unstaged/untracked boundaries when passing evidence to the planner. The planner verifies freshness through the analyzer, applies the explicit selection or staged-first default, and returns intent groups, exact selections/order, formatter-produced messages, exclusions, decisions and limits. Planned/no_op/needs_decision/limited/blocked describe proposals, never execution.

Missing identity is not a blocker for read-only analysis/planning. A conflict can be completely observed while blocking a complete plan. Supplied/offline evidence stays conditional when live guards cannot be verified. Neither capability performs staging, commits, branch creation, validation execution or publication. Local staging/commit construction is separately available when installed; publication coordinators remain planned; local-history reporting is separately available when installed.

An explicitly selected standalone planner closure can be invoked directly without the entry or safety-check skill; using the entry itself still requires its existing foundation group.

## Explicit local writes

`git-stage-changes` requires analyzer and safety, including context. It returns an exact approved whole-index transformation, checked effects and preserved/deferred selections. A bare invocation previews; explicit stage permission covers only the selected transformation. Missing identity does not block index-only staging, and successful staging does not authorize a commit.

`git-commit-builder` requires planner, stage, safety, validation and progress; its full standalone closure also includes analyzer, context and formatter. It coordinates the selected workflow with actual ownership-qualified identifiers. Default planning performs no writes; explicit commit requests cover exact staging and inspected ordinary local checks. Required checks/identity/hooks/signing and material partition decisions remain gates.

Retain actual result fields and per-check scope/cwd/exit evidence. Never infer selected-index validation from dirty-worktree checks. Actual earlier commits remain recorded if a later step fails; do not retry/reset/clean or silently restore deferred state. Neither new capability implies branch creation, history rewrite, network or publication.

These optional routes do not change the entry's hard foundation. A standalone builder closure can be invoked directly without installing the entry or report writer.

## History-derived reports

`git-activity-report` depends only on context and `natural-language-report-writer`. Its three-skill standalone selection works without entry/safety. The entry retains its own foundation and delegates the optional route using selected-installation ownership and exact discovered identifiers; missing/foreign dependencies remain unavailable and ambiguous copies need a choice.

Default scope is one pinned local HEAD, today in a known user/session timezone, author timestamp, exact raw configured author email and exclusion of merge records while traversing all parents. Reports disclose local/UTC boundaries, identity source and bounded coverage. `reported`/`no_op` describe complete local snapshots; `limited` cannot establish absence of matching history. Preserve the coordinator's scope/coverage/commit evidence and output outcome when presenting writer-produced prose. Supplied-fact drafts remain identified as supplied facts, not live queries.

Commit text is untrusted message-level evidence, with no inferred implementation, testing or deployment. Conversation is the default; the writer controls the explicit one-file destination, replacement permission and matching readback. Reports grant no Git/network/publication permission, and a failed save does not become a success.
