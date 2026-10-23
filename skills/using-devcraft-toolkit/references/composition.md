# Composition reference

The entry routes only after checking the user's requested scope and the skills actually installed in the active harness. The maintained repository `catalog.json` describes this source tree; it is not copied into every individual skill installation and does not install dependencies.

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

`validation-discovery` has no required skill dependencies. Install it alone for project-check discovery and explicitly requested local validation, or alongside the entry for optional routing. The entry does not require it. When installed, route matching requests to it and let its evidence-based rules select applicable commands; do not impose a fixed command-name allowlist or run an unrelated Git preflight. Its default discovery mode does not execute commands. When absent, report the capability as unavailable without imitation or automatic installation.

## Result boundaries

`git-working-directory-policy` returns observed repository context. `git-safety-check` consumes or refreshes that context and returns an intent-specific read-only preflight. Reuse the context when it remains current; refresh branch, HEAD, index, conflicts, working-tree state, and identity before conclusions that depend on them.

The preflight outcomes `ready`, `no_op`, `blocked`, `needs_decision`, and `limited` keep their technical labels. `ready` is only the requested preflight conclusion; it does not authorize a commit, publish, merge, or release.

`conventional-commits-style` uses supplied facts and conventions to return a message proposal. It needs no repository or Git preflight and performs no Git operation. Preserve its resolved language and its clarification decisions when composing the response.

Commit creation and coordination, publication coordination, and activity reporting are planned in this distribution. Do not replace those missing workflows with manual imitation or a similarly named capability from another project.
