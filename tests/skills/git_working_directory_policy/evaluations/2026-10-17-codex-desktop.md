# Evaluation: git-working-directory-policy

- Date: 2026-10-17
- Harness: Codex desktop task; repo-local skills cannot be dynamically activated here, so the instructions were followed directly during this task. Harness version was not exposed.
- Automated fixture command: `python -m unittest discover -s tests/skills/git_working_directory_policy/integration -p "test_*.py" -v` using Python 3.14.3; result: 6 passed.

## Observed evidence

- Git operated in a fixture path containing spaces and `ü`.
- Normal, unborn `main`, linked-worktree, and detached states were distinguished using Git output.
- Read-only context queries preserved refs, HEAD, index bytes, and working-file digests.
- Fixture commits used repository-local identity only.

## Limitations

- A submodule fixture and an isolated missing-Git executable were not exercised in this harness; those scenarios remain documented as limited.
- This is implementation self-evaluation, not an independent model-behavior result. It does not establish compatibility with other coding harnesses.
