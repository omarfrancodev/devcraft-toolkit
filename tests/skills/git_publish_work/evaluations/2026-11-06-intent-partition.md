# Commit intent partition evaluation

Date: 2026-11-06. Owners: `git-plan-commits`, `git-commit-builder`, and `git-publish-work`.

## Planner replays

Fresh Codex Desktop assistant contexts applied the unchanged installed Devcraft Toolkit `0.1.0-preview.11` planner or the revised development resources. The actors read the planner, analyzer, context and formatter resources and received only the request and supplied observations. These were read-only replays without live freshness verification.

The baseline passed both cases. For the exact PW-06 patch, it selected the parser hunk `@@ -1,6 +1,6 @@` and logging hunk `@@ -13,4 +13,4 @@` in separate groups using A1, with no dependencies. For half-cent rounding, it grouped B1 and B2 and explained how the implementation and test protect the same behavior. These observations do not establish a baseline failure for PW-06.

| Revised replay | Observed output |
| --- | --- |
| PW-06 supplied patch | `limited`. Two independent groups use disjoint exact unstaged selections of A1. The subjects describe empty-input errors and raw-token redaction. |
| PLAN-10 | `limited`. One group cites B1 and B2. Its rationale connects the `Decimal` `ROUND_HALF_UP` implementation and the `1.005 → 1.01` regression to the same half-cent rule. |
| PLAN-11 | `needs_decision`. Proposed two exact staged selections from C1, kept their messages pending repartition, and excluded C2, an unstaged debug edit in the same file. |
| PLAN-12 | `needs_decision`. The metadata-only logo change stayed pending. The response identified the missing purpose and exact path/layer evidence. |
| PLAN-13 | `limited`. The reusable address normalization (E1) and its checkout consumer (E2) remained separate. E2 depends on E1 because it consumes the helper. |

## PW-06 live application

The fresh actor ran in Codex Desktop using Git for Windows 2.45.0 and Python 3.14.3. It read a copied development closure with `git-publish-work`, `git-publish-changes`, `git-create-work-branch`, `git-commit-builder`, `git-plan-commits`, `git-analyze-changes`, `git-stage-changes`, `git-safety-check`, `git-working-directory-policy`, `conventional-commits-style`, `validation-discovery` and `todo-workflow-controller`. The fixture used an isolated Git configuration, a trace wrapper, and a disposable bare `origin` on the same host. Its initial `main` was `47d9b1dc89cd1b06c9201d74da9d4c7d73652208`, with a clean staged delta and exactly one modified file, `work.txt`. No required project checks were detected.

The actor received the publication request and the live fixture. Before the first staging mutation, it returned this handoff from the observed unstaged diff:

| Group | Intent and rationale | Evidence and selection | Dependencies | Message |
| --- | --- | --- | --- | --- |
| G1 | Correct the parser section's empty-input result, a concern independent of token logging. | A1, unstaged `work.txt`, only `@@ -1,6 +1,6 @@` | None | `docs(parser): document empty-input errors` |
| G2 | Document raw-token redaction in the logging policy, independently of empty-input behavior. | A1, unstaged `work.txt`, only `@@ -13,4 +13,4 @@` | None | `docs(logging): document raw token redaction` |

Order followed the file order. Both groups were complete, with no exclusions or pending decisions.

### Independent Git verification

Outcome: `completed`. The actor trace recorded one branch creation, two exact cached patch applications, two ordinary commits and one normal push, in that order. All six mutations exited 0. The push used the verified second OID as its source.

| Remote commit | Parent | Subject | Only change relative to parent |
| --- | --- | --- | --- |
| `2b39c53575c82a1e513e85b9b421fe209f02ac34` | `47d9b1dc89cd1b06c9201d74da9d4c7d73652208` | `docs(parser): document empty-input errors` | `Empty input returns a token.` → `Empty input returns an error.` |
| `8b04996c585cf5573cc9a56274b3a30c3bdf1612` | `2b39c53575c82a1e513e85b9b421fe209f02ac34` | `docs(logging): document raw token redaction` | `Logs may include raw tokens.` → `Logs redact raw tokens.` |

Direct reads from the bare remote found exactly these two commits above the base and resolved `refs/heads/fix/parser-notes` to `8b04996c585cf5573cc9a56274b3a30c3bdf1612`. The client had a clean index and worktree. Local and remote `main`, unrelated refs and local configuration were preserved.

Fixture setup initially hit the Windows path-length limit. The evaluation used a shorter disposable path. An unprivileged remote preflight read could not launch the local Git transport, so the actor used scoped permission for the local-only transport. The traced push completed on its first attempt.

## Second-group failure

In a separate disposable fixture, a local `commit-msg` hook accepted the parser documentation commit and rejected the logging commit with exit 1 and `fixture: reject second group`. Independent Git observations found HEAD still at the first commit `8f932051960cb3b18b9c4f3576eef1403c32b8f6`, the second hunk staged, and only `main` at `4828e7d1fc9756c3df6dde03eedd6802a5b873ef` on the bare remote.

The deterministic hook was exercised in a Git control. A separate fresh assistant received the resulting failure receipt and applied the revised coordinator and builder policies at that decision point. It returned `partial`, preserved the verified first commit and staged second hunk, and stopped the push. This separation evaluates the post-failure decision without asking a live coordinator to ignore a known downstream blocker.

## Other checks and limits

- All 20 focused Python tests passed, including planner fixtures, commit-builder controls, publication package closure, and Git composition.
- Repository catalog and distribution validation passed. A fresh read-only review found no actionable issues.
- The live result measures one application of copied instructions in a disposable repository. Native skill loading and hosted publication were outside the evaluation. The Python composition control uses a prescribed partition and is evidence for Git mechanics.
