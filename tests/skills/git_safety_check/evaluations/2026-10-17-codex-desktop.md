# Evaluation: git-safety-check

- Date: 2026-10-17
- Harness: Codex desktop task; repo-local skills cannot be dynamically activated here, so the instructions and decision matrix were followed directly during this task. Harness version was not exposed.
- Automated fixture command: `python -m unittest discover -s tests/skills/git_safety_check/integration -p "test_*.py" -v` using Python 3.14.3; result: 8 passed.

## Observed evidence

- Fixtures established clean, unborn, dirty, staged, conflicted, detached, and missing-identity states.
- Read-only status, HEAD, and identity-origin queries preserved refs, HEAD, index bytes, Git metadata outside the object database, and working-file contents and modes across all fixture states.
- A stale-file-metadata control showed plain `git status` refreshes the index; `git --no-optional-locks status` preserved its bytes.
- A temporary `GIT_CONFIG_GLOBAL` file showed the inherited identity value and origin; the fixture file remained byte-identical across read queries, and process environment was not mutated.
- The scenario matrix maps clean publish to `ready`, clean commit to `no_op`, unborn publish and conflicts to `blocked`, missing identity to `blocked` for commit, and detached mutation to `needs_decision`.

## Limitations

- The skill's decision quality was self-evaluated by following its instructions in this task; this is not independent model-behavior evidence.
- The scenario requiring an unanswered user decision and missing progress/question tools was not interactively evaluated. It remains documented, and no preflight result implies write authorization.
- No other coding harness compatibility is claimed.
