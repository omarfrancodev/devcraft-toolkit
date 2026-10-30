# Plugin metadata across clients

The suite keeps portable identity in root `plugin.json`. The project homepage,
repository, description, author and keywords are available to compatible
Agent Plugins consumers. `name` remains `devcraft-toolkit`; a display label does
not change installation identifiers or skill namespaces.

Presentation is client-specific. The same asset can be reused where a client
documents an image field, but an OpenAI extension does not configure other clients.

| Client | Maintained metadata | Image and category limits |
| --- | --- | --- |
| Codex | `extensions.com.openai.interface` and `.agents/plugins/marketplace.json` | `Developer Tools` in both locations; `logo` and `composerIcon` point to the packaged PNG. |
| Claude Code | `.claude-plugin/plugin.json`: `displayName`, homepage, repository, keywords and `icon`; shared marketplace category and tags | Anthropic documents `icon` for its directory, not runtime loading. The field does not establish a custom icon in Claude Code's UI. |
| Copilot CLI | Portable identity and links; `.claude-plugin/marketplace.json` category, tags and marketplace description | No image override is established by the reviewed CLI reference. The OpenAI logo fields are not Copilot settings. |
| Copilot in VS Code | Portable metadata and the shared marketplace | No plugin-specific logo field is established by the reviewed authoring reference. Catalog fields do not prove that a particular UI renders them. |
| Kiro IDE | Portable description, author, repository, homepage and activation keywords | The reviewed Power format has no documented custom-logo or category field. Installed metadata display is documented for IDE 1.4.26+. |
| Kiro CLI V3 | The shared Power's portable manifest, or standalone skill metadata for the folder fallback | Power discovery is separate from IDE display. No CLI logo override is claimed. |
| Kiro Crew | Imported skills' names and descriptions | The documented route imports skill folders, not the suite manifest or its logo/category. No App or agent template is added. |

The shared marketplace includes `metadata.description` and its single plugin
entry's `category: Developer Tools` and discovery `tags`. Claude's `icon` stays
in the plugin manifest; it is not a supported shared marketplace-entry field.
Claude display metadata stays out of the portable root: Agent Plugins 1.0 rejects
unknown top-level fields such as `icon`, `displayName` and `category`.

The PNG and editable SVG are in root `assets/`. Icon paths resolve from the plugin
root. They do not create a dependency from individually installed skills to
repository-level assets.

## Validation and updates

The offline distribution validator checks this package's finite contract,
including both clients' declared PNG resources and metadata placement. It is not
a complete implementation of every external schema or a native UI test.

Claude Code 2.1.300 accepts the updated manifest and marketplace with `--strict`;
see the [metadata evaluation](../../tests/integration/distribution/evaluations/2026-10-30-plugin-metadata/native.md).
Anthropic documents recognition of directory fields by its validator from
2.1.281; older validators can warn about `icon`. No new minimum version or visual
compatibility claim is inferred for other clients.

Publish an updated source and use the owning client's update/reload flow before
checking its UI. Pinned sources stay pinned until deliberately changed. Directory
submission and release publication remain separate operations.

## Official references

- [Agent Plugins 1.0 schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)
- [OpenAI package guide](https://developers.openai.com/plugins/build/plugins)
- [Claude manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference)
- [Claude marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference)
- [Copilot CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference)
- [VS Code plugin authoring reference](https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference)
- [Kiro Power authoring](https://kiro.dev/docs/powers/create/)
- [Kiro installed metadata](https://kiro.dev/docs/powers/installation/)
- [Kiro Crew skill import](https://kiro.dev/docs/crew/capabilities/skills/)
