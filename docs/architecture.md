# Architecture

Devcraft Toolkit is a maintained collection of composable, instruction-first skills. `catalog.json` records each capability's canonical name, role, planned or available status, installation path, and declared skill dependencies. It is a project inventory, not a plugin or installer standard.

Skills are independently usable unless their catalog entry declares a dependency. Each available skill keeps its references within its own folder. A standalone installation must include the skill's declared dependency closure; the catalog does not cause an installer to fetch it.

The repository validator and tests are development tools. Installed skills do not depend on them at runtime. Repository tests are grouped under `tests/repository/`, `tests/skills/<normalized-skill-name>/`, or shared integration/support areas when they cover multiple named skills.

The current distribution has seven available skills and ten planned entries. The available set is `using-devcraft-toolkit`, `git-working-directory-policy`, `git-safety-check`, `conventional-commits-style`, `todo-workflow-controller`, `natural-language-report-writer`, and `validation-discovery`; the entry depends on both supporting skills; the formatter, progress controller, report writer, and validation discovery remain independently usable with no dependencies. Centralized structural validation and behavioral scenarios live under the repository root's `scripts/` and `tests/` directories.

CCR workflows, a custom automatic installer, and release automation remain deferred. Native packaging follows the [installation design](superpowers/specs/2026-10-23-distribution-installation-design.md): root plugin.json is the portable manifest; .claude-plugin/plugin.json is its compatibility mirror. The .agents/plugins/marketplace.json and .claude-plugin/marketplace.json adapters both point at this repository root, using one canonical skills/ tree. The offline distribution validator checks this finite contract and reuses repository inventory validation. It is not a runtime dependency or a full external-schema implementation.

The primary consumer path is complete remote native suite installation from this same repository through each client's own plugin manager. Client-managed Git/cache storage is expected; no user-managed checkout, separate marketplace repository or custom installer is introduced. Individual skills remain an optional route that copies complete chosen folders with explicit dependency closure. Native suite installation packages the same seven skills; installed entry routing uses discovered ownership and identifiers, not a persisted registry or runtime root catalog.

Metadata, filesystem installation, manually followed behavior and native activation are separate evidence levels. Local and remote file placement passed in disposable containers; native remote registration was observed for Codex and Claude, while authenticated activation and IDE rows remain partially validated. See [installation](installation.md), [composition](composition.md), and [compatibility evidence](compatibility.md) for user-facing constraints.

See the [capability roadmap](roadmap.md) for the sequence of product increments.
