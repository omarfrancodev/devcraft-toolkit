`outcome: needs_decision`

Mode: supplied-evidence analysis; no mutation performed.

The reported request authorizes creation but does not supply a valid available literal target. Reject `@{-1}` before any branch-aware parser: it is previous-checkout expression syntax and must not expand to the reported `release` branch.

Do not attempt the fallback `feature/parser`. Reported evidence says `refs/heads/feature/parser` already exists at another commit and is selected in another worktree. Its reported `branch.feature/parser.remote=private` configuration must remain unchanged. Neither switching to that branch nor resetting it is authorized.

Required decision: supply one exact, valid, unused local branch name. Do not invent a suffix or reinterpret the requested expression.

Operation: stop before branch creation. No Git creation, switching, configuration change, retry, or recovery operation was attempted.

Verification/outcome: no live Git verification was performed; all repository facts above are reported evidence from the actor input. Current source OID, HEAD, repository context, helper effects, preservation state, and fresh guards remain unverified. A chosen valid name would require those checks before one bounded create-and-switch attempt. No `created` or `no_op` result is established.

Resources read under `C:/Users/Developer.INSCORSOF2/Documents/Proyectos-Code/omarfrancodev/devcraft-toolkit/.worktrees/publish-work`:

- `skills/git-create-work-branch/SKILL.md`
- `skills/git-create-work-branch/references/branch.md`
- `skills/git-working-directory-policy/SKILL.md`
- `skills/git-working-directory-policy/references/context.md`
- `tests/skills/git_create_work_branch/fixtures/WB-02.json`
