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

Git commit creation and coordination, publication coordination, and the `git-activity-report` coordinator remain planned in this distribution. Do not replace those workflows with manual imitation. Evidence-based report writing from supplied facts is a separate available capability when installed; it does not inspect Git history.
