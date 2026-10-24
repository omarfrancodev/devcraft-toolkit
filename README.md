# Devcraft Toolkit

A modular toolkit of composable skills for repository context, Git inspection and planning, exact authorized staging, requested local commits, project validation, reporting, and portable progress tracking. Compatibility is recorded only for harnesses actually exercised.

The distribution currently includes eleven available skills: `using-devcraft-toolkit`, `git-working-directory-policy`, `git-safety-check`, `conventional-commits-style`, `todo-workflow-controller`, `natural-language-report-writer`, `validation-discovery`, `git-analyze-changes`, `git-plan-commits`, `git-stage-changes`, and `git-commit-builder`. Publication coordination and the Git activity-report coordinator remain planned capabilities, not usable skills in this distribution. CCR integration is outside the current scope.

Skill definitions and default templates use English. User-facing content follows an explicit language preference or the language of the user's request, defaulting to English when neither can be determined. Tests are maintained outside individual skill directories, grouped by the owning skill and then by test scope; repository infrastructure and cross-skill coverage have separate shared groups.

The [catalog](catalog.json) records all seventeen target capabilities and marks each as `available` or `planned`. Eleven are available and six remain planned. See [installation](docs/installation.md), [architecture](docs/architecture.md), [language behavior](docs/language.md), and [compatibility evidence](docs/compatibility.md).

The [capability roadmap](docs/roadmap.md) links the self-contained designs and plans for upcoming increments.

## Install the complete suite

Install the complete toolkit directly from GitHub using your client's documented route. Native plugins/Powers deliver all available skills from the selected source; Crew imports the complete skill set. Kiro CLI without an IDE has an explicit full-set alternative. No user-managed clone is needed.

Choose [Codex](docs/installation/codex.md), [Copilot CLI](docs/installation/copilot-cli.md), [Copilot in VS Code](docs/installation/copilot-vscode.md), [Claude Code](docs/installation/claude-code.md), [Kiro CLI V3](docs/installation/kiro-cli.md), [Kiro IDE](docs/installation/kiro.md), or [Kiro Crew](docs/installation/kiro-crew.md). The [installation overview](docs/installation.md) explains scope and the Kiro project fallback.

The default-branch recipes use the integrated package. See [preview.4 release details](docs/releases/v0.1.0-preview.4.md) for version-pinned source options; [earlier preview sources](docs/installation/preview.md) are historical evidence. Native activation remains partially validated; no official catalog listing is claimed.

Need selected capabilities instead? Use [individual skill installation](docs/installation/individual-skills.md). Package contributors and manual-copy users can use [local development/reference](docs/installation/development.md).

## Preview release

[v0.1.0-preview.4](https://github.com/omarfrancodev/devcraft-toolkit/releases/tag/v0.1.0-preview.4) adds exact authorized staging and coordinated local commit construction to the complete eleven-skill suite. See the [changelog](CHANGELOG.md), [release details](docs/releases/v0.1.0-preview.4.md) and [installation guide](docs/installation.md). Native compatibility remains partial.

`git-stage-changes` preserves excluded index/worktree content; `git-commit-builder` creates explicitly requested normal commits with scoped validation, effective identity and hook checks, and actual partial-progress reporting. A proposal or ready preflight grants no write permission. See the [design](docs/superpowers/specs/2026-10-24-git-staging-commit-construction-design.md), [plan](docs/superpowers/plans/2026-10-24-git-staging-commit-construction.md) and [roadmap](docs/roadmap.md).

Earlier [preview.3](docs/releases/v0.1.0-preview.3.md) remains the nine-skill read-only analysis/planning snapshot; [preview.2](docs/releases/v0.1.0-preview.2.md) contains seven skills, and preview.1 is source-only. Historical native registration/resource evidence does not establish activation of the added skills.
