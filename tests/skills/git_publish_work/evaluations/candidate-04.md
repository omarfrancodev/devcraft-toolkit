Mode: supplied-facts assessment only; no Git/provider operations performed. Selected installation: tests/.tmp/publication-install/full. The request authorizes selected commits, explicit synchronization with origin feature/demo, normal push and PR creation to main. It does not authorize merge or upstream setup.

Owners: git-publish-work coordinates; git-commit-builder owns the full commit workflow with git-plan-commits, git-stage-changes, git-analyze-changes, conventional-commits-style, validation-discovery, git-safety-check, git-working-directory-policy and todo-workflow-controller. git-sync-branch owns synchronization; git-publish-changes owns push; git-manage-pull-request owns PR creation. All identifiers refer to the selected installation. Track steps inline from evidence.

1. Expected own transitions A -> B -> C

Outcome: limited, with reported completed local effects and publication remaining. Reuse the existing selected work branch; branch creation is skipped. Preserve the builder's verified A -> B transition and the sync owner's verified fast-forward B -> C as reported completed steps. C is the refreshed final source for publication; A and B are stale publication sources. Do not reject the two verified own transitions as unexpected movement, or rerun commits/sync.

Sync scope is origin refs/heads/feature/demo, using its fetch endpoint; main is the distinct PR target, never an inferred sync source. The facts do not identify the push endpoint/destination, local branch name, full OIDs, hosted account/projects, validations, clean-state evidence or PR identity. Do not infer push routing from the sync selection. Bind those missing identities and refresh relevant gates before dependent writes, including checks applicable to C; earlier check coverage cannot be invented.

Push and PR remain pending. Once resolved and freshly guarded, hand the full C OID and exact destination to git-publish-changes for one normal pinned push and independent verification. An already equal destination is no_op. Then hand verified publication, fresh source/target/compare/template evidence and complete duplicate-search results to git-manage-pull-request: one exact existing open match is no_op without edits; confirmed absence permits one creation and readback. Overall completed requires both requested effects verified.

2. Unexpected D after guards pinned C

Outcome: stopped; earlier reported commit/sync effects remain completed, push and PR are blocked. D is not an accepted own transition. Do not publish D under the old proposal, push stale C automatically, or rewrite D away. Preserve actual state, obtain a focused decision on the changed source, and on explicit continuation reobserve guards and derive remaining authorized work. No automatic retry or rollback.

3. Push before commit, with the new commit included

Outcome: needs_decision before effects. The requested order cannot publish a commit that does not yet exist; selected dirty work also cannot bypass the publisher's clean-state gate. Ask whether to authorize commit -> explicit sync -> push -> PR, or revise the expected publication content/order. Do not silently reorder, add a second push, broaden staging, stash or clean. Dependent steps remain blocked until resolved. Promotion and upstream setup are skipped in all cases.
