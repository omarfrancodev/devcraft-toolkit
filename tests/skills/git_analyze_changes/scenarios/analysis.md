# Change analysis scenarios

Owner: `git-analyze-changes`. Allowed effects: none in the selected repository.
Replay facts: [analysis-facts.json](../fixtures/analysis-facts.json).
Fresh baseline and candidate actors receive the same request/facts; candidate actors additionally load the complete installed skill and its context dependency. Five samples per arm check record shaping. Replays establish instruction following, not native loading or real collection. Real Git recipes have separate fixture tests.

| ID | Request/condition | Expected evidence/result |
| --- | --- | --- |
| ANA-01 | Spanish replay; staged + unstaged same path, unknown identity, untracked/binary metadata | Spanish; seven required record fields; exact paths/layers; bounded coverage, partial staging, no invented content; no mutation |
| ANA-02 | Same status code but content hash changed during inspection | Discard combined result; one bounded retry or limited, never claim stable |
| ANA-03 | External diff/textconv, monitor, clean/process filters or missing local objects | Disable helpers/lazy fetch; filter gate limits worktree hashing; no helper/network/write |
| ANA-04 | Space/shell-looking/pathspec-magic names, rename pair, delete, symlink/submodule | NUL/literal exact paths; no execution or recursive traversal; preserve kind/coverage |
| ANA-05 | Unborn, detached, missing identity, conflict or active operation | Inspection possible with facts; disclose planning constraints; no resolution/identity write |
| ANA-06 | Missing context dependency or unpreserved NUL/index guard | Unavailable dependency or explicitly limited evidence; never fabricate |
| ANA-07 | Clean selected scope vs empty staged area with untracked changes | no_op only for completely observed selected scope |
