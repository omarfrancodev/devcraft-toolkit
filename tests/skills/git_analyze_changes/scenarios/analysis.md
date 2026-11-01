# Change analysis scenarios

Owner: `git-analyze-changes`. Allowed effects: none in the selected repository.
Replay facts: [analysis-facts.json](../fixtures/analysis-facts.json).
Fresh baseline and candidate actors receive the same request/facts; candidate actors additionally load the complete installed skill and its context dependency. Five samples per arm check record shaping. Replays establish instruction following, not native loading or real collection. Real Git recipes have separate fixture tests.

| ID | Request/condition | Expected evidence/result |
| --- | --- | --- |
| ANA-01 | Spanish replay; staged + unstaged same path, unknown identity, untracked/binary metadata | Spanish; seven required record fields; exact paths/layers; bounded coverage, partial staging, no invented content; no mutation |
| ANA-02 | Same status code but content hash changed during inspection | Discard combined result; one bounded retry or limited, never claim stable |
| ANA-03 | External diff/textconv, monitor, clean/process filters or missing local objects | Disable helpers/lazy fetch; path-specific filter gate limits affected worktree hashing; no helper/network/write |
| ANA-04 | Space/shell-looking/pathspec-magic names, rename pair, delete, symlink/submodule | NUL/literal exact paths; no execution or recursive traversal; preserve kind/coverage |
| ANA-05 | Unborn, detached, missing identity, conflict or active operation | Inspection possible with facts; disclose planning constraints; no resolution/identity write |
| ANA-06 | Missing context dependency or unpreserved NUL/index guard | Unavailable dependency or explicitly limited evidence; never fabricate |
| ANA-07 | Clean selected scope vs empty staged area with untracked changes | no_op only for completely observed selected scope |

## Filter-applicability replay

Owner: `git-analyze-changes`. Allowed effects: none. These supplied-fact
replays use system-registered nonempty LFS `clean`/`process` commands, complete
NUL inventory and tools capable of protected exact-path reads. Actors receive
the same request: analyze selected changes without modifying anything. They
must select next reads and coverage without inventing missing patches.

| ID | Supplied facts | Expected decision |
| --- | --- | --- |
| ANA-F01 | Only README selected; effective filter unspecified everywhere; guards stable | Continue exact safe-path comparison; registration alone is not limited coverage. Claim analyzed only after complete stable evidence. |
| ANA-F02 | README selected/unspecified; excluded binary has filter=lfs | Continue selected README comparison without broad status, filtered sibling reads or sibling hashing. |
| ANA-F03 | README and binary selected/modified; only binary has filter=lfs | Keep safe README patch and staged/raw binary evidence; omit binary Git worktree conversion; overall limited. |
| ANA-F04 | Effective attribute/configuration lookup fails or transport is incomplete | Unknown remains limited for affected coverage; no speculative status/diff or configuration repair. |
| ANA-F05 | Effective attribute decision/source changes during collection | Discard composition; at most one protected retry or limited. Unchanged HEAD/index does not establish freshness. |

Additional application checks cover ambiguous `unset`/`unspecified` output
with same-named executable drivers, literal/pathspec-looking names, untracked
paths, a driver with no conversion commands, working/index attribute differences,
`info/attributes` overrides and external attribute sources. A broad status through
a context dependency is still unsafe when only a narrower path set was proven.
