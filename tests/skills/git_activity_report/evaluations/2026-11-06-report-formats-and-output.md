# Git activity report formats and output evaluation

## Test layers

Package tests check that each new reference exists, is linked from the coordinator and passes repository validation. Format actor samples manually load the coordinator and writer with supplied evidence. Live output checks use manually loaded instructions, a real Git fixture and Windows filesystem operations. None of these layers exercises native plugin activation.

## Task 1: Report format

- Structural RED: `HistoryPackageTests.test_report_format_reference_is_packaged` failed because the format reference was absent. The focused integration suite then passed all 15 tests after adding the reference and coordinator changes.
- Baseline actor: a Spanish request for a daily file elicited only an exact-path question. Complete zero matches produced a factual no-activity sentence without daily rows. An English output override and the local date conversion were already respected.
- FMT-01 candidate: the first response was «¿Prefieres un informe general o uno agrupado por día, que incluya los días sin commits? Te sugiero agrupado por día, como pediste.» It did not compose or write. «Por día» resumed the same request and kept file intent. Plain chat supported the question when no structured tool was available.
- FMT-02 candidate: the daily sample retained November 2–4, including the middle empty date. Complete zero matches retained all rows and `no_op`. General reported the same period without a daily table.
- FMT-03–05 candidate: the author-date record at 05:45 UTC fell on November 2 at UTC−06:00. The ordinary midnight endpoint added no November 4 row. Limited coverage qualified the empty November 3 row. The committer-date variant excluded the record. The Spanish question and explicit English report both used the requested languages, and escaping preserved the two columns and the identifier. Conflicting offsets requested a reporting zone. Blocked history and insufficient table capacity stopped composition.
- FMT-06 review regression: the old wording would drop the endpoint date even when a prior offset segment had already intersected it. The timezone fixture reproduced the two midnights at UTC 04:00 and 05:00 on November 1. The revised rule uses the union of dates across offset segments. The fixture checks timezone facts; it does not invoke an actor or renderer.

## Task 2: Output

- Structural RED: `HistoryPackageTests.test_report_output_reference_is_packaged` failed because the output reference was absent. All four package tests passed after adding and linking the reference.
- Task 1 baseline actor: after format selection, file intent without a path asked for the exact path. A supplied existing-parent path delegated to the writer; a missing parent stopped the save and created no fallback. Content-only returned the report in chat.
- Live default save: a Spanish daily report from a real Windows linked worktree selected two matching author-date commits, rendered three dates and included the complete-empty November 3 row. The report was independently read back at `activities-report/activity-report-2026-11-02-to-2026-11-04.md` (564 UTF-8 bytes; SHA-256 `b977573891e5659c34d64bbfbb74629572354d1b70f4f6b7906ac883a8ca2ffc`). No report appeared in the primary checkout. Tracked files, both worktrees' HEADs and indices, refs and local configuration were unchanged.
- Live explicit save used an absolute path with an existing parent and verified exact content. The missing-parent attempt created neither a parent nor a fallback report.
- Live collision and junction: exclusive creation preserved a concurrently occupied target. A Windows junction at the default report directory was rejected and its destination stayed empty.
- Live replacement checked the original file identity and contents through an opened handle. A swapped file with identical bytes, an in-place content change and a target with an added hard link each preserved existing bytes and required a new decision. Authorized replacement of the inspected file passed. A readback error injected after a real write left the file in place and returned `failed` separately from history status.
- Live path-stability controls: the first probes showed that holding only the worktree and report-directory handles did not stop an ancestor rename, and metadata-only handles did not stop leaf relocation. With directory read access and delete sharing denied for every directory from the trusted volume root through the report folder, attempts to rename the ancestor, worktree and report directory all failed with Windows sharing violation 32. A separate read handle resolved to the exact requested path, the same volume/file identity and the same bytes.
- Supplied-fact simulations covered complete empty and limited daily output, blocked history, an explicit worktree-relative path, save and show together, and the single-day filename. These simulations did not execute filesystem writes. The existing standalone writer still asks for an exact path, uses an existing parent and reads the file back.
- Standalone RPT-05 ran in a separate temporary fixture with only the report writer. Content-only rendered the supplied facts without a write. A separate request wrote only the exact existing-parent report.md and matched the independent readback (310 UTF-8 bytes). Input and unrelated file hashes stayed unchanged.
- Verification scope: actual file safety probes ran on Windows using native capabilities in owned temporary fixtures. Other hosts and native activation were not exercised.

## Independent review

Review found two important edge cases: repeated midnight could suppress an intersected date, and a directory descriptor can stay valid after its path moves. The changes retain intersected dates across timezone transitions and require a stable path before writes and through readback. They also define history status by inspection/composition independently of output delivery. The repeated-midnight fixture and the Windows relocation probes above substantiate the corresponding corrections.

## Execution

The full repository run completed with 227 tests, 225 passed and two Windows symlink controls skipped because the host did not grant the required privilege. That run started before the independent review added the repeated-midnight fixture. The final focused run covered the revised sources and all 17 coordinator integration tests, including that fixture. Repository and distribution validation passed on the revised sources. The implementation steps left changes in the selected worktree without a commit.
