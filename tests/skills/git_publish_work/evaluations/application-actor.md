outcome: completed (owned fixture and emulated GitHub only).

Applied the selected copied installation by reading and executing its instructions directly; no native skill-invocation tool was available. Owners: git-publish-work, git-publish-changes, git-create-work-branch, git-commit-builder, git-plan-commits, git-analyze-changes, git-stage-changes, git-safety-check, git-working-directory-policy, conventional-commits-style, validation-discovery, todo-workflow-controller, git-manage-pull-request. Only their installed references/assets and selected fixture metadata/content were inspected; no catalog, root project documentation, evaluation recipes, helper implementation, or raw provider state was read.

Authorization selected all current work.txt edits on main, literal new feature/parser, one normal commit/push, and a non-draft cross-project PR. Progress used the inline fallback. Branch, commit, push, and PR steps completed; sync, upstream setup, promotion, and release were skipped as unrequested.

Observed normal checkout at publication-application/git/client, initial main/HEAD ed35b20fd40acea3f90f44204af875160111c73e. The index held only unchanged work.txt; its sole unstaged change added “Parser accepts selected input.” No other working files, conflicts, operation markers, external filters, active hooks, signing configuration, or target branch/config collision were detected. Effective author/committer were Fixture User <fixture@example.invalid>, from local configuration.

One guarded switch --no-guess --no-track --no-recurse-submodules --no-overwrite-ignore -c feature/parser <initial-OID> exited 0. Complete index semantics, file inventory/bytes, original/unrelated refs, and configuration were preserved.

Group G1 selected the complete working version of work.txt, with no exclusions or partition. One literal-path add exited 0; the whole index matched mode 100644/blob c31d8477a0fe3eb0c9d9339cd57f71ed0467e2e4. One ordinary commit --file=- --cleanup=verbatim with stdin message exited 0:
4716a4d44aa844a9430e6273f7bd211749560c2a
docs(parser): record selected input support
Verified parent ed35b20fd40acea3f90f44204af875160111c73e, tree 669082a6538441c15f846cdaa9603f4141319fc9, complete tree contents, message, identity, clean index/worktree, and preserved main/configuration/worktree bytes.

Validation discovery: not_detected; the selected checkout contained only work.txt and no command definitions. Automated tests: not_run. No arbitrary helper or substitute test was executed. Provider check records referenced aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa; they were not accepted as validation of this revision.

Origin’s effective push endpoint was the owned local “remote space.git”; its selected branch was absent (ls-remote exit 2). Safe direct/absent tracking destination and mapping were inspected. One protected push with push.autoSetupRemote=false, --porcelain --no-follow-tags --recurse-submodules=no and full pinned-OID:refs/heads/feature/parser exited 0. Independent endpoint advertisement returned the exact commit. Only the expected direct origin/feature/parser tracking ref was added; original main, other refs, index/worktree, and local/global configuration hashes remained preserved.

Declared wire capabilities/read/list established github.fixture.invalid, fixture-user, project 42 feature/parser -> project 7 org/repo main. Fresh complete compare covered work.txt; duplicate listing was complete and empty. Local fallback PR template was used. One JSON-stdin create, draft=false, exited 0. Independent readback verified PR #7 (global_id 10007), exact title/body/scope/OIDs, open/non-draft/unmerged state:
https://github.fixture.invalid/org/repo/pull/7
Title: Document selected parser input support.
Body accurately describes the text addition and not_run validation. Target remained the original main OID. Post-PR local guards exactly matched verified post-push guards.

Limitations: observation guards are not atomic locks; this demonstrates copied-resource application, not native activation or real hosting. All directly launched Git processes stripped inherited GIT_* and used the required fixture global config, NOSYSTEM, trace, explicit cwd, and profile-free shell. Early wire reads used direct shell environment; later read/list/create/read used the sanitized environment. Two initial unprivileged wire reads failed before Python started because WindowsApps Python was inaccessible; only those reads were retried with escalation. No mutation was retried, no uncertain effect remained, and no cleanup/config repair or auxiliary repository file was created.