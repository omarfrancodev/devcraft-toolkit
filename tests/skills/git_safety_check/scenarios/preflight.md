# Behavioral scenarios: git-safety-check

Canonical owner: `git-safety-check`; dependency: `git-working-directory-policy`.

## Intent matrix

| Fixture and intent | Expected outcome | Evidence |
| --- | --- | --- |
| Clean committed branch, `publish` | `ready` | HEAD exists; index and worktree are clean. No remote freshness claim without a read-only source. |
| Clean committed branch, `commit` | `no_op` | No staged or unstaged changes. |
| Unborn branch with known local identity, `inspect` | `ready` | Named branch, absent HEAD, untracked README. |
| Unborn branch with known local identity, `commit` | `ready` | Initial-commit preparation is possible; no commit is made. |
| Unborn branch, `publish` | `blocked` | No commit exists to publish. |
| Conflicted index, `commit` or `publish` | `blocked` | Unmerged paths and in-progress operation are reported. |
| Missing identity, `inspect` | `ready` | Inspection remains read-only and reports identity unavailable. |
| Missing identity, `commit` | `blocked` | Future commit cannot be authored with known identity. |
| Detached HEAD, mutation intent | `needs_decision` | Ask for a branch strategy before a future mutation. |

## Preserve existing selections

Use a fixture with staged changes and a separate unstaged edit. Ask for a commit preflight and compare refs, HEAD, index digest, and working-file digests before and after.

Expected evidence: preserve every staged and unstaged selection exactly; do not stage, unstage, commit, switch, fetch, push, stash, or repair files. `ready` is only the requested preflight result and does not authorize a write.

## Identity and missing tools

With an inherited global identity but no resolved personal/work context, `inspect` may report the value and origin; a future commit must return `needs_decision`. Missing todo or structured-question tools do not change safety status, but the assistant must wait when a required decision is unanswered. Mark unavailable Git or unexercised harness behavior as limited rather than inferring success.
