# Capability roadmap

## Current foundation

The distribution provides repository context, read-only Git preflight, a composition entry, standalone Conventional Commit message formatting, and portable progress tracking. The catalog records seventeen target capabilities, with five available and twelve planned. The formatter can be installed alone or optionally alongside the entry; it has no hard skill dependencies.

## Shared capabilities

The shared-capability sequence began with progress control, which is available; the remaining capabilities are evidence-based natural-language reports and project validation discovery. Each capability has an independent contract and tests grouped by its canonical skill owner. Conventional Commit formatting is available and is not a runtime dependency of the remaining shared capabilities.

## Git coordinators

Commit construction, activity reporting, and publication are separate increments. Their designs must define inputs, evidence, state changes, authorization boundaries, and acceptance criteria before implementation. Planned capabilities have no discoverable skill placeholders and are not emulated by the entry.

## Deferred capabilities

CCR and Jira integration, plugin packaging, automated installation, CI distribution, and release automation are outside the current scope. A later design must establish the applicable interfaces and checks before introducing any of them. No license is selected by this increment.

## Shared-capability designs

Each capability has its own self-contained spec and implementation plan. The execution order is formatting, progress control, reporting, and validation; these are independent deliveries, not runtime dependencies.

| Capability | Status | Design | Plan |
| --- | --- | --- | --- |
| conventional-commits-style | available | [Commit message formatting](superpowers/specs/2026-10-22-commit-message-formatting-design.md) | [Implementation](superpowers/plans/2026-10-22-commit-message-formatting.md) |
| todo-workflow-controller | available | [Progress control](superpowers/specs/2026-10-22-progress-control-design.md) | [Implementation](superpowers/plans/2026-10-22-progress-control.md) |
| natural-language-report-writer | planned | [Natural-language reporting](superpowers/specs/2026-10-22-natural-language-reporting-design.md) | [Implementation](superpowers/plans/2026-10-22-natural-language-reporting.md) |
| validation-discovery | planned | [Project validation](superpowers/specs/2026-10-22-project-validation-design.md) | [Implementation](superpowers/plans/2026-10-22-project-validation.md) |

The table reflects catalog availability. Planned designs do not create installable skill placeholders or imply completed behavior.
