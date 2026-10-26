# Alternative: individual skills

Use this route only when you want selected capabilities instead of the native suite, or the explicit project skill-set fallback. For the usual complete installation, start with [the native suite](../installation.md).

## Remote source and requirements

The default remote source uses the integrated package. For a fixed version use the [release-pinned source](../releases/v0.1.0-preview.6.md#version-pinned-sources). CLI examples use Node.js >=22.20.0, npm and Skills CLI 1.7.4. Complete-folder manual copying is available in [development/reference](development.md#manual-complete-folder-copying).

Crew uses its [native individual/full importer](kiro-crew.md), not an assumed external installer selector. Its default user store is `~/.kiro/crew/skills/`; active-project `.kiro/skills/` requires Crew's project-skill enablement and trust. Use exact imported paths and dependencies.

Run from the selected project's root. This PowerShell example selects Codex; choose the documented selector for your client:

| Client | Selector | Project folder | Manual user folder |
| --- | --- | --- | --- |
| Codex | `codex` | `.agents/skills/` | `~/.agents/skills/` |
| Copilot CLI and VS Code | `github-copilot` | `.agents/skills/` | `~/.copilot/skills/` |
| Claude Code | `claude-code` | `.claude/skills/` | `~/.claude/skills/` |
| Kiro CLI V3 and IDE | `kiro-cli` | `.kiro/skills/` | `~/.kiro/skills/` |

```powershell
$toolkitSource = 'https://github.com/omarfrancodev/devcraft-toolkit'
$toolkitAgent = 'codex'
npx --yes skills@1.7.4 add "$toolkitSource" --skill natural-language-report-writer --agent "$toolkitAgent" --copy
```

For the same skill in user/global scope:

```powershell
npx --yes skills@1.7.4 add "$toolkitSource" --skill natural-language-report-writer --agent "$toolkitAgent" --copy --global
```

The leading npm `--yes` permits acquisition of the pinned CLI; Skills remains interactive. Inspect the selected destinations before confirming and explicitly authorize replacement of existing content. `--copy` avoids Windows symlink privilege requirements; source changes do not automatically update copies.

## Source inventory and dependency selection

Current candidate source `0.1.0-preview.7` is unpublished and has sixteen available skills. The table and complete selection below describe this candidate. Until it is integrated, the default GitHub/main source and pinned preview.6 have fourteen and do not contain hosted management/promotion. For these new selections, choose a candidate checkout that actually contains both folders:

```powershell
$toolkitSource = (Resolve-Path -LiteralPath (Read-Host 'Path to the candidate Devcraft Toolkit checkout')).Path
```

Use the same local source with the [development native-suite route](development.md) when testing the complete candidate plugin. Source selection does not establish native activation. Published preview.6 retains fourteen; preview.5 twelve; preview.4 eleven; preview.3 nine; preview.2 seven. Old tags retain their original inventories and resource evidence.

## Explicit dependency selection

| Requested skill | Names to pass after --skill |
| --- | --- |
| `using-devcraft-toolkit` | `using-devcraft-toolkit git-working-directory-policy git-safety-check` |
| `git-safety-check` | `git-safety-check git-working-directory-policy` |
| `git-working-directory-policy` | That name only |
| `conventional-commits-style` | That name only |
| `todo-workflow-controller` | That name only |
| `natural-language-report-writer` | That name only |
| `validation-discovery` | That name only |
| `git-sync-branch` | `git-sync-branch git-working-directory-policy git-safety-check` |
| `git-publish-changes` | `git-publish-changes git-working-directory-policy git-safety-check` |
| `git-manage-pull-request` | `git-manage-pull-request git-working-directory-policy` |
| `git-promote` | `git-promote git-manage-pull-request git-working-directory-policy` |
| `git-activity-report` | `git-activity-report git-working-directory-policy natural-language-report-writer` |
| `git-analyze-changes` | `git-analyze-changes git-working-directory-policy` |
| `git-plan-commits` | `git-plan-commits git-analyze-changes git-working-directory-policy conventional-commits-style` |
| `git-stage-changes` | `git-stage-changes git-analyze-changes git-safety-check git-working-directory-policy` |
| `git-commit-builder` | `git-commit-builder git-plan-commits git-stage-changes git-safety-check validation-discovery todo-workflow-controller git-analyze-changes git-working-directory-policy conventional-commits-style` |

The installer does not resolve `catalog.json` dependencies. A bare entry installs only the entry. Supply every listed name explicitly. All resources, including local references and assets, belong to the installed folder. The remaining planned `git-publish-work` has no installable SKILL.md.

## Complete skill-set fallback

When the native project suite is unavailable (notably Kiro's project Power), select all sixteen candidate skills explicitly from the selected candidate source:

```powershell
$toolkitSkills = @('using-devcraft-toolkit', 'git-working-directory-policy', 'git-safety-check', 'conventional-commits-style', 'todo-workflow-controller', 'natural-language-report-writer', 'validation-discovery', 'git-analyze-changes', 'git-plan-commits', 'git-stage-changes', 'git-commit-builder', 'git-activity-report', 'git-sync-branch', 'git-publish-changes', 'git-manage-pull-request', 'git-promote')
npx --yes skills@1.7.4 add "$toolkitSource" --skill $toolkitSkills --agent "$toolkitAgent" --copy
```

For Kiro CLI V3/IDE set `$toolkitAgent = 'kiro-cli'` before this command; the project destination is `.kiro/skills/`. Crew can use those project folders only after enabling/trusting the active project; this does not install into Crew's own user store. Add `--global` for a user skill set. This delivers folders, not a native plugin/Power registration.

## Discovery, collisions and lifecycle

Start/reload the client and inspect the discovered installation before invocation. A target selector is not access control: clients can share discovery roots. Skills CLI 1.7.4 wrote Copilot global copies to `~/.agents/skills/`; the manual Copilot path above is independently supported. Inspect actual output, shared storage and locks (`skills-lock.json` in projects and user `.agents/.skill-lock.json`).

Do not silently choose between a plugin and a standalone copy with the same name. Keep both until the user chooses the installation.

For copy updates, inspect the selected newer source and authorize replacement, then explicitly add it again. For remotely tracked updates inspect `skills@1.7.4 update --help` and the recorded source/lock before acting. Remove only the named skill with the same selector and scope, for example `npx --yes skills@1.7.4 remove natural-language-report-writer --agent codex`; add `--global` for user removal. Preserve other scopes, locks and unrelated content.

[Local filesystem evidence](../../tests/integration/distribution/evaluations/2026-10-23-installation/filesystem.md) and [compatibility limits](../compatibility.md) distinguish file placement from native activation.
