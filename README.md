# Devcraft Toolkit

A modular toolkit of composable skills for repository context, read-only Git preflight, project validation discovery, standalone Conventional Commit drafting, and portable progress tracking. Compatibility is recorded only for harnesses actually exercised.

The distribution currently includes seven available skills: `using-devcraft-toolkit`, `git-working-directory-policy`, `git-safety-check`, `conventional-commits-style`, `todo-workflow-controller`, `natural-language-report-writer`, and `validation-discovery`. Git commit coordination, publication coordination, and the Git activity-report coordinator remain planned capabilities, not usable skills in this distribution. CCR integration is outside the current scope.

Skill definitions and default templates use English. User-facing content follows an explicit language preference or the language of the user's request, defaulting to English when neither can be determined. Tests are maintained outside individual skill directories, grouped by the owning skill and then by test scope; repository infrastructure and cross-skill coverage have separate shared groups.

The [catalog](catalog.json) records all seventeen target capabilities and marks each as `available` or `planned`. Seven are available and ten remain planned. See [installation](docs/installation.md), [architecture](docs/architecture.md), [language behavior](docs/language.md), and [compatibility evidence](docs/compatibility.md).

The [capability roadmap](docs/roadmap.md) links the self-contained designs and plans for upcoming increments.

## Install the complete suite

Install the complete toolkit directly from GitHub using your client's documented route. Native plugins/Powers deliver all seven skills; Crew imports the complete skill set. Kiro CLI without an IDE has an explicit full-set alternative. No user-managed clone is needed.

Choose [Codex](docs/installation/codex.md), [Copilot CLI](docs/installation/copilot-cli.md), [Copilot in VS Code](docs/installation/copilot-vscode.md), [Claude Code](docs/installation/claude-code.md), [Kiro CLI V3](docs/installation/kiro-cli.md), [Kiro IDE](docs/installation/kiro.md), or [Kiro Crew](docs/installation/kiro-crew.md). The [installation overview](docs/installation.md) explains scope and the Kiro project fallback.

Default-branch recipes apply after the package is integrated. Until then, the [remote preview sources](docs/installation/preview.md) identify existing sources containing the candidate. Native activation remains partially validated; no official catalog listing or new release is claimed.

Need selected capabilities instead? Use [individual skill installation](docs/installation/individual-skills.md). Package contributors and manual-copy users can use [local development/reference](docs/installation/development.md).

## Preview release

[v0.1.0-preview.1](https://github.com/omarfrancodev/devcraft-toolkit/releases/tag/v0.1.0-preview.1) is the first experimental distribution. See the [changelog](CHANGELOG.md) and [installation guide](docs/installation.md) for its scope and installation steps. Native skill loading and compatibility with other harnesses have not been verified.
