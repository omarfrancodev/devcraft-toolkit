# Local development and reference installation

These procedures are for working on the package or installing complete folders manually. Consumers normally use the [remote native suite](../installation.md); [individual skills](individual-skills.md) are the optional selective route.

## Local checkout

Clone the repository when you intend to develop it, then select that checkout explicitly in PowerShell:

```powershell
$toolkitSource = (Resolve-Path -LiteralPath (Read-Host 'Path to the Devcraft Toolkit checkout')).Path
```

It must contain root `plugin.json`, both marketplace adapters and the complete `skills/` tree.

- Codex: `codex plugin marketplace add "$toolkitSource"`, then `codex plugin add devcraft-toolkit@devcraft-toolkit`. Follow the target guide's user/project enablement rules. Git marketplace upgrade rejects a local-directory source; update the selected source and restart/reload as directed, then verify resources.
- Claude: `claude plugin marketplace add "$toolkitSource"`, then install the qualified plugin with explicit `--scope user` or `--scope project`. The observed client reads directly from the folder: updates report nothing to fetch and edits take effect at session start or `/reload-plugins`.
- Copilot in VS Code: merge the selected absolute directory into experimental `chat.pluginLocations` with value `true`. Preserve other entries; `false` disables that registration. Generate a fragment with `@{ 'chat.pluginLocations' = @{ $toolkitSource = $true } } | ConvertTo-Json -Depth 3`.
- Copilot CLI: `copilot plugin marketplace add "$toolkitSource"` then install the qualified suite. Use a disposable user/container; see [CLI scope and lifecycle](copilot-cli.md).
- Kiro IDE: Powers > Add Custom Power > Import power from a folder; choose the package root. Do not infer project-only isolation.
- Kiro CLI V3: `kiro-cli powers install "$toolkitSource"` accepts a local Power directory in the inspected interface; verify actual V3 discovery separately. This local route does not establish arbitrary GitHub URL support.
- Kiro Crew: copy complete chosen folders into an owned Crew store or selected trusted project, then inspect existing-agent discovery. A local Power directory is not a Crew import. See [Crew source/scope rules](kiro-crew.md).

For local selective testing, the optional Skills CLI accepts the same `$toolkitSource` with the [explicit selections and target/scope](individual-skills.md). Local-source observations do not prove remote acquisition.

## Manual complete-folder copying

Choose the full dependency closure from the individual guide. Copy each selected `skills/<skill-name>/` folder to its documented project/user root, including every `references/` and `assets/` resource. Stop on collisions until replacement is explicitly authorized; preserve unrelated directories. Installed skills do not require the catalog, root docs, scripts or tests.

For a source-only ZIP, download the archive and SHA256SUMS.txt from the [release page](https://github.com/omarfrancodev/devcraft-toolkit/releases), verify the checksum and extract it before copying. The published preview.1 has no native metadata; a source ZIP is not a plugin install.

## Developer validation

Use Python 3.11+ and the isolated development dependencies in requirements-dev.txt. These checks do not install the product:

```sh
python -B -m unittest discover -s tests -p "test_*.py" -v
python -B scripts/validate_repository.py --root .
python -B -m scripts.validate_distribution --root .
git diff --check
```

Claude's metadata checks are `claude plugin validate .claude-plugin/plugin.json --json --strict` and `claude plugin validate .claude-plugin/marketplace.json --json --strict`. Accepted metadata is not native activation.

Installation tests require disposable actual users/containers or verified client isolation, selected/control projects and sanitized retained evidence. Never test global operations against a maintainer's personal profile or copy authentication stores.

## Current release resources

Release `0.1.0-preview.8` contains eighteen available folders, including git-create-work-branch and git-publish-work. Select a checkout/revision that actually contains them; preview.7 contains sixteen. In individual/full-set test recipes, set `$toolkitSource` to that checkout's absolute path before selecting the current names. This is a contributor validation route; complete native remote suite installation remains the primary consumer route. Copy complete owner folders plus explicit mandatory and selected conditional closures. No root inventory is installed as a runtime dependency.

The [metadata guide](metadata.md) records supported fields and native validation limits by client.
