# Git preflight reference

Return a concise record in this shape:

```text
intent: inspect | commit | publish
outcome: ready | no_op | blocked | needs_decision | limited
repository: <selected root and branch/HEAD state>
evidence: <conflicts, operations, commit, index/worktree status, identity source as relevant>
decision_needed: <specific unresolved choice or none>
limitations: <unavailable evidence or none>
side_effects: none
```

Treat the index and working files as separate sources. A staged addition, modification, or deletion is an existing user selection. Unstaged and untracked files remain outside that selection unless the user separately asks to include them. A conflict blocks future mutation but not read-only inspection.

An unborn branch is not detached: the symbolic branch exists without a commit. It can be prepared for an initial commit when identity is known, but it cannot be published. A clean branch with a commit can pass publish preflight without a network check; report that remote freshness was not established.

Never use `ready` as authorization for an operation beyond the requested preflight.
