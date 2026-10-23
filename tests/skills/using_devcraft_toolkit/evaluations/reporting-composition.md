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

## Follow-up baseline — exact supplied-facts activity-report request

Date: 2026-10-22

Method: five independent fresh contexts received the exact current installed entry, composition reference, and standalone report skill. Each received the same user request and facts. No root documentation, scenario assertions, or evaluation files were shown.

Request: “Use Devcraft Toolkit to write an activity report from these supplied facts. Return it here in Spanish.”

Facts: Date: 2026-10-20. Empty-name validation was added. A clear error for missing names was added. Search rendering is pending. Twelve fixture cases passed.

**Baseline result: FAIL (5/5).** Three actors said the report could not be produced because activity reporting was planned or unavailable. Two actors produced a report but described the toolkit capability as unavailable and treated `natural-language-report-writer` only as a separate alternative. Thus the same installed configuration yielded a refusal or a contradictory fallback instead of an observable optional route. The reports that were produced preserved the date, count, and pending state. No actor inspected Git or the project history, and none wrote files.

The exact user-facing dispositions were: (1) “No puedo redactar el informe mediante Devcraft Toolkit” and no report; (2) “El flujo de informes de actividad de Devcraft Toolkit no está disponible” followed by a report attributed to the standalone skill; (3) “Devcraft Toolkit aún no ofrece la capacidad” followed by an alternative report; (4) “La distribución instalada ... no ofrece la capacidad” and no report; (5) “esa capacidad está planificada y no disponible en esta distribución base” and no report.

## Follow-up GREEN — installed and absent variants

Date: 2026-10-22

Method: ten independent fresh contexts received the exact final installed resources and the same request/facts as the follow-up baseline. Five contexts had the entry, its foundation dependencies, and `natural-language-report-writer` installed; five had only the entry and its foundation dependencies. Actors did not see the scenario assertions, root docs, or evaluation files. Repository-local skill loading remains unavailable, so each actor manually followed the supplied resource files.

**REPORTING-ENTRY-02 — installed route: PASS (5/5).** Every actor selected `natural-language-report-writer` and returned a Spanish report from the supplied facts. All preserved 2026-10-20, the count 12, and search rendering as pending. None inspected Git/history or wrote a file. The five renderings varied naturally in phrasing while preserving those facts.

**REPORTING-ENTRY-03 — skill absent: PASS (5/5).** Every actor reported `natural-language-report-writer` unavailable and did not draft or imitate the report, install the skill, inspect Git/history, or access other files beyond the two supplied entry resources.

The installed wording resolves the baseline inconsistency and the absent-installation rule remains consistent. These results establish manual instruction following in fresh Codex desktop collaboration-agent contexts; they do not establish native skill loading or cross-harness behavior.
