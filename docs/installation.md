# Installation

Install **Devcraft Toolkit as a complete suite** using the route for your client. Native plugins/Powers include all available skills and resources from the selected revision. Crew imports the complete set through its own dashboard; CLI-only Kiro has a full-set alternative. These routes need no user-managed clone.

The default-branch recipes below use the integrated remote package. [v0.1.0-preview.7 release details](releases/v0.1.0-preview.7.md) provide version-pinned source options and download verification. The earlier `v0.1.0-preview.1` is source-only and cannot serve as a native plugin source. [Historical pre-integration sources](installation/preview.md) describe earlier probes, not the current release's native acceptance.

## Install the complete suite

Choose your installed client:

| Client | Native remote route | Scope |
| --- | --- | --- |
| [Codex](installation/codex.md) | Register the GitHub marketplace and install the suite | User enablement or trusted-project enablement |
| [Copilot CLI](installation/copilot-cli.md) | Register the GitHub marketplace and install the same suite | User install or repository declarative activation |
| [Copilot in VS Code](installation/copilot-vscode.md) | Add the GitHub marketplace and install through the plugin UI | User/workspace enablement |
| [Claude Code](installation/claude-code.md) | Register the GitHub marketplace and install the suite | Explicit user or project scope |
| [Kiro CLI V3](installation/kiro-cli.md) | Pick up the IDE-installed Power; full remote skill set without IDE | Shared Power; separate user/project skill sets |
| [Kiro IDE](installation/kiro.md) | Import the GitHub repository as a Power | User Power; separate project skill-set fallback |
| [Kiro Crew](installation/kiro-crew.md) | Import the complete available set from GitHub with the native importer | Own user snapshots or trusted project skill set |

You need the client, network access and Git where its remote installer requires it. Native plugin/Power routes and Crew's importer do not require the third-party Skills CLI or a user-managed checkout. CLI-only Kiro's complete-set fallback uses Node/npm and the pinned external Skills CLI. Each client manages its own download/cache. This repository is the marketplace/source; no official catalog listing is claimed. A complete imported/copied skill set has a different lifecycle from a native plugin or Power. No Crew template or App is delivered.

Start/reload the client as directed, inspect its discovered skills and invoke `using-devcraft-toolkit` for a supported request. Installing the suite does not authorize Git writes or unrelated actions.

## Alternatives and reference

- [Install individual skills](installation/individual-skills.md): optional remote selection, explicit dependencies, destinations and the complete project skill-set fallback.
- [Local development and manual copying](installation/development.md): local checkout, source ZIPs and developer checks.
- [Compatibility and evidence](compatibility.md): native activation remains partially validated. File copying, registration and authenticated invocation are separate evidence levels.

For updates and removal use the selected client's guide and the same installation scope. Inspect existing installations before replacement; keep unrelated skills and settings intact. Avoid installing duplicate suite/standalone names without choosing which installation should serve the request.

## Source inventory

Version `0.1.0-preview.7` has sixteen skills, adding `git-manage-pull-request` and `git-promote`; only `git-publish-work` remains planned. Default-branch recipes use the integrated suite; use this tag for fixed complete/individual selections. Preview.6 retains fourteen and lacks these hosted capabilities; preview.5 has twelve, preview.4 eleven, preview.3 nine and preview.2 seven. Select a revision that contains the requested capabilities. Source selection and publication do not establish native activation. Historical tags and native resource evidence remain version-specific; installation does not authorize a runtime write.
