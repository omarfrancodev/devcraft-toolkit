# Suite and Selective Skill Installation Design

**Date:** 2026-10-23
**Status:** Approved remote-first revision; metadata and local evidence implemented, native activation remains partially validated.
**Scope:** Codex local clients, GitHub Copilot in VS Code, Claude Code local clients, and Kiro IDE.
**Related implementation plan:** [Installation plan](../plans/2026-10-23-distribution-installation.md).

## Intent and current state

Make remote installation of the complete native suite the primary adoption path. Installing individual skills is an alternative; local checkout installation is a development/reference path. Harness and scope remain explicit choices. A user must be able to install a usable set for one project or for their user account without installing planned capabilities.

The candidate contains seven available skills, native metadata, four guides and retained local installation evidence; ten capabilities remain planned. The published first preview is source-only. Native authenticated invocation and IDE sessions are not fully verified. The revision replaces checkout-first onboarding without changing skill behavior or declaring a new release.

## Goals and non-goals

- Keep one canonical copy of each skill under `skills/<canonical-name>/`.
- Lead with remote installation of one complete native suite, `devcraft-toolkit`; offer selective installation with explicit dependency closures separately.
- Require no user-managed clone, source-path variable, Node.js or Skills CLI for the normal native suite route. Client-managed Git/cache storage is expected.
- Keep first-use instructions short; place scope detail, local development, manual copies and developer validation behind named links.
- Document user/global and project/workspace scope for every target, distinguishing installation storage from enablement.
- Verify resource integrity, discovery, routing, scope boundaries, and lifecycle operations without changing existing personal installations.
- Keep instructions, examples, templates, and documentation in English; invoked skills retain the user's resolved language.

New Git coordinators, CCR integration, external business integrations, release automation, automatic dependency resolution, public directory submission, cloud clients, and license selection are excluded. No MCP server, lifecycle hook, custom runtime installer, onboarding skill, or executable install hook is needed.

## Approaches and selected direction

1. Manual copying and selective CLI installation only: smallest change, but leaves the suite without native plugin discovery.
2. Remote-first native suite over one shared skill tree, portable metadata, a Claude compatibility manifest and small marketplace adapters: short consumer onboarding with selective and local routes kept separately. This is the selected direction.
3. Independent packages or repositories per harness: creates synchronization and maintenance costs without changing the skill contracts.

The selected direction preserves both suite and individual adoption. It adds no custom installer, separate marketplace repository, official-directory listing requirement, lifecycle hook or automatic bootstrap. The same repository serves source and marketplace metadata.

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
| `docs/installation.md` | Consumer overview: complete remote suite first, alternative skill installation second |
| `docs/installation/individual-skills.md` | Optional remote selective recipes, dependency table, destinations and collisions |
| `docs/installation/development.md` | Local checkout recipes, manual copying, source-only ZIPs and developer checks |
| `docs/installation/preview.md` | Concrete pinned remote source for pre-integration validation |
| `docs/installation/{codex,copilot-vscode,claude-code,kiro}.md` | Target-specific native and standalone procedures |

Do not create `.codex-plugin/`, `POWER.md`, copied skill trees, or a second package unless a separately reviewed compatibility finding requires one. The consulted interfaces support a root portable manifest for Codex, Copilot, and Kiro; Claude has an explicit compatibility manifest.

## Manifest and marketplace contract

Root `plugin.json` contains exactly the initial fields `$schema`, `name`, `version`, `description`, and `author`. The schema URI is `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`. Description is `Composable Git and development skills for coding agents.` Author is `{"name": "omarfrancodev"}`. Standard root `skills/` discovery exposes only available skills. Do not add empty connector configuration.

The Claude manifest contains `name`, `version`, `description`, and `author` with identical values. Omit a `skills` override because the standard directory already exists; adding the same directory again can duplicate component loading.

The Codex marketplace contains `name`, `interface.displayName` (`Devcraft Toolkit`), and one `plugins` entry. That entry has `name: devcraft-toolkit`, `source: {"source":"local","path":"./"}`, `policy: {"installation":"AVAILABLE","authentication":"ON_INSTALL"}`, and `category: Productivity`. The relative source resolves from the marketplace's repository root, not the manifest directory. The authentication policy does not add an authentication step to this connector-free package.

The Claude/Copilot marketplace contains `name`, `owner: {"name":"omarfrancodev"}`, and one `plugins` entry with `name: devcraft-toolkit`, `source: ./`, and the package description. Do not redeclare components or duplicate the package version there.

Both adapters target this same repository root. Adapter equality is semantic, not byte equality. No marketplace entry installs a planned capability or fetches custom catalog dependencies.

## Remote source and documentation contract

Use the public Git repository https://github.com/omarfrancodev/devcraft-toolkit.git. Normal post-integration recipes use its default branch through the native client; no official catalog listing is claimed. This revision does not merge the branch, create a release/tag or publish a separate marketplace.

Until the metadata is integrated into the default branch, label default-source recipes as post-integration. Use existing immutable revision b05a8c4367dc02e33ac9d19a8eb98e0bdb31c04e for actual remote pre-integration checks: it is already published, contains both marketplaces and the seven-skill package, and is not a release tag. Do not silently test a local copy and call the remote route passed.

Codex supports remote marketplace registration with an explicit --ref. Claude accepts a Git URL suffixed with #ref. Copilot's marketplace configuration accepts owner/repo#ref; use its marketplace UI for enablement rather than mixing inventories or imposing direct-install scope promises. Kiro documents repository URL import but the reviewed interface does not establish a pinned-ref import; keep that row unverified until IDE evidence exists. Do not invent ref flags for Kiro. Its documented default-source Power recipe applies after integration.

README and the overview lead with the complete suite and link four concise target guides. Each target guide starts with native remote install, then essential scope/lifecycle information and links the alternative individual guide. The individual guide owns Node/npm prerequisites, explicit dependency sets, complete-set fallback and destination differences. Development owns user-managed clones, local source variables, manual folder copying and validation commands.

No quickstart promises immediate authenticated activation, identical scopes across clients, or installation from the source-only preview. Retain evidence references without requiring users to execute the test matrix to install.

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

Use a verified release Git ref for released instructions and the existing immutable source revision above for pre-integration checks. Local implementation checks remain separate from remote tests; do not claim that adding metadata changes the existing preview. Avoid `--all` because it can select every detected harness. Prefer copies initially to avoid requiring symlink privileges on Windows. Document source refs, copy update behavior, removal, and the external CLI's lock files after observing them.

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
- `DIST-06`: README and each target lead with complete remote native installation; optional skills and local/developer procedures have separate linked guides. Each target retains concrete discovery, invocation, update, removal, collision, dependency, and scope instructions. Unsupported cells and unrun checks are visible.
- `DIST-07`: The existing skills, catalog schema, and available/planned statuses remain unchanged except for the entry's package-identifier routing clarification, if implemented as specified.
- `DIST-08`: No compatibility claim or new release is made merely because metadata tests pass. Publication and public marketplace submission are separate actions.

The implementation can deliver metadata and documentation with native cells still blocked, but it must remain explicitly partially validated. No all-four-harness compatibility claim is acceptable until the relevant native rows pass.

## Remote-first acceptance

- REMOTE-01: A consumer can identify the complete native suite route without first selecting skill names, providing a checkout path or installing the external Skills CLI.
- REMOTE-02: All four target guides separate normal remote installation, user/project semantics and the explicit alternative skill route. Kiro's project Power exception remains visible.
- REMOTE-03: Actual remote Codex and Claude registration/install operations use the published immutable revision, retain exact command/results and verify all seven available names/resources. Optional Skills CLI checks use a remote source and explicit selections.
- REMOTE-04: Default-branch availability, pinned test source and published releases are distinct. Pre-integration caveats and blocked IDE/authenticated checks are visible.
- REMOTE-05: No skill/catalog/runtime change, extra repository, custom installer or automatic hook is introduced merely to simplify onboarding.

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
