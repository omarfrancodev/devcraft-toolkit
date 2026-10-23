# Kiro IDE installation

This guide targets the unreleased development checkout with native package metadata. Select a checkout that contains `plugin.json`; `v0.1.0-preview.1` does not. Run standalone commands from your chosen project's root. For native registration, the source variable still identifies the toolkit checkout.

```powershell
$toolkitSource = (Resolve-Path -LiteralPath (Read-Host 'Path to the Devcraft Toolkit checkout')).Path
$toolkitSkills = @('using-devcraft-toolkit', 'git-working-directory-policy', 'git-safety-check', 'conventional-commits-style', 'todo-workflow-controller', 'natural-language-report-writer', 'validation-discovery')
```

CLI recipes use Node.js >=22.20.0, npm and pinned Skills CLI 1.7.4. In a non-PowerShell shell use the equivalent source path and argument list. Manual copying requires neither Node nor npm. Read the [selection/dependency table](../installation.md#individual-skill-dependencies) before selecting an entry or preflight skill.

## Native suite as a Power

Kiro's Agent Plugins Power format uses the root `plugin.json` and the existing `skills/` tree. No extra POWER.md or copied skill set is required for that format.

1. Open Powers > Add Custom Power.
2. Import from a folder containing this checkout's root `plugin.json`, or import a public Git repository ref that actually includes it.
3. Inspect the Power's provided skills.
4. Test activation and resource access in Kiro IDE.

Use the Power's update/removal controls in the same IDE and observe its actual scope. This guide does not invent CLI scope flags for those UI operations.

An isolated project-only Power installation has not been established for this distribution. For a project-scoped suite, install all seven skill folders under `.kiro/skills/` using the project recipe below. That is explicitly the skill-set fallback, not evidence of a native project Power. Kiro CLI V3 may share configuration with the IDE, but a CLI result is not a substitute for IDE activation evidence.


## Selected skills: project and user scope

Inspect existing selected directories before confirming any installation. The leading npm `--yes` only obtains the CLI; Skills remains interactive. Use `--copy` so updates are explicit and Windows symlink privileges are not required.

One independent skill in the selected project:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill natural-language-report-writer --agent kiro-cli --copy
```

The same skill for your user account:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill natural-language-report-writer --agent kiro-cli --copy --global
```

The complete available skill set in this project:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill $toolkitSkills --agent kiro-cli --copy
```

The same set for your user account:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill $toolkitSkills --agent kiro-cli --copy --global
```

For the entry alone select `using-devcraft-toolkit git-working-directory-policy git-safety-check` explicitly; for preflight select `git-safety-check git-working-directory-policy`. The installer does not resolve these custom dependencies.

## Manual copying and destinations

| Scope | Complete-folder destination |
| --- | --- |
| Project | `.kiro/skills/<skill-name>/` under the selected project |
| User/global | `~/.kiro/skills/<skill-name>/` |

Copy each selected `skills/<skill-name>/` folder, including all local `references/` and `assets/`. Inspect every destination before copying, stop on collisions, and obtain replacement authorization before changing existing content. Preserve unrelated directories.

Shared roots can be discovered by another client. Selecting `--agent kiro-cli` does not guarantee exclusive visibility. Check the actual target directory, the CLI's canonical store if present, and its project/user lock files.

## Verify discovery and scope

Open Agent Steering & Skills in Kiro IDE, inspect discovery, then invoke the selected skill using its displayed slash command and read one bundled resource. The external installer's selector is named kiro-cli, but copying to these directories does not establish IDE loading.

Test project scope against a second unrelated project and test user scope across both. Inspect resource reads and the invoked installation's identity, not just the existence of folders. Existing personal and project copies may have different precedence in different clients; ask for an installation choice if ownership is ambiguous. Installation grants no extra workflow permissions.

## Standalone update and removal

For a local source, explicitly re-run the selected install command after inspecting changes and authorizing replacement. Verify that copied resources changed and unrelated files did not. Do not assume copied skills track source edits.

For remote tracked sources, inspect `npx --yes skills@1.7.4 update --help` and the recorded lock/source before updating. Automatic remote updating was not substituted for local-source replacement in the filesystem evaluation.

Remove only the named project installation:

```powershell
npx --yes skills@1.7.4 remove natural-language-report-writer --agent kiro-cli
```

For the user installation, add `--global`. The remove operation may also affect its canonical store and lock entry; inspect those observed effects, preserve unrelated skills, and do not manually delete internal caches.

## Validation status

See [filesystem evidence](../../tests/integration/distribution/evaluations/2026-10-23-installation/filesystem.md) and [compatibility limits](../compatibility.md). CLI and manual-copy results establish file placement/resources only. Native discovery, activation, control-project visibility, and native lifecycle results require a real isolated Kiro IDE session; a blocked or unrun case remains explicit.

Official procedures: [Power installation](https://kiro.dev/docs/powers/installation/) and [skill discovery roots](https://kiro.dev/docs/skills/). The IDE rows remain blocked pending an isolated Kiro IDE session.

[Per-scope native results and remaining gates](../../tests/integration/distribution/evaluations/2026-10-23-installation/native.md) distinguish registry observations from authenticated activation.
