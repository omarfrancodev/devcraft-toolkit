# Suite and Selective Skill Installation Design

**Date:** 2026-10-23
**Status:** Proposed design; installation implementation and compatibility validation are not executed.
**Scope:** Codex local clients, GitHub Copilot in VS Code, Claude Code local clients, and Kiro IDE.
**Related implementation plan:** [Installation plan](../plans/2026-10-23-distribution-installation.md).

## Intent and current state

Provide one maintained suite that users can adopt as a native plugin or as individually selected skills. Selection, harness, and scope are independent choices. A user must be able to install a usable set for one project or for their user account without installing planned capabilities.

The repository currently distributes seven available skills as complete folders and records ten planned capabilities. The first preview provides a source ZIP and manual copying guidance. It has no native plugin metadata or verified native installation matrix. This design does not describe those missing pieces as already shipped.

## Goals and non-goals

- Keep one canonical copy of each skill under `skills/<canonical-name>/`.
- Offer one native suite, `devcraft-toolkit`, plus selective installation with explicit dependency closures.
- Document user/global and project/workspace scope for every target, distinguishing installation storage from enablement.
- Verify resource integrity, discovery, routing, scope boundaries, and lifecycle operations without changing existing personal installations.
- Keep instructions, examples, templates, and documentation in English; invoked skills retain the user's resolved language.

New Git coordinators, CCR integration, external business integrations, release automation, automatic dependency resolution, public directory submission, cloud clients, and license selection are excluded. No MCP server, lifecycle hook, custom runtime installer, onboarding skill, or executable install hook is needed.

## Approaches and selected direction

1. Manual copying and selective CLI installation only: smallest change, but leaves the suite without native plugin discovery.
2. One shared skill tree with portable metadata, a Claude compatibility manifest, and small marketplace adapters: supports the requested adoption paths without duplicating instructions. This is the selected direction.
3. Independent packages or repositories per harness: creates synchronization and maintenance costs without changing the skill contracts.

The suite/individual direction was selected before this design. Metadata names, candidate version, file layout, and the fallback for unsupported native project scope are design proposals, not claims of prior implementation.

## Fixed package identity and file map

- Plugin name: `devcraft-toolkit`.
- Marketplace name: `devcraft-toolkit`; qualified native identity: `devcraft-toolkit@devcraft-toolkit`.
- Candidate package version: `0.1.0-preview.2`, unpublished. This work does not publish, move, or modify `v0.1.0-preview.1`.
- Author name: `omarfrancodev`. Do not add a license or invent contact metadata.

Planned files and responsibilities:

| Path | Responsibility |
| --- | --- |
| `plugin.json` | Canonical portable identity, version, description, and Agent Plugins schema marker |
| `.claude-plugin/plugin.json` | Minimal Claude metadata with identical name, version, and description |
| `.agents/plugins/marketplace.json` | Codex marketplace adapter pointing to the repository-root plugin |
| `.claude-plugin/marketplace.json` | Claude/Copilot marketplace adapter pointing to the same root |
| `skills/` | Existing seven canonical skill directories, unchanged by packaging |
| `scripts/validate_distribution.py` | Offline development validation of this distribution contract |
| `tests/repository/test_distribution_validation.py` | Metadata/inventory regression tests |
| `tests/integration/distribution/` | Installation scenarios and retained cross-skill evidence |
| `docs/installation.md` | Scope/selection overview, dependency table, manual fallback |
| `docs/installation/{codex,copilot-vscode,claude-code,kiro}.md` | Target-specific native and standalone procedures |

Do not create `.codex-plugin/`, `POWER.md`, copied skill trees, or a second package unless a separately reviewed compatibility finding requires one. The consulted interfaces support a root portable manifest for Codex, Copilot, and Kiro; Claude has an explicit compatibility manifest.

## Manifest and marketplace contract

Root `plugin.json` contains exactly the initial fields `$schema`, `name`, `version`, `description`, and `author`. The schema URI is `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`. Description is `Composable Git and development skills for coding agents.` Author is `{"name": "omarfrancodev"}`. Standard root `skills/` discovery exposes only available skills. Do not add empty connector configuration.

The Claude manifest contains `name`, `version`, `description`, and `author` with identical values. Omit a `skills` override because the standard directory already exists; adding the same directory again can duplicate component loading.

The Codex marketplace contains `name`, `interface.displayName` (`Devcraft Toolkit`), and one `plugins` entry. That entry has `name: devcraft-toolkit`, `source: {"source":"local","path":"./"}`, `policy: {"installation":"AVAILABLE","authentication":"ON_INSTALL"}`, and `category: Productivity`. The relative source resolves from the marketplace's repository root, not the manifest directory. The authentication policy does not add an authentication step to this connector-free package.

The Claude/Copilot marketplace contains `name`, `owner: {"name":"omarfrancodev"}`, and one `plugins` entry with `name: devcraft-toolkit`, `source: ./`, and the package description. Do not redeclare components or duplicate the package version there.

Both adapters target this same repository root. Adapter equality is semantic, not byte equality. No marketplace entry installs a planned capability or fetches custom catalog dependencies.

## Selection and dependency contract

The native suite includes every currently available skill. The selective path installs an explicitly enumerated set; external installers do not interpret `catalog.json` as a dependency resolver.

| Requested skill | Complete selected set |
| --- | --- |
| `using-devcraft-toolkit` | `using-devcraft-toolkit`, `git-working-directory-policy`, `git-safety-check` |
| `git-safety-check` | `git-safety-check`, `git-working-directory-policy` |
| `git-working-directory-policy` | That skill only |
| `conventional-commits-style` | That skill only |
| `todo-workflow-controller` | That skill only |
| `natural-language-report-writer` | That skill only |
| `validation-discovery` | That skill only |

All selected folders include every local resource, especially `references/` and `assets/`. Do not create placeholder `SKILL.md` files for planned entries. A missing dependency is reported honestly; it does not authorize imitation or automatic installation.

## Standalone installation matrix

Use these documented destinations; `~` denotes the actual selected user's home and `<project>` the explicitly selected project root.

| Target | CLI selector | Project destination | User/global destination |
| --- | --- | --- | --- |
| Codex | `codex` | `<project>/.agents/skills/` | `~/.agents/skills/` |
| Copilot in VS Code | `github-copilot` | `<project>/.agents/skills/` | `~/.copilot/skills/` |
| Claude Code | `claude-code` | `<project>/.claude/skills/` | `~/.claude/skills/` |
| Kiro IDE | `kiro-cli` writes Kiro's shared skill directories | `<project>/.kiro/skills/` | `~/.kiro/skills/` |

A target selector chooses installation destinations, not access control. Codex and Copilot share the documented project .agents/skills path; other clients may also scan shared roots. Document this overlap and do not promise that a standalone skill is visible exclusively to the selected harness. Treat the external CLI's observed shared store and lock files as disclosed installation artifacts. Native plugin enablement is the preferred route when the user needs harness-specific activation.

The Kiro selector is the third-party installer's identifier; it is not evidence of Kiro IDE activation. Native validation must run in Kiro IDE. CLI V3 may be recorded separately and cannot stand in for IDE evidence.

The optional Vercel Skills CLI route requires Node.js/npm. At implementation time inspect and record an exact CLI version, then pin commands as `npx skills@<tested-version> add <source> --skill <explicit-selection> --agent <selector> --copy`. Add `--global` for user scope and run project-scoped commands from the selected project. Replace all tokens in published examples with tested values; never publish an unresolved token as an executable recipe.

Use a verified release Git ref for released instructions. Local implementation checks use a local package source; do not claim that adding metadata changes the existing preview. Avoid `--all` because it can select every detected harness. Prefer copies initially to avoid requiring symlink privileges on Windows. Document source refs, copy update behavior, removal, and the external CLI's lock files after observing them.

Manual complete-folder copying is a first-class fallback with the same destinations and dependency sets. No Node dependency is imposed on manual installation or installed skill execution.

## Native suite scope matrix

| Target | User/global route | Project/workspace route |
| --- | --- | --- |
| Codex | Register the marketplace and install through the client's plugin browser | Use trusted project marketplace/configuration enablement; distinguish shared cache from per-project activation |
| Copilot in VS Code | Install from a marketplace or repository source | Use workspace plugin enablement/recommendations; a recommendation is not proof that collaborators downloaded it |
| Claude Code | `claude plugin install devcraft-toolkit@devcraft-toolkit --scope user` | The same install with `--scope project`; collaborators still perform their own installation |
| Kiro IDE | Import the repository-root Agent Plugins package as a Power | No isolated project-scoped Power installation is established by the consulted documentation; provide the full dependency-complete skill set under `.kiro/skills/` as the explicitly labeled project suite fallback |

For Claude, register the marketplace first with `claude plugin marketplace add omarfrancodev/devcraft-toolkit`. For Codex, the documented registration entry point is `codex plugin marketplace add omarfrancodev/devcraft-toolkit --ref <verified-ref>`, followed by installation in the supported client. Project enablement uses `[plugins."devcraft-toolkit@devcraft-toolkit"]` and `enabled = true` in trusted project `.codex/config.toml`; document how to disable it elsewhere when testing project isolation.

Copilot instructions use the installed VS Code version's plugin UI and must cover user/workspace enablement. Kiro instructions use Powers > Add Custom Power > Import from GitHub or folder. Do not manufacture a `--scope project` option for either application.

This matrix does not claim sixteen equivalent native installation modes. The project Power cell is `not_supported` pending documented native support; its tested skill-set fallback is a separate delivery mode. If a tested client cannot enforce project-only activation without leaking globally enabled skills, mark that native cell `limited` and provide the project skill route. Never change another project's settings to force a passing result.

## Installation, update, and collision behavior

- Scope means observed visibility in the selected project and in a second unrelated project; physical installation location alone is insufficient evidence.
- Inspect existing destinations and plugin registrations first. Show collisions; do not overwrite personal skills, remove another package, or assume consistent precedence across harnesses.
- Preserve installed canonical skill names. Map harness-discovered namespaced identifiers only when discovery identifies this package as the owner; do not strip a foreign package's prefix to satisfy a dependency.
- If a user explicitly selected a particular installation, route to it. If both suite and standalone copies exist and discovery cannot resolve ownership, ask a focused choice rather than silently selecting one.
- Keep existing entry behavior for absent optional skills. Installation does not grant repository, network, publication, or validation permissions.
- Document native update/uninstall by qualified plugin identity and scope. A marketplace refresh and plugin update are different operations.
- For standalone copies, document the observed CLI removal/update behavior or explicit scoped manual replacement; require replacement authorization and preserve unrelated directories.
- Never edit host plugin caches, global identity, credentials, or security controls as an installation workaround.

## Verification levels and evidence

Evidence belongs under `tests/integration/distribution/evaluations/<run>/`, with synthetic fixtures under `tests/integration/distribution/fixtures/` if needed. Do not create test folders in a skill.

Keep three levels separate: `structural` (metadata, inventory, relative paths), `filesystem` (actual selected copied files and dependency closures), and `native` (real client discovery, activation, and scope). Mock loaders and manual following are never native evidence.

Use an isolated temporary project and a second control project. User-scope tests require a disposable OS user/profile/container supported by the client, or a verified client-specific profile override. Do not assume changing HOME, USERPROFILE, or CODEX_HOME isolates every client's skills, registry, account, and cache. If isolation or authentication cannot be obtained safely, record `blocked` or `not_run`; do not install into the maintainer's real account.

For each available mode/scope/target cell, record client and installer versions, OS, source Git ref, selected skills and dependency closure, installation/enablement location, observed invocation identifier, resource read evidence, control-project visibility, lifecycle results, and before/after inventories. Record `passed`, `failed`, `blocked`, `not_run`, `limited`, or `not_supported` with evidence.

## Acceptance criteria

- `DIST-01`: Both manifest identities and versions agree; both marketplace adapters resolve the same root; the suite discovers exactly the seven available skills, never the ten planned names.
- `DIST-02`: All seven individual dependency closures and the full available set copy complete resources to the selected matrix destination, without writing to an unrelated scope or target-specific directory.
- `DIST-03`: Direct skill use and entry routing work with discovered package-qualified identifiers; missing capabilities and ambiguous duplicate ownership preserve the existing boundaries.
- `DIST-04`: Native user/project scope is verified against a second project wherever documented; the Kiro project Power exception is explicit and its skill-set fallback is verified independently.
- `DIST-05`: Native and standalone update/removal preserve unrelated files and registrations; repeated installation is observed rather than assumed idempotent; copies and symlinks are not conflated.
- `DIST-06`: Each target has concrete installation, discovery, invocation, update, removal, collision, dependency, and scope instructions. Unsupported cells and unrun checks are visible.
- `DIST-07`: The existing skills, catalog schema, and available/planned statuses remain unchanged except for the entry's package-identifier routing clarification, if implemented as specified.
- `DIST-08`: No compatibility claim or new release is made merely because metadata tests pass. Publication and public marketplace submission are separate actions.

The implementation can deliver metadata and documentation with native cells still blocked, but it must remain explicitly partially validated. No all-four-harness compatibility claim is acceptable until the relevant native rows pass.

## Development interfaces and checks

`scripts/validate_distribution.py` exposes `validate_distribution(root: Path) -> list[ValidationIssue]`, reusing `ValidationIssue(code, path, message)` from `scripts.validate_repository`, and `main(argv: list[str] | None = None) -> int`. Invoke it as `python -B -m scripts.validate_distribution --root .`. It reads local files only, returns exit 0 for a valid distribution and 1 for contract violations, and performs no installation, network access, or edits.

Its finite contract checks are not a claim to implement the entire external Agent Plugins schema. Use native validators separately when available.

Required regression cases: identity/version drift, malformed metadata, a source escaping the root, a missing root source, duplicate marketplace entries, a discoverable planned skill, copied or omitted available skills, resource completeness, and changed catalog dependency closure. Behavioral scenarios cover namespace ownership and collisions. Installation matrices exercise real files and clients as separately labeled operations.

## Official references

Consulted 2026-10-23. Recheck relevant versioned client help before implementation; do not invent a minimum client version from these pages.

- [Agent Plugins package format and Codex marketplaces](https://developers.openai.com/plugins/build/plugins).
- [Codex local skill scope](https://learn.chatgpt.com/docs/build-skills).
- [Copilot plugin usage and workspace enablement](https://code.visualstudio.com/docs/agent-customization/agent-plugins).
- [Copilot plugin format reference](https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference).
- [Copilot standalone skill locations](https://code.visualstudio.com/docs/agent-customization/agent-skills).
- [Claude plugin manifest](https://code.claude.com/docs/en/plugins-reference).
- [Claude installation and scope](https://code.claude.com/docs/en/discover-plugins).
- [Claude standalone skills](https://code.claude.com/docs/en/skills).
- [Kiro Power installation](https://kiro.dev/docs/powers/installation/).
- [Kiro Agent Plugins packaging](https://kiro.dev/docs/powers/create/).
- [Kiro standalone skill scope](https://kiro.dev/docs/skills/).
- [Selective CLI interface](https://github.com/vercel-labs/skills/blob/main/README.md) and [target directory mapping](https://github.com/vercel-labs/skills/blob/main/docs/agents.md).

## Decisions left to the implementer

Choose the tested external CLI/client versions based on actual availability, record them, and replace recipe placeholders before publication. Choose a safe disposable environment that the real client supports. Resolve minor UI wording from that tested client. These choices cannot expand the declared scope, create fake native evidence, or change the unsupported Kiro project Power cell without a documented source and an updated reviewed contract.
