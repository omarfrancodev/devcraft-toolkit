# Repository context reference

Use Git's output as the source of truth. A compact result can follow this shape:

```text
root: <physical worktree root>
git_dir: <Git directory>
common_dir: <shared Git directory>
kind: normal checkout | linked worktree | submodule | not identified
branch_state: branch <name> | detached at <commit> | unborn branch <name>
identity: user.name=<value or unknown> (from <origin or unknown>); user.email=<value or unknown> (from <origin or unknown>)
working_tree: <observed summary or not inspected>
execution_directory: <explicit directory or git -C path>
limitations: <observed limits or none>
```

An unborn branch has a symbolic branch name but no resolvable `HEAD`. Detached HEAD has a resolvable commit and no current branch. A submodule check takes precedence over the linked-worktree comparison because submodules also have separate Git metadata. Report paths returned by Git in the context of the selected worktree; do not infer other repositories from nearby directories.

All commands in this reference are read-only. Missing identity is useful evidence for later write preflight, but it does not prevent repository-context inspection.
