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

## Directory creation identity

A Windows fixture reproduced the remaining creation-to-open gap. After a separate directory create, an ordinary directory replaced it at the same pathname. Exclusive Markdown creation and matching readback succeeded in the replacement while the original directory remained empty.

The corrected recipe uses exclusive directory creation relative to a pinned worktree handle and keeps the returned handle without reopening the pathname. The native probe observed `FILE_CREATED`, denied an immediate rename with Windows sharing violation 32, and successfully created and read back the report. With read-only sharing held on the entire ancestor chain, a competing write-access open of the report directory also failed with sharing violation 32 while normal Markdown creation and readback still worked. When a competing ordinary directory already existed, it received `STATUS_OBJECT_NAME_COLLISION` and wrote no Markdown. A separate dangling-junction probe demonstrated that exclusive creation alone can follow the junction. With `OBJ_DONT_REPARSE`, the native call failed without a handle or a new junction target. A metadata-only write-attributes handle could still set a junction on the pinned directory. An absolute child write then reached its sibling target. The corrected no-reparse child create, relative to the pinned directory handle, refused the operation and created no file at the relative target or in the sibling. These probes check the filesystem operation in owned fixtures. They do not exercise native skill activation.

## Concurrent hard links and junction capability

A Windows NTFS control used a metadata-only handle to attach a hard link after the single-link check. It succeeded for an existing report and for a new, still-open report before its first write. Both read sharing and zero sharing allowed the alias. Subsequent writes were visible through the additional name. Exclusive creation and successful readback therefore do not establish confinement of the bytes.

The default-save recipe now requires a demonstrated hard-link guard before any filesystem mutation. The previous successful creation and replacement probes establish path and readback behavior in their fixtures. They do not establish this additional guarantee. The native Windows path recipe alone cannot authorize a default save on NTFS. A trusted destination volume without hard-link support or a host operation that enforces isolation can satisfy the new guard.

In a supplied-facts behavior check, the default route declined both an NTFS first save with no report directory and an authorized replacement when only native path guards were available. History status remained independent. A trusted local volume without hard-link support passed the gate when all other write requirements were supplied. This behavior check did not perform a filesystem write.

A handle-based volume query identified NTFS and reported hard-link support in the local fixture. All 23 coordinator integration tests passed, and both repository and distribution validation passed. All six native Windows tests passed on the local volume when the required fixture operations were permitted. In the restricted Windows environment, the three ordinary controls passed. The two junction cases skipped during setup with WinError 5, and the hard-link probe skipped when the capability check returned access denied. Injected setup controls verified that an unexpected WinError 2 and an assertion failure still propagated.

## Execution

The full repository run completed with 227 tests, 225 passed and two Windows symlink controls skipped because the host did not grant the required privilege. That run started before the independent review added the repeated-midnight fixture. The final focused run covered the revised sources and all 17 coordinator integration tests, including that fixture. Repository and distribution validation passed on the revised sources. The implementation steps left changes in the selected worktree without a commit.

## Independent hard-link outcomes

The existing-report and new-report hard-link controls now use separate unittest methods. All seven native Windows tests passed on the local volume. Two additional runs injected SkipTest into only one hard-link setup at a time. Both methods were attempted in each run, exactly the selected method was skipped, and the other method completed its real filesystem assertions. These injections establish independent results under partial capability without claiming a new restricted-host run.

The revised coordinator suite passed all 24 tests. Repository and distribution validation and the whitespace check also passed.

## 2026-11-07 exclusive-create refusal statuses

The complete publication check reproduced two failures with the unchanged sources from published main `a2937e2`. Both guarded `NtCreateFile` calls returned `STATUS_OBJECT_NAME_COLLISION` (`0xC0000035`) on this Windows host. The existing assertions accepted only reparse-specific failure codes.

The junction probes now also accept the observed collision refusal from exclusive creation. Both still require a null returned handle. The dangling-junction case checks that its target remains absent and the junction remains present. The relative child case checks that no report appears through the junction, removes only the fixture's reparse metadata, and verifies the original directory is empty. The absolute-path control still reaches the sibling target.

All seven native Windows probes passed after the assertion correction, including both hard-link controls. The general exclusive-create and no-reparse semantics are documented in [NtCreateFile](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntcreatefile) and [OBJECT_ATTRIBUTES](https://learn.microsoft.com/en-us/windows/win32/api/ntdef/ns-ntdef-_object_attributes). The collision status is an observation from this host, with filesystem postconditions checked independently.
