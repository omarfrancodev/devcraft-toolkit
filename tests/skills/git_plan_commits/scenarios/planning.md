# Commit planning scenarios

Owner: `git-plan-commits`. Allowed effects: none in the selected repository.
[Replay facts](../fixtures/planning-facts.json) include a prior analysis record; no live repository is attached.
Five fresh baseline controls and five complete-instruction candidate samples use identical facts. Score semantic record structure separately from baseline judgment. Replay plans remain conditional/limited, not current executable plans.

| ID | Condition | Expected |
| --- | --- | --- |
| PLAN-01 | Spanish request; staged rounding code/tests, unstaged debug same file, metadata-only untracked entries | Existing staged selection; one intent group for code/tests; excluded layers; seven top-level/group fields; proposed message from formatter; limited freshness in replay |
| PLAN-02 | User requests all layers; same file contains two independent intents | Separate evidence and layer/hunk boundaries, explicit repartition decision; no stage-all advice |
| PLAN-03 | Current live analysis, no staged work, independent implementation/test/docs + dependent follow-up | Group by intent, justified order and complete selected evidence; proposed messages only |
| PLAN-04 | Prior record guards differ, guards unavailable, or old repository selection differs | Refresh through analyzer or limited; no current actionable plan from stale/offline record |
| PLAN-05 | Explicit staged-only scope empty while worktree dirty | Selected-scope no_op only after complete verified observation; exclude worktree without calling repo clean |
| PLAN-06 | Missing formatter/analyzer or foreign namespaced dependency | Unavailable; no imitation/install or cross-installation substitution |
| PLAN-07 | Conflict/active operation, unknown binary intent or ambiguous overlapping hunks | Blocked/needs_decision/limited for affected selections, conditional unaffected groups; no fabricated message/resolution |
| PLAN-08 | English request or explicit language override | English or explicit language output; preserve identifiers/technical keys |
| PLAN-09 | Path-only request for src/total.py; A1 staged fix + A2 unstaged debug; A3 supporting staged test outside path | Select A1 only by staged-first default; exclude A2/A3 without an unnecessary layer decision. If selected path has no staged work, staged content elsewhere does not suppress its unstaged fallback. |
| PLAN-10 | One unstaged diff changes half-cent rounding to `Decimal` `ROUND_HALF_UP` (B1) and adds a regression for `1.005 → 1.01` (B2) | One group selects B1/B2. Its rationale links the implementation and regression to the same half-cent behavior. |
| PLAN-11 | The two independently observable hunks from [PW-06](../../git_publish_work/fixtures/PW-06.json) are both staged. An unrelated debug edit in the same file is unstaged. | Propose two exact staged hunk selections. Report `needs_decision` for repartition, keep affected messages pending and preserve the index and excluded debug edit. |
| PLAN-12 | One selected path has a metadata-only binary change, or the supplied evidence cannot locate separate parts of a mixed-intent hunk. | Identify the missing purpose evidence or exact hunk boundary and keep affected work pending. Never treat the unknown portion as part of a complete group. |
| PLAN-13 | An unstaged change introduces reusable address normalization (D1). A separate unstaged checkout feature consumes it (D2). | Two exact groups with D1 before D2 and a reason for the dependency. Do not merge both changes under the checkout objective. |
