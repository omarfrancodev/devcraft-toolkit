# Kiro IDE installation

## Install the complete remote suite as a Power

The repository's default branch must contain `plugin.json`; this recipe applies [after integration](../installation.md). In Kiro IDE:

1. Open Powers > Add Custom Power.
2. Select Import power from GitHub.
3. Enter `https://github.com/omarfrancodev/devcraft-toolkit`.
4. Review and install the Power, then inspect its skills.

Kiro's Agent Plugins format uses the root manifest and the canonical `skills/` tree. There is no manual clone, extra POWER.md or third-party Skills CLI in this normal route.

The reviewed import interface does not establish how to pin a Git ref. Before integration, do not assume a branch/tree URL works: the [preview source note](preview.md#kiro-ide) keeps this native check unverified.

## CLI and Crew are separate clients

[Kiro CLI V3](kiro-cli.md) documents pickup of IDE-installed Powers under the same user. Verify discovery/invocation in each session separately. [Kiro Crew](kiro-crew.md) uses its own complete skill import; inheritance of this Power into Crew is not established. No toolkit agent template is needed for the documented Crew default-agent route.

## Project use

A project-only native Power installation is `not_supported` under the approved interface. For the complete suite's capabilities in one project, use the [complete project skill-set fallback](individual-skills.md#complete-skill-set-fallback), which copies all seven folders to `.kiro/skills/`. This is a separately labeled skill-set route, not native Power isolation.

Use the Power in the IDE and verify the actual discovered skills, resources and scope. Kiro CLI file placement does not establish Kiro IDE activation.

## Update and remove

Use the installed Power's update/removal controls in Kiro IDE and observe scope/reload requirements. Keep unrelated skills and settings intact. Do not invent CLI scope/ref flags for Power management.

## Optional routes and evidence

[Individual skills](individual-skills.md) use the third-party selector `kiro-cli` to write Kiro's shared folders. [Local development](development.md) covers folder imports separately.

The [official Power installation guide](https://kiro.dev/docs/powers/installation/) establishes the remote import route. No isolated Kiro IDE session was available; [native activation remains blocked](../compatibility.md).
