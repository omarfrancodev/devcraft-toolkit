# Devcraft Toolkit

A modular toolkit of composable skills for repository context, read-only Git preflight, project validation discovery, standalone Conventional Commit drafting, and portable progress tracking. Compatibility is recorded only for harnesses actually exercised.

The distribution currently includes seven available skills: `using-devcraft-toolkit`, `git-working-directory-policy`, `git-safety-check`, `conventional-commits-style`, `todo-workflow-controller`, `natural-language-report-writer`, and `validation-discovery`. Git commit coordination, publication coordination, and the Git activity-report coordinator remain planned capabilities, not usable skills in this distribution. CCR integration is outside the current scope.

Skill definitions and default templates use English. User-facing content follows an explicit language preference or the language of the user's request, defaulting to English when neither can be determined. Tests are maintained outside individual skill directories, grouped by the owning skill and then by test scope; repository infrastructure and cross-skill coverage have separate shared groups.

The [catalog](catalog.json) records all seventeen target capabilities and marks each as `available` or `planned`. Seven are available and ten remain planned. See [installation](docs/installation.md), [architecture](docs/architecture.md), [language behavior](docs/language.md), and [compatibility evidence](docs/compatibility.md).

The [capability roadmap](docs/roadmap.md) links the self-contained designs and plans for upcoming increments.

## Install from this checkout

The unreleased candidate includes native plugin metadata and the same seven independently selectable skill folders. Native installation and selective installation both support documented user/project routes; native activation remains subject to the evidence matrix.

Choose a target: [Codex](docs/installation/codex.md), [Copilot in VS Code](docs/installation/copilot-vscode.md), [Claude Code](docs/installation/claude-code.md), or [Kiro IDE](docs/installation/kiro.md). The [installation overview](docs/installation.md) explains dependency selections, complete-folder copying, collisions and updates.

For Claude Code, after choosing a local checkout containing the new manifests:

```powershell
$toolkitSource = (Resolve-Path -LiteralPath (Read-Host 'Path to the Devcraft Toolkit checkout')).Path
claude plugin marketplace add "$toolkitSource"
claude plugin install devcraft-toolkit@devcraft-toolkit --scope user
```

For one independent skill in a project, with Node.js >=22.20.0 and npm:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill natural-language-report-writer --agent claude-code --copy
```

Inspect existing destinations before confirming. This example does not install the entry or resolve dependencies automatically. Follow the target guide for global scope or the full selection.

## Preview release

[v0.1.0-preview.1](https://github.com/omarfrancodev/devcraft-toolkit/releases/tag/v0.1.0-preview.1) is the first experimental distribution. See the [changelog](CHANGELOG.md) and [installation guide](docs/installation.md) for its scope and installation steps. Native skill loading and compatibility with other harnesses have not been verified.
