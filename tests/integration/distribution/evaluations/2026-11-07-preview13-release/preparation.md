# Preview.13 release preparation

Date: 2026-11-07. Reviewed implementation is integrated in main at
`1410bbc3d1cc6ff634a654e7367839e21bbf640b` through PR #16.
Both manifests select `0.1.0-preview.13`; the inventory remains twenty skills.

This release includes commit grouping by evidenced intent, a rationale for each
complete single-group plan, preservation of the partition through construction
and publication, PW-06, and portable Windows exclusive-create refusal checks.
Native activation and activity-report hard-link isolation retain their existing
limitations. The baseline also split the PW-06 patch, as recorded by its
evaluation.

The intended publication date is 2026-11-07 in America/Mexico_City and must match
the actual GitHub publication timestamp before completion. Source preparation
belongs to a release PR before its ordinary merge. The tag and archive use
that exact merge, with candidate/merge tree equality verified independently.

## Verification

Run the full suite and repository/distribution validators on the prepared
source. Preserve sanitized full-suite output. Check current local Markdown
targets, synchronized manifest versions, unchanged historical changelog and
release pages, and the complete skill inventory.

Generate the ZIP from the merge and compare all files to their Git blobs.
Run extracted validators and compile packaged Python sources without execution.
Use a draft prerelease, download both uploaded assets independently and compare
their hashes, then publish and verify the public tag, assets and date.

## Observed source checks

- Both manifest versions are `0.1.0-preview.13`.
- Repository and distribution validators passed. Twenty skills and twenty presentation sidecars are present.
- All 392 local Markdown targets checked in README, changelog and docs exist. Historical release pages and the preview.12-and-older changelog content are unchanged.
- Runtime skill contents match main `1410bbc`; this branch changes release metadata and documentation.
- Claude strict plugin and marketplace parsing returned success with no manifest errors. Its optional directory audit retains the missing-license finding and could not inspect the protected `.agents` directory in this environment. Native directory acceptance is outside this check.

- Independent release-source review found no actionable issues. It confirmed version agreement, twenty-skill inventory, historical preservation, accurate PW-06 coverage, retained save/native-activation limits and the package verification procedure. Runtime validation and publication remained pending at review time.

## Fresh full-suite result

The release-prepared source passed the complete suite: 236 tests discovered,
234 passed and two Windows symlink-privilege controls skipped, exit zero.
The run took 394.002 seconds. [Full sanitized output](premerge-tests.log)
retains the observed results. All seven native activity-report controls passed,
including both junction refusal cases and both hard-link controls.

Both local validators and the strict manifest parsers passed. The candidate
still requires exact merge-tree, archive, extracted-package and public asset
verification. The skipped controls retain their own outcome.
