# Planning reference

## From analysis to selected evidence

The analyzer returns `outcome`, `repository`, `scope`, `snapshot`, `changes`, `constraints` and `unknowns`. Each change has a local evidence ID, exact path(s), layer, kind, observed facts and coverage. Preserve those IDs within this execution; do not assign new meaning to an old ID after refreshing evidence.

For a live request, use the analyzer's guarded reads to verify a prior record before relying on it. A different repository/scope or changed HEAD/index/content means refresh, not reuse. If the analyzer cannot establish freshness, return limited. A timestamp or matching status code alone is not verification. An offline example remains conditional even if its recorded guards were equal.

Choose the selection in this order:
1. The user's explicit paths/layers. A staged-only selection may be empty while other layers are dirty.
2. Otherwise, existing staged content when nonempty.
3. Otherwise, unstaged and untracked changes within the requested scope.

A limited analysis of unselected work does not automatically block a fully observed selected subset. State the limited coverage outside that selection. Unknown content or purpose inside the selection prevents a complete group/message for that content.

## Intent, layers and order

One commit explains one intent. A change to behavior plus its tests/docs is usually one group; unrelated debug output is another possible intent, even in the same path. Filename, directory and extension alone are not enough to infer the purpose.

For each proposed group, include:
- `id`: execution-local group ID.
- `intent`: one evidenced purpose or pending decision.
- `evidence`: analyzer change IDs used.
- `selection`: exact paths and staged/unstaged/untracked layers, plus observed hunk boundaries when a path/layer must be divided. If boundaries are not observed, mark pending instead of inventing line numbers.
- `depends_on`: earlier group IDs only, with a factual reason; empty when independent.
- `rationale`: why this grouping is coherent and exclusions are separate.
- `message`: formatter-produced proposal, or pending with the material question.

An existing staged area is a user selection. If it contains several intents, propose possible groups but record an explicit repartition decision. If the user explicitly requests a multi-commit decomposition, that permits proposing the split, not executing index changes; preserve exact boundaries and make their review explicit. Cross-layer inclusion also stays a decision unless the user requested those layers. Never advise add-all as the implementation of a mixed-layer plan.

Order groups only for actual dependency: a feature using a new helper follows the helper; unrelated changes have no invented dependency. A cyclic or ambiguous dependency requires a decision. No group can claim selected evidence it does not cover, and no hunk belongs to multiple complete groups.

## Outcomes and blockers

- `blocked`: required dependency/access is unavailable, unresolved conflicts or an active operation prevents completing the affected plan. Do not resolve or abort it. Conditional unaffected groups are explanatory, not executable approval.
- `needs_decision`: a material intent/selection/boundary choice prevents a complete proposal. Ask one focused question; leave affected groups/messages pending.
- `limited`: selected evidence/freshness cannot be established. Provide conditional useful groups with explicit limits.
- `no_op`: the completely observed selected scope is empty; this says nothing about excluded layers.
- `planned`: selected evidence is current and complete, groups have justified boundaries/order and proposed messages, with no material decision pending.

When several limits apply, report the strongest applicable blocker and list the others. A complete plan does not prove validation or author identity readiness; later mutation workflows must run their own fresh preflight.

## Example

Evidence A1 is the staged rounding fix in `src/total.py`; A2 is a later unstaged debug print in that path; A3 is its staged test. With no broadening request, G1 selects A1/A3 as the staged rounding correction. Exclude A2. Ask whether to keep debug output only if that choice affects the requested selection; do not block the staged proposal on an unrelated excluded change.

Supply the evidenced correction and repository conventions to `conventional-commits-style`; for an English request a suitable proposal could be `fix(totals): correct decimal rounding`. This is message text, not a command. In a supplied-fact replay the overall result remains limited until live guards can be verified.

