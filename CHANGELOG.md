# Changelog

Release dates use the GitHub publication date in America/Mexico_City. Pre-releases are experimental snapshots; interfaces and behavior may change before a stable release.

## unreleased

### Added

#### Distribution and documentation

- Define native suite and selective skill installation for Codex, Copilot in VS Code, Claude Code, and Kiro IDE, with user/project scope, dependency closures, client-specific limitations, and separate structural and native acceptance checks.

### Changed

#### Distribution and documentation

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
