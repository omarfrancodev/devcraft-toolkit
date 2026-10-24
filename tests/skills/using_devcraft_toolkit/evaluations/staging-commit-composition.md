# Staging/commit entry composition

Date: 2026-10-24. Owner: `using-devcraft-toolkit`.
Fresh Codex desktop contexts manually loaded only the entry/reference: gpt-6.1-sol medium for baseline, high for candidate. These are synthetic discovery facts, not native loader/tool execution.

## Baseline

The old entry lacked a stage route and explicitly declared commit creation unavailable despite supplied installed capabilities. Cases A/B therefore failed new routing expectations. Existing C (foreign-only stage), D (missing owned dependency) and E (owned formatter-only) boundaries held and are baseline successes.

Verbatim: A: “No staging route available.” B: “Commit creation unavailable.” E chose `toolkit:conventional-commits-style` without Git preflight.

## Candidate

| Case | Observed | Result |
| --- | --- | --- |
| A | Exact `toolkit:git-stage-changes`; owned closure; unresolved dependency invocation IDs remain unresolved; selected hunk only | Pass |
| B | Exact `toolkit:git-commit-builder`; explicit commit workflow permission, identity/check/effect/partition gates; no branch/publication implication | Pass |
| C | Foreign-only stage unavailable; no imitation/install/substitution | Pass |
| D | Owned builder unavailable without selected validation dependency; foreign copy rejected | Pass |
| E | Exact owned formatter alone, no Git context/preflight | Pass |
| F | Complete direct standalone nine-skill builder closure usable without entry/reportwriter; no invented namespace | Pass |
| G | Bare invocation/proposal defaults to planning; no staging/commit/check execution permission inferred | Pass |

Retained excerpts: A: “nunca inferir whole-file staging” is reflected by the selected-hunk response; actual actor wording: “Delegate target and postcondition decisions to the staging skill; never infer whole-file staging.” D: “Do not run builder planning or execution through an incomplete closure.” G: “A bare builder invocation or proposal request means read-only planning.”

The candidate did not execute capabilities. Actual owned-repository staging/commit evidence belongs to the corresponding skill evaluations. Native registration/activation remains unverified for these new capabilities.
