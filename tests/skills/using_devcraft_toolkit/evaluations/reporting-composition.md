# Natural-language report writer composition evaluation

Date: 2026-10-22
Canonical composed capability: `natural-language-report-writer`
Harness: Codex desktop; fresh collaboration-agent contexts, version unavailable
Method: Each actor received only its request, facts, installed-state variant, and exact installed skill resources. Assertions and scenario/evaluation files were withheld. Repository-local skill activation is unavailable, so actors manually followed the actual current instructions and resources. No repository root or Git task was supplied. The current entry and composition reference were unchanged throughout these cases.

## REPORTING-ENTRY-01 — direct call

The fresh actor used the standalone report skill without a repository root. It returned a Spanish report with translated headings, the exact date `2026-10-20`, the name-validation changes, twelve fixture cases, and search rendering marked pending.

**PASS.** The reporter's owned behavior worked without the development catalog or root documentation.

## REPORTING-ENTRY-02 — optional route with the skill installed

The fresh actor received the toolkit entry, its foundation group, and the standalone report skill as installed. It treated the report skill as an in-scope available capability and returned a Spanish activity report. It preserved the date and count, included both validation changes, and kept search rendering pending. No repository root or Git preflight result was used.

**PASS.** The requested report was handled by the installed report capability without unrelated Git work; the report's language and evidence boundaries held.

## REPORTING-ENTRY-03 — optional skill absent

The fresh actor received the toolkit entry and foundation group, with `natural-language-report-writer` absent. It replied in Spanish that activity reporting was unavailable in this installation and named the missing skill. It did not draft the report or install/imitate the absent capability.

**PASS.** The missing capability was reported honestly without an invented completed result.

## Assessment and final verification

The existing entry's general rule to offer an in-scope installed alternative handled the optional report skill, and its absent-capability rule handled the missing installation. All three cases passed, so no change to the entry or composition reference was warranted. Since the final entry contents are identical to the evaluated baseline, these same exact case runs are the final verification; they were not duplicated after a no-op implementation step.

All actors followed the actual current resource files manually in fresh contexts. This does not establish native loading or behavior on another harness. No files, Git refs, or external services were changed by the behavior actors.
## Repository checks

- `python -m unittest discover -s tests -p "test_*.py" -v`: 57 tests passed; one Windows symlink fixture skipped because the OS denied symlink creation (exit 0).
- `python scripts/validate_repository.py --root .`: passed with `Repository catalog is valid.`
- `git diff --check`: passed with no whitespace errors.
