# Git Activity Report Formats and File Output Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ask for the report layout, show the complete requested period and save a verified Markdown report when a file is requested.

**Architecture:** Keep the existing coordinator and its two dependencies. Build the selected layout from the verified snapshot, have the writer compose localized prose, then route chat output, the default local save or the writer's existing explicit-path save.

**Tech Stack:** Markdown skill resources and scenario fixtures, Python 3.11+ unittest for development checks, Git 2.45+ for local history.

**Spec:** [Git Activity Report Formats and File Output Design](../specs/2026-11-06-git-activity-report-output-design.md)

**Execution evidence:** [Format and output evaluation](../../../tests/skills/git_activity_report/evaluations/2026-11-06-report-formats-and-output.md).

## Global Constraints

- Keep the three-skill installation closure and keep runtime instructions self-contained. No new runtime dependency, installation mechanism, provider integration or release change is needed.
- Git access remains read-only and offline.
- Maintained text and the new report layout reference use English. User-facing report language follows an explicit report-language instruction, then the request language, then English.
- The shared writer's standalone write rules stay intact.
- Keep tests, scenarios, fixtures and retained evaluations under root `tests/`, grouped by skill and scope.

## Review Focus

1. A format supplied in the first request still needs a choice, while the answer to that question resumes the same request (Task 1, FMT-01).
2. An instant interval ending at midnight excludes the endpoint instant. A repeated midnight can still leave that date in scope. Date conversion uses the selected timestamp and timezone (Task 1, FMT-03 and FMT-06).
3. Zero observed commits in partial coverage cannot become a confirmed empty day (Task 1, FMT-04).
4. An occupied, substituted or relocated default path cannot trigger an overwrite or escape the worktree (Task 2, OUT-03–04).
5. A created file with failed readback remains unverified. A failed explicit-path save cannot redirect to the default folder (Task 2, OUT-02 and OUT-05).

## File map

| Path | Responsibility |
| --- | --- |
| `skills/git-activity-report/SKILL.md` | Format gate, history-to-writer handoff and output dispatch |
| `skills/git-activity-report/references/history.md` | Date and coverage data required to render the selected format |
| `skills/git-activity-report/references/report-format.md` (new) | General and daily layouts and localization rules |
| `skills/git-activity-report/references/report-output.md` (new) | Destination, permissions, safe persistence and verification |
| `AGENTS.md` | Repository policy for the narrow default-output exception |
| `tests/skills/git_activity_report/scenarios/report-formats-and-output.md` (new) | Scenario inputs and evaluator assertions |
| `tests/skills/git_activity_report/evaluations/2026-11-06-report-formats-and-output.md` (new) | Actual baseline/candidate observations and execution limits |
| `tests/skills/git_activity_report/integration/test_package_closure.py` | Installed report references present and reachable in the same package |
| `tests/skills/git_activity_report/integration/test_windows_output_directory.py` | Native Windows probes for atomic directory identity, collisions and junctions |

## Task 1: Ask for the format and render verified dates

**Files:** Change the coordinator entry and history reference. Add `report-format.md`, the scenario and evaluation files, and one package test for that reference.

**Interface:** Produce `format = general | daily` after the user's choice, `scope` with first/last local date plus the actual interval and author/date basis, and `days` as ordered pairs of ISO date and matching evidence IDs for the daily layout. Pass `coverage = complete | limited` and the resolved report language to the writer. A blocked query has no renderable input.

- [x] **Step 1: Define behavioral controls and a failing package test.** Add `test_report_format_reference_is_packaged` to `HistoryPackageTests`. Assert the reference exists under the coordinator, is linked from its entry, and validates using the existing package checker. Add these independent behavior inputs and assertions:

  | Case | Input | Required observation |
  | --- | --- | --- |
  | FMT-01 | Spanish request, file intent, daily already named. Then user answers daily. | First response asks the two choices in Spanish, emits no report and writes nothing. The next response resumes the same scope once. Repeat with no structured question tool and with an unanswered question. |
  | FMT-02 | Complete November 2–4, 2026 range, matching commits on November 2 and 4 only. Repeat for complete zero matches and for general. | Daily shows three chronological rows, with November 3 marked empty. The zero-match run keeps three rows and reports `no_op`. General states the period with no mandatory daily table. |
  | FMT-03 | `2026-11-02T23:30:00-06:00` to exclusive `2026-11-04T00:00:00-06:00`. A commit authored `2026-11-03T05:45:00Z` has a committer date on November 4 locally. | Only November 2 and 3 appear. The commit lands on November 2 under author date. A committer-date selection excludes it. Different endpoint offsets without an established reporting zone prompt before daily grouping or default naming. An empty or reversed interval prompts before inspection. |
  | FMT-04 | A three-day period with limited traversal and no observed commits on the middle day. Repeat with blocked traversal and with a range too large to render. | Limited output qualifies the empty row and coverage. Blocked emits no report. Capacity failure asks for a shorter range or general layout without dropping dates. |
  | FMT-05 | Spanish request with an explicit English report, evidence containing `ORDER-7`, a pipe and a newline. Repeat without the language override. | The question stays Spanish. The report uses the requested language, preserves dates and identifier, and renders a two-column table. |
  | FMT-06 | A named timezone repeats midnight at UTC 04:00 and 05:00 on November 1. The interval starts October 31 locally and ends at the second midnight. | Include both October 31 and November 1 in the table and default range filename. |

- [x] **Step 2: Capture baseline results.** Run the package test command below before implementing and retain the missing-reference failure. Apply identical scenario inputs to the existing skill in a fresh context and record observed gaps. Keep evaluator assertions separate from actor input.
- [x] **Step 3: Implement the format gate and handoff.** Add the question and continuation rules in the coordinator, retain the date conversion and traceability in the history reference, and define the two layouts in `report-format.md`. Keep persistence behavior as-is for this task.
- [x] **Step 4: Verify the deliverable.** Run `python -B -m unittest tests.skills.git_activity_report.integration.test_package_closure -v` and `python -B -m unittest discover -s tests/skills/git_activity_report/integration -p "test_*.py" -v`. Require exit 0 and record fresh candidate outcomes for FMT-01–06. Use the timezone fixture in the history integration suite to verify both occurrences of midnight in FMT-06.
- [ ] **Step 5: Commit the format change if implementation commit authority has been granted.** Use `feat(git-activity-report): add selectable report formats` for the scoped files.

## Task 2: Save requested files to the default or explicit destination

**Files:** Change the coordinator entry, add `report-output.md`, update the repository policy and extend the scenario, evaluation and package test files. Leave the writer's source unchanged.

**Interface:** Consume Task 1's resolved format, scope, history status and report content. Choose `destination = conversation | default_file | explicit_file`. Record the exact file path and `output = not_requested | pending_decision | verified | failed` separately from history status. An explicit-file call passes the exact selected path and replacement authorization to the writer.

- [x] **Step 1: Add failing package and write controls.** Add `test_report_output_reference_is_packaged` with the same packaging assertions as Task 1. Exercise real filesystem behavior in owned temporary worktree fixtures. Record before/after inventories, selected file readback and Git snapshot equality independently of assistant claims.

  | Case | Input | Required observation |
  | --- | --- | --- |
  | OUT-01 | Explicit file request with no path, absent folder, and November 2 or November 2–4 scope. Repeat as content-only. | One verified Markdown under `activities-report/` with the exact deterministic single-day or range filename. The content-only run creates nothing. |
  | OUT-02 | Explicit repository-relative and absolute Markdown paths with existing parents. Repeat with missing parent or ambiguous path. | Exact path is used and verified. Missing or ambiguous destination prompts or blocks, with no parent creation or default fallback. |
  | OUT-03 | Pre-existing default report, followed by explicit replacement permission for the exact path. Repeat with a conflicting file appearing during creation. | Initial bytes survive until authorized replacement. The race causes a no-clobber failure. |
  | OUT-04 | Default folder or report path redirected through a symlink/junction. Try substituting a newly created directory before its first open, colliding with exclusive directory creation, and relocating an open directory or a worktree ancestor before a write. Repeat with a selected linked worktree and an ordinary folder. | Redirected paths cannot be written. Ordinary output stays in the selected worktree and never uses the primary checkout's folder. |
  | OUT-05 | Write succeeds but readback fails or differs, then a separate blocked history query. | Receipt reports actual partial effects and no verified save. Blocked history creates nothing. |
  | OUT-06 | Complete zero-match daily report, then a limited-history daily report, both with authorized default-file output. | Each usable report saves with the correct table and status. The limited receipt keeps its coverage caveat. |

- [x] **Step 2: Capture baseline results.** Run the package test before implementing and retain the missing-reference failure. Apply the output scenarios against Task 1 and retain the observed default-path gaps and existing explicit-path behavior.
- [x] **Step 3: Implement bounded persistence.** Add the policy exception in `AGENTS.md`, the destination and verification rules in `report-output.md`, and the three dispatch paths in the coordinator. Preserve the default path's containment and no-clobber rules and keep explicit saves under the writer's existing contract.
- [x] **Step 4: Verify both save paths and existing behavior.** Reapply OUT-01–06 and the existing report writer standalone file scenarios. Run the commands below from the worktree. Require exit 0 and retain actual candidate observations. A symlink/junction test the host cannot exercise is recorded as unverified with the reason, never as a pass. Distinguish manually loaded skill behavior from native harness activation.

  ```bash
  python -B -m unittest discover -s tests -p "test_*.py" -v
  python -B scripts/validate_repository.py --root .
  python -B -m scripts.validate_distribution --root .
  git diff --check
  ```

- [ ] **Step 5: Commit the output change if implementation commit authority has been granted.** Use `feat(git-activity-report): save requested Markdown reports` for the scoped files.
