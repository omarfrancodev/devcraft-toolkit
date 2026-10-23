# Kiro Crew installation

## Import the complete remote skill set

Use Crew's native GitHub skill importer with the existing default agent.
No toolkit agent template, App, crewmate or Power registration is required
by this route. IDE/CLI Power inheritance into Crew is not established here.

1. Open Settings > Skills > Discover.
2. Enter `omarfrancodev/devcraft-toolkit`, or the
   [existing preview source](preview.md#kiro-crew) before integration.
3. Select/import all seven available skill directories. The interface may confirm
   each import separately; this is a complete skill set, not an atomic plugin.
4. Inspect each imported source revision, actual discovery path and all bundled
   references/assets. The set must include the entry and both of its dependencies.
5. In the existing default agent, inspect discovery and request a supported task
   through `using-devcraft-toolkit`. Observe the actual resource reads.

The [selection table](individual-skills.md#explicit-dependency-selection) lists
the seven names. Planned capabilities have no installable directories. Native
import needs no Node.js, external Skills CLI or user-managed checkout.
A registry preview through `skill_fetch` reads only the main instruction file;
it is not installation of sibling resources.

## User store, project scope and existing agents

Crew's default user store is `~/.kiro/crew/skills/`. GitHub imports use
source-specific subdirectories under `github/`; inspect their actual paths
instead of guessing the generated suffix. Do not treat `~/.kiro/skills/`
or an IDE Power cache as proof that Crew has the toolkit.

For project use, install the explicit complete set into the active project's
`.kiro/skills/`, using the [project fallback](individual-skills.md#complete-skill-set-fallback).
Enable project skills and grant trust to that exact active project in Crew.
Inspect a control project too. Existing global imports can remain available:
project folders do not automatically suppress them.

The default agent without restrictive mappings can discover the imported set.
If the selected existing agent has explicit skill mappings, inspect whether
all required skills are included. Report unavailable capabilities rather than
changing the agent, switching models or creating a template automatically.
Different Crew/backend versions need their own session validation.

## Individual import, update and removal

For an individual capability, Discover accepts e.g.
`omarfrancodev/devcraft-toolkit:skills/natural-language-report-writer`.
Import every dependency separately when using the entry or preflight; the
importer does not resolve this repository's catalog.

Imports are snapshots pinned to their resolved commit, not branch subscriptions.
Re-import the same source/path to review and explicitly approve a replacement.
Inspect `.skill-import-source.json` and the actual resource set; a GitHub push
alone does not update the installed copy.

Use the installed version's supported Skills management to remove only the
chosen imports. For manual copies, [complete-folder reference](development.md#manual-complete-folder-copying)
applies. Preserve other sources and check existing agent mappings before removal.
There is no native toolkit Power/App uninstall to run for this skill-set route.

## Evidence

This is a documented native importer route, not a completed Crew session test.
[Client evidence](../../tests/integration/distribution/evaluations/2026-10-23-client-expansion/clients.md)
keeps import, discovery, resources, active-agent scope and lifecycle distinct.
No template is necessary for the documented default-agent use case; no claim is
made that importing skills gives every restricted agent access.

Official references: [native import](https://kiro.dev/docs/crew/capabilities/skills/),
[source/resource rules](https://github.com/kirodotdev/KiroCrew/blob/main/src/kiro_crew/docs/skills.md)
and [existing agent mappings](https://github.com/kirodotdev/KiroCrew/blob/main/src/kiro_crew/docs/agents.md).
