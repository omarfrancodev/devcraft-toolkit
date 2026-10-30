# Preview.9 release preparation — 2026-10-30

PR #11 includes presentation metadata, regression tests and all release source
preparation. The implementation reviewed for this release is
`f365456c8cdf2e760a416cc058d3e0e4697e6e79..2fe07d75296539e857be2d551d4cc43b886816e2`.
Release preparation changes the two manifest versions and current documentation,
and adds these release records. Skill instructions/resources, catalog, validator
code, existing tests and older release pages remain unchanged from that head.

Both manifests select `0.1.0-preview.9`; inventory remains eighteen available
skills, each with presentation-only `agents/openai.yaml`. The intended publication
date is 2026-10-30 in America/Mexico_City and must be confirmed from GitHub's actual
`published_at` before completion. Source preparation must not follow the merge.

## Release gates

- Fresh full suite, repository/distribution validators and whitespace checks.
- Independent read-only pre-merge review; resolve material findings before merge.
- Current policy, review/check coverage, exact source and ordinary merge method.
- Candidate and exact-merge archive validation with every member equal to its
  Git blob, both extracted-package validators and all eighteen metadata files.
- Draft upload/download digest equality for ZIP and checksum assets.
- Published prerelease, tag/merge equality, local publication-date agreement and
  unchanged older release/tag metadata.

Native UI rendering, authenticated invocation and cross-client scope/lifecycle
remain separately unverified. Structural validation does not close those gates.

## Fresh prepared-source verification

- Full unittest discovery: **209 discovered, 207 passed, two Windows symlink
  privilege skips**, exit 0 in **257.460 seconds**. The [complete log](premerge-tests.log)
  replaces machine-specific paths with stable placeholders.
- Repository and distribution validators passed, as did the whitespace check.
- Claude Code 2.1.300 accepted the prepared manifest and marketplace with
  `--json --strict`, with no errors or schema warnings.
- The [independent source review](review.md) found no confirmed critical,
  important or minor findings. Its scope and excluded native-rendering behaviors
  are retained explicitly; release-only preparation was outside its frozen range.
- All **419 protected existing source/resource/test and historical-release files**
  remain byte-equivalent to their Git blobs after normal Git attribute handling.
  The two existing manifests differ only in version. Published changelog entries
  are preserved. Current documentation pointers select preview.9.
- The preparation link pass resolved **195 local Markdown targets** with zero
  missing files. Generated archive/download checks happen after this source
  record and are retained as release metadata/local artifacts, without a later
  preparation commit on main.

The current main ruleset allows ordinary merge commits, requires no formal
approvals or status checks, and has no bypass actor. GitHub repository settings
preserve the source branch. These gates are refreshed at the actual prepared
source revision before the conditional merge; empty check lists are not claimed
as passing checks.
