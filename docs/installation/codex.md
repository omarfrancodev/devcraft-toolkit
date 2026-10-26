# Codex installation

## Install the complete remote suite

The default-source recipe uses the integrated package; [release details](../releases/v0.1.0-preview.6.md#version-pinned-sources) describe version-pinned installation. Run in the installed Codex CLI:

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
