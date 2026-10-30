# Codex installation

## Install the complete remote suite

The default-source recipe uses the integrated package; [release details](../releases/v0.1.0-preview.8.md#version-pinned-sources) describe version-pinned installation. Run in the installed Codex CLI:

```sh
codex plugin marketplace add omarfrancodev/devcraft-toolkit
codex plugin add devcraft-toolkit@devcraft-toolkit
```

This installs the complete suite through Codex's managed storage. No manual clone, Node.js or Skills CLI is needed. It does not place Devcraft Toolkit in an official catalog.

Inspect `codex plugin list`, then start/reload a session and select the entry skill. The documented commands were inspected in Codex CLI 0.162.0; [evidence](../../tests/integration/distribution/evaluations/2026-10-23-installation/native.md) distinguishes registry checks from active-session behavior.

## User or project enablement

The add command enables the plugin for the user. For user-wide use, retain that enablement; it can be inherited by all projects.

For **project-only** use, installation storage is still shared. Before starting the suite session, merge only this setting into the selected user's Codex configuration (`~/.codex/config.toml` by default, under the configured CODEX_HOME otherwise):

```toml
[plugins."devcraft-toolkit@devcraft-toolkit"]
enabled = false
```

Then enable it in the chosen trusted project's `.codex/config.toml`:

```toml
[plugins."devcraft-toolkit@devcraft-toolkit"]
enabled = true
```

Preserve other preferences and plugin registrations. Use the ordinary project trust flow. Run `codex plugin list --json` from this project and an unrelated control project: expect enabled in the selected project and disabled in the control. Other projects' explicit enablement remains their independent choice; do not remove it to manufacture isolation.

This precedence passed a real registry regression. Authenticated-session isolation/resource reads remain pending. If project-only activation cannot be established in your client, use the [complete project skill-set alternative](individual-skills.md#complete-skill-set-fallback).

## Update and remove

For a Git marketplace request refresh with `codex plugin marketplace upgrade devcraft-toolkit`, then inspect the installed version/resources and follow any client refresh/reinstall requirement. A catalog refresh alone does not establish an installed update. A pinned source stays pinned until deliberately changed.

Remove the selected suite with `codex plugin remove devcraft-toolkit@devcraft-toolkit`. Disabling its configuration is distinct from uninstalling it.

## Optional routes

[Individual skills](individual-skills.md) use selector `codex`. [Local development](development.md) covers local marketplace sources and their different update behavior. Shared `.agents/skills` discovery roots are not cross-client access control.

## Plugin presentation

The Codex marketplace entry declares `Developer Tools`. Root `plugin.json` supplies
listing metadata through `extensions.com.openai.interface`, including the display
name, project website and category. Both `logo` (listing) and `composerIcon`
(composer) use `./assets/logo.png`; `assets/logo.svg` is the editable source.
Paths resolve from the plugin root, not the manifest directory. Claude's
compatibility manifest declares its own fields; see [metadata across clients](metadata.md).

For this package, the offline distribution validator requires the declared
presentation, matching category and packaged PNG icons under `assets/`. It checks
path containment, a 5 MiB file limit, square dimensions from 48 to 4096 pixels,
PNG signature and chunk integrity. It does not render images or establish their
appearance in the desktop app.

Refresh the marketplace and inspect the installed revision after a published
presentation update, then restart the app. A version-pinned installation keeps its
selected version until deliberately changed. Editing the repository does not
change an already installed plugin cache.

See OpenAI's [package guide](https://developers.openai.com/plugins/build/plugins)
and [listing metadata reference](https://developers.openai.com/plugins/deploy/submission).

Each available skill also supplies a concise selector title and description in
its own `agents/openai.yaml`. These labels omit the plugin prefix while preserving
canonical names and namespaces. See [skill labels](metadata.md#skill-labels-in-codex)
for the package contract and update/reload requirements.
