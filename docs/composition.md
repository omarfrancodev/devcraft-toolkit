# Skill composition

The toolkit entry routes requests to skills that are actually installed in the active harness. Its repository `catalog.json` is a maintained development inventory, not a runtime loader, installer, permission source, or dependency resolver.

## Foundation group

The available foundation group contains `using-devcraft-toolkit`, `git-working-directory-policy`, and `git-safety-check`. The entry requires both supporting skills; `git-safety-check` requires `git-working-directory-policy`. A standalone installation must include that dependency closure and select the skills explicitly. No tested plugin installation is claimed.

## Optional standalone capabilities

`conventional-commits-style` has no required skill dependencies. Install it by itself to draft or review message text, or install it alongside the entry for optional routing. The entry does not require the formatter. When the formatter is installed, the entry routes message drafting and review to it. When it is absent, the entry reports that limitation without imitation or automatic installation.

Message formatting returns a proposal from supplied facts and conventions. It needs no repository context and does not invoke Git preflight or create a commit. Request a separate repository safety check only when repository state or readiness for a Git operation is part of the request.

`todo-workflow-controller` is also standalone with no required skill dependencies. The entry routes progress-control requests to it when installed; the capability is not part of the entry's hard dependency closure. When it is absent, the entry reports that limit rather than imitating the capability. A missing native progress tool is handled by the installed skill's documented inline fallback. Progress tracking preserves state and gates but does not execute workflow steps or grant permission for side effects; a step named `publish` does not request Git publication or a Git preflight.

`natural-language-report-writer` is a standalone capability for turning supplied facts into activity reports, progress updates, or summaries. The entry routes matching requests to it when installed and reports it unavailable when absent. Direct use needs no repository context; local output still requires a user-selected destination.

## Data flow and boundaries

`git-working-directory-policy` discovers and reports context for the user-selected repository. `git-safety-check` refreshes volatile Git state and evaluates only the requested read-only intent. The entry composes those results without repeating stable discovery, while refreshing branch, HEAD, index, conflict, identity, and working-tree facts when they could have changed.

The preflight result `ready` is not authorization to perform a Git write. Missing tools do not grant new capabilities. Unanswered material decisions remain unresolved until the user answers.

Git commit creation and coordination, publication coordination, and the `git-activity-report` coordinator remain planned in this distribution. Do not replace those workflows with manual imitation. Evidence-based report writing from supplied facts is a separate available capability when installed; it does not inspect Git history.
