# Remote preview sources

Before package metadata is integrated into the default branch, normal repository-source recipes cannot install it from that branch. Codex and applicable filesystem recipes use the existing public source revision `b05a8c4367dc02e33ac9d19a8eb98e0bdb31c04e` where the client supports refs. It contains both marketplaces and the seven-skill candidate; it is not a release tag or the source-only published preview.1.

## Codex

```sh
codex plugin marketplace add omarfrancodev/devcraft-toolkit --ref b05a8c4367dc02e33ac9d19a8eb98e0bdb31c04e
codex plugin add devcraft-toolkit@devcraft-toolkit
```

Then follow the [Codex scope guide](codex.md). This registration remains pinned until deliberately changed.

## Claude Code

```sh
claude plugin marketplace add https://github.com/omarfrancodev/devcraft-toolkit.git#docs/distribution-installation
claude plugin install devcraft-toolkit@devcraft-toolkit --scope user
```

Claude Code 2.1.300 clones a branch/tag here; passing a commit SHA failed. This preview branch is mutable, not an immutable pin. Its resolved revision is recorded in the remote evaluation. After integration use the normal repository source. Use `--scope project` for the selected project instead. See [Claude scope and lifecycle](claude-code.md).

## Copilot in VS Code

Add `omarfrancodev/devcraft-toolkit#b05a8c4367dc02e33ac9d19a8eb98e0bdb31c04e` to `chat.plugins.marketplaces`, preserving existing entries, then install through the marketplace UI described in [the target guide](copilot-vscode.md). Its isolated native session remains unverified.

## Kiro IDE

The reviewed GitHub import UI does not establish pinned-ref syntax. Do not assume this source can be imported as a branch/tree URL. The default-source native Power recipe applies after integration; for pre-integration project use select the remote complete skill set below. IDE activation remains unverified.

## Individual skills and project fallback

In the [individual guide](individual-skills.md), replace only the source variable with this concrete remote source, keeping explicit selection, target and scope:

```powershell
$toolkitSource = 'https://github.com/omarfrancodev/devcraft-toolkit/tree/b05a8c4367dc02e33ac9d19a8eb98e0bdb31c04e'
```

A native-suite registration or correct copied files does not establish authenticated invocation. See [compatibility](../compatibility.md) for actual results and remaining gates.
