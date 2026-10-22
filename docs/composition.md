# Skill composition

The toolkit entry routes requests to skills that are actually installed in the active harness. Its repository `catalog.json` is a maintained development inventory, not a runtime loader, installer, permission source, or dependency resolver.

## Foundation group

The available foundation group contains `using-devcraft-toolkit`, `git-working-directory-policy`, and `git-safety-check`. The entry requires both supporting skills; `git-safety-check` requires `git-working-directory-policy`. A standalone installation must include that dependency closure and select the skills explicitly. No tested plugin installation is claimed.

## Data flow and boundaries

`git-working-directory-policy` discovers and reports context for the user-selected repository. `git-safety-check` refreshes volatile Git state and evaluates only the requested read-only intent. The entry composes those results without repeating stable discovery, while refreshing branch, HEAD, index, conflict, identity, and working-tree facts when they could have changed.

The preflight result `ready` is not authorization to perform a Git write. Missing tools do not grant new capabilities. Unanswered material decisions remain unresolved until the user answers.

Commit coordination, publication coordination, and activity reporting remain planned capabilities in this distribution. Report their absence honestly; do not emulate them or claim they ran.
