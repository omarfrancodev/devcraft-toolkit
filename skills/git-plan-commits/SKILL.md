---
name: git-plan-commits
description: Use when local Git changes need a proposed commit sequence, an existing staged selection contains multiple intents, or commit boundaries are unclear.
---

# Plan Commits from Evidence

Propose reviewable commits; leave repository state unchanged. Planning performs no staging, commits, branch creation, validation execution, network access or persisted output.

## Establish inputs

Require installed `git-analyze-changes` (and its `git-working-directory-policy` dependency) plus `conventional-commits-style`. Resolve actual discovered identifiers/ownership in the selected installation. Missing dependencies make this capability unavailable; do not emulate, install or substitute a foreign copy.

Resolve language from explicit preference, then request language, then English. Preserve technical names, keys and status values.

Obtain or refresh the selected repository/scope analysis through the analyzer. Reuse a prior record only after its HEAD/index/content guards are verified current. A supplied/offline record without live verification supports only a conditional `limited` proposal. Missing author identity does not block read-only planning or establish commit readiness.

## Choose commit boundaries

Follow the local [planning reference](references/planning.md).

Default to the existing staged selection when nonempty; otherwise consider unstaged/untracked work. Respect an explicit path/layer selection, including an empty staged-only scope. Record excluded evidence. Broaden only when requested.

Group by one evidenced intent: implementation, related tests and documentation usually belong together. Identify exact evidence IDs and layer/hunk selections; one filename can represent multiple selections. Proposing a split of the index or combining layers creates a pending decision before downstream execution, not permission to restage.

Give dependent groups a justified order. If intent, boundaries or selected content are materially unknown, ask one focused question and keep affected groups pending. Conflicts and active operations block a complete plan; preserve useful unaffected proposals as conditional. Do not invent resolutions, tickets, outcomes or validation success.

Use the installed formatter for each evidenced group's proposed message and explicit conventions. A pending material decision means a pending message, not a fabricated completed proposal. Formatting text alone needs no preflight.

## Return the proposal

| Field | Required content |
| --- | --- |
| `outcome` | `planned`, `no_op`, `needs_decision`, `limited`, or `blocked` |
| `analysis_snapshot` | Source repository/scope, evidence IDs and verified freshness or its limits |
| `selection_policy` | Explicit scope or staged-first default; any requested broadening |
| `groups` | Each group's `id`, `intent`, `evidence`, `selection`, `depends_on`, `rationale`, `message` |
| `excluded` | Omitted layers/changes and why |
| `decisions` | Material choices and affected pending groups |
| `limitations` | Coverage, freshness and execution limits |

Return this semantic record in conversation prose/tables, not a required JSON serialization. `planned` needs complete current selected evidence and no pending decision; `no_op` needs a completely observed empty selection. Otherwise state the applicable decision, coverage or access blocker. A proposal never authorizes later writes.

Common mistakes: grouping only by extension, treating a partially staged file as wholly selected, turning metadata-only evidence into intent, or mistaking a plan/message for an executed commit.

