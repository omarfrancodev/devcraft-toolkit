---
name: validation-discovery
description: Use when a user asks to discover, select, run, or assess project validation checks such as tests, linters, builds, or type checks.
---

# Validation Discovery

Inspect the selected project and report evidence for each requested validation check. A discovered command is not permission to run it.

## Choose the mode

- **Discover** by default. Inspect the applicable project instructions and existing command definitions; return sourced candidates without executing them.
- **Run** only when the user or an authorized composing workflow requests execution. Run only the selected, inspected checks within that request's scope.

For each discovered candidate, state its source, exact command and working directory, intended check, expected effects, and whether it is authorized to run.

Use the selected project or subproject root. Git is optional. Preserve paths with spaces and use the actual supported working-directory and interpreter settings.

Before running a wrapper, inspect its full command composition, relevant hooks, dependencies, environment requirements and output locations. Shell operators call for inspecting the whole composition; they are not an automatic reason to reject a fully understood local check. Do not run installation, update, autofix, cleanup, migration, deployment, publication, destructive or external business operations as ordinary validation. If effects are unknown or unapproved, block that check and ask only for the specific decision needed.

Report every required check separately using `passed`, `failed`, `not_run`, `blocked` or `not_detected`. Use `passed` or `failed` only for an observed execution result. Use `not_run` when execution was unavailable or was not attempted; use `blocked` when an authorization or safety boundary prevented it; use `not_detected` when no applicable command is supported by project evidence. Never invent output or count a missing/skipped check as passed. A passing check does not satisfy another required gate.

For each result, include the exact command, source when discovered, working directory, observed exit code and output, affected artifacts and limitations. If a shell or tool wrapper can mask the command's exit status, capture the process status during that same invocation; do not rerun a deterministic check only to recover its code. Retry only when there is evidence of a transient cause, and retain the first result. For exit 0 with an unexpected change, preserve the file and before/after evidence, report the discrepancy, and pause affected downstream writes. Do not clean, reset, stage or rerun to hide it.

Resolve response language from explicit user preference, then the request, then English when indeterminate. Keep commands, status labels, schema keys and supplied identifiers unchanged. Read [check selection](references/check-selection.md) for source selection, wrapper inspection and result decisions.
