# Preview.6 release preparation — 2026-10-25

## Scope and review

PR #8 contains scoped synchronization/publication and this release preparation. The [approving re-review](https://github.com/omarfrancodev/devcraft-toolkit/pull/8#issuecomment-6405709082), ID CR-e769b6b8f291454dbe94, evaluated 36a224dbb05d35810e5e94fb4be4adbddb46508e..984b1de3b32ecff9a0c1aa221a9af896a727a6bb, resolved F002 and found no actionable defects. Its environment/fixture failures and successful repeats remain in the discussion; they are not broader compatibility evidence.

Release preparation changes documentation and retained verification only. Skills, catalog, manifests, scripts and existing tests/resources retain their reviewed blobs; both manifests already select 0.1.0-preview.6. The versioned changelog, release page and consumer sources are prepared before merge. ZIP/checksum assets and tag must use that exact merge commit, with no later source-preparation commit.

## Publication boundary

Verify a candidate archive from the prepared head, then merge with the expected head. Require identical prepared/merge trees. Build the final ZIP with command-local LF settings, compare every file with its Git blob, run extracted-package checks and verify draft uploaded/downloaded digests before publication. Previously published preview.1–5 release/tag metadata were captured for preservation checks. Fourteen skills are available and three remain planned. This record precedes merge; GitHub release metadata records the eventual publication result.

## Fresh pre-merge verification

- Full unittest discovery: 140 tests, 139 passed, one existing Windows symlink privilege skip; exit 0 in 232.601 seconds. See [premerge-tests.log](premerge-tests.log).
- Repository/distribution validators passed; native loading is not established.
- Complete-base whitespace against 36a224dbb05d35810e5e94fb4be4adbddb46508e passed.
- Whole-PR changed-document check resolved 189 local targets with zero missing before this log link was added.
- All 256 original reviewed resource/test/manifest/historical release files in the protected blob inventory remain unchanged. Preparation modifies only current documentation and adds this release's records.
- The publishing CLI is authenticated as omarfrancodev; repository-local commit identity remains omarfrancodev <fofe2803@gmail.com>.

The candidate archive is checked after the prepared commit, without another source edit; the later GitHub release records exact-merge package/asset verification. Historical 135/138/140 implementation runs retain their original scope. No hosted CI or native activation result is inferred.

 See [compatibility limits](../../../../../docs/compatibility.md) and [release details](../../../../../docs/releases/v0.1.0-preview.6.md).
