# Codex installation

This guide targets the unreleased development checkout with native package metadata. Select a checkout that contains `plugin.json`; `v0.1.0-preview.1` does not. Run standalone commands from your chosen project's root. For native registration, the source variable still identifies the toolkit checkout.

```powershell
$toolkitSource = (Resolve-Path -LiteralPath (Read-Host 'Path to the Devcraft Toolkit checkout')).Path
$toolkitSkills = @('using-devcraft-toolkit', 'git-working-directory-policy', 'git-safety-check', 'conventional-commits-style', 'todo-workflow-controller', 'natural-language-report-writer', 'validation-discovery')
```

CLI recipes use Node.js >=22.20.0, npm and pinned Skills CLI 1.7.4. In a non-PowerShell shell use the equivalent source path and argument list. Manual copying requires neither Node nor npm. Read the [selection/dependency table](../installation.md#individual-skill-dependencies) before selecting an entry or preflight skill.

## Native suite

Codex CLI 0.162.0 exposes the following local-checkout registration and installation commands:

```powershell
codex plugin marketplace add "$toolkitSource"
codex plugin add devcraft-toolkit@devcraft-toolkit --json
codex plugin list
```

The supported plugin browser is an alternative. These operations change your user plugin configuration/cache and must run only when you choose that installation. A release-based marketplace registration can use a verified ref containing these manifests; the old source-only preview is not such a ref.

### User/global enablement

The add command above enables the plugin at user scope. Inspect its configuration and `codex plugin list`; a user-enabled plugin can be inherited by every project. The user configuration is `~/.codex/config.toml` by default, or the config under the chosen CODEX_HOME. Preserve existing configuration and merge only the selected plugin's entry:

```toml
[plugins."devcraft-toolkit@devcraft-toolkit"]
enabled = true
```

### Project-only enablement

Registration and shared installation are prerequisites, but the add command's user enablement must not remain active for a project-only setup. Before starting a session that uses the suite, merge the following value into that same **user** configuration, preserving all other preferences and plugin registrations:

```toml
[plugins."devcraft-toolkit@devcraft-toolkit"]
enabled = false
```

Then enable the suite only in the selected trusted project's `.codex/config.toml`:

```toml
[plugins."devcraft-toolkit@devcraft-toolkit"]
enabled = true
```

Use Codex's ordinary trust flow for the chosen project; do not disable trust protections. Check `codex plugin list --json` from both the selected project and an unrelated control project before invoking the suite: the selected installation should be enabled in the former and disabled in the latter. Other projects with their own explicit enablement remain independent choices; do not remove their settings to manufacture isolation. If the client cannot establish project-only activation, use the project seven-folder skill selection below rather than treating a globally enabled plugin as project-only.

The [registry scope regression](../../tests/integration/distribution/evaluations/2026-10-23-installation/native.md#codex-project-enablement-regression) reproduced both-project enablement before the user-disable step and selected-only enablement afterward. This checks registry/configuration precedence, not skill activation in authenticated sessions.

This is project activation, not a separate physical project cache. Leaving user enablement active would expose it to projects inheriting that setting; the project-only route above explicitly disables it first. Disabling a plugin is distinct from removing it. Use the installed client's configuration/plugin UI for enablement and `codex plugin remove devcraft-toolkit@devcraft-toolkit` for native uninstall. `codex plugin marketplace upgrade devcraft-toolkit` applies to Git marketplaces; the observed local-directory registration rejects that command. For local development update the selected source checkout and restart/reload as directed by the client, then verify the active version and resources. A Git catalog refresh is not proof of an installed-plugin update. The guide does not claim native activation passed merely because metadata validates.


## Selected skills: project and user scope

Inspect existing selected directories before confirming any installation. The leading npm `--yes` only obtains the CLI; Skills remains interactive. Use `--copy` so updates are explicit and Windows symlink privileges are not required.

One independent skill in the selected project:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill natural-language-report-writer --agent codex --copy
```

The same skill for your user account:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill natural-language-report-writer --agent codex --copy --global
```

The complete available skill set in this project:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill $toolkitSkills --agent codex --copy
```

The same set for your user account:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill $toolkitSkills --agent codex --copy --global
```

For the entry alone select `using-devcraft-toolkit git-working-directory-policy git-safety-check` explicitly; for preflight select `git-safety-check git-working-directory-policy`. The installer does not resolve these custom dependencies.

## Manual copying and destinations

| Scope | Complete-folder destination |
| --- | --- |
| Project | `.agents/skills/<skill-name>/` under the selected project |
| User/global | `~/.agents/skills/<skill-name>/` |

Copy each selected `skills/<skill-name>/` folder, including all local `references/` and `assets/`. Inspect every destination before copying, stop on collisions, and obtain replacement authorization before changing existing content. Preserve unrelated directories.

Shared roots can be discovered by another client. Selecting `--agent codex` does not guarantee exclusive visibility. Check the actual target directory, the CLI's canonical store if present, and its project/user lock files.

## Verify discovery and scope

Select the installed skill from Codex's skill picker or invoke its discovered identifier. With the native suite, inspect the plugin's ownership and use the identifier Codex exposes; do not assume it equals a standalone name.

Test project scope against a second unrelated project and test user scope across both. Inspect resource reads and the invoked installation's identity, not just the existence of folders. Existing personal and project copies may have different precedence in different clients; ask for an installation choice if ownership is ambiguous. Installation grants no extra workflow permissions.

## Standalone update and removal

For a local source, explicitly re-run the selected install command after inspecting changes and authorizing replacement. Verify that copied resources changed and unrelated files did not. Do not assume copied skills track source edits.

For remote tracked sources, inspect `npx --yes skills@1.7.4 update --help` and the recorded lock/source before updating. Automatic remote updating was not substituted for local-source replacement in the filesystem evaluation.

Remove only the named project installation:

```powershell
npx --yes skills@1.7.4 remove natural-language-report-writer --agent codex
```

For the user installation, add `--global`. The remove operation may also affect its canonical store and lock entry; inspect those observed effects, preserve unrelated skills, and do not manually delete internal caches.

## Validation status

See [filesystem evidence](../../tests/integration/distribution/evaluations/2026-10-23-installation/filesystem.md) and [compatibility limits](../compatibility.md). CLI and manual-copy results establish file placement/resources only. Native discovery, activation, control-project visibility, and native lifecycle results require a real isolated Codex session; a blocked or unrun case remains explicit.

[Per-scope native results and remaining gates](../../tests/integration/distribution/evaluations/2026-10-23-installation/native.md) distinguish registry observations from authenticated activation.
