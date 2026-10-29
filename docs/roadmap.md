# Capability roadmap

## Current foundation

Current source contains eighteen available capabilities and zero planned names, recorded in the [approved inventory](capability-inventory.md). Work-branch creation and full publication coordination are delivered in unpublished candidate preview.8. Published preview.7 retains sixteen available/one planned across its historical seventeen names; preview.6 retains fourteen, preview.5 twelve, preview.4 eleven and preview.3 nine. Every capability retains its explicit operation/authorization contract; optional entry routes add no hard dependency.

## Shared capabilities

The shared-capability sequence delivered progress control, evidence-based natural-language reporting, and project validation discovery. Each capability has an independent contract and tests grouped by its canonical skill owner. Conventional Commit formatting is available and is not a runtime dependency of the other shared capabilities.

## Installation and distribution

The 0.1.0-preview.2 distribution leads with remote adoption of one complete suite through native plugins/Powers or the documented complete skill-set routes, with selective skill installation as an alternative for Codex, Copilot CLI, Copilot in VS Code, Claude Code, Kiro CLI V3, Kiro IDE, and Kiro Crew, covering user/global and project/workspace scope. See the [installation design](superpowers/specs/2026-10-23-distribution-installation-design.md) and [implementation plan](superpowers/plans/2026-10-23-distribution-installation.md). Root and compatibility manifests, both marketplace adapters, offline validation, seven client installation guides and installation-aware entry routing are implemented. The [installation evidence](../tests/integration/distribution/evaluations/2026-10-23-installation/filesystem.md) records 128 filesystem cases and eight CLI lifecycle cases. [Native validation](../tests/integration/distribution/evaluations/2026-10-23-installation/native.md) is partial: Codex/Claude registration was observed, while authenticated invocation, complete scope/lifecycle checks and IDE sessions remain pending. The [remote suite evaluation](../tests/integration/distribution/evaluations/2026-10-23-remote-suite/remote.md) adds actual GitHub acquisition, Codex/Claude installation and complete resource hashes. Consumer, optional skill and development guides are separate. Default-source recipes use integrated metadata; historical pre-integration sources remain explicitly described. [Release details](releases/v0.1.0-preview.2.md) retain experimental scope. Task 4's native execution step remains incomplete.

Project-scoped native plugin activation is distinct from project-local installation storage. Kiro's project suite fallback uses workspace skills; no isolated project Power installation is claimed. Target-specific discovery and actual validation status must remain explicit.

The [seven-client extension](../tests/integration/distribution/evaluations/2026-10-23-client-expansion/clients.md) adds limited remote Copilot CLI resource/lifecycle evidence. Crew uses native full skill import without a toolkit template or App; CLI/IDE/Crew activation and per-client scope/lifecycle remain independent gates.

## Git coordinators

Local commit construction is available in preview.4 with bounded index/commit writes. Git-history activity reporting is available in preview.5 through context and report-writer composition. Scoped synchronization and standalone push are available in preview.6 with independent context/safety closures and bounded explicit authorization. Hosted PR management and explicit promotion are available in preview.7. Independent work-branch creation and full publication coordination are available in unpublished candidate preview.8; all eighteen current target capabilities are implemented. Installed capabilities retain their owned dependencies and explicit authorization boundaries.

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
2. **Staging and commit construction — available in preview.4.** `git-stage-changes` and `git-commit-builder` implement exact selection, explicit mutation authorization, current preflight/effective identity, scoped validation and preserved partial progress. See the [design](superpowers/specs/2026-10-24-git-staging-commit-construction-design.md) and [plan](superpowers/plans/2026-10-24-git-staging-commit-construction.md). Branch creation is not implied; native invocation remains unverified.
3. **Git-history activity reporting — available in preview.5.** `git-activity-report` provides pinned local history, exact author/date/timezone selection, bounded coverage and report-writer reuse with explicit file output/readback. See the [design](superpowers/specs/2026-10-24-git-activity-report-design.md) and [plan](superpowers/plans/2026-10-24-git-activity-report.md). Native invocation remains unverified.
4. **Scoped synchronization and push — available in preview.6.** `git-sync-branch` implements one-branch fetch and fast-forward only; `git-publish-changes` implements pinned normal single-branch push and separately requested two-key local upstream setup. See the [design](superpowers/specs/2026-10-25-git-sync-publish-design.md) and [plan](superpowers/plans/2026-10-25-git-sync-publish.md). Both default to offline inspection and remain independently installable.
5. **PR management and promotion — available in preview.7.** `git-manage-pull-request` owns proposal/inspection, creation and selected title/body updates. `git-promote` owns explicitly requested ordinary source-conditional merge of an existing request, current policy/review/check gates and post-merge provenance/containment. See the [design](superpowers/specs/2026-10-25-git-pr-promotion-design.md) and [plan](superpowers/plans/2026-10-25-git-pr-promotion.md). Two-/three-folder closures remain independent of local publication preflight. Authenticated provider/native validation stays open.
6. **Work branches and full publication coordination - available in unpublished preview.8 candidate.** `git-create-work-branch` independently preserves current committed work on one new local branch; `git-publish-work` delegates selected preparation/push/request flows with conditional owners, explicit sync/promotion/upstream permissions, blocker forecasts and actual partial-effect handoffs. See the [design](superpowers/specs/2026-10-26-git-work-publication-design.md), [plan](superpowers/plans/2026-10-26-git-work-publication.md) and [eighteen-name current inventory](capability-inventory.md). All eighteen target names are available; native/authenticated acceptance remains open.
7. **Native/authenticated validation — next validation track.** Start with a small authenticated Codex invocation of the published preview, then Copilot CLI and VS Code, followed by Claude Code and Kiro CLI V3/IDE/Crew. Verify resource reads, user/project scope and version-changing lifecycle per client. Keep unobserved rows open; this track does not block building the read-only capabilities.

CCR, a custom installer, release automation and public directory submission remain deferred. Catalog availability is the current product inventory; old spec/plan checkboxes retain historical execution records and do not establish native validation. In particular, the earlier installation plan's authenticated execution gate remains open.

## Read-only preparation release

[Preview.3](releases/v0.1.0-preview.3.md) delivers analysis and planning as a nine-skill suite. Its changelog and release preparation belong to PR #5; the tag/assets target that PR's exact merge commit. The subsequent staging/commit increment is delivered in preview.4.

## Staging and commit construction release

[Preview.4](releases/v0.1.0-preview.4.md) delivers exact staging and requested local commit construction as an eleven-skill suite. Its changelog and release preparation belong to PR #6; the tag/assets target that PR's exact merge commit, without a later source-preparation commit. The subsequent activity-report coordinator is delivered in preview.5.

## Local-history reporting release

[Preview.5](releases/v0.1.0-preview.5.md) delivers local-history reporting as a twelve-skill suite. Its changelog and release preparation belong to PR #7; the tag/assets target that PR's exact merge commit without a later source-preparation commit. Scoped synchronization/push are implemented in preview.6; full publication coordination is available in the current candidate and native invocation continues as a separate validation track.

## Scoped synchronization and publication release

[Preview.6](releases/v0.1.0-preview.6.md) delivers independent synchronization and normal single-branch publication as a fourteen-skill suite. Changelog and release preparation belong to PR #8; tag and assets target its exact merge commit with no later preparation commit on main. At that release, three capabilities remained planned: PR management, promotion and full publication coordination. Preview.7 implements the first two; `git-publish-work` is available in the current unpublished candidate. Native invocation remains a separate validation track.

## Hosted requests and promotion release

[Preview.7](releases/v0.1.0-preview.7.md) delivers hosted request management and explicitly requested ordinary promotion as a sixteen-skill suite. The versioned changelog, release notes, source pointers and preparation evidence belong to PR #9; tag/assets target its exact merge commit with no later preparation commit on main. At that release only git-publish-work remained planned; current source delivers it and independent work-branch creation. Authenticated provider/native activation remains a separate validation track.

## Next work after the target inventory

Validate a small authenticated Codex invocation with selected installation identity and source/resource checks, then exercise Copilot CLI and VS Code, Claude Code and Kiro CLI V3/IDE/Crew separately. Verify user/project scope and actual version-changing update/removal as applicable. Keep unobserved rows open. Use resulting evidence to improve existing instructions and integration behavior; do not invent new planned capability names. CCR, custom installer, release automation and public-directory submission remain deferred. Preparing or publishing this candidate requires its own later release request.
