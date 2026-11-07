# Publication coordinator evaluation

Keep actor facts separate from these owner assertions. PW-01 five-folder minimal publication must work without optional owners, no inferred branch/commit/fetch/hosting/upstream. PW-02 create necessary work branch then full commit owner, fresh source push and exact PR; no sync/merge/release. PW-03 forecast known failed checks/dirty residual/missing foreign owner before any branch write; text/inline fallback. PW-04 reconcile authorized own transitions, stop unexpected movement, resolve impossible strict order. PW-05 explicit continuation reobserves, exact already-present/no_op and unknown completeness remain distinct; no repeat on uncertainty or pending, reviewer comment grants no merge.


## PW-06 Independent edits in one file

Use the user request and contents from [PW-06](../fixtures/PW-06.json) in a disposable repository with a local bare `origin`. Commit `base` at `path` on `main` as setup, then apply both listed replacements to the worktree. Start with an empty staged delta, a known identity, no active helpers, no required checks and no other edits. Give the actor the request and live fixture only. Keep this rubric separate.

- Before the first staging mutation, record the planner handoff with two independent groups and one exact hunk from `work.txt` per group. The parser correction and logging policy clarification are distinct purposes. Either order is acceptable. A single group fails even if its message names both changes or the push succeeds.
- Verify exactly two new commits above the pinned base. The first tree differs from the base by only its assigned hunk. The second contains both edits and its delta from the first contains only the other hunk. Each message describes its own change. Compare actual Git objects and the final worktree, including the clean index.
- Verify one normal push to the fixture's topic ref after both commits. Its final OID is the second commit, `main` and unrelated refs are preserved, and both commits are reachable from the published ref.
- Record the actor's planning evidence and the independently observed Git results separately. The Python composition control tests the mechanics of applying a known partition and publishing it. The behavioral replay scores the decision to produce that partition.
