**Outcome: `limited` — creation authorized, execution withheld in this supplied-facts-only test.**

Reported evidence identifies attached `main` at `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`, no active operations, and toolkit-owned context available. The requested literal target is `feature/parser`, canonically `refs/heads/feature/parser`. Missing commit identity does not block branch creation. Dirty and partially staged work is compatible with creating a branch at the same commit.

The supplied evidence does not establish the selected repository root, Git/common directories, superproject state, exact context identifier, target absence/configuration/occupancy, supported Git options, helper/hook effects, or complete preservation snapshots. These gates must be resolved before an attempt; no repository facts were inferred.

**Operation, after the missing gates pass:** execute once in the owned worktree directory, passing separate literal arguments:

```text
git --no-pager --no-optional-locks --no-lazy-fetch --no-replace-objects
-c core.fsmonitor=false -c maintenance.auto=false -c gc.auto=0
-c log.showSignature=false -c submodule.recurse=false
switch --no-guess --no-track --no-recurse-submodules
--no-overwrite-ignore -c feature/parser
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

First validate the literal name and installed support, inspect write hooks/helpers and filters, and pin full refs/configuration, original HEAD, complete semantic index, operation markers, and file inventory/modes/bytes. Immediately refresh every guard; movement stops the operation without repinning.

**Verification:** independently establish selected `feature/parser` and its exact source OID; unchanged `main`, `release`, other refs, and configuration; no new tracking; unchanged index semantics and protected content. Specifically preserve README’s staged A and unstaged B separately, the tracked deletion, untracked `diseño.txt`, and ignored `.env`. Their preservation is currently reported intent, not verified fact.

No creation command, repository inspection, or mutation was performed. No actual exit/output or postconditions exist to report. A future failed hook or unexpected effect must stop dependent work without retry or rollback; `created` requires one successful attempt and every postcondition verified.

**Resources read** under `C:/Users/Developer.INSCORSOF2/Documents/Proyectos-Code/omarfrancodev/devcraft-toolkit/.worktrees/publish-work/`:

- `skills/git-create-work-branch/SKILL.md`
- `skills/git-create-work-branch/references/branch.md`
- `skills/git-working-directory-policy/SKILL.md`
- `skills/git-working-directory-policy/references/context.md`
- `tests/skills/git_create_work_branch/fixtures/WB-01.json`
