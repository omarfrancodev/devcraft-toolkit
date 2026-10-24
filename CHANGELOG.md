# Changelog

Release dates use the GitHub publication date in America/Mexico_City. Pre-releases are experimental snapshots; interfaces and behavior may change before a stable release.

## unreleased

### Added

#### Distribution and documentation

- Add portable and compatibility plugin manifests and two root-relative marketplace adapters for the seven available skills.
- Add offline distribution validation and regression tests for metadata, versions, source containment and inventory.
- Document complete remote suite adoption as the primary route and selective skills as an alternative for Codex, Copilot CLI, Copilot in VS Code, Claude Code, Kiro CLI V3, Kiro IDE, and Kiro Crew, with explicit dependency closures, user/project scope, complete-folder copying, collisions and lifecycle procedures.
- Document Crew's complete native snapshot import without a new template or App; distinguish it from shared Kiro IDE/CLI Powers and CLI-only full skill-set fallback.
- Verify Copilot CLI remote registration/resources and same-ref lifecycle with 20 corrected commands; retain the rejected SHA attempt and explicit mutable branch recipe. Authenticated invocation, repository auto-install and VS Code crossover remain unverified.
- Verify remote Git acquisition and native managed package resources for Codex/Claude, plus selected remote folder copies; retain the version-specific Claude ref failure and corrected branch recipe.
- Retain 128 filesystem installation cases, eight CLI lifecycle cases and separate limited native registration evidence. Authenticated activation and IDE compatibility remain unverified.

### Changed

#### Distribution and documentation

- Add portable activation keywords for Kiro Powers and validate their non-empty string-array contract; retain pending native activation and distinguish historical probes of the earlier manifest.
- Separate consumer quickstarts, optional individual/dependency instructions and local development/reference procedures.
- Route toolkit capabilities through the selected installation's discovered identifiers and ownership; ask before resolving materially ambiguous duplicate copies.
- Narrow the documented integration scope and retain CCR as a deferred capability.

## 0.1.0-preview.1 — 2026-10-23

### Added

#### Repository context and Git safety

- Provide standalone repository, worktree, branch, and identity discovery through `git-working-directory-policy`.
- Provide read-only inspection and commit/publish readiness checks through `git-safety-check`, with an explicit dependency on repository context discovery. Readiness does not authorize Git writes.

#### Shared capabilities

- Draft and review Conventional Commit messages from supplied facts through `conventional-commits-style`, without requiring a repository or creating commits.
- Track progress, required gates, blockers, decisions, and handoffs through `todo-workflow-controller`, including an inline fallback when a native tracking tool is unavailable.
- Produce evidence-based reports in the user's language through `natural-language-report-writer`, with local file output only for an explicitly selected destination.
- Discover project validation commands and run explicitly authorized local checks through `validation-discovery`, preserving separate results for each required check.

#### Skill routing and composition

- Route requests through `using-devcraft-toolkit` to skills actually installed in the active harness, respecting required dependencies and reporting missing optional capabilities.
- Keep all seven available skills self-contained, with English source instructions and templates and user-facing output in the resolved request language.

#### Distribution and documentation

- Publish a catalog distinguishing seven available skills from ten planned capabilities, with installation, architecture, composition, and compatibility guidance.
- Validate catalog metadata, dependency closure, local resources, discoverable skill folders, and test ownership with repository tooling.
- Retain behavioral evaluation evidence and its limits: manual instruction following in Codex desktop does not establish native loading or compatibility with other harnesses.
