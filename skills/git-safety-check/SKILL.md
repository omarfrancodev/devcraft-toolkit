---
name: git-safety-check
description: Read Git state for an inspect, commit, or publish request and return an evidence-based preflight without changing the repository.
---

# Git safety check

Use this skill only to preflight the user's requested Git intent. It depends on `git-working-directory-policy` for repository context when that skill is available. Context is not a lock: refresh volatile Git facts before deciding.

## Inputs and evidence

Accept intent `inspect`, `commit`, or `publish`, plus the selected repository context when available. If no context exists, discover only the selected repository. Use explicit working directories or `git -C` in every separately launched command. Keep spaces and Unicode intact.

Refresh the facts relevant to the intent with read-only Git commands: conflict and in-progress-operation state, branch/HEAD state, staged/index state, unstaged and untracked files, effective `user.name` and `user.email` plus their origins, and whether a commit exists. Run status inspection as `git --no-optional-locks status ...` so Git cannot refresh optional index data. Do not run stage, unstage, commit, checkout/switch, fetch, push, stash, reset, clean, or repair commands.

Preserve the user's exact existing index selection and unstaged exclusions. Do not stage untracked or unstaged content on the user's behalf. Inspecting state does not require Git identity.

## Decide by intent

- `inspect`: report observed facts even when identity is missing, HEAD is unborn, or conflicts exist. Use `ready` if the requested inspection completed; use `limited` if Git or necessary evidence was unavailable.
- `commit`: return `no_op` when an existing committed worktree has no changes to commit. An unborn branch with a known, unambiguous identity can be `ready` for initial-commit preparation; do not create the commit. Conflicts or an active operation return `blocked`. Missing or conflicting identity blocks a future commit. Inherited global identity with unclear personal/work context returns `needs_decision`. Detached HEAD returns `needs_decision` until the user gives a branch strategy.
- `publish`: require an existing commit and a clean index and worktree. No commit, conflicts, active operations, or dirty state return `blocked`. Detached HEAD returns `needs_decision` until the user chooses a branch strategy. Do not fetch to test remote freshness; state when that evidence was not inspected.

Ask only for a material unresolved decision. A missing progress or structured-question tool alone is not a safety failure. If a required decision remains unanswered, wait before any dependent mutation.

## Return

Return one outcome: `ready`, `no_op`, `blocked`, `needs_decision`, or `limited`. Include the affected intent, the Git evidence that supports the outcome, identity values and sources when relevant, and any limitation. A `ready` preflight authorizes only this conclusion; it is not permission to mutate, publish, merge, or release.

Match the user's explicit language preference, then the language of the request, then English when indeterminate. Preserve status labels and technical identifiers. See the local [preflight reference](references/preflight.md) for the result shape.
