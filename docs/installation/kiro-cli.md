# Kiro CLI installation

## Complete suite through a shared Power

Use the **V3 harness**. Install the remote Power using the
[Kiro IDE procedure](kiro.md), then start CLI V3 under the same user:

```sh
kiro-cli --v3
```

Inspect `/powers` and `/config skills` in that session. Confirm discovery of
the seven toolkit skills and their resources before invoking the entry. Kiro
documents pickup of IDE-installed Powers by CLI V3; CLI and IDE activation
still require independent checks.

The [root keywords contract](kiro.md#activation-keywords-and-native-validation) also applies to this Power. Correct metadata is not proof of CLI activation; old pinned registration probes predate the correction.

CLI 2.25.0 introduced `kiro-cli powers install <name|path>` and uninstall for
catalog names/local directories. The inspected 2.28.0 help retains that
interface. Devcraft Toolkit is not claimed to be in the curated catalog.
Arbitrary GitHub URL installation, ref flags and project-only Power scope are
not established by those arguments.

## Complete remote set without an IDE

If you use only CLI, use the
[complete skill-set fallback](individual-skills.md#complete-skill-set-fallback).
Select all seven names with `--agent kiro-cli`; use `--global` for user scope
or run in the chosen project for `.kiro/skills/`. This route needs Node/npm and
the pinned external Skills CLI. It requires no user-managed clone.

This provides the complete capabilities as folders, **not a native Power**.
Project-only Power installation is `not_supported` under this contract;
the project skill set is the documented alternative. Check the active and
unrelated control project, including any globally installed copy.

## Discovery, update and removal

Inspect actual V3 discovery and a bundled reference/template read. A third-party
installer selector or correct files cannot prove native activation. CLI V2 is
outside this guide's Power contract.

Manage a shared Power from the interface that installed it. CLI documents
`kiro-cli powers uninstall <name>`; do not assume removal is confined to the
current project or harmless to the IDE's shared installation. Verify actual
ownership and scope first. Use the IDE's remote update controls for its Power.

For folder copies follow [individual lifecycle](individual-skills.md#discovery-collisions-and-lifecycle):
inspect the new source, authorize replacement and remove only the chosen set
in the original scope. Preserve unrelated content. [Development](development.md)
covers local Power installation separately.

## Evidence

[Compatibility](../compatibility.md) distinguishes inspected CLI version/help,
remote file copies and real sessions. CLI activation does not pass IDE or Crew.
No authenticated CLI V3 session has passed in an isolated environment here.

Official references: [V3 discovery](https://kiro.dev/docs/cli/v3/new-features/),
[Power management from CLI 2.25.0](https://kiro.dev/changelog/cli/2-25/)
and [skill scopes](https://kiro.dev/docs/skills/).
