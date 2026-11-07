# Commit Partitioning by Intent Implementation Plan

> **For agentic workers:** Use `superpowers:executing-plans` to implement this plan task by task. Steps use checkbox syntax for tracking.

**Goal:** Separate evidenced intents, including multiple intents in one file, and explain every complete single-commit proposal.

**Architecture:** Keep intent analysis in `git-plan-commits` and carry its existing group records through `git-commit-builder` and `git-publish-work`. Evaluate both assistant decisions and Git composition against the same publication fixture.

**Tech stack:** Markdown skills, JSON fixtures, Python `unittest`, Git, disposable local remotes.

**Spec:** [Commit Partitioning by Intent](../specs/2026-11-06-intent-based-commit-partition-design.md).

## Global constraints

- Keep the existing skill ownership, staging permissions, checks and push requirements.
- Preserve the existing group fields, including exact selection, evidence, dependencies, rationale and message.
- Keep existing staged-first behavior, exclusions, and exact authorization for staged repartition or index deferral.
- Use owned disposable repositories and a local bare remote for the behavioral run. Keep the assertion rubric separate from the actor.

## Review focus

- Two fully staged independent hunks must surface a repartition decision before index writes.
- Selected content with incomplete coverage must remain pending with the missing evidence identified.
- A behavior change and its directly related test must form one group with an evidence-linked rationale.
- A distinct dependent follow-up must be ordered after the prerequisite without being folded into it.
- A failed second group must preserve the first commit and stop the dependent push.

## Task 1 — Make intent boundaries explicit in the planner

**Files**

- Modify `skills/git-plan-commits/SKILL.md` under “Choose commit boundaries” and `skills/git-plan-commits/references/planning.md` under “Intent, layers and order.”
- Extend `tests/skills/git_plan_commits/scenarios/planning.md` with the planner-specific assertions below.

**Interface**

The planner consumes current selected evidence IDs with observed paths, layers and hunks. It returns the existing `groups` fields. A complete single group's `rationale` carries the common-purpose justification.

- [x] Define planner replays for the coherent code-and-test case, two staged intents, unknown or overlapping boundaries, and a distinct dependent follow-up. Score one rationale linking both IDs, two proposed groups with an explicit pending index decision, pending affected evidence, and a justified dependency between separate groups, respectively.
- [x] Replay the current instructions in a fresh assistant context against PW-06 and the coherent code-and-test case. Save the actual pre-change grouping and rationale. Score against the new rubric and record any unexpected baseline passes.
- [x] In the planner skill, require the selected diff to be assessed for distinct purposes before finalizing groups. In its reference, spell out insufficient grouping evidence, observed same-file hunk splits, exact coverage, and the existing `rationale` requirement for a single complete group.
- [x] Re-run the planner replays in fresh contexts and compare their groups, rationales and pending decisions to the rubric. Run `python -B -m unittest tests.skills.git_plan_commits.integration.test_planning_fixtures -v` to verify the fixture mechanics.

## Task 2 — Verify that publication preserves the plan

**Files**

- Modify `skills/git-commit-builder/references/commit-flow.md` and `skills/git-publish-work/references/publication.md` where they consume the planner result and the builder receipt.
- Use [PW-06](../../../tests/skills/git_publish_work/fixtures/PW-06.json), its [scenario](../../../tests/skills/git_publish_work/scenarios/publication.md#pw-06-independent-edits-in-one-file), and `tests/skills/git_publish_work/integration/test_composition_controls.py`.

**Interface**

The builder receives the ordered groups, exact selections, rationale and decisions from Task 1. The publisher receives verified commit receipts and the resulting final OID.

- [x] Require the builder to carry the evidenced partition and rationale into exact staging. Preserve pending decisions and refresh rules. Require the coordinator to preserve the verified sequence in its handoff and to push only after all requested groups are verified.
- [x] Replay PW-06 in a fresh assistant context using the revised owned closure. Capture the plan before staging and inspect both real commit deltas, the branch, and the local remote tip independently. Pass only when there are two one-intent groups and two matching commits on the published branch.
- [x] Replay a failure after the first commit in an owned fixture with an inspected commit hook that rejects only the second group. Verify the first commit still exists and the remote topic ref remains absent. Compare with the existing second-group failure control in `tests/skills/git_commit_builder/integration/test_commit_flow.py`.
- [x] Run the focused controls and local package validators from the worktree root.

```text
python -B -m unittest tests.skills.git_publish_work.integration.test_composition_controls tests.skills.git_commit_builder.integration.test_commit_flow -v
python -B scripts/validate_repository.py --root .
python -B -m scripts.validate_distribution --root .
```

- [x] Record the exact harness and resources used, the planner handoff, and the independent Git observations under `tests/skills/git_publish_work/evaluations/`. Keep outcomes for behavior, Git controls and package validation separate.

[Observed evaluation](../../../tests/skills/git_publish_work/evaluations/2026-11-06-intent-partition.md)

