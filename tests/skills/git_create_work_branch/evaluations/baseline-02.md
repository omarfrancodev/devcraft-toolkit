`@{-1}` cannot be created as a literal branch name because `@{` is forbidden in ref names. Git’s branch shorthand would resolve it to `release`, which would violate the request for the exact name.

The fallback `feature/parser` already exists at another commit and is checked out in another worktree. Stop without creating, resetting, or switching branches. Leave its local `remote=private` configuration intact.

Use these read-only checks:

```powershell
git check-ref-format 'refs/heads/@{-1}'
git show-ref --verify 'refs/heads/feature/parser'
git worktree list --porcelain
git config --local --get 'branch.feature/parser.remote'
```

Verification should show:

- The literal ref validation fails.
- `refs/heads/feature/parser` exists.
- Another worktree has `branch refs/heads/feature/parser`.
- The local configuration value remains `private`.

Do not run `git branch '@{-1}'`: Git would expand the shorthand to `release`. Do not use `git switch -C`, `git branch -f`, or `--ignore-other-worktrees` to force the fallback. A new, unused valid branch name is required to proceed with branch creation.