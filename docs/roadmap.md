# Capability roadmap

## Current foundation

The distribution provides repository context, read-only Git preflight, a composition entry, standalone Conventional Commit message formatting, portable progress tracking, evidence-based report writing, and project validation discovery. The catalog records seventeen target capabilities, with seven available and ten planned. Optional capabilities can be installed alone or alongside the entry; none adds a hard skill dependency. The entry routes commit-message, progress-control, natural-language-reporting, and project-validation requests to the matching optional skill when installed, and reports unavailable capabilities honestly when absent.

## Shared capabilities

The shared-capability sequence delivered progress control, evidence-based natural-language reporting, and project validation discovery. Each capability has an independent contract and tests grouped by its canonical skill owner. Conventional Commit formatting is available and is not a runtime dependency of the other shared capabilities.

## Installation and distribution

The 0.1.0-preview.2 distribution leads with remote adoption of one complete suite through native plugins/Powers or the documented complete skill-set routes, with selective skill installation as an alternative for Codex, Copilot CLI, Copilot in VS Code, Claude Code, Kiro CLI V3, Kiro IDE, and Kiro Crew, covering user/global and project/workspace scope. See the [installation design](superpowers/specs/2026-10-23-distribution-installation-design.md) and [implementation plan](superpowers/plans/2026-10-23-distribution-installation.md). Root and compatibility manifests, both marketplace adapters, offline validation, seven client installation guides and installation-aware entry routing are implemented. The [installation evidence](../tests/integration/distribution/evaluations/2026-10-23-installation/filesystem.md) records 128 filesystem cases and eight CLI lifecycle cases. [Native validation](../tests/integration/distribution/evaluations/2026-10-23-installation/native.md) is partial: Codex/Claude registration was observed, while authenticated invocation, complete scope/lifecycle checks and IDE sessions remain pending. The [remote suite evaluation](../tests/integration/distribution/evaluations/2026-10-23-remote-suite/remote.md) adds actual GitHub acquisition, Codex/Claude installation and complete resource hashes. Consumer, optional skill and development guides are separate. Default-source recipes use integrated metadata; historical pre-integration sources remain explicitly described. [Release details](releases/v0.1.0-preview.2.md) retain experimental scope. Task 4's native execution step remains incomplete.

Project-scoped native plugin activation is distinct from project-local installation storage. Kiro's project suite fallback uses workspace skills; no isolated project Power installation is claimed. Target-specific discovery and actual validation status must remain explicit.

The [seven-client extension](../tests/integration/distribution/evaluations/2026-10-23-client-expansion/clients.md) adds limited remote Copilot CLI resource/lifecycle evidence. Crew uses native full skill import without a toolkit template or App; CLI/IDE/Crew activation and per-client scope/lifecycle remain independent gates.

## Git coordinators

Git commit construction, Git-history activity reporting, and publication are separate increments. Their designs must define inputs, evidence, state changes, authorization boundaries, and acceptance criteria before implementation. Planned capabilities have no discoverable skill placeholders and are not emulated by the entry.

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
