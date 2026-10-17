# Compatibility and validation evidence

## Intended portability

The available skills use Markdown instructions, YAML frontmatter, relative resources, and Git commands. Their instructions prefer explicit command working directories or `git -C` and do not depend on a persistent shell. This design intent is not a compatibility claim for any untested harness.

## Observed in this implementation task

- Harness: Codex desktop task, 2026-10-17. The app did not expose a way to dynamically activate repository-local skills in this task, so the authored instructions were followed directly and recorded as self-evaluations.
- Python: 3.14.3; PyYAML: 6.0.3; Git for Windows: 2.45.0.windows.1.
- The final suite ran from a worktree virtual environment with system site packages. PyYAML was available from the base Python; isolated package installation could not be confirmed because PyPI DNS/network access was unavailable.
- Automated fixtures exercised normal, unborn, linked-worktree, detached, dirty, staged, conflicted, and missing-identity Git states.
- Read-only context/preflight queries preserved refs, HEAD, index bytes, and working-file digests in the fixture suites.
- The Windows symlink escape fixture was skipped because the OS denied the required symlink privilege. The validator includes containment checks, but that symlink case was not dynamically exercised here.

## Limits

The recorded skill evaluations are self-evaluations in the implementation task, not independent model-behavior evaluations. The submodule scenario, isolated missing-Git executable, external standalone installation, and unanswered-decision interaction were not dynamically exercised. No other harness or plugin installation has been validated. Structural tests prove repository checks and fixture state, not language quality or instruction following.
