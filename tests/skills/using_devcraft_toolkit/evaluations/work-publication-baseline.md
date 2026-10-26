This is a routing response only. No repository, Git, or provider operations are authorized or performed.

For the selected `toolkit` installation:

- **Create a work branch:** The current entry defines no branch-creation route. Its existing preparation, synchronization, publication, and hosted-request routes do not authorize branch creation. Report this routing limitation without synthesizing a branch workflow.
- **Prepare changes, push, and open a PR:** `git-publish-work` remains planned and unavailable under the current entry. Do not emulate that coordinator. Available individual capabilities can be identified separately: `toolkit:git-commit-builder` for coordinated preparation proposals, `toolkit:git-publish-changes` for an explicitly requested normal push, and `toolkit:git-manage-pull-request` for explicit PR creation. Preparation does not itself authorize committing. These routes retain their own dependency, evidence, authorization, and verification gates; this response does not execute or compose them into a replacement coordinator.
- **Push existing commits only:** Route to `toolkit:git-publish-changes`, with owned `toolkit:git-working-directory-policy` and `toolkit:git-safety-check`. The scope is a pinned normal single-branch push and verification. It does not imply fetch, upstream setup, branch creation, commit preparation, or PR creation. No live facts are available to establish readiness.
- **Write a report from supplied facts:** Route directly to `toolkit:natural-language-report-writer`. Supplied facts remain identified as supplied facts. Return the report in the conversation unless the user explicitly selects a local destination. No Git inspection or safety preflight is needed.

Separate discovery cases:

- **Coordinator present with a minimal five-folder closure; branch, commit, and PR capabilities absent:** The current entry still declares publication coordination planned and unavailable. Do not treat discovery alone as permission to override that boundary, emulate the coordinator, or install its absent alternatives.
- **Only a foreign branch skill available:** It cannot supply a capability of the selected installation. Preserve both installations and report the selected installation's limitation; do not substitute the foreign skill.
- **Two indistinguishable coordinator owners:** Before any dependent invocation, ask: “Which installation should own this publication request?” Preserve both copies. Resolving ownership would not itself override the current entry's unavailable-coordinator boundary.
