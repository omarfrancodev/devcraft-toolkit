# Inspection and evidence reference

Use this reference as part of the analyzer. All examples are local read operations from the selected repository root, not shell text to concatenate with untrusted data.

## Safe command setup

Use an argument-vector API where available. A shell must quote each literal argument for that shell; never interpolate filenames/configuration values as code. The following prefix is denoted SAFE below:

```text
git --no-pager --no-optional-locks --no-lazy-fetch -c core.fsmonitor=false -c core.untrackedCache=false -c core.splitIndex=false -c submodule.recurse=false -c diff.autoRefreshIndex=false
```

If Git does not support a protective option, stop the affected reads and return limited; do not remove it silently. Do not set persistent configuration. No aliases, external diff/textconv, hooks, clean/process filters, validation commands or recursive submodule reads may execute.

## Decide filter applicability per path

A registered filter is not evidence that it applies to a selected file. Git LFS commonly registers `clean` and `process` commands at system or user scope even in repositories that do not use LFS. Do not request removal, disablement or reinstallation of LFS on that evidence.

Perform these metadata-only steps before any dependency status, worktree diff or Git content hashing:

1. Resolve repository/Git paths through `git-working-directory-policy` without its optional status summary. Use SAFE for Git reads. Staged-only index-to-HEAD inspection does not need worktree conversion; unknown filters must not hide that evidence.
2. Inspect effective filter commands with SAFE followed by `config --null --get-regexp ^filter\..*\.(clean|process)$`. Pass the regex as one literal argument. Exit 1 means no matching definitions; another failure is unknown. Parse NUL-terminated key/newline/value records without treating command strings as code. For each returned attribute value that could name a driver (including the ambiguous strings `unset` and `unspecified`), resolve the winning single-valued command with `config --null --get <literal-key>` for its `clean` and `process` keys; do not treat an overridden lower-precedence definition as effective. Exit 1 is an absent key, other errors are unknown. Empty values are not executable commands. Retain relevant configuration for the freshness guard.
3. Enumerate exact selected tracked and nonignored untracked paths without status, using `ls-files --cached -z` and `ls-files --others --exclude-standard -z`, restricted by literal pathspecs. Deduplicate the inventory, preserve exclusions and keep index stages/modes separately. Do not infer an empty worktree from an empty staged diff. Unknown/truncated inventory limits the affected coverage.
4. Resolve the effective working-tree `filter` attribute for those exact paths with SAFE followed by:

   ```text
   check-attr -z --stdin filter
   ```

   Supply NUL-separated literal path names on stdin and parse exact path/attribute/value NUL triplets. Verify one result for every supplied path. This metadata lookup does not execute the filter. Let Git resolve precedence, including nested/working-tree attributes, index fallback, `info/attributes`, and user/system attribute sources. Reading only root `.gitattributes` or using only `--cached` does not establish working-tree applicability. Safe separate literal arguments with `check-attr -z filter -- <paths>` are an alternative when NUL stdin is unavailable; otherwise return limited rather than lossy splitting.
5. Partition selected paths using the observed attributes and effective commands:

   | Observation | Permitted worktree evidence |
   | --- | --- |
   | `filter` is `unspecified` or `unset`, with successful queries and no nonempty conversion command for a same-named driver | Protected, exact-path Git comparison; unrelated registered commands do not block it. |
   | A named driver has no nonempty effective `clean` or `process` command, proven by the successful configuration query | Protected, exact-path Git comparison; record that there is no executable conversion. |
   | A named driver has any nonempty effective `clean` or `process` command, including `lfs` | No Git worktree diff/hashing for that path. Keep index-to-HEAD, metadata and bounded raw file evidence; mark its unverified normalized delta limited. |
   | Failed/incomplete query, unresolved attribute value such as bare `set`, or unknown applicability | Keep only independently safe evidence and limit affected worktree coverage. Unknown is not absence. |

Git serializes `-filter` and `filter=unset` identically; likewise `!filter`/absence and `filter=unspecified`. These strings alone do not prove absence. If a same-named driver has a nonempty effective command, classify the path as limited rather than allowing conversion. Do not infer that a known output word is always a boolean state.

Do not run a filter to identify or trust it, clear/override its configuration or attributes, use a driver-name allowlist, or replace normalized Git comparison with an unlabelled raw comparison. Known LFS commands remain external programs. A selected mixed scope retains full safe-path patches and separately limited filtered paths; it is `limited` overall when requested evidence is missing. Filters on excluded paths do not require reading those files or limiting the selected safe-path comparison.

Use exact approved safe-path arguments for worktree diffs, with `--no-renames` and SAFE's `diff.autoRefreshIndex=false` to avoid broad refresh and rename discovery. Never pass a directory, wildcard or empty safe list as an unrestricted command. With no safe paths, skip the worktree diff. Do not use repository-wide status through the context/safety dependency or another command as a shortcut. Status is permitted only when its entire potential worktree scan has been established free of executable/unknown filters; in a mixed or narrower proof use metadata inventory and safe-path diffs instead. Attribute/index metadata alone is not a verified worktree delta.

Repeat the effective attribute/configuration observations around selected content reads. Guard participating readable attribute sources and the selected index/inventory too; preserve source-specific limitations rather than claiming an atomic snapshot. A changed decision or source invalidates the combined evidence: discard it, retry the protected collection at most once or return limited. No change to a filter setting is authorized by analysis.

## Read recipes

For a scope whose entire scan passes the gate, use SAFE with:

```text
status --porcelain=v1 -z --untracked-files=all --ignore-submodules=all
diff --cached --no-ext-diff --no-textconv --ignore-submodules=all
diff --no-renames --no-ext-diff --no-textconv --ignore-submodules=all
```

For a narrower or mixed scope, omit status and append `--` plus exact safe paths to the worktree diff, with global `--literal-pathspecs`. Keep the index-to-HEAD comparison separately restricted to its requested paths.

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
- Effective filter commands, path-level attribute results and participating attribute-source guards used for the applicability decision.
- Active-operation markers resolved through Git paths, such as MERGE_HEAD, CHERRY_PICK_HEAD, REVERT_HEAD, rebase-merge, rebase-apply, sequencer and BISECT_START. Inspect only marker presence/needed metadata.

Use filesystem reads/hashing that do not write cache files. HEAD/status alone misses same-status edits. A changed guard invalidates the composed result; one bounded retry is allowed, then return limited. Inaccessible guards, truncated output, missing local objects or unpreserved NUL records also limit the result. This verifies an observed interval, not an atomic guarantee or future readiness.

## Example

For one file staged with a rounding fix and later edited with an unrelated debug print, create two evidence entries, such as `A1: src/total.py, staged, rounding fix` and `A2: src/total.py, unstaged, debug print`. Report partial staging in constraints. A binary name with no inspected contents is metadata-only coverage, never proof of a specific behavior.

A registered-but-unused LFS driver permits the selected README comparison. If a selected binary uses an executable LFS driver, retain its staged evidence/raw coverage and compare only the unfiltered selected text paths; do not mark the whole mixed scope fully analyzed.

Official command semantics: [attributes](https://git-scm.com/docs/gitattributes), [check-attr](https://git-scm.com/docs/git-check-attr), [status](https://git-scm.com/docs/git-status), [diff](https://git-scm.com/docs/git-diff), [global options](https://git-scm.com/docs/git).
