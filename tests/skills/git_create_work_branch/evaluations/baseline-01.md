Create `feature/parser` directly at the supplied current commit. Switching at the same commit preserves the index and working files, including README’s separate staged and unstaged changes. No commit, stash, identity configuration, or network access is needed.

Proposed PowerShell commands; not executed:

```powershell
$expected = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

if ((git branch --show-current) -ne 'main') {
    throw 'Expected main.'
}
if ((git rev-parse HEAD) -ne $expected) {
    throw 'Current commit differs from the supplied commit.'
}

$beforeStatus = git status --porcelain=v1 --untracked-files=all --ignored
$beforeStaged = git diff --cached --binary
$beforeUnstaged = git diff --binary

git switch -c feature/parser $expected
if ($LASTEXITCODE -ne 0) {
    throw 'Branch creation failed; stop without further changes.'
}

if ((git branch --show-current) -ne 'feature/parser') {
    throw 'Unexpected active branch.'
}
if ((git rev-parse HEAD) -ne $expected) {
    throw 'Unexpected branch commit.'
}
if (
    (($beforeStatus -join "`n") -cne
        ((git status --porcelain=v1 --untracked-files=all --ignored) -join "`n")) -or
    (($beforeStaged -join "`n") -cne
        ((git diff --cached --binary) -join "`n")) -or
    (($beforeUnstaged -join "`n") -cne
        ((git diff --binary) -join "`n"))
) {
    throw 'Working state differs from its original snapshot.'
}
```

Expected outcome: `feature/parser` becomes active at `aaaaaaaa…`; `main` and `release` retain their existing pointers. README’s staged A and unstaged B, the tracked deletion, untracked `diseño.txt`, and ignored `.env` remain in place. If `feature/parser` already exists, creation fails without replacing it.