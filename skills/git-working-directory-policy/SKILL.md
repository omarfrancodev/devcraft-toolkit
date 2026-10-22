---
name: git-working-directory-policy
description: Discover and report the selected Git repository, worktree, branch, identity, and tool limits without changing repository state.
---

# Git working directory policy

Use this skill when the user asks where a repository is, which branch or worktree is active, or what Git context applies to a requested operation. Resolve the requested scope before inspecting anything. Do not load or inspect unrelated repositories.

## Discover context

Use the terminal's explicit working-directory option when available. Otherwise run Git with `-C <user-selected-path>`; this read-only discovery does not require approval. Do not assume a terminal session persists between commands. Preserve spaces and Unicode in paths by passing each argument separately.

Collect evidence with read-only Git commands:

- `git rev-parse --show-toplevel` for the worktree root.
- `git rev-parse --git-dir` and `git rev-parse --git-common-dir` for the worktree Git directory and shared Git directory.
- `git rev-parse --show-superproject-working-tree` to detect a submodule.
- `git symbolic-ref --short -q HEAD` and `git rev-parse --verify HEAD` to distinguish a named branch, an unborn branch, and detached HEAD.
- `git --no-optional-locks status --short --branch` for the observed branch and working-tree summary when relevant. Keep optional locks disabled for every `status` inspection so Git does not refresh and write optional index data.
- `git config --show-origin --get user.name` and `git config --show-origin --get user.email` for effective Git identity and the configuration source Git reports.

Use the selected path as the command working directory or pass it to `git -C` on every independently launched command. If Git reports that the path is not a repository, say so plainly. If Git is unavailable, report that limitation. Never invent a root, branch, identity, or configuration origin.

## Classify the repository

Resolve the physical worktree root from Git. A nonempty superproject path identifies a submodule. Otherwise, differing Git and common Git directories identify a linked worktree. A normal checkout generally uses the same Git and common Git directory. Report detached HEAD only when HEAD exists and there is no symbolic branch; report unborn HEAD when the symbolic branch exists but HEAD does not resolve.

Identity is observational. Report each value and its origin as Git returned it. If a value is absent or conflicting, say that it is unavailable or conflicting; do not substitute a machine identity. Do not change repository or global Git configuration.

## Return

Give a compact context record containing:

- Repository root, Git directory, and common Git directory.
- Repository kind: normal checkout, linked worktree, submodule, or not identified.
- Branch, detached, or unborn state, with HEAD evidence when available.
- Effective `user.name` and `user.email`, each with its reported source or an explicit unknown value.
- Relevant working-tree summary, observed tool limitations, and the directory used for command execution.

Use the local [context reference](references/context.md) for a concise result shape and state distinctions.

Match the user's explicit language preference, then the language of the request, then English if the language is indeterminate. Keep Git commands and identifiers unchanged. This skill only discovers context; it does not authorize Git writes or decide whether a commit or publication is safe.
