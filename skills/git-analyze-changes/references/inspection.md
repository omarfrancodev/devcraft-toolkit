# Inspection and evidence reference

Use this reference as part of the analyzer. All examples are local read operations from the selected repository root, not shell text to concatenate with untrusted data.

## Safe command setup

Use an argument-vector API where available. A shell must quote each literal argument for that shell; never interpolate filenames/configuration values as code. The following prefix is denoted SAFE below:

```text
git --no-pager --no-optional-locks --no-lazy-fetch -c core.fsmonitor=false -c core.untrackedCache=false -c core.splitIndex=false -c submodule.recurse=false
```

If Git does not support a protective option, stop the affected reads and return limited; do not remove it silently. Do not set persistent configuration. No aliases, external diff/textconv, hooks, clean/process filters, validation commands or recursive submodule reads may execute.

First inspect effective external filter configuration with SAFE followed by:

```text
config --get-regexp ^filter\..*\.(clean|process)$
```

Pass the regex as one literal argument. Exit 1 means no matching entries; another failure means unknown, not no filters. Any configured nonempty clean/process command triggers the conservative gate: skip status and worktree diff/content-hashing Git commands; retain index-to-HEAD evidence and metadata/raw bounded file reads as limited. Do not clear config or run a filter to get a better comparison. Attribute/index metadata alone is not a verified worktree delta.

## Read recipes

After the filter gate permits worktree hashing, use SAFE with:

```text
status --porcelain=v1 -z --untracked-files=all --ignore-submodules=all
diff --cached --no-ext-diff --no-textconv --ignore-submodules=all
diff --no-ext-diff --no-textconv --ignore-submodules=all
```

The first diff compares index to HEAD (also supports unborn HEAD); the second compares working files to the index. These patches omit untracked content. Read selected untracked files through a bounded raw filesystem reader only when safe; do not call git add to inspect them.

For names, use NUL records, not human patch headers or whitespace splitting:

```text
ls-files --stage -z
ls-files --others --exclude-standard -z
diff --cached --name-status -z --no-ext-diff --no-textconv --ignore-submodules=all
```

Porcelain v1 -z renames contain destination then source as separate NUL records; parse that documented order. Name-status diff uses its own status/source/destination record format. Preserve exact names separately from quoted display labels. Do not claim the terminal's lossy/escaped rendering is a byte-exact parser.

For restricted paths, add global `--literal-pathspecs` before the subcommand and pass `--` plus each exact path as separate arguments. For a rename touching the selected scope, report its associated endpoint without traversing unrelated paths. Do not turn a path restriction into permission to inspect sibling content. Conflicts are identified through unmerged index stages; do not interpret a combined conflict diff as a resolved patch.

Submodules: `--ignore-submodules=all` avoids traversing their worktrees and hides gitlink changes in status/diff. Therefore inspect `ls-files --stage -z` and the local HEAD tree's gitlink entries separately when needed; report pointer changes from those OIDs, and internal dirtiness as uninspected. Never label suppressed submodule internals clean. Symlinks are link data: read the target string, not the target's contents; preserve external/unknown targets as uninspected.

## Freshness

Record an observation interval and these guards before/after all selected evidence reads:
- Named/unborn/detached HEAD and its object ID where present.
- Index bytes/hash from `rev-parse --git-path index`, resolving relative paths against the selected root; a missing index is a valid unborn fact.
- Exact selected inventory/layer records, and hashes or repeat raw reads of every bounded content input actually used (including untracked files and link target strings).
- Active-operation markers resolved through Git paths, such as MERGE_HEAD, CHERRY_PICK_HEAD, REVERT_HEAD, rebase-merge, rebase-apply, sequencer and BISECT_START. Inspect only marker presence/needed metadata.

Use filesystem reads/hashing that do not write cache files. HEAD/status alone misses same-status edits. A changed guard invalidates the composed result; one bounded retry is allowed, then return limited. Inaccessible guards, truncated output, missing local objects or unpreserved NUL records also limit the result. This verifies an observed interval, not an atomic guarantee or future readiness.

## Example

For one file staged with a rounding fix and later edited with an unrelated debug print, create two evidence entries, such as `A1: src/total.py, staged, rounding fix` and `A2: src/total.py, unstaged, debug print`. Report partial staging in constraints. A binary name with no inspected contents is metadata-only coverage, never proof of a specific behavior.

Official command semantics: [status](https://git-scm.com/docs/git-status), [diff](https://git-scm.com/docs/git-diff), [global options](https://git-scm.com/docs/git).
