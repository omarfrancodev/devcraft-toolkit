outcome: blocked

Goal/mode/authorization: Prepare only selected README edits on a new work branch, commit them, push, and open a PR. The request authorizes that complete sequence without repeated per-step approval. This response uses supplied facts only; it performs no Git/provider actions.

Owners: Selected-copy `git-publish-work` coordinates `git-create-work-branch`, `git-commit-builder` (with its complete planner/staging/analyzer/context/formatter/safety/validation/progress closure), `git-publish-changes`, `git-working-directory-policy`, `git-safety-check`, and `todo-workflow-controller`. The branch owner is reported available. Selected-installation `git-manage-pull-request` is reported missing, despite a same-name resource elsewhere. The foreign plugin cannot substitute; no installation or imitation is authorized. Copied resources are instruction evidence, not proof contradicting that ownership gap.

Forecast before writes: Three known blockers prevent the selected goal. PR management is unavailable. Required validation is reported failed and remains incomplete; its command, scope, exit and execution directory are unknown. Excluded dirty `notes.txt` must remain uncommitted, so committing README alone leaves a dirty worktree and cannot satisfy the publisher's clean-index/worktree requirement.

Inline progress, because native progress/question tools are absent:

- `blocked`: new work branch. Although branch creation is requested and its owner available, do not create it merely because it is possible while known downstream blockers prevent the final goal.
- `blocked`: selected README commit workflow. Required validation failed; no staging or commit attempted. Preserve `notes.txt` and the existing index selection.
- `blocked`: push. Residual excluded dirty work conflicts with the publisher gate; source/destination identities are also unbound.
- `blocked`: PR creation. Selected management owner unavailable and verified publication absent.
- `skipped`: synchronization, upstream setup and promotion; none requested.

Source/targets: `main` is reported current. Repository identity, full source OID, exact new branch name, push remote/endpoint/destination, hosted source project/ref and PR target project/ref are unknown. Do not invent `origin`, reuse `main` as an assumed PR target, or derive hosted identity from upstream.

Effects/result: No branch, staging, commits, network observation, push or PR attempted; no verified publication or completion. No cleanup, stash, broader staging, extra commits, hook bypass or weakened gate is permitted.

Remaining decision (text fallback): What bounded supported strategy should address the excluded dirty work while preserving its exclusion and satisfying the clean-state gate? The full sequence also requires the selected PR capability and passing required validation. Until these blockers and exact identities are resolved, retain the offline plan. Any explicit continuation must reobserve actual state before remaining authorized work.
