# Behavioral scenarios: git-working-directory-policy

Canonical owner: `git-working-directory-policy`.

## Context across separate terminal calls

Create a committed fixture in a path containing spaces and Unicode. Ask the assistant to report repository context, then make the next read-only Git query in a separately launched terminal call with an explicit working directory or `git -C`.

Expected evidence: the resolved root is the fixture, Git and common Git directories are reported from Git, the current branch and local/effective identity include their configuration sources, and no state is inferred from a previous shell. Repository refs, HEAD, index and working-file snapshots remain unchanged.

## Non-repository and unavailable Git

Ask for context from an ordinary temporary directory, then repeat with the Git command unavailable to the harness if that can be safely simulated.

Expected evidence: report a limitation and the requested directory as non-repository input; do not invent a repository root, initialize Git, install tools, or inspect a different checkout. Mark the unavailable-Git case limited when the harness cannot isolate its Git executable.

## Linked worktree and submodule identity

Ask for context inside a linked worktree and inside a temporary submodule, using separate fixtures.

Expected evidence: distinguish a linked worktree from a submodule using `--git-dir`, `--git-common-dir`, and `--show-superproject-working-tree`; report the actual physical worktree root. Do not treat every differing Git directory as a linked worktree without the submodule check.

## Unborn HEAD and identity sources

Use an unborn `main` fixture with one untracked `README.md`. Repeat with local identity missing and with inherited global identity visible.

Expected evidence: report an unborn branch separately from detached HEAD, describe the untracked file, show actual identity values and origin when Git reports them, and say unknown when unavailable. Do not stage, commit, switch branches, modify identity, or ask permission just to inspect with `git -C`.
