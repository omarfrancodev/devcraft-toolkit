# Capability roadmap

## Current foundation

The distribution provides repository context, read-only Git preflight, a composition entry, standalone Conventional Commit message formatting, portable progress tracking, evidence-based report writing, and project validation discovery. The catalog records seventeen target capabilities, with seven available and ten planned. Optional capabilities can be installed alone or alongside the entry; none adds a hard skill dependency. The entry routes commit-message, progress-control, natural-language-reporting, and project-validation requests to the matching optional skill when installed, and reports unavailable capabilities honestly when absent.

## Shared capabilities

The shared-capability sequence delivered progress control, evidence-based natural-language reporting, and project validation discovery. Each capability has an independent contract and tests grouped by its canonical skill owner. Conventional Commit formatting is available and is not a runtime dependency of the other shared capabilities.

## Git coordinators

Git commit construction, Git-history activity reporting, and publication are separate increments. Their designs must define inputs, evidence, state changes, authorization boundaries, and acceptance criteria before implementation. Planned capabilities have no discoverable skill placeholders and are not emulated by the entry.

## Deferred capabilities

CCR and Jira integration, plugin packaging, automated installation, CI distribution, and release automation are outside the current scope. A later design must establish the applicable interfaces and checks before introducing any of them. No license is selected by this increment.

## Shared-capability designs

Each capability has its own self-contained spec and implementation plan. The execution order is formatting, progress control, reporting, and validation; these are independent deliveries, not runtime dependencies.

| Capability | Status | Design | Plan |
| --- | --- | --- | --- |
| conventional-commits-style | available | [Commit message formatting](superpowers/specs/2026-10-22-commit-message-formatting-design.md) | [Implementation](superpowers/plans/2026-10-22-commit-message-formatting.md) |
| todo-workflow-controller | available | [Progress control](superpowers/specs/2026-10-22-progress-control-design.md) | [Implementation](superpowers/plans/2026-10-22-progress-control.md) |
| natural-language-report-writer | available | [Natural-language reporting](superpowers/specs/2026-10-22-natural-language-reporting-design.md) | [Implementation](superpowers/plans/2026-10-22-natural-language-reporting.md) |
| validation-discovery | available | [Project validation](superpowers/specs/2026-10-22-project-validation-design.md) | [Implementation](superpowers/plans/2026-10-22-project-validation.md) |

The table reflects catalog availability. Planned designs do not create installable skill placeholders or imply completed behavior.
