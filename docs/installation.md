# Installation

Install **Devcraft Toolkit as a complete suite** using the route for your client. Native plugins/Powers include all available skills and resources from the selected revision. Crew imports the complete set through its own dashboard; CLI-only Kiro has a full-set alternative. These routes need no user-managed clone.

The default-branch recipes below use the integrated remote package. [v0.1.0-preview.10 release details](releases/v0.1.0-preview.10.md) provide version-pinned source options and download verification. The earlier `v0.1.0-preview.1` is source-only and cannot serve as a native plugin source. [Historical pre-integration sources](installation/preview.md) describe earlier probes, not the current release's native acceptance.

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

Current source contains twenty available skills, adding independent `issue-builder`. This addition reaches default remote recipes after integration and is absent from fixed preview.10/older sources. Use a selected checkout/revision that contains it; it needs only its complete folder.

Preview.10 adds `prompt-refiner`, making nineteen available skills, and corrects registered-but-unused filter handling. The prompt refiner needs only its own folder and is absent from preview.9. Default remote recipes include the complete set after integration; select preview.10 for fixed nineteen-skill sources.

Version `0.1.0-preview.9` has eighteen skills, retaining `git-create-work-branch` and `git-publish-work` while adding client presentation metadata and explicit Codex skill labels. Default-branch recipes use the integrated suite; use preview.10 for the current fixed nineteen-skill selections. Preview.7 retains sixteen and lacks the two additions; preview.6 retains fourteen without hosted management/promotion; preview.5 has twelve, preview.4 eleven, preview.3 nine and preview.2 seven. Select a revision that contains the requested capabilities. Source selection and publication do not establish native activation. Historical tags and native resource evidence remain version-specific; installation does not authorize a runtime write.


Release `0.1.0-preview.10` has nineteen available skills and no planned entries. Native remote suite installation includes the complete selected revision without a new installer. Local contributor checks remain an optional [development route](installation/development.md). [Individual selections](installation/individual-skills.md) distinguish mandatory and conditional closures.

## Presentation across clients

See [plugin metadata](installation/metadata.md) for display names, categories,
project links, logo fields and the supported presentation limits in each client.
