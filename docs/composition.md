# Skill composition

The toolkit entry routes requests to skills that are actually installed in the active harness. Its repository `catalog.json` is a maintained development inventory, not a runtime loader, installer, permission source, or dependency resolver.

## Foundation group

The available foundation group contains `using-devcraft-toolkit`, `git-working-directory-policy`, and `git-safety-check`. The entry requires both supporting skills; `git-safety-check` requires `git-working-directory-policy`. A standalone installation must include that dependency closure and select the skills explicitly. No tested plugin installation is claimed.

## Optional standalone capability

`conventional-commits-style` has no required skill dependencies. Install it by itself to draft or review message text, or install it alongside the entry for optional routing. The entry does not require the formatter. When the formatter is installed, the entry routes message drafting and review to it. When it is absent, the entry reports that limitation without imitation or automatic installation.

Message formatting returns a proposal from supplied facts and conventions. It needs no repository context and does not invoke Git preflight or create a commit. Request a separate repository safety check only when repository state or readiness for a Git operation is part of the request.

## Data flow and boundaries

`git-working-directory-policy` discovers and reports context for the user-selected repository. `git-safety-check` refreshes volatile Git state and evaluates only the requested read-only intent. The entry composes those results without repeating stable discovery, while refreshing branch, HEAD, index, conflict, identity, and working-tree facts when they could have changed.

The preflight result `ready` is not authorization to perform a Git write. Missing tools do not grant new capabilities. Unanswered material decisions remain unresolved until the user answers.

Commit creation and coordination, publication coordination, and activity reporting remain planned capabilities in this distribution. Report their absence honestly; do not emulate them or claim they ran.
