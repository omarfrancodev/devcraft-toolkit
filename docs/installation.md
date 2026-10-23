# Installation

Install **Devcraft Toolkit as a complete native suite**. It contains all seven available skills and their required resources; you do not select individual folders or manage a local clone.

The remote default-branch recipes below apply once the package metadata is integrated into that branch. While this change is under review, use the [remote preview sources](installation/preview.md) where supported. The published `v0.1.0-preview.1` is source-only and cannot serve as a native plugin source. Candidate metadata `0.1.0-preview.2` does not mean a release has been published.

## Install the complete suite

Choose your installed client:

| Client | Native remote route | Scope |
| --- | --- | --- |
| [Codex](installation/codex.md) | Register the GitHub marketplace and install the suite | User enablement or trusted-project enablement |
| [Copilot in VS Code](installation/copilot-vscode.md) | Add the GitHub marketplace and install through the plugin UI | User/workspace enablement |
| [Claude Code](installation/claude-code.md) | Register the GitHub marketplace and install the suite | Explicit user or project scope |
| [Kiro IDE](installation/kiro.md) | Import the GitHub repository as a Power | User Power; separate project skill-set fallback |

You need the client, network access and Git where its remote installer requires it. The suite route does not require Node.js, the third-party Skills CLI, or a user-managed checkout. Each client manages its own download/cache. This repository is the marketplace source; no official catalog listing is claimed.

Start/reload the client as directed, inspect its discovered skills and invoke `using-devcraft-toolkit` for a supported request. Installing the suite does not authorize Git writes or unrelated actions.

## Alternatives and reference

- [Install individual skills](installation/individual-skills.md): optional remote selection, explicit dependencies, destinations and the complete project skill-set fallback.
- [Local development and manual copying](installation/development.md): local checkout, source ZIPs and developer checks.
- [Compatibility and evidence](compatibility.md): native activation remains partially validated. File copying, registration and authenticated invocation are separate evidence levels.

For updates and removal use the selected client's guide and the same installation scope. Inspect existing installations before replacement; keep unrelated skills and settings intact. Avoid installing duplicate suite/standalone names without choosing which installation should serve the request.
