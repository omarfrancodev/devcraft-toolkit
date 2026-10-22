# Devcraft Toolkit

A modular toolkit of composable skills for repository context, read-only Git preflight, and standalone Conventional Commit message drafting. Compatibility is recorded only for harnesses actually exercised.

The distribution currently includes four available skills: `using-devcraft-toolkit`, `git-working-directory-policy`, `git-safety-check`, and `conventional-commits-style`. Commit coordination, publication coordination, and activity reporting are planned capabilities, not usable skills in this distribution. CCR integration is outside the current scope.

Skill definitions and default templates use English. User-facing content follows an explicit language preference or the language of the user's request, defaulting to English when neither can be determined. Tests are maintained outside individual skill directories, grouped by the owning skill and then by test scope; repository infrastructure and cross-skill coverage have separate shared groups.

The [catalog](catalog.json) records all seventeen target capabilities and marks each as `available` or `planned`. See [installation](docs/installation.md), [architecture](docs/architecture.md), [language behavior](docs/language.md), and [compatibility evidence](docs/compatibility.md).

The [capability roadmap](docs/roadmap.md) links the self-contained designs and plans for upcoming increments.
