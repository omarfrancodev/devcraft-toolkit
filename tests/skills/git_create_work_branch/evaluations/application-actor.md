Outcome: **created**. Explicit authorization applied only to the owned disposable fixture at:

`C:/Users/Developer.INSCORSOF2/Documents/Proyectos-Code/omarfrancodev/devcraft-toolkit/.worktrees/publish-work/tests/.tmp/branch-application/repo`

Read only the two selected copied skills and their local references. No project catalog, tests, helpers or evaluation files were inspected.

Observed Git `2.45.0.windows.1`, normal checkout, `.git` as Git/common directory. Identity: `Fixture User <fixture@example.invalid>`, both from `.git/config`. Initial source was `refs/heads/main`, raw committed HEAD:

`5b838a40469f2880c2a3c2fa509445acc56e27a3`

Original refs `refs/heads/main` and `refs/heads/release` both pointed to that OID.

Reviewed effective configuration and actual hook inventory: no custom filters/helpers/hooksPath, no active relevant hooks, only `.sample` hooks. No active operation, conflicts, alternate worktrees, sparse/split index, special index flags or gitlinks. Index was version 2, one entry, only `TREE` extension. Exact target name validated; target ref/config absent. Two in-memory snapshots immediately preceding mutation matched.

One actual attempt:

```text
git [protected context] switch --no-guess --no-track --no-recurse-submodules --no-overwrite-ignore -c feature/parser 5b838a40469f2880c2a3c2fa509445acc56e27a3
```

Exit **0**. stdout: `M	README.md`; stderr: `Switched to a new branch 'feature/parser'`.

Independent post-checks verified:

- HEAD is `refs/heads/feature/parser`; target OID equals the pinned source above.
- Original and unrelated refs preserved; only expected new ref added.
- Effective/local/global configuration unchanged; no tracking configuration added.
- Full NUL-safe index mode/OID/stage records and flags preserved.
- All four working files retained identical inventory, attributes, lengths and SHA-256 bytes.
- Staged plus unstaged `README.md`, untracked `.gitignore` and `diseño.txt`, and ignored `.env` preserved. No deleted working files existed in the observed fixture.
- Other Git metadata files unchanged; exceptions restricted to expected HEAD/new-ref/reflog/index metadata.

Every Git process stripped inherited `GIT_*` variables and used the specified isolated global config plus `GIT_CONFIG_NOSYSTEM=1`. No network, commits, config changes, extra files, retries or recovery actions.

Limit: snapshot guards detect observed movement; they do not provide an atomic lock against concurrent external writers.