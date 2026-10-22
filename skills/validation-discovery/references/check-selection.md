# Check Selection and Result Decisions

## Find evidence without guessing

Start with an explicit user-supplied command, then inspect applicable project instructions and definitions that exist in the selected project or subproject. Relevant sources can include `package.json`, `Makefile`, `pyproject.toml`, `composer.json`, solution or project files, and task-runner definitions. Report the source location, exact command, working directory and intended check. If no applicable definition is found, return `not_detected`; do not substitute a conventional command from memory. A non-Git directory may still be a valid project.

In discover mode, return the candidates and their apparent effects without execution output. A package script may have lifecycle hooks or wrappers, so inspect the full command path before treating its friendly name as an ordinary test or lint command. Check relevant dependencies, environment assumptions and output locations. An unknown or materially unapproved effect blocks that candidate; it does not silently authorize execution.

## Inspect composed commands

Read each component of a wrapper, including pre/post hooks and chained shell commands. Identify installation, update, autofix, cleanup, migration, deployment, publication, destructive or external effects. Do not run those operations under an ordinary validation request. A fully inspected local composite may run when the user requested the validation and its effects fit the selected project and authorized scope. If the supported shell or required tool is unavailable, record the limitation and do not invent an outcome.

## Record each gate independently

Give every required check its own status and evidence:

| Status | Use when |
| --- | --- |
| `passed` | The check ran and its observed result satisfies the gate. |
| `failed` | The check ran and its observed result does not satisfy the gate. |
| `not_run` | The check was not attempted or execution was unavailable. Include why and any limitation. |
| `blocked` | A safety boundary or missing authorization prevented execution. State what decision is needed. |
| `not_detected` | Project evidence does not define an applicable check. |

Capture the actual command, source if discovered, working directory, exit status, stdout/stderr, relevant artifacts and limitations. If a shell or tool wrapper can mask the command's exit status, capture the process status during that same invocation; do not rerun a deterministic check just to recover its code. Do not claim a multi-check request passed until every required gate has an observed passing result. A deterministic failure is retained; retry only once when a transient cause is observed, and preserve the first failure.

## Unexpected changes

Compare the selected project's relevant state before and after execution when the task depends on a clean result. Expected, scoped local test/build artifacts may be allowed when disclosed. If exit 0 coincides with an unexpected file, index or working-tree change, preserve the evidence, report the exact change and pause dependent writes. Do not remove the change, reset, stage or rerun simply to make the record look clean. A later justified check is additional evidence and never replaces the original result.

## Language

Use the user's explicit language preference, then the request language, then English when indeterminate. Translate explanatory text and default templates; preserve commands, status labels, schema keys, filenames and supplied identifiers exactly.
