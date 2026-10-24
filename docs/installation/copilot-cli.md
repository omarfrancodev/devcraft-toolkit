# GitHub Copilot CLI installation

## Install the complete remote suite

Use the existing marketplace; no separate Copilot package is needed. The normal
source uses the integrated package. [Release details](../releases/v0.1.0-preview.3.md#version-pinned-sources)
describe a version-pinned marketplace source.

```sh
copilot plugin marketplace add omarfrancodev/devcraft-toolkit
copilot plugin install devcraft-toolkit@devcraft-toolkit
copilot plugin list
```

Review the source and trust prompts. Inspect all skills installed from the selected revision and
resources, then use the toolkit entry in a Copilot session. A successful plugin
list does not prove a model loaded the entry or read its bundled resources.

## User and repository scope

The imperative install above uses the selected user's Copilot installation.
For repository-declared installation, merge this fragment into the selected
repository's `.github/copilot/settings.json`, preserving other settings:

```json
{
  "extraKnownMarketplaces": {
    "devcraft-toolkit": {
      "source": {
        "source": "github",
        "repo": "omarfrancodev/devcraft-toolkit"
      }
    }
  },
  "enabledPlugins": {
    "devcraft-toolkit@devcraft-toolkit": true
  }
}
```

Use the release ref from the linked guide when selecting a pinned source. These CLI keys
declare marketplace acquisition and repository activation, not merely editor
recommendations. In clients supporting this interface, a repository-only enabled
plugin stays disabled globally unless user settings also enable it. Inspect both
the selected trusted repository and a control repository. Existing user
enablement may make it active elsewhere; shared files do not prove isolation.

Do not run global enable/disable as a substitute for changing a repository's
controlling overlay. Managed organization policy can also govern these settings.
This repository does not install its own plugin into itself.

## VS Code crossover and lifecycle

VS Code can discover CLI-installed plugins. Inspect them in the
[VS Code guide](copilot-vscode.md); do not install a duplicate just because it
does not appear in another inventory. Discovery and workspace enablement still
need to be checked in VS Code.

```sh
copilot plugin marketplace update devcraft-toolkit
copilot plugin update devcraft-toolkit@devcraft-toolkit
copilot plugin uninstall devcraft-toolkit@devcraft-toolkit
```

Marketplace refresh and plugin update are different. Use the installed client's
help/list output to confirm the accepted identity and any restart requirement.
A repository declaration can reinstall a removed plugin on the next session:
first remove only that toolkit declaration if removal is intended. Preserve
other settings, scopes and plugins.

## Individual skills and evidence

[Individual installation](individual-skills.md) uses the same
`github-copilot` selector as VS Code and copies complete folders. Do not assume
a single-file URL install through `copilot skill add` also obtains sibling
references/assets; these skills require their complete folders.

See [local development](development.md), [compatibility](../compatibility.md)
and the [client expansion evidence](../../tests/integration/distribution/evaluations/2026-10-23-client-expansion/clients.md).
Native authenticated invocation and repository/session isolation remain separate
gates from remote registration.

Official references: [plugin installation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing),
[package reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference)
and [settings/scopes](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference).
