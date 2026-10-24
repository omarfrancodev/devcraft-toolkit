# Devcraft Toolkit

A modular toolkit of composable skills for repository context, read-only Git preflight, project validation discovery, standalone Conventional Commit drafting, and portable progress tracking. Compatibility is recorded only for harnesses actually exercised.

The distribution currently includes nine available skills: `using-devcraft-toolkit`, `git-working-directory-policy`, `git-safety-check`, `conventional-commits-style`, `todo-workflow-controller`, `natural-language-report-writer`, `validation-discovery`, `git-analyze-changes`, and `git-plan-commits`. Git commit coordination, publication coordination, and the Git activity-report coordinator remain planned capabilities, not usable skills in this distribution. CCR integration is outside the current scope.

Skill definitions and default templates use English. User-facing content follows an explicit language preference or the language of the user's request, defaulting to English when neither can be determined. Tests are maintained outside individual skill directories, grouped by the owning skill and then by test scope; repository infrastructure and cross-skill coverage have separate shared groups.

The [catalog](catalog.json) records all seventeen target capabilities and marks each as `available` or `planned`. Nine are available and eight remain planned. See [installation](docs/installation.md), [architecture](docs/architecture.md), [language behavior](docs/language.md), and [compatibility evidence](docs/compatibility.md).

The [capability roadmap](docs/roadmap.md) links the self-contained designs and plans for upcoming increments.

## Install the complete suite

Install the complete toolkit directly from GitHub using your client's documented route. Native plugins/Powers deliver all available skills from the selected source; Crew imports the complete skill set. Kiro CLI without an IDE has an explicit full-set alternative. No user-managed clone is needed.

Choose [Codex](docs/installation/codex.md), [Copilot CLI](docs/installation/copilot-cli.md), [Copilot in VS Code](docs/installation/copilot-vscode.md), [Claude Code](docs/installation/claude-code.md), [Kiro CLI V3](docs/installation/kiro-cli.md), [Kiro IDE](docs/installation/kiro.md), or [Kiro Crew](docs/installation/kiro-crew.md). The [installation overview](docs/installation.md) explains scope and the Kiro project fallback.

The default-branch recipes use the integrated package. See [preview.2 release details](docs/releases/v0.1.0-preview.2.md) for version-pinned source options; [earlier preview sources](docs/installation/preview.md) are historical evidence. Native activation remains partially validated; no official catalog listing is claimed.

Need selected capabilities instead? Use [individual skill installation](docs/installation/individual-skills.md). Package contributors and manual-copy users can use [local development/reference](docs/installation/development.md).

## Preview release

[v0.1.0-preview.2](https://github.com/omarfrancodev/devcraft-toolkit/releases/tag/v0.1.0-preview.2) adds remote suite packaging and installation guidance for seven local clients. See the [changelog](CHANGELOG.md), [release details](docs/releases/v0.1.0-preview.2.md) and [installation guide](docs/installation.md). Native compatibility remains partial; preview.1 is the earlier source-only distribution.

## Development candidate

The current checkout is the unpublished `0.1.0-preview.3` candidate. `git-analyze-changes` returns guarded, layer-specific local evidence; `git-plan-commits` proposes intent groups and messages while preserving the staged selection. Both are read-only; staging and commit execution remain planned. [Their design and acceptance gates](docs/superpowers/specs/2026-10-24-git-analysis-planning-design.md) and [the remaining sequence](docs/roadmap.md#next-increments-and-acceptance-gates) describe the boundaries.

Published `v0.1.0-preview.2` still contains seven skills and does not include these two capabilities. New capabilities require a source revision containing this increment; no preview.3 release or native activation is claimed.
