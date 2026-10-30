# Claude Code installation

## Install the complete remote suite

The default-source recipe uses the integrated package; [release details](../releases/v0.1.0-preview.8.md#version-pinned-sources) describe version-pinned installation. Register this repository from your shell:

```sh
claude plugin marketplace add omarfrancodev/devcraft-toolkit
claude plugin install devcraft-toolkit@devcraft-toolkit --scope user
```

This installs all available skills from the selected revision and bundled resources without a manual clone or the third-party Skills CLI. Marketplace registration is normally a one-time step. Review the marketplace trust prompt when using the interactive plugin UI.

## Project scope

To install for a selected project, run from that project's root and use project scope instead of user scope:

```sh
claude plugin install devcraft-toolkit@devcraft-toolkit --scope project
```

Project enablement is recorded in `.claude/settings.json`; collaborators still download the plugin on their own machines. User and project scope may share managed cache storage. Preserve unrelated settings and compare `claude plugin list` in this project and a control project.

Start a new session or use the client's normal `/reload-plugins` flow. Inspect the skills actually discovered under the plugin, then invoke the entry using the identifier shown by the client. Claude Code 2.1.300 accepted the package and enumerated its seven components; authenticated invocation and resource reads remain [unverified](../compatibility.md).

## Update and remove

Refresh the Git marketplace with `claude plugin marketplace update devcraft-toolkit`; request an installed update with `claude plugin update devcraft-toolkit@devcraft-toolkit --scope user` (or `--scope project`). Check the actual version/resources and reload instructions. A pinned source does not automatically advance to another revision.

Remove only the chosen scope with `claude plugin uninstall devcraft-toolkit@devcraft-toolkit --scope user`, or the matching project scope. Preserve the other scope and unrelated plugins.

## Optional routes

[Individual skills](individual-skills.md) use selector `claude-code`. [Local development](development.md) is separate: local-folder updates do not use the Git marketplace refresh path.

See the [official installation and scope reference](https://code.claude.com/docs/en/discover-plugins).

## Presentation metadata

The Claude manifest declares `Devcraft Toolkit` as its `displayName`, project
homepage/repository links, discovery keywords and `icon: ./assets/logo.png`.
The shared marketplace declares `Developer Tools` and discovery tags.
Anthropic documents `icon` for its directory; Claude Code ignores that field at
runtime, so it does not establish a custom icon in the CLI/plugin UI.
See [metadata across clients](metadata.md) for validator versions and evidence.
