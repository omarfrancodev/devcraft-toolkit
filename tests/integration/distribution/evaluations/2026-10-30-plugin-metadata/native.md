# Cross-client metadata evaluation

Date: 2026-10-30. This evaluation checks the presentation increment on top of
`0c42e1379dcccde33372bc21ef65df10df6406c9`. The [native report](claude-validation.json)
binds each checked manifest to its SHA-256, preserving paths as `<package-root>`.
Historical installation evaluations remain unchanged.

## Observed native checks

Claude Code **2.1.300** ran these from the package root:

```sh
claude plugin validate .claude-plugin/plugin.json --json --strict
claude plugin validate .claude-plugin/marketplace.json --json --strict
```

Both exited 0 with `success: true`, no manifest errors and no schema warnings.
The plugin check also returned non-gating README installation advice; that is
retained in the report and is not a passed installation/session check. Baseline
strict marketplace validation had warned about its missing description; the
maintained `metadata.description` resolves that warning.

The installed Copilot CLI reported **1.0.91** and exposed no plugin-validation
subcommand in its help. Kiro CLI reported **2.28.0**, which is not CLI V3.
Neither was installed, updated, or invoked as an authenticated skill session.
No personal plugin registrations or client settings were changed.

## Contract and coverage

- Portable root: homepage/repository links, existing author/description/keywords,
  and OpenAI-specific presentation only inside its extension namespace.
- Claude: display name, common project metadata, discovery keywords and packaged
  directory icon. The icon is not a claim about Claude Code runtime UI rendering.
- Shared Claude/Copilot catalog: category/tags plus marketplace description.
- Kiro IDE/CLI: documented portable Power fields only. No undocumented branding
  extension, legacy `POWER.md`, App or agent template is introduced.
- Crew: the skill-folder import route remains separate from suite metadata.

Offline package regressions exercise missing/malformed metadata, asset paths,
image dimensions/chunk checks and incorrect field placement. They do not emulate
client rendering. See [the client field matrix](../../../../../docs/installation/metadata.md)
for reviewed official sources and per-client limitations.

No client UI has been checked against this new package, and no cross-client
logo/category display, authenticated invocation, scope isolation or update
lifecycle is established by these results.
