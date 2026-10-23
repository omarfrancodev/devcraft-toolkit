# Installation

This checkout packages the seven available skills as one native plugin and as individually selectable folders. The metadata version is the unreleased candidate `0.1.0-preview.2`. The published `v0.1.0-preview.1` remains a source-only preview and has no plugin manifests; do not use that tag as a native plugin source.

## Choose delivery, target, and scope

| Choice | Meaning |
| --- | --- |
| Native suite | One `devcraft-toolkit` package containing all seven available skills |
| Selected skills | Complete individual folders plus the dependency closure listed below |
| Project | Files or native enablement for the selected repository/workspace |
| User/global | Files or enablement across that local user's projects |

A target selector chooses destinations, not exclusive access. Several clients discover shared roots such as `.agents/skills/`. Native installation storage and project-only enablement are separate concepts.

Target guides provide concrete local-checkout recipes and client-specific native instructions:

- [Codex](installation/codex.md)
- [GitHub Copilot in VS Code](installation/copilot-vscode.md)
- [Claude Code](installation/claude-code.md)
- [Kiro IDE](installation/kiro.md)

Use a checkout containing `plugin.json` and `.claude-plugin/plugin.json`. From the chosen project's root, PowerShell users can select that existing checkout without inventing a path:

```powershell
$toolkitSource = (Resolve-Path -LiteralPath (Read-Host 'Path to the Devcraft Toolkit checkout')).Path
```

The optional CLI recipes use `skills@1.7.4` and require Node.js `>=22.20.0` plus npm. The leading `npx --yes` permits npm to obtain that pinned CLI; no trailing Skills `--yes` is supplied in user recipes, so its installation confirmation remains interactive. Inspect existing selected destinations before confirming. Do not overwrite personal skills without explicitly authorizing replacement.

No Node.js installation is required for the manual complete-folder route. Installation grants no authority to run the installed workflows or change repositories.

## Individual skill dependencies

| Requested capability | Explicit selection |
| --- | --- |
| Entry/composition | `using-devcraft-toolkit git-working-directory-policy git-safety-check` |
| Read-only Git preflight | `git-safety-check git-working-directory-policy` |
| Repository context | `git-working-directory-policy` |
| Commit-message formatting | `conventional-commits-style` |
| Progress tracking | `todo-workflow-controller` |
| Evidence-based reporting | `natural-language-report-writer` |
| Project validation | `validation-discovery` |

The external CLI does not resolve this repository's `catalog.json` dependencies. A bare entry selection installs only the entry; select the trio explicitly. Each optional shared capability works alone. The entry reports absent optional capabilities rather than installing or imitating them.

The complete available selection is:

```powershell
$toolkitSkills = @('using-devcraft-toolkit', 'git-working-directory-policy', 'git-safety-check', 'conventional-commits-style', 'todo-workflow-controller', 'natural-language-report-writer', 'validation-discovery')
```

Ten catalog entries remain planned and have no installable `SKILL.md`.

## Manual complete-folder route

Copy each selected directory from `skills/` to the guide's project or user destination, including all `references/` and `assets/`. A skill does not require root documentation, developer scripts, tests, or the catalog at runtime. Make the complete dependency selection before copying, and stop on a pre-existing destination until replacement is explicitly authorized.

For a source-only release, download its ZIP and `SHA256SUMS.txt` from the [release page](https://github.com/omarfrancodev/devcraft-toolkit/releases), verify the ZIP checksum and extract it first. A source ZIP is not itself a plugin installation. Published examples must use a ref that actually contains the native metadata; this checkout does not claim that the next release has been published.

## Discovery and verification

After installation start or reload the selected client as its guide describes. Inspect the client's discovered skill list, invoke a directly installed skill, and read one bundled resource. For the suite, also invoke the entry and check routing to a skill owned by this package. A copied directory or accepted manifest does not establish native discovery.

See [compatibility and limitations](compatibility.md) and the [installation evidence](../tests/integration/distribution/evaluations/2026-10-23-installation/filesystem.md). Filesystem checks and native activation are separate evidence levels.

## Updates, removal, and collisions

- Native suite: use the qualified identity `devcraft-toolkit@devcraft-toolkit` and the chosen client's update/remove UI or commands. Updating a marketplace does not by itself prove the installed plugin changed.
- Copied skills: after inspecting collisions and obtaining replacement authorization, explicitly install again from the selected newer checkout and verify the copied resources. This local-source replacement was exercised separately from automatic remote updates.
- Skills CLI: remove named skills with explicit target and scope. It may maintain `skills-lock.json` for project installations, a user lock under `.agents/`, and canonical shared skill storage. Inspect the actual effects rather than manually deleting its internal state.
- Do not install the same names from the suite and standalone sources without deciding which installation should serve the workflow. Client precedence varies; ambiguous ownership requires a choice.

## Development checks

The validation tools are developer-only. Use Python 3.11+ with `requirements-dev.txt` installed in an isolated Python environment:

```sh
python -B -m unittest discover -s tests -p "test_*.py" -v
python -B scripts/validate_repository.py --root .
python -B -m scripts.validate_distribution --root .
git diff --check
```

These commands do not install skills or establish compatibility with a client.
