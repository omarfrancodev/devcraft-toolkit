# Commit coordinator scenarios

Owner: `git-commit-builder`. Real mutations occur only in explicitly owned disposable fixtures.

| ID | Case | Expected |
| --- | --- | --- |
| COMMIT-01 | Five baseline then five complete-instruction supplied-transcript records | Outcome/mode/auth/groups/validations/actual commits/remaining/state/limits; preserve provenance |
| COMMIT-02 | Plan-only request; explicit commit request; formatter-only request | No implicit writes from planning; no redundant authorization for exact requested commits |
| COMMIT-03 | Unrelated staged data or multiple intents | Concrete partition/deferral decision; no commit -a/--only/alternate-index bypass |
| COMMIT-04 | Dirty-worktree validation vs selected index; required failed/not_run check | Scope truthful; required unavailable gate blocks, no silent stash/install |
| COMMIT-05 | Unknown hooks/signing; exit0 changed committed tree/message; failed hook | No bypass; preserve actual effects and stop |
| COMMIT-06 | First commit verified, second fails | partial with actual first SHA, remaining scope and state; no rollback/retry |
| COMMIT-07 | Foreign/missing dependency, identity ambiguity, detached strategy, stale record | Block/decision/limited before affected writes |
| COMMIT-08 | Actual one-group live fixture | Requested index commit, exact tree/message/parent/identity, excluded worktree retained |
