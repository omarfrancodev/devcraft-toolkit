Create `feature/parser` in the existing linked worktree at `eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`. Use Git directly; the two indistinguishable toolkit installations provide no basis for choosing one. Disable hooks for this invocation so the uninspected helper cannot run, and explicitly disable submodule recursion.

Run from the linked worktree:

```powershell
$parserBase = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
$parserHooks = Join-Path ([IO.Path]::GetTempPath()) ("parser-empty-hooks-" + [guid]::NewGuid())
New-Item -ItemType Directory -Path $parserHooks -ErrorAction Stop | Out-Null

$parserStatusBefore = @(git status --porcelain=v2 --untracked-files=all --ignored)
$parserMainBefore = git rev-parse refs/heads/main
$parserTaskBefore = git rev-parse refs/heads/task

git -c "core.hooksPath=$parserHooks" -c submodule.recurse=false switch --no-recurse-submodules -c feature/parser $parserBase
if ($LASTEXITCODE -ne 0) {
    throw 'Branch creation failed; stop without cleanup or recovery operations.'
}

git symbolic-ref --short HEAD
git rev-parse HEAD
git rev-parse refs/heads/task
git rev-parse refs/heads/main

$parserStatusAfter = @(git status --porcelain=v2 --untracked-files=all --ignored)
Compare-Object $parserStatusBefore $parserStatusAfter
```

Verification must show:

- Current branch: `feature/parser`.
- `HEAD`: the supplied commit.
- `task` and `main`: their recorded values.
- No status differences, including dirty submodule and ignored-file entries.

If the branch already exists or Git refuses the switch, stop and report the error. Do not force, reset, clean, stash, update submodules, or execute the helper.