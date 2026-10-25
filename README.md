# Devcraft Toolkit

A modular toolkit of composable skills for repository context, Git inspection and planning, exact authorized staging, requested local commits, project validation, reporting, and portable progress tracking. Compatibility is recorded only for harnesses actually exercised.

The distribution includes twelve available skills: `using-devcraft-toolkit`, `git-working-directory-policy`, `git-safety-check`, `conventional-commits-style`, `todo-workflow-controller`, `natural-language-report-writer`, `validation-discovery`, `git-analyze-changes`, `git-plan-commits`, `git-stage-changes`, `git-commit-builder`, and `git-activity-report`. Publication coordination remains planned and unavailable in this distribution. CCR integration is outside the current scope.

Skill definitions and default templates use English. User-facing content follows an explicit language preference or the language of the user's request, defaulting to English when neither can be determined. Tests are maintained outside individual skill directories, grouped by the owning skill and then by test scope; repository infrastructure and cross-skill coverage have separate shared groups.

The [catalog](catalog.json) records all seventeen target capabilities and marks each as `available` or `planned`. Twelve are available and five remain planned. See [installation](docs/installation.md), [architecture](docs/architecture.md), [language behavior](docs/language.md), and [compatibility evidence](docs/compatibility.md).

The [capability roadmap](docs/roadmap.md) links the self-contained designs and plans for upcoming increments.

## Install the complete suite

Install the complete toolkit directly from GitHub using your client's documented route. Native plugins/Powers deliver all available skills from the selected source; Crew imports the complete skill set. Kiro CLI without an IDE has an explicit full-set alternative. No user-managed clone is needed.

Choose [Codex](docs/installation/codex.md), [Copilot CLI](docs/installation/copilot-cli.md), [Copilot in VS Code](docs/installation/copilot-vscode.md), [Claude Code](docs/installation/claude-code.md), [Kiro CLI V3](docs/installation/kiro-cli.md), [Kiro IDE](docs/installation/kiro.md), or [Kiro Crew](docs/installation/kiro-crew.md). The [installation overview](docs/installation.md) explains scope and the Kiro project fallback.

The default-branch recipes use the integrated package. See [preview.5 release details](docs/releases/v0.1.0-preview.5.md) for version-pinned source options; [earlier preview sources](docs/installation/preview.md) are historical evidence. Native activation remains partially validated; no official catalog listing is claimed.

Need selected capabilities instead? Use [individual skill installation](docs/installation/individual-skills.md). Package contributors and manual-copy users can use [local development/reference](docs/installation/development.md).

## Preview release

[v0.1.0-preview.5](https://github.com/omarfrancodev/devcraft-toolkit/releases/tag/v0.1.0-preview.5) adds `git-activity-report` to the complete twelve-skill suite. See the [changelog](CHANGELOG.md), [release details](docs/releases/v0.1.0-preview.5.md) and [installation guide](docs/installation.md). Native compatibility remains partial.

The coordinator inspects a pinned local history with explicit period/timezone, author-date or committer-date selection, exact raw-author filtering, bounded coverage and message-level evidence. It delegates prose and explicitly requested one-file output to `natural-language-report-writer`; a saved report requires a selected destination, replacement permission when needed and matching readback. Reporting grants no Git or publication permission. See the [design](docs/superpowers/specs/2026-10-24-git-activity-report-design.md), [plan](docs/superpowers/plans/2026-10-24-git-activity-report.md) and [roadmap](docs/roadmap.md).

Earlier [preview.4](docs/releases/v0.1.0-preview.4.md) retains eleven skills with exact staging and local commit construction but no history-report coordinator. [Preview.3](docs/releases/v0.1.0-preview.3.md) has nine, [preview.2](docs/releases/v0.1.0-preview.2.md) has seven, and preview.1 is source-only. Historical native registration/resource evidence does not establish activation of added skills.
