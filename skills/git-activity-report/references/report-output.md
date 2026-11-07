# Git Activity Report Output

## Select the destination

- **Conversation:** A request for report content alone, or an explicit request for chat-only output. Return the report in chat. Create nothing.
- **Default file:** The user explicitly asks for a local file without selecting a path. Use the repository context's selected worktree root, including for linked worktrees. A bare repository or an unverified worktree root cannot supply this destination.
- **Explicit file:** Use the exact user-selected Markdown path. Resolve a relative path from the selected worktree root. Honor a permitted absolute path. The parent must exist. Pass the exact resolved path and any applicable replacement authorization to the report writer, which owns this write and matching readback. If the explicit path is ambiguous, unusable or denied, ask for clarification or report the failure. Never switch it to the default path.

If the user asks to save and also show the report, use the requested file route and include the report inline. Clarify contradictory instructions about whether to save. Do not write while a format, scope or destination decision is outstanding. A blocked history query supplies no report to save. A complete zero-match result or a report with disclosed limited coverage can be saved. Compose the report in memory before any write; only the explicit-file route gives the writer file authority.

## Derive the default path

Use the literal direct child `activities-report` of the selected worktree root. Use `activity-report-YYYY-MM-DD.md` for one local date or `activity-report-YYYY-MM-DD-to-YYYY-MM-DD.md` for multiple local dates. Use the resolved first and last local dates, including for instant ranges. Keep these path components language-independent. Never derive them from a commit message, branch name or generated prose.

Inspect the worktree anchor and both output components without following indirection. Reject symlinks, junctions, other reparse points and wrong entry types. Open an existing report directory under the worktree guard and keep its verified handle. Treat only a definite missing-name result as absence. After validating the draft and all save prerequisites, including the hard-link guard below, create the one missing directory only through an operation that binds its identity to a protected handle from creation, or an equivalent guarantee covering the entire creation-to-first-open interval. A separate mkdir followed by opening the pathname cannot establish that identity. If creation collides with a competing entry, stop the save without adopting the competing directory. A pre-existing target also needs explicit permission to replace that exact report or a new user-selected path. Ask before writing and keep the inspected file identity as part of the pending decision. A differently named file, a numbered suffix or an implicit replacement is outside the request.

## Save and verify the default file

Use a host capability that anchors the operation to the verified worktree and directory and keeps them stable through writing and readback. Use literal path components and an exclusive new-file creation primitive. A separate existence check followed by a general overwrite command does not protect against collisions.

Prefer a scoped filesystem operation that supports no-follow entry checks, exclusive creation, stable opened handles and readback. On descriptor-based hosts, use operations relative to verified directory handles with no-follow and exclusive-create flags only when the host also enforces that the destination directory stays at its verified path through the operation. A directory descriptor alone can follow the opened directory after it moves outside the worktree. A path recheck after writing cannot supply missing protection. Block if the host cannot prevent relocation before each possible write.

### Windows native operations

Use [NtCreateFile](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntcreatefile) for guarded operations relative to a directory handle. Start with a verified native handle to the trusted filesystem root. Open each existing component through the worktree and report directory one at a time, relative to the previous verified handle. Set `RootDirectory` to that handle, `ObjectName` to one literal component, and the attribute flags to `OBJ_DONT_REPARSE`. See the [OBJECT_ATTRIBUTES reference](https://learn.microsoft.com/en-us/windows/win32/api/ntdef/ns-ntdef-_object_attributes).

- Use `FILE_OPEN` for existing directories, directory options `FILE_DIRECTORY_FILE | FILE_SYNCHRONOUS_IO_NONALERT`, and access `FILE_LIST_DIRECTORY | FILE_READ_ATTRIBUTES | SYNCHRONIZE` with `FILE_SHARE_READ` only. Verify type, path and lack of reparse points before advancing. Keep every verified handle through writing and readback. Metadata-only access does not provide the required sharing guard, and a sharing guard alone does not prevent all changes to reparse metadata.
- For a missing report directory, use the same relative directory settings with exclusive `FILE_CREATE` under the pinned worktree handle. Require a successful result, `IO_STATUS_BLOCK.Information == FILE_CREATED` and a valid returned directory handle. Verify it and use it as the guard from creation, without closing it and reopening by path. A collision or ambiguous result stops the save. Never use `CreateDirectoryW` followed by a separate open.
- For the Markdown, use the same single-component, no-reparse binding relative to the verified report-directory handle. Use `FILE_CREATE` for a new file, or `FILE_OPEN` without truncation for a replacement whose exact identity and contents have been authorized. Apply the hard-link guard below before any file creation or write. Use `FILE_NON_DIRECTORY_FILE | FILE_SYNCHRONOUS_IO_NONALERT` and access `FILE_READ_DATA | FILE_WRITE_DATA | FILE_READ_ATTRIBUTES | SYNCHRONIZE`, without write or delete sharing. Validate the returned file handle before writing. An absolute pathname reopened for writing could follow a reparse point set after directory validation.
- Check directory attributes and identities before the file operation and verify the original path and read-back file again through the trusted, no-reparse chain before reporting success. If a component changed, a safe operation is unavailable, or the creation identity cannot be established, stop and disclose actual effects. Do not redirect a write or certify a path based only on matching read-back bytes.


### Hard-link guard for default saves

Before any default-save mutation, require evidence that the host can keep report bytes confined to the selected file. The guard must prevent additional hard links from the verified single-link state through the last content write, including any truncation or buffered write that has yet to complete. Apply this to new files as well as authorized replacements. Suitable evidence is an enforced host operation with that guarantee, or a verified volume that does not support hard links. A single link-count check, exclusive creation, a handle denying write/delete sharing, or a post-write recheck cannot provide this guarantee on a hard-link-capable volume.

On Windows, query capabilities from the pinned handle on a trusted local destination volume. A successful capability query that establishes the absence of `FILE_SUPPORTS_HARD_LINKS` can satisfy the hard-link requirement on that volume. If the volume supports hard links or the query is inconclusive, require a separately demonstrated guard. The native handle recipe above establishes path confinement but does not itself supply that guard. See [GetVolumeInformationByHandleW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getvolumeinformationbyhandlew).

If the host cannot establish the guard, return output `failed` without creating the directory or file, truncating or modifying an existing report, or choosing another destination. If a proven guard later fails, stop before any further writes and report actual effects.

### File write and verification

On authorized replacement, open the existing file without following links or truncating it first. Confirm the handle still names the inspected regular file and has no other hard links. Require a fresh decision if its identity or inspected contents have changed. Write through the verified handle only while the hard-link and path guards hold. For new files, a concurrent collision preserves the other file. If the directory or target is substituted or becomes unsafe, stop.

Flush the write, read back the same file and compare with the intended Markdown. Verify that the exact reported path still resolves to the read-back file under the pinned directory before returning a verified receipt. Preserve actual effects on failure, including a newly created directory or a file whose write or readback failed. Do not delete or retry automatically. Create no other directories, temporary or companion files, and perform no Git writes or external posting.

## Return the result

Track history status independently from output status: `not_requested`, `pending_decision`, `verified` or `failed`. A verified save returns the exact path and status in the user's report language, with any material coverage caveat. Include the full report inline only if requested. A denied write, failed comparison or uncertain readback is never a verified save.
