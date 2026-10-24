# Exact index operations

## Preconditions and protection

Resolve location/Git paths first without hashing worktree content. Apply the analyzer's no-pager/no-optional-locks/no-lazy-fetch, disabled filesystem monitor/cache and nonrecursive protections while using context/preflight as well. Disable external diff/textconv. Inspect effective clean/process filters before any dependency status/worktree hashing; configured external filters keep affected worktree analysis unsupported/limited. Do not execute a filter to improve coverage.

Check repository/index selection, GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE overrides, current HEAD/index/content/inventory guards, conflicts and active operations. Do not clear an override or change repository/identity/configuration to make an operation work. Unsupported intent-to-add, sparse/skip-worktree entries, binary hunk splits or unknown modes stop the affected selection without clearing flags. Stage-only operation needs no author identity.

The operation request contains mode, actual user authorization, selected repository/index, analysis snapshot, exact selection/exclusions and a complete expected stage-zero manifest. Each manifest entry has the exact path, mode and blob OID; include unchanged unrelated entries. Initial staging may create a previously absent index. Necessary index/blob objects are permitted only in authorized mutation mode.

Observe complete target bytes and modes before mutation. For ordinary full-file content, Git hash-object without -w can calculate the expected normalized blob using the selected path/effective built-in attributes; the external-filter gate must already permit it. Never use -w in preview. Guard the effective attributes/configuration too. Symlinks are link bytes, not target contents. Gitlinks require exact local pointer evidence; do not recurse. If the harness cannot obtain exact target bytes/OIDs/modes safely, return limited.

## Supported transformations

Use argument vectors or correct literal quoting. NUL paths/patch stdin must survive transport; otherwise use safe exact argument paths where possible or return limited. Strings such as `$(noop).txt` and `[draft].txt` are data.

For selected complete working versions, use the protected Git prefix with global `--literal-pathspecs` and:

```text
add --pathspec-from-file=- --pathspec-file-nul
```

Supply only exact approved file paths separated by NUL; include explicit tracked deletions. An alternative is `add -- <exact-path> ...` with separate literal arguments. Never add a directory/glob, -A, -a or all files as a substitute for an observed selection. A path with excluded later edits is not a whole-path candidate.

For a completely understood approved text patch:

```text
apply --cached --check --whitespace=nowarn -
apply --cached --whitespace=nowarn -
```

The first command checks without writing; the second changes only the index. Refresh guards between check and mutation. Verify all patch paths and expected changes against the approved target before applying; a parseable patch is not authorization. Do not use --index instead of --cached (it writes working files), --3way, --reject, --unsafe-paths or --whitespace=fix.

An explicitly approved staged partition can use the same pair with `--reverse` to defer only its known staged patch. Record the exact deferred selection and its retained worktree content. No implicit index reset or unstage of unrelated entries is allowed. A future coordinator may restore only the approved deferrals through a fresh exact operation; failure is a stop, not automatic restoration.

## Postconditions

Capture the process exit/output in the same invocation. Read the whole index with protected `ls-files --stage -z` and compare every path/mode/OID to the approved target. Verify preserved HEAD/ref/branch, bounded worktree/link bytes, configuration and exclusions. A zero exit with extra content is stopped, not staged. A nonzero exit may still have effects: inspect and report them; never claim nothing changed from the exit code alone.

Revalidate between operations; observation is not an atomic lock against another actor. Do not persist an analysis JSON, patch, message file or fallback state machine as part of this skill. Use in-memory/harness transport. Missing safe transport is a limitation, not permission to interpolate shell source.

## Example

An index has README base content and an unrelated keep.txt selection. The working README adds a rounding line and a debug line. A cached patch selecting only the rounding line must leave keep.txt's OID unchanged, preserve both lines in the worktree and change no HEAD/ref/config value. Adding the whole README would violate that target even if Git succeeds.

Official semantics: [add](https://git-scm.com/docs/git-add), [apply](https://git-scm.com/docs/git-apply), [hash-object](https://git-scm.com/docs/git-hash-object).
