# Alternative: individual skills

Use this route only when you want selected capabilities instead of the native suite, or the explicit project skill-set fallback. For the usual complete installation, start with [the native suite](../installation.md).

## Remote source and requirements

The default remote source applies after package integration. Before then, use the [pinned preview source](preview.md#individual-skills-and-project-fallback). CLI examples use Node.js >=22.20.0, npm and Skills CLI 1.7.4. Complete-folder manual copying is available in [development/reference](development.md#manual-complete-folder-copying).

Run from the selected project's root. This PowerShell example selects Codex; choose the documented selector for your client:

| Client | Selector | Project folder | Manual user folder |
| --- | --- | --- | --- |
| Codex | `codex` | `.agents/skills/` | `~/.agents/skills/` |
| Copilot in VS Code | `github-copilot` | `.agents/skills/` | `~/.copilot/skills/` |
| Claude Code | `claude-code` | `.claude/skills/` | `~/.claude/skills/` |
| Kiro IDE | `kiro-cli` | `.kiro/skills/` | `~/.kiro/skills/` |

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

The installer does not resolve `catalog.json` dependencies. A bare entry installs only the entry. Supply every listed name explicitly. All resources, including local references and assets, belong to the installed folder. Ten planned capabilities have no installable SKILL.md.

## Complete skill-set fallback

When the native project suite is unavailable (notably Kiro's project Power), select all seven skills explicitly:

```powershell
$toolkitSkills = @('using-devcraft-toolkit', 'git-working-directory-policy', 'git-safety-check', 'conventional-commits-style', 'todo-workflow-controller', 'natural-language-report-writer', 'validation-discovery')
npx --yes skills@1.7.4 add "$toolkitSource" --skill $toolkitSkills --agent "$toolkitAgent" --copy
```

For Kiro set `$toolkitAgent = 'kiro-cli'` before this command; the project destination is `.kiro/skills/`. Add `--global` for a user skill set. This delivers folders, not a native plugin/Power registration.

## Discovery, collisions and lifecycle

Start/reload the client and inspect the discovered installation before invocation. A target selector is not access control: clients can share discovery roots. Skills CLI 1.7.4 wrote Copilot global copies to `~/.agents/skills/`; the manual Copilot path above is independently supported. Inspect actual output, shared storage and locks (`skills-lock.json` in projects and user `.agents/.skill-lock.json`).

Do not silently choose between a plugin and a standalone copy with the same name. Keep both until the user chooses the installation.

For copy updates, inspect the selected newer source and authorize replacement, then explicitly add it again. For remotely tracked updates inspect `skills@1.7.4 update --help` and the recorded source/lock before acting. Remove only the named skill with the same selector and scope, for example `npx --yes skills@1.7.4 remove natural-language-report-writer --agent codex`; add `--global` for user removal. Preserve other scopes, locks and unrelated content.

[Local filesystem evidence](../../tests/integration/distribution/evaluations/2026-10-23-installation/filesystem.md) and [compatibility limits](../compatibility.md) distinguish file placement from native activation.
