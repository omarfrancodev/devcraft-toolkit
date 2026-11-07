# Planning reference

## From analysis to selected evidence

The analyzer returns `outcome`, `repository`, `scope`, `snapshot`, `changes`, `constraints` and `unknowns`. Each change has a local evidence ID, exact path(s), layer, kind, observed facts and coverage. Preserve those IDs within this execution; do not assign new meaning to an old ID after refreshing evidence.

For a live request, use the analyzer's guarded reads to verify a prior record before relying on it. A different repository/scope or changed HEAD/index/content means refresh, not reuse. If the analyzer cannot establish freshness, return limited. A timestamp or matching status code alone is not verification. An offline example remains conditional even if its recorded guards were equal.

First restrict evidence to the user's requested paths; this narrows files without choosing additional layers. Then choose layers:
1. Explicitly requested layers only. A staged-only selection may be empty while other layers are dirty.
2. Without an explicit layer request, existing staged content within the path scope when nonempty.
3. Otherwise, unstaged and untracked changes within that path scope.

A request such as “plan commits for src/total.py” selects only that path's staged changes when present; it does not also select its later unstaged debug edit. Exclude supporting tests outside the requested paths rather than silently broadening. If staged work exists only outside the requested paths, it does not suppress the fallback for the selected paths.

A limited analysis of unselected work does not automatically block a fully observed selected subset. State the limited coverage outside that selection. Unknown content or purpose inside the selection prevents a complete group/message for that content.

## Intent, layers and order

Identify the reasons for the selected changes from the diff before deciding how many groups to propose. Keep independently describable purposes in separate groups. A shared file, layer, component, ticket, PR or publication request is insufficient to establish a common purpose. Implementation and its directly supporting tests or documentation can belong together when the diff connects them to the same behavior.

Split a file within a layer when observed hunks serve separate purposes. Use the analyzer's evidence ID together with the exact hunk selection. Groups may reference the same evidence ID for disjoint selections. Across complete groups, account for each selected change exactly once. If the evidence cannot establish a purpose or a stageable boundary, identify what is missing and keep the affected selection pending.

For each proposed group, include:
- `id`: execution-local group ID.
- `intent`: one evidenced purpose or pending decision.
- `evidence`: analyzer change IDs used.
- `selection`: exact paths and staged/unstaged/untracked layers, plus observed hunk boundaries when a path/layer must be divided. If boundaries are not observed, mark pending instead of inventing line numbers.
- `depends_on`: earlier group IDs only, with a factual reason; empty when independent.
- `rationale`: why this grouping is coherent and exclusions are separate. If the complete plan has one group, name the concrete common purpose, connect every selected change or set of supporting edits to it, and explain why they form one commit. A file list or summary of the publication goal is insufficient.
- `message`: formatter-produced proposal, or pending with the material question.

An existing staged area is a user selection. If it contains several intents, propose possible groups but record an explicit repartition decision. If the user explicitly requests a multi-commit decomposition, that permits proposing the split, not executing index changes; preserve exact boundaries and make their review explicit. Cross-layer inclusion also stays a decision unless the user requested those layers. Never advise add-all as the implementation of a mixed-layer plan.

Order groups only for actual dependencies. A feature using a new helper follows the helper when each has a distinct purpose. Leave independent groups without dependencies and record a decision for cyclic or ambiguous dependencies.

## Outcomes and blockers

- `blocked`: required dependency/access is unavailable, unresolved conflicts or an active operation prevents completing the affected plan. Do not resolve or abort it. Conditional unaffected groups are explanatory, not executable approval.
- `needs_decision`: a material intent/selection/boundary choice prevents a complete proposal. Ask one focused question; leave affected groups/messages pending.
- `limited`: selected evidence/freshness cannot be established. Provide conditional useful groups with explicit limits.
- `no_op`: the completely observed selected scope is empty; this says nothing about excluded layers.
- `planned`: selected evidence is current and complete, groups have justified boundaries/order and proposed messages, with no material decision pending.

When several limits apply, report the strongest applicable blocker and list the others. A complete plan does not prove validation or author identity readiness; later mutation workflows must run their own fresh preflight.

## Example

Evidence A1 is the staged rounding fix in `src/total.py`. A2 is a later unstaged debug print in the same path, and A3 is the staged regression test. G1 selects A1 and A3 under the staged-first default. Its rationale names correct half-cent rounding as the common purpose. A1 changes the rounding behavior and A3 verifies that same behavior, so they form one commit. Exclude A2 as unrelated unstaged work. Ask about it only if it affects the requested selection.

Supply the evidenced correction and repository conventions to `conventional-commits-style`; for an English request a suitable proposal could be `fix(totals): correct decimal rounding`. This is message text, not a command. In a supplied-fact replay the overall result remains limited until live guards can be verified.
