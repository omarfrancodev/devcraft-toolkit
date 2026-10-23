# GitHub Copilot in VS Code installation

This guide targets the unreleased development checkout with native package metadata. Select a checkout that contains `plugin.json`; `v0.1.0-preview.1` does not. Run standalone commands from your chosen project's root. For native registration, the source variable still identifies the toolkit checkout.

```powershell
$toolkitSource = (Resolve-Path -LiteralPath (Read-Host 'Path to the Devcraft Toolkit checkout')).Path
$toolkitSkills = @('using-devcraft-toolkit', 'git-working-directory-policy', 'git-safety-check', 'conventional-commits-style', 'todo-workflow-controller', 'natural-language-report-writer', 'validation-discovery')
```

CLI recipes use Node.js >=22.20.0, npm and pinned Skills CLI 1.7.4. In a non-PowerShell shell use the equivalent source path and argument list. Manual copying requires neither Node nor npm. Read the [selection/dependency table](../installation.md#individual-skill-dependencies) before selecting an entry or preflight skill.

## Native suite

For an existing local checkout, use the documented experimental `chat.pluginLocations` setting. In VS Code Settings JSON at the chosen user or workspace scope, merge an entry mapping the selected absolute checkout path to `true`. Generate the fragment from the already selected path:

```powershell
@{ 'chat.pluginLocations' = @{ $toolkitSource = $true } } | ConvertTo-Json -Depth 3
```

Preserve other registered locations. Set that entry to `false` to disable it; remove only that registration to stop using the local checkout. Source changes and reload behavior must be checked in the actual session.

For a marketplace installation, configure `chat.plugins.marketplaces` with a file URI to the locally cloned marketplace repository, then browse its plugin in Agent Customizations or the Agent Plugins view. For a published Git source choose a verified revision containing these manifests. The Install Plugin from Source command accepts a Git repository URL; it is not the local-folder recipe.

Marketplace plugins can be enabled or disabled globally or for a workspace. Recommendations in `.github/copilot/settings.json` do not download the plugin for collaborators. Physical storage, enablement and recommendations are distinct.

The Copilot harness also offers `/plugin marketplace add`, `/plugin install`, `/plugin list`, `/plugin update` and `/plugin uninstall`. Its slash-command inventory and Agent Customizations currently differ: manage a plugin in the interface that installed it. A direct Git install in that slash-command inventory cannot be toggled enabled/disabled; uninstall it to stop using it. Do not apply marketplace scope promises to that route.

See [VS Code's official plugin instructions](https://code.visualstudio.com/docs/agent-customization/agent-plugins). These are documented procedures, not observed native activation in this evaluation.

## Selected skills: project and user scope

Inspect existing selected directories before confirming any installation. The leading npm `--yes` only obtains the CLI; Skills remains interactive. Use `--copy` so updates are explicit and Windows symlink privileges are not required.

One independent skill in the selected project:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill natural-language-report-writer --agent github-copilot --copy
```

The same skill for your user account:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill natural-language-report-writer --agent github-copilot --copy --global
```

The complete available skill set in this project:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill $toolkitSkills --agent github-copilot --copy
```

The same set for your user account:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill $toolkitSkills --agent github-copilot --copy --global
```

For the entry alone select `using-devcraft-toolkit git-working-directory-policy git-safety-check` explicitly; for preflight select `git-safety-check git-working-directory-policy`. The installer does not resolve these custom dependencies.

## Manual copying and destinations

| Scope | Complete-folder destination |
| --- | --- |
| Project | `.agents/skills/<skill-name>/` under the selected project |
| User/global | `~/.copilot/skills/<skill-name>/` |

Skills CLI 1.7.4 was observed to write the global selection to `~/.agents/skills/`, a shared discovery root, rather than the manual `~/.copilot/skills/` destination above. Both paths were independently exercised; inspect the CLI output and filesystem instead of assuming the manual path.

Copy each selected `skills/<skill-name>/` folder, including all local `references/` and `assets/`. Inspect every destination before copying, stop on collisions, and obtain replacement authorization before changing existing content. Preserve unrelated directories.

Shared roots can be discovered by another client. Selecting `--agent github-copilot` does not guarantee exclusive visibility. Check the actual target directory, the CLI's canonical store if present, and its project/user lock files.

## Verify discovery and scope

Use the Copilot harness, open Configure Skills/Agent Customizations, and inspect the actual discovered list. Invoke the standalone skill or the plugin-qualified command shown there. A Codex or Claude session hosted in VS Code is a different target.

Test project scope against a second unrelated project and test user scope across both. Inspect resource reads and the invoked installation's identity, not just the existence of folders. Existing personal and project copies may have different precedence in different clients; ask for an installation choice if ownership is ambiguous. Installation grants no extra workflow permissions.

## Standalone update and removal

For a local source, explicitly re-run the selected install command after inspecting changes and authorizing replacement. Verify that copied resources changed and unrelated files did not. Do not assume copied skills track source edits.

For remote tracked sources, inspect `npx --yes skills@1.7.4 update --help` and the recorded lock/source before updating. Automatic remote updating was not substituted for local-source replacement in the filesystem evaluation.

Remove only the named project installation:

```powershell
npx --yes skills@1.7.4 remove natural-language-report-writer --agent github-copilot
```

For the user installation, add `--global`. The remove operation may also affect its canonical store and lock entry; inspect those observed effects, preserve unrelated skills, and do not manually delete internal caches.

## Validation status

See [filesystem evidence](../../tests/integration/distribution/evaluations/2026-10-23-installation/filesystem.md) and [compatibility limits](../compatibility.md). CLI and manual-copy results establish file placement/resources only. Native discovery, activation, control-project visibility, and native lifecycle results require a real isolated GitHub Copilot in VS Code session; a blocked or unrun case remains explicit.

[Per-scope native results and remaining gates](../../tests/integration/distribution/evaluations/2026-10-23-installation/native.md) distinguish registry observations from authenticated activation.
