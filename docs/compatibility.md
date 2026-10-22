# Compatibility and validation evidence

## Intended portability

The available skills use Markdown instructions, YAML frontmatter, relative resources, and Git commands. Their instructions prefer explicit command working directories or `git -C` and do not depend on a persistent shell. This design intent is not a compatibility claim for any untested harness.

## Observed in this implementation task

- Harness: Codex desktop, 2026-10-22. Fresh agent contexts evaluated behavior without the candidate skill, followed by fresh contexts manually following repository instructions for GREEN. A separate context assessed baseline results. This environment did not expose native activation of repository-local skills, so the results do not verify native skill discovery or loading.
- Conventional Commit standalone behavior: eight named cases covered ambiguity and correction, project-specific type/scope/body, breaking markers, shell-looking text, language changes without a repository, missing intent, and ticket placement. All final GREEN assertions passed under manual following; no Git or ticket tools were used.
- Toolkit composition behavior: direct use, optional routing, and absent formatter installation were evaluated. Initial route runs disagreed: one discovered the formatter through its description, while another treated the word “commit” as a Git preflight request. An explicit route for message drafting and review resolved that ambiguity. The absent-installation case reports the missing formatter without imitation or installation.
- Python: 3.14.3; PyYAML: 6.0.3; Git for Windows: 2.45.0.windows.1.
- The automated suite discovered 57 tests and passed with one environmental skip. The Windows symlink escape fixture was skipped because the OS denied the required symlink privilege. The validator includes containment checks, but that symlink case was not dynamically exercised here.
- Read-only context/preflight queries preserved refs, HEAD, index bytes, Git metadata outside the object database, and working-file contents and modes in the fixture suites.

## Limits

The skill behavior evaluations are manual instruction-following assessments in fresh agent contexts, not native skill-loader tests. Isolated package installation could not be confirmed because PyPI DNS/network access was unavailable. The submodule scenario, isolated missing-Git executable, external standalone installation, and unanswered-decision interaction were not dynamically exercised. No other harness or plugin installation has been validated. Structural tests prove repository checks and fixture state, not language quality or instruction following.
