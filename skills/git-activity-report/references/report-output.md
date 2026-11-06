# Git Activity Report Output

## Select the destination

- **Conversation:** A request for report content alone, or an explicit request for chat-only output. Return the report in chat. Create nothing.
- **Default file:** The user explicitly asks for a local file without selecting a path. Use the repository context's selected worktree root, including for linked worktrees. A bare repository or an unverified worktree root cannot supply this destination.
- **Explicit file:** Use the exact user-selected Markdown path. Resolve a relative path from the selected worktree root. Honor a permitted absolute path. The parent must exist. Pass the exact resolved path and any applicable replacement authorization to the report writer, which owns this write and matching readback. If the explicit path is ambiguous, unusable or denied, ask for clarification or report the failure. Never switch it to the default path.

If the user asks to save and also show the report, use the requested file route and include the report inline. Clarify contradictory instructions about whether to save. Do not write while a format, scope or destination decision is outstanding. A blocked history query supplies no report to save. A complete zero-match result or a report with disclosed limited coverage can be saved. Compose the report in memory before any write; only the explicit-file route gives the writer file authority.

## Derive the default path

Use the literal direct child `activities-report` of the selected worktree root. Use `activity-report-YYYY-MM-DD.md` for one local date or `activity-report-YYYY-MM-DD-to-YYYY-MM-DD.md` for multiple local dates. Use the resolved first and last local dates, including for instant ranges. Keep these path components language-independent. Never derive them from a commit message, branch name or generated prose.

Inspect the worktree anchor and both output components without following indirection. Create only the single report directory when absent, after validating the draft and the available safe write/readback capability. If directory creation races with an existing entry, inspect the winner under the same rules before using it. Reject symlinks, junctions, other reparse points and wrong entry types. A pre-existing target also needs explicit permission to replace that exact report or a new user-selected path. Ask before writing and keep the inspected file identity as part of the pending decision. A differently named file, a numbered suffix or an implicit replacement is outside the request.

## Save and verify the default file

Use a host capability that anchors the operation to the verified worktree and directory and keeps them stable through writing and readback. Use literal path components and an exclusive new-file creation primitive. A separate existence check followed by a general overwrite command does not protect against collisions.

Prefer a scoped filesystem operation that supports no-follow entry checks, exclusive creation, stable opened handles and readback. On descriptor-based hosts, use operations relative to verified directory handles with no-follow and exclusive-create flags only when the host also enforces that the destination directory stays at its verified path through the operation. A directory descriptor alone can follow the opened directory after it moves outside the worktree. A path recheck after writing cannot supply missing protection. Block if the host cannot prevent relocation before each possible write.

On Windows with path-based native operations, pin every renamable directory component from a trusted filesystem root through the worktree and report folder. Open existing components from top to bottom with `OPEN_EXISTING`, access `FILE_LIST_DIRECTORY | FILE_READ_ATTRIBUTES`, read/write sharing without `FILE_SHARE_DELETE`, and flags `FILE_FLAG_BACKUP_SEMANTICS | FILE_FLAG_OPEN_REPARSE_POINT`. Verify type, path and lack of reparse points before advancing. A metadata-only handle does not enforce the required sharing restriction. Keep all handles open through writing and readback. Pin a newly created report directory before opening the file. Holding only the worktree and report-directory handles does not protect against ancestor relocation. Use `CREATE_NEW` with no-follow semantics for a new target. Validate handle types and confinement. If the host cannot establish these guarantees or report the effects, report the tool limitation rather than weakening the checks.

On authorized replacement, open the existing file without following links or truncating it first. Confirm the handle still names the inspected regular file and has no other hard links. Require a fresh decision if its identity or inspected contents have changed. Write through the verified handle only when replacement and the host's concurrency guarantees cover that file. For new files, a concurrent collision preserves the other file. If the directory or target is substituted or becomes unsafe, stop.

Flush the write, read back the same file and compare with the intended Markdown. Verify that the exact reported path still resolves to the read-back file under the pinned directory before returning a verified receipt. Preserve actual effects on failure, including a newly created directory or a file whose write or readback failed. Do not delete or retry automatically. Create no other directories, temporary or companion files, and perform no Git writes or external posting.

## Return the result

Track history status independently from output status: `not_requested`, `pending_decision`, `verified` or `failed`. A verified save returns the exact path and status in the user's report language, with any material coverage caveat. Include the full report inline only if requested. A denied write, failed comparison or uncertain readback is never a verified save.
