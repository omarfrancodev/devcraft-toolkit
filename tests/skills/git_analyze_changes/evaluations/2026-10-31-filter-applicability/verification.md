# Verification of path-specific filter applicability

Date: 2026-10-31. Owner: `git-analyze-changes`.
Environment: Windows, Git 2.45.0.windows.1, Python 3.14.3.

## Observed checks

| Check | Observed result |
| --- | --- |
| `python -B -m unittest discover -s tests -p "test_*.py" -v` | Exit 0; 219 discovered, 217 passed, 2 skipped; 298.275 seconds. This run preceded the final reserved-driver regression. |
| `python -B -m unittest tests.skills.git_analyze_changes.integration.test_inspection_recipes tests.skills.git_analyze_changes.integration.test_filter_scope_recipes -v` | Final owner run: exit 0; all 18 passed in 53.221 seconds, including the added reserved-driver case. |
| `python -B scripts/validate_repository.py --root .` | Exit 0; repository catalog valid. |
| `python -B -m scripts.validate_distribution --root .` | Exit 0; maintained distribution contract valid; native loading is not verified. |
| `git diff --check` | Exit 0. |
| Five previous-instruction controls, five initial candidates and one final edge replay | Manually assessed decisions are retained in behavior.md and replay-facts.json; no live Git commands by actors. |
| Manual application of final source recipe | Actual system-registered LFS definitions did not block the selected unfiltered path; patch collected and evidence guards unchanged. See local-application.json. |
| Independent read-only review | One confirmed Important finding (reserved attribute-value collisions), corrected and inspected again; no confirmed remaining Critical, Important or Minor findings. |

The complete project run and the final owner run are distinct observations;
no final 220-test whole-project invocation is claimed. The final owner run
covers every changed integration control, while the earlier whole-project run
covers existing integration and structural suites.

## Regression and effects

All five baseline actors unnecessarily limited safe paths under registered LFS
configuration. The applicability recipe corrected this behavior in five fresh
candidate contexts. A final fresh edge actor also preserved the reserved-name,
configuration-precedence and staged-only boundaries.

The reserved-driver positive control initially failed its expected-OID assertion:
fixture HEAD retained CRLF while inherited automatic normalization produced LF.
Only the disposable fixture now sets `core.autocrlf=false` for that control.
The rerun and final owner run passed. No developer configuration was changed.
The positive control intentionally executes an inspected clean-only fixture
helper and expects its local sentinel write; normal protected-read phases
assert snapshots and sentinel absence. No installed LFS program runs.

Source skills remain instruction/reference resources. Real Git controls prove
command behavior and preservation on fixtures, not that every harness will
select the commands correctly. Installed plugin caches were not changed and
no release was published. Native authenticated multi-client activation and
scope/lifecycle checks remain on the existing roadmap.
