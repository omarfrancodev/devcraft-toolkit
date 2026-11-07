# Preview.12 release preparation

Date: 2026-11-07. Reviewed implementation: 395f09acbd8bcadb3874a3a988ea8c4a963d18e3.
PR #15 targets main at e1291bb135afcf8c3e599c0ae18228049cf24f99.
Both manifests select 0.1.0-preview.12 and the inventory remains twenty skills.

The latest review confirms the separate existing-report and new-report
hard-link outcomes and records no new defects. The user accepted its NTFS
reservation. Default saves remain unavailable on a hard-link-capable volume
unless the host can demonstrate additional protection. Successful isolated
writes and native plugin activation remain distinct, unverified acceptance
paths. Release preparation adds no new runtime behavior.

All changelog, version and release preparation belongs to PR #15 before its
merge. Intended publication date is 2026-11-07 in America/Mexico_City, checked
against the actual GitHub publication timestamp.

## Verification

Run the full suite and both validators on the release-prepared source. Preserve
the complete test outcomes with personal path prefixes sanitized. Verify
current document links and unchanged historical release content. Validate
the candidate/merge tree identity and exact archive contents before uploading
assets. Use a draft prerelease, independently download assets for hash checks,
then publish and verify the tag and actual publication date.

## Observed checks

- Repository and distribution validators passed.
- Claude strict plugin and marketplace parsing returned success with no manifest errors. Its optional directory audit reported a missing license. No directory acceptance or native activation is inferred.
- 166 local document targets exist. Historical preview.11-and-older changelog content is preserved.

- Independent release-source review against implementation 395f09a found no blocking issue. It checked both versions, twenty skills/sidecars, local links, historical preservation and the NTFS limitation. Full-suite and publication verification were still pending when that review completed.

## Fresh full-suite result

The release-prepared source passed the complete suite: 235 tests discovered,
233 passed and two Windows symlink-privilege controls skipped, exit zero.
The unittest run took 359.211 seconds. [Full output](premerge-tests.log)
retains actual results with personal path prefixes sanitized. All seven native
activity-report controls ran successfully in this environment. A skipped
control remains separate from a passing test.

The nine changed existing source files are limited to release documentation
and manifest versions. Runtime skills and historical release pages match the
reviewed implementation. Publication still requires fresh hosted gates,
candidate/merge tree equality, exact archive validation and asset roundtrip.
