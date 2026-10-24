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

