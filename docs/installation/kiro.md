# Kiro IDE installation

## Install the complete remote suite as a Power

The integrated default branch contains the corrected `plugin.json` and canonical skills. In Kiro IDE:

1. Open Powers > Add Custom Power.
2. Select Import power from GitHub.
3. Enter `https://github.com/omarfrancodev/devcraft-toolkit`.
4. Review and install the Power, then inspect its skills.

Kiro's Agent Plugins format uses the root manifest and the canonical `skills/` tree. There is no manual clone, extra POWER.md or third-party Skills CLI in this normal route.

## Activation keywords and native validation

The root manifest includes `keywords`: `git`, `commit`, `report` and
`validation`. The [portable schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)
makes this field optional, while [Kiro's Power authoring guide](https://kiro.dev/docs/powers/create/)
lists it as required for activation. This package follows Kiro's guidance; its
offline validator requires a non-empty array of non-empty strings. Consumers
do not need to edit the downloaded manifest. The Claude compatibility manifest
also carries discovery keywords with client-specific semantics.

The historical b05a8c4 payload predates this correction and omits these keywords.
Its earlier registration/resource checks do not validate the new manifest.
Keywords alone do not prove import or trigger matching. Native validation must
still import the corrected Power in an isolated Kiro IDE, observe its skill
inventory and activate it with a relevant request that reads bundled resources;
compare an unrelated control project. These checks remain pending under
[compatibility](../compatibility.md#kiro-keywords-correction-f001).

The reviewed import interface does not establish how to pin a Git ref. Do not assume a branch/tree URL works: the [release source note](../releases/v0.1.0-preview.8.md#version-pinned-sources) keeps pinned Power import unverified.

## CLI and Crew are separate clients

[Kiro CLI V3](kiro-cli.md) documents pickup of IDE-installed Powers under the same user. Verify discovery/invocation in each session separately. [Kiro Crew](kiro-crew.md) uses its own complete skill import; inheritance of this Power into Crew is not established. No toolkit agent template is needed for the documented Crew default-agent route.

## Project use

A project-only native Power installation is `not_supported` under the approved interface. For the complete suite's capabilities in one project, use the [complete project skill-set fallback](individual-skills.md#complete-skill-set-fallback), which copies all available folders to `.kiro/skills/`. This is a separately labeled skill-set route, not native Power isolation.

Use the Power in the IDE and verify the actual discovered skills, resources and scope. Kiro CLI file placement does not establish Kiro IDE activation.

## Update and remove

Use the installed Power's update/removal controls in Kiro IDE and observe scope/reload requirements. Keep unrelated skills and settings intact. Do not invent CLI scope/ref flags for Power management.

## Optional routes and evidence

[Individual skills](individual-skills.md) use the third-party selector `kiro-cli` to write Kiro's shared folders. [Local development](development.md) covers folder imports separately.

The [official Power installation guide](https://kiro.dev/docs/powers/installation/) establishes the remote import route. No isolated Kiro IDE session was available; [native activation remains blocked](../compatibility.md).

## Presentation metadata

The portable manifest includes homepage and repository links as well as the
existing author, description and activation keywords. Kiro IDE 1.4.26+ documents
installed-manifest metadata in the Power list and details view. No custom icon
or category field is established by the reviewed Power authoring format; the
OpenAI logo extension does not configure Kiro. See [metadata across clients](metadata.md)
for supported fields and the separate CLI/Crew routes.
