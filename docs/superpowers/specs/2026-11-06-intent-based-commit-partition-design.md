# Commit Partitioning by Intent

## Problem and scope

`git-publish-work` delegates commit construction to `git-commit-builder`, which uses the groups supplied by `git-plan-commits`. The planner asks for one evidenced intent per group, but a request to publish all work or a shared file or PR objective can be mistaken for evidence of a single intent. The publication evaluation needs a case where the chosen boundaries can be checked against real commits.

Strengthen the planner's interpretation of the selected diff, use its existing result contract, and require the publication handoff to preserve its partition. Keep the existing skill ownership, staging permissions, checks and push requirements.

## Planning requirements

1. Resolve paths, layers and exclusions using the existing selection rules. Read the selected evidence through `git-analyze-changes` before assigning groups. If selected purpose, coverage or hunk boundaries are materially unknown, keep the affected work pending under the existing `needs_decision`, `limited` or `blocked` outcome as applicable.
2. Identify the distinct reasons to change the selected content. Treat changes as separate when the selected evidence shows they serve independently describable purposes. A shared path, layer, ticket, component, PR or publication request is insufficient evidence of a shared purpose. Implementation and directly supporting tests or documentation may share a group when they support the same behavior. A real dependency orders groups and can coexist with distinct purposes.
3. Cover each selected change exactly once across complete groups. Split same-file work at observed hunk boundaries when needed, even when all selected changes are in the same layer. Preserve the existing group fields, including exact selection, evidence, dependencies, rationale and message. Keep ambiguous or unstageable boundaries pending and identify the evidence or decision needed.
4. When a complete proposal has one group, use its existing `rationale` to name the concrete common purpose, connect each selected change or set of supporting edits to that purpose, and explain why the selected changes form a single commit. A file list or a restatement of the PR goal is insufficient. A coherent change may still produce one commit. The number of files has no bearing on the required count.
5. Keep existing staged-first behavior, exclusions, and exact authorization for staged repartition or index deferral. An observed split of an existing staged selection must be proposed even if it requires a decision before execution. A request covering all edits does not authorize an unspecified index transformation.

## Publication handoff

`git-commit-builder` consumes the complete planner groups, exact selections and rationale before staging. Pending groups stay pending. For each authorized group, stage the intended tree, verify the commit, and reconcile expected transitions before the next group. `git-publish-work` uses the resulting verified tip after the complete requested sequence and publishes it through the existing owner and clean-state gates. A final clean tree is compatible with several commits.

## Alternatives considered

- Put the intent analysis and single-group rationale in the planner, then carry them through the existing handoff. This applies the same rule to direct planning and publication and requires no new result field. This is the proposed design.
- Add grouping logic to the publication coordinator. That would create two places to decide the partition and could make direct planning and publication disagree.
- Group by file or use a minimum count. File grouping misses mixed intents in one path, and a minimum count splits coherent changes.

## Acceptance

- [PW-06](../../../tests/skills/git_publish_work/scenarios/publication.md#pw-06-independent-edits-in-one-file) selects two independent hunks in one unstaged file. The planner returns two groups, the builder creates two commits with one hunk each, and the local fixture remote receives the final tip. Either group may come first.
- A selected behavior change and its directly related test or documentation can produce one group whose rationale connects all selected evidence to the same purpose.
- Two intents already staged together produce a proposed split with a pending repartition decision, preserving the index and any excluded edits. Materially unclear evidence stays pending instead of falling into a broad group.
- A dependent follow-up with a distinct purpose follows the prerequisite in its own group. An unexpected partial commit sequence does not trigger the push.
- The Python control verifies Git mechanics with a prescribed partition. A separate assistant replay of the installed instructions is the evidence for intent judgment and the end-to-end handoff.
