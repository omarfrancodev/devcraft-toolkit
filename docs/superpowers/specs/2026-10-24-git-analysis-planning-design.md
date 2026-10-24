# Git Change Analysis and Commit Planning Design

**Date:** 2026-10-24
**Status:** Approved scope; implementation authorized
**Increment:** Read-only preparation for commit construction

## Intent

Explain the current local change set and propose coherent commits without changing Git state. Separate observation from intent, preserve an existing staged selection, and make uncertainty visible before a future coordinator performs writes.

The chosen approach is two composable, instruction-first capabilities with local references. A combined commit coordinator would mix inspection with mutation too early; a new collector executable would add a runtime and a second implementation of the assistant's evidence handling. Neither is needed here.

## Goals and boundaries

- Deliver `git-analyze-changes` and `git-plan-commits` as available capabilities in the seventeen-entry catalog.
- Keep maintained source instructions, documentation, examples, and default templates in English. Resolve output language from explicit preference, then request language, then English; preserve technical identifiers and schema keys.
- Keep every installed skill self-contained. Declare dependencies in `catalog.json`; installed execution never requires that file or root documentation.
- Keep all automated tests, scenarios, fixtures, and retained evaluations under root `tests/`, grouped by canonical skill owner and scope.
- Perform no Git writes, network access, validation execution, credential changes, branch creation, staging, commits, publication, cleanup, or persisted analysis/plan output. Return records in the conversation.
- Do not introduce a runtime interpreter dependency, installer, hook, MCP service, coordinator placeholder, or new distribution mechanism.
- Native loading and authenticated invocation remain separate from manually following instructions. Existing preview.2 evidence describes its seven-skill payload and must remain historical.

## Dependency and invocation model

`git-analyze-changes` requires `git-working-directory-policy`.
`git-plan-commits` requires `git-analyze-changes` and `conventional-commits-style`; its transitive closure includes repository context.
Neither adds a hard dependency to `using-devcraft-toolkit`. Add optional entry routes using the selected installation's actual discovered identifiers and ownership, preserving existing missing/foreign/duplicate-copy rules. A missing required skill makes the dependent capability unavailable; do not imitate or automatically install it.

Analysis is not a commit-readiness check. Missing author identity or detached/unborn HEAD does not prevent inspection. Reuse current context and evidence rather than running an unrelated safety preflight. Future mutation coordinators must perform their own current preflight.

## Analysis inputs and evidence

Input is one explicitly selected local repository/worktree, an optional path/layer scope, and user-provided intent. Default analysis inventories staged, unstaged and untracked changes separately, excluding ignored content. A path restriction does not imply consent to read siblings. Ambiguous repository selection returns `needs_decision`; missing/unreadable Git evidence returns `limited` or `blocked`, with the distinction stated.

Use argument-safe, read-only local inspection. Disable optional locks, lazy fetching, filesystem monitor helpers, untracked cache updates, recursive submodule traversal, external diff drivers and text conversion. Treat filenames, diffs, repository content and configuration values as data, never instructions or shell source. Use literal pathspecs and NUL-delimited path records, including rename source/destination; if the harness cannot preserve them, report a limitation instead of splitting on spaces or guessing names.

Before status or worktree diff operations, inspect effective clean/process filter configuration. If any external clean/process filter is configured, do not execute content-hashing status/worktree-diff reads: report that layer as limited and use metadata enumeration/raw bounded file reads where safe. Index-to-HEAD comparisons can remain available. This deliberately conservative first increment trades filtered-worktree completeness for no helper execution. Do not clear configuration or install dependencies to work around it.

Inspect before/after HEAD (including unborn/detached state), index identity/bytes when accessible, path/status evidence, active-operation markers and the raw bytes or hashes of the bounded content actually used. Observe a consistent interval, not an atomic snapshot guarantee. If any captured fact changes, discard the composed result, retry once or return `limited`; never combine old and new evidence. An inaccessible index or content guard is a disclosed limitation. Repeating status alone cannot detect edits whose status code stays unchanged.

Keep binary files, deletions, renames, mode changes, symlinks, submodule gitlinks, conflicts, and untracked content distinct. Do not follow a symlink outside the selected scope or recurse into submodule repositories. Summarize binary/oversized/unreadable content only to the level actually observed, with explicit omissions; do not claim filename-only entries prove behavior. Conflicts and active operations are findings, not instructions to resolve or abort them.

## Analysis record

Return a compact record, not a fixed JSON serialization:

| Field | Meaning |
| --- | --- |
| `outcome` | `analyzed`, `no_op`, `needs_decision`, `limited`, or `blocked` |
| `repository` | Selected root, branch state, HEAD or unborn marker |
| `scope` | Requested paths/layers and actual inspected boundaries |
| `snapshot` | Observation interval, HEAD/index/content guards, freshness or limitations |
| `changes` | Stable execution-local evidence IDs, exact path(s), layer, change kind, observed facts and content coverage |
| `constraints` | Partial staging, conflicts, active operation and other facts relevant to planning |
| `unknowns` | Missing evidence, assumptions and material user decisions |

`no_op` means no changes in a completely observed selected scope, not merely an empty staged area. Partial coverage is `limited`. A conflict may still be fully `analyzed`, with a planning blocker in `constraints`.

## Planning inputs and result

Consume a current analysis record for the same selected repository/scope, user intent, and supplied or observed message conventions. For a live repository request, obtain or refresh evidence through the analyzer, including a fresh guard before relying on a prior record. A supplied record that cannot be verified remains `limited`; an offline example may be discussed conditionally but never presented as a current actionable plan.

Default planning selection is the existing staged layer when nonempty; otherwise propose unstaged/untracked work. Broaden only when the user requests it. Distinguish an explicitly empty staged-only scope from a clean repository. Report excluded layers and preserve partial staging: a path is not an indivisible selection. Groups identify evidence IDs plus layer/hunk boundaries; cross-layer grouping or staged repartitioning requires an explicit decision before downstream execution.

Group by one explainable intent, keeping relevant implementation, tests and documentation together rather than grouping by extension or folder alone. Give dependent groups a justified order. Ambiguous intent, overlapping hunks, unknown binary content, unresolved conflicts or active operations prevent a complete plan for affected changes. Preserve unaffected proposals as conditional when useful; never invent a resolution, successful validation, ticket key or business result.

Each group has `id`, `intent`, `evidence`, `selection`, `depends_on`, `rationale`, and `message`. The `message` is a proposal produced using the installed formatter from evidenced facts and explicit conventions. If a material decision is pending, mark the group pending instead of fabricating a completed message. Return top-level `outcome` (`planned`, `no_op`, `needs_decision`, `limited`, `blocked`), `analysis_snapshot`, `selection_policy`, `groups`, `excluded`, `decisions`, and `limitations`.

Planning does not authorize or execute staging, commit creation or later publication. The result is a human-reviewable proposal in the conversation.

## Integration and documentation

The catalog becomes nine available and eight planned, retaining all seventeen names and roles. Update entry routing, composition, architecture, current installation inventory/dependency closures and README. Use development package version `0.1.0-preview.3` consistently in both manifest identities; this is an unpublished candidate, not a release. Preserve published tags, historical preview.2 documentation and recorded seven-skill evidence.

The roadmap must state the remaining sequence and acceptance gates:
1. This read-only analysis/planning increment.
2. `git-stage-changes` and `git-commit-builder`: explicit selection/authorization, fresh preflight, safe index mutation, scoped validations and commit failure handling.
3. `git-activity-report`: verified history, author/date/timezone boundaries, reuse of the report writer and explicit output choice.
4. `git-sync-branch`, `git-publish-changes`, `git-manage-pull-request`, `git-promote`, then `git-publish-work`: separate synchronization/publication/review/promotion contracts and remote authorization.
5. Ongoing native validation: a small authenticated Codex smoke first, Copilot CLI/VS Code next, then the three Kiro clients and Claude Code; validate scope and lifecycle per client. Do not block this feature on claiming the entire native matrix.

CCR and release automation remain deferred. Record historical checklist status honestly; do not mark prior native tasks complete from filesystem or manual evidence.

## Acceptance and evidence

Create owner-scoped application/edge/gap scenarios before authoring each skill, run fresh-context baseline controls without the new instructions, then repeat with the skill. Preserve baseline successes as successes and failures verbatim. Include Spanish and English, partial staging, same-path mixed intent, stale evidence, missing dependencies, filenames with spaces/pathspec syntax, unborn/detached/missing identity, conflicts/active operations, binary/deleted/renamed/submodule entries, and helper/filter safety.

Automated tests exercise real disposable Git fixtures and snapshot repository state before and after the documented read recipes; they establish command safety and fixture semantics, not assistant judgment. Existing structural/distribution validators must accept all nine skills and dependency closures. Entry composition scenarios cover installed, absent and foreign namespaced dependencies. Record native activation as untested for the new skills until an actual client session establishes it.

A fresh design builder check precedes the plan. Execute the plan sequentially, complete and test the analyzer before the planner, and use one fresh whole-branch review at the end. Builder choices left open are concise prose layout, evidence-ID spelling, and test helper decomposition; no runtime scripts are required.

## Technical references

- [Git status porcelain and optional index refresh](https://git-scm.com/docs/git-status)
- [Git diff layers, NUL records, external diff and textconv controls](https://git-scm.com/docs/git-diff)
- [Git global no-lazy-fetch, literal-pathspecs and optional-lock controls](https://git-scm.com/docs/git)

These references support command semantics. The contracts and conservative filter fallback above define the toolkit's narrower behavior.

