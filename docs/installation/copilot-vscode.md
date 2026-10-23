# GitHub Copilot in VS Code installation

## Install the complete remote suite

Use a **Copilot** harness session in VS Code. The default-source recipe applies [after integration](../installation.md); the [remote preview](preview.md#copilot-in-vs-code) identifies a source already containing the package.

1. In VS Code Settings, add `omarfrancodev/devcraft-toolkit` to `chat.plugins.marketplaces`. Preserve existing entries; this setting is currently experimental.
2. Open Agent Customizations > Plugins, or the Agent Plugins view.
3. Browse the `devcraft-toolkit` marketplace, review trust and install `devcraft-toolkit`.
4. Inspect the suite's discovered skills before invoking its entry.

The editor downloads the complete suite; you do not clone the repository or select skill folders. No Node.js or third-party Skills CLI is required for this native route.

## User and workspace enablement

Use the installed marketplace plugin's context menu or customization controls to choose global or workspace enablement. Physical storage, activation and recommendations are separate. Recommendations in `.github/copilot/settings.json` do not download the package for collaborators.

A globally enabled installation can remain active elsewhere. Verify the selected workspace against a control workspace. Do not assume one client's discovery proves another harness hosted in VS Code works.

## Update and remove

Manage the plugin in the interface that installed it. Use its update controls/extension update check, inspect the actual installed revision/resources, and observe any reload requirement. Uninstall only the selected plugin from the installed view; disabling it is a separate action.

Copilot slash commands and Agent Customizations currently have different inventories. Direct Git installs in the slash-command inventory cannot be enabled/disabled like marketplace installs. The primary route above deliberately uses the marketplace UI.

## Optional routes and evidence

[Individual skills](individual-skills.md) use selector `github-copilot`. [Local development](development.md) documents local plugin locations separately.

The [official plugin guide](https://code.visualstudio.com/docs/agent-customization/agent-plugins) documents these interfaces. An isolated authenticated Copilot session was unavailable; this route is documented, not a native activation pass. [Compatibility](../compatibility.md) preserves that limit.
