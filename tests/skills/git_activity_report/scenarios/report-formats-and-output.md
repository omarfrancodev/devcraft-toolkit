# Git activity report format and output scenarios

Give only the request and inputs to the actor. Keep the expected observations with the evaluator. Run each case with a fresh context. Use the same inputs for baseline and candidate. For behavioral inputs supplied as facts, treat any response as a simulation. For live cases, independently inspect the owned fixture and compare the actual effects.

| Case | Request and inputs | Expected observations |
| --- | --- | --- |
| FMT-01 | In Spanish, ask for a file with daily grouping already named. Reply “por día” only after the format question. Repeat without a question tool and with no answer. | Ask both choices in Spanish before rendering or writing. Resume once and retain scope and file intent. Without a choice, no output file or completed report. |
| FMT-02 | November 2–4, 2026 with complete history and selected commits on November 2 and 4. Repeat for complete zero matches and for the general choice. | Daily table has three chronological rows, including November 3. Complete zero matches has three empty rows and history status `no_op`. The general report shows the period and has no required daily table. |
| FMT-03 | Inclusive start `2026-11-02T23:30:00-06:00`, exclusive end `2026-11-04T00:00:00-06:00`. Author time `2026-11-03T05:45:00Z`, committer date on November 4 locally. Try both date bases and vary the offsets without a known reporting zone. | Table dates are November 2 and 3. The author date places the commit on November 2 and the committer date excludes it. Conflicting offsets require a zone decision for daily grouping or default naming. An empty or reversed interval requires correction before inspection. |
| FMT-04 | A three-day period with limited history and no observed matching commit on the middle day. Repeat with blocked history and with insufficient output capacity. | Empty row qualifies the observation; report discloses the limit. Blocked history yields no report. Capacity failure asks for a narrower range or general format without omitting days. |
| FMT-05 | Request in Spanish, explicit English report, evidence includes `ORDER-7`, a pipe and a newline. Repeat without the language override. | Spanish question. Report follows the resolved report language, preserves dates and identifiers, and the daily table has exactly two columns. |
| FMT-06 | Cuba timezone with repeated midnight, from `2026-11-01T03:30:00Z` to exclusive `2026-11-01T05:00:00Z`. The first midnight is `04:00Z`; the second is `05:00Z`. | The report includes October 31 and November 1. The default range filename, when requested, uses both dates. |

## Output cases

| Case | Request and inputs | Expected observations |
| --- | --- | --- |
| OUT-01 | Request a file without a path for November 2 or November 2–4, with no report folder. Repeat as content-only. | Create and read back one Markdown with the deterministic single-day or range name in activities-report/. Content-only creates nothing. An explicit save-and-show request retains the save and displays the report. |
| OUT-02 | Select exact worktree-relative and absolute Markdown paths with existing parents. Repeat with a missing parent or an ambiguous path. | Use the exact selected file. For missing or ambiguous destinations ask or block, without parent creation or default fallback. |
| OUT-03 | Start with an existing report and grant permission to replace that exact file in a follow-up. Separately introduce a conflicting file after initial inspection. | Preserve old bytes before authorization. Replace only the inspected target when authorized. A collision on creation preserves the other file. |
| OUT-04 | Substitute the default folder or report target with a symbolic link or junction. Try relocating the opened default directory or a worktree ancestor before the write. Repeat normal output from a linked worktree. | Block redirection. Keep normal output in the selected worktree. |
| OUT-05 | Write the intended file but simulate readback failure or mismatch. Separately block history inspection. | Report actual effects and no verified save after a failed readback. No file for blocked history. |
| OUT-06 | Request the default file for complete zero-match and limited daily reports. | Save each usable daily table and preserve its history status and coverage caveat. |

For live variants, snapshot fixture files, relevant Git refs, HEAD, index and local configuration before/after. Verify the exact report bytes independently. When exercising a writer outside the default path, keep standalone writer permission and replacement expectations from the writer-owned scenarios.
