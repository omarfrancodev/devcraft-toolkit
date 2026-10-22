# Cross-skill scenario: context refresh before Git preflight

Participating skills: `git-working-directory-policy`, `git-safety-check`.

1. Discover context for a clean committed fixture and retain its reported HEAD/status.
2. Change a tracked file and stage a distinct new file after discovery.
3. Request a commit preflight using the previous context packet.

Expected evidence: `git-safety-check` refreshes volatile Git state, reports the unstaged and staged changes as they exist now, and preserves the exact index/worktree snapshots. It must not reuse the stale clean result or change repository state.
