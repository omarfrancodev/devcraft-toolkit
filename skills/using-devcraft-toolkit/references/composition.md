# Composition reference

The entry routes only after checking the user's requested scope and the skills actually installed in the active harness. The maintained repository `catalog.json` describes this source tree; it is not copied into every individual skill installation and does not install dependencies.

## Discovery and ownership

Keep a small in-memory mapping from canonical capability to the selected installation's discovered invocation identifier and ownership evidence. Harness metadata or explicit user selection establishes the installation; spelling alone does not. A discovered identifier such as `devcraft-toolkit:conventional-commits-style` is an example, not a universal namespace convention.

Use the harness-provided identifier exactly. Plugin ownership must match the active entry's installation; an explicitly selected standalone set uses its own discovered identifiers. A same-named skill from a foreign or unselected installation does not fill a missing optional capability. Do not read root manifests or a development catalog to guess runtime ownership.

If multiple copies cannot be disambiguated from actual discovery or the user's selection, ask one focused question before dependent routing. Do not change, remove or reinstall copies to resolve the ambiguity. Skill-local references remain relative to the invoked skill folder; qualified invocation names do not rewrite resource paths.

## Available dependency group

The foundation group is:

- `using-devcraft-toolkit`
- `git-working-directory-policy`
- `git-safety-check`

The entry depends on both supporting skills. `git-safety-check` depends on `git-working-directory-policy`. A standalone installation needs the declared dependency closure and must select each skill explicitly in its harness.

## Optional standalone capabilities

`conventional-commits-style` has no required skill dependencies. Install it separately to use directly, or alongside the entry for optional routing. The entry does not require it; when it is installed, the entry routes commit-message drafting or review to that skill. When absent, the entry reports the missing capability without imitation or automatic installation.

`todo-workflow-controller` has no required skill dependencies. Install it by itself for multi-step progress tracking, or alongside the entry for optional routing. The entry does not require it. When installed, route progress-control requests to it. When absent, report the missing capability without manually imitating it or installing it. The standalone skill can use inline status when a native progress tool is unavailable; a missing tool does not mean the skill itself is unavailable.

Progress tracking preserves workflow state; it does not execute tracked steps, create files or schedules as a fallback, or grant permission for side effects. A step named `publish` does not by itself request Git publication or a Git preflight.

`natural-language-report-writer` has no required skill dependencies. Install it alone for evidence-based activity reports, progress updates, or summaries from supplied facts, or alongside the entry for optional routing. The entry does not require it. When installed, route supplied-facts report requests to it; when absent, report the missing capability without drafting the report, imitating the skill, or installing it automatically. It returns content in the conversation by default; writing a local report requires an explicitly selected destination.

`validation-discovery` has no required skill dependencies. Install it alone for project-check discovery and explicitly requested local validation, or alongside the entry for optional routing. The entry does not require it. When installed, route matching requests to it and let its evidence-based rules select applicable commands; do not impose a fixed command-name allowlist or run an unrelated Git preflight. Its default discovery mode does not execute commands. When absent, report the capability as unavailable without imitation or automatic installation.

## Result boundaries

`git-working-directory-policy` returns observed repository context. `git-safety-check` consumes or refreshes that context and returns an intent-specific read-only preflight. Reuse the context when it remains current; refresh branch, HEAD, index, conflicts, working-tree state, and identity before conclusions that depend on them.

The preflight outcomes `ready`, `no_op`, `blocked`, `needs_decision`, and `limited` keep their technical labels. `ready` is only the requested preflight conclusion; it does not authorize a commit, publish, merge, or release.

`conventional-commits-style` uses supplied facts and conventions to return a message proposal. It needs no repository or Git preflight and performs no Git operation. Preserve its resolved language and its clarification decisions when composing the response.

Publication coordination remains planned in this distribution; do not imitate it or substitute another capability. History-derived reporting uses the available optional `git-activity-report` coordinator with its owned context/writer closure. The standalone writer still handles supplied-facts reports without inspecting Git history.

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

## Local-history reporting

`git-activity-report` requires only `git-working-directory-policy` and `natural-language-report-writer`; its direct standalone closure has three skills and needs neither entry nor safety preflight. Resolve those owned discovered identifiers before dependent execution. The entry itself retains its existing foundation requirements and adds no hard dependency on reporting.

The coordinator pins one local revision, resolves period/timezone, author/committer basis, exact author selection and merge policy, then inspects a bounded graph and delegates evidence to the writer. It preserves `status`, `scope`, `coverage`, `commits`, `report`, and `output`, including missing/partial source limits. `reported` and `no_op` are complete local snapshot results; `limited` never proves no matching history. Supplied-fact drafts must remain identified as supplied facts, not verified local queries.

The writer controls prose language/format and an explicitly selected report destination, replacement permission and readback. Installation, a routing decision or a content-only request grants no filesystem/Git/network mutation. A missing or foreign writer/context makes the dependent coordinator unavailable; an ambiguous copy needs a focused choice. No runtime root catalog read, automatic installation or fallback imitation is allowed. Pure supplied-fact reports continue directly to the writer.
