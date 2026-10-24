# Capability roadmap

## Current foundation

The development candidate catalog provides eleven available skills and six planned entries across seventeen names. Exact scoped staging and commit construction join the foundation, shared capabilities and read-only preparation. Their explicit authorization boundaries permit selected index writes and requested normal commits; the earlier capabilities retain their own contracts. Optional entry routes add no hard dependency to the entry. Published preview.3 remains a nine-skill snapshot; preview.4 is unpublished.

## Shared capabilities

The shared-capability sequence delivered progress control, evidence-based natural-language reporting, and project validation discovery. Each capability has an independent contract and tests grouped by its canonical skill owner. Conventional Commit formatting is available and is not a runtime dependency of the other shared capabilities.

## Installation and distribution

The 0.1.0-preview.2 distribution leads with remote adoption of one complete suite through native plugins/Powers or the documented complete skill-set routes, with selective skill installation as an alternative for Codex, Copilot CLI, Copilot in VS Code, Claude Code, Kiro CLI V3, Kiro IDE, and Kiro Crew, covering user/global and project/workspace scope. See the [installation design](superpowers/specs/2026-10-23-distribution-installation-design.md) and [implementation plan](superpowers/plans/2026-10-23-distribution-installation.md). Root and compatibility manifests, both marketplace adapters, offline validation, seven client installation guides and installation-aware entry routing are implemented. The [installation evidence](../tests/integration/distribution/evaluations/2026-10-23-installation/filesystem.md) records 128 filesystem cases and eight CLI lifecycle cases. [Native validation](../tests/integration/distribution/evaluations/2026-10-23-installation/native.md) is partial: Codex/Claude registration was observed, while authenticated invocation, complete scope/lifecycle checks and IDE sessions remain pending. The [remote suite evaluation](../tests/integration/distribution/evaluations/2026-10-23-remote-suite/remote.md) adds actual GitHub acquisition, Codex/Claude installation and complete resource hashes. Consumer, optional skill and development guides are separate. Default-source recipes use integrated metadata; historical pre-integration sources remain explicitly described. [Release details](releases/v0.1.0-preview.2.md) retain experimental scope. Task 4's native execution step remains incomplete.

Project-scoped native plugin activation is distinct from project-local installation storage. Kiro's project suite fallback uses workspace skills; no isolated project Power installation is claimed. Target-specific discovery and actual validation status must remain explicit.

The [seven-client extension](../tests/integration/distribution/evaluations/2026-10-23-client-expansion/clients.md) adds limited remote Copilot CLI resource/lifecycle evidence. Crew uses native full skill import without a toolkit template or App; CLI/IDE/Crew activation and per-client scope/lifecycle remain independent gates.

## Git coordinators

Local commit construction is available in the development candidate with bounded index/commit writes. Git-history activity reporting and remote publication remain separate planned increments; define their evidence, side effects and authorization boundaries before implementation. Planned capabilities have no discoverable skill placeholders and are not emulated by the entry.

## Deferred capabilities

CCR integration, a custom automatic installer, CI distribution, release automation, and public directory submission remain deferred. Native activation across the seven target clients remains a validation gate before broader compatibility claims; it must not be inferred from delivered metadata. No license is selected by this increment.

## Shared-capability designs

Each capability has its own self-contained spec and implementation plan. The execution order is formatting, progress control, reporting, and validation; these are independent deliveries, not runtime dependencies.

| Capability | Status | Design | Plan |
| --- | --- | --- | --- |
| conventional-commits-style | available | [Commit message formatting](superpowers/specs/2026-10-22-commit-message-formatting-design.md) | [Implementation](superpowers/plans/2026-10-22-commit-message-formatting.md) |
| todo-workflow-controller | available | [Progress control](superpowers/specs/2026-10-22-progress-control-design.md) | [Implementation](superpowers/plans/2026-10-22-progress-control.md) |
| natural-language-report-writer | available | [Natural-language reporting](superpowers/specs/2026-10-22-natural-language-reporting-design.md) | [Implementation](superpowers/plans/2026-10-22-natural-language-reporting.md) |
| validation-discovery | available | [Project validation](superpowers/specs/2026-10-22-project-validation-design.md) | [Implementation](superpowers/plans/2026-10-22-project-validation.md) |

The table reflects catalog availability. Planned designs do not create installable skill placeholders or imply completed behavior.

## Next increments and acceptance gates

1. **Read-only analysis and commit planning — available.** Deliver `git-analyze-changes` and `git-plan-commits`, preserving staged/unstaged boundaries and freshness. See the [design](superpowers/specs/2026-10-24-git-analysis-planning-design.md) and [plan](superpowers/plans/2026-10-24-git-analysis-planning.md). Owner-scoped replay/edge evidence, real Git fixture safety checks and dependency-aware optional entry routes are implemented. Native invocation of the new capabilities remains unverified.
2. **Staging and commit construction — available in the development candidate.** `git-stage-changes` and `git-commit-builder` implement exact selection, explicit mutation authorization, current preflight/effective identity, scoped validation and preserved partial progress. See the [design](superpowers/specs/2026-10-24-git-staging-commit-construction-design.md) and [plan](superpowers/plans/2026-10-24-git-staging-commit-construction.md). Branch creation is not implied; native invocation remains unverified.
3. **Git-history activity reporting — planned.** Design `git-activity-report` with verified history, author/date/timezone filters, evidence limits, report-writer reuse and an explicit output destination when saving.
4. **Remote publication — planned.** Design `git-sync-branch`, `git-publish-changes`, `git-manage-pull-request` and `git-promote` before composing `git-publish-work`. Define independent synchronization, publication, review/promotion and authorization boundaries; no automatic remote mutation from an inspection request.
5. **Native validation — ongoing.** Start with a small authenticated Codex invocation of the published preview, then Copilot CLI and VS Code, followed by Claude Code and Kiro CLI V3/IDE/Crew. Verify resource reads, user/project scope and version-changing lifecycle per client. Keep unobserved rows open; this track does not block building the read-only capabilities.

CCR, a custom installer, release automation and public directory submission remain deferred. Catalog availability is the current product inventory; old spec/plan checkboxes retain historical execution records and do not establish native validation. In particular, the earlier installation plan's authenticated execution gate remains open.

## Read-only preparation release

[Preview.3](releases/v0.1.0-preview.3.md) delivers analysis and planning as a nine-skill suite. Its changelog and release preparation belong to PR #5; the tag/assets target that PR's exact merge commit. The subsequent staging/commit increment is available in the unpublished development candidate. Git-history activity reporting is next; native invocation continues as a separate validation track.
