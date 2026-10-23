# Devcraft Toolkit

A modular toolkit of composable skills for repository context, read-only Git preflight, project validation discovery, standalone Conventional Commit drafting, and portable progress tracking. Compatibility is recorded only for harnesses actually exercised.

The distribution currently includes seven available skills: `using-devcraft-toolkit`, `git-working-directory-policy`, `git-safety-check`, `conventional-commits-style`, `todo-workflow-controller`, `natural-language-report-writer`, and `validation-discovery`. Git commit coordination, publication coordination, and the Git activity-report coordinator remain planned capabilities, not usable skills in this distribution. CCR integration is outside the current scope.

Skill definitions and default templates use English. User-facing content follows an explicit language preference or the language of the user's request, defaulting to English when neither can be determined. Tests are maintained outside individual skill directories, grouped by the owning skill and then by test scope; repository infrastructure and cross-skill coverage have separate shared groups.

The [catalog](catalog.json) records all seventeen target capabilities and marks each as `available` or `planned`. Seven are available and ten remain planned. See [installation](docs/installation.md), [architecture](docs/architecture.md), [language behavior](docs/language.md), and [compatibility evidence](docs/compatibility.md).

The [capability roadmap](docs/roadmap.md) links the self-contained designs and plans for upcoming increments.

## Preview release

[v0.1.0-preview.1](https://github.com/omarfrancodev/devcraft-toolkit/releases/tag/v0.1.0-preview.1) is the first experimental distribution. See the [changelog](CHANGELOG.md) and [installation guide](docs/installation.md) for its scope and installation steps. Native skill loading and compatibility with other harnesses have not been verified.
