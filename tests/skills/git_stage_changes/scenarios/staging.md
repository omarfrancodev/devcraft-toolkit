# Scoped staging cases

Owner: `git-stage-changes`. Runtime effects require the exact case authorization. Use disposable fixtures only.

| ID | Case | Expected |
| --- | --- | --- |
| STAGE-01 | Five supplied-transcript record controls then five complete-instruction actors | Exact whole-index comparison, preserved keep.txt/debug/HEAD, provenance, required result fields |
| STAGE-02 | Preview or bare skill invocation, or only ready preflight | planned/decision, no write permission inferred |
| STAGE-03 | Stale raw content/index, patch failure or unknown target | No write; limited/blocked; no apply fallback/reset |
| STAGE-04 | Scoped literal paths/deletions; partial file and approved reverse deferral | Exact entries/hunks only; worktree/HEAD unchanged |
| STAGE-05 | Missing identity, unborn HEAD, foreign dependency | Identity not needed for staging; no substitution for missing required skill |
| STAGE-06 | Filter/helper, sparse/intent-to-add/override or binary split | Protective gate; unsupported scope limited, no silent bypass |
| STAGE-07 | Actual live scoped patch in owned fixture | Verified index mutation only; report real execution separately from replay |
