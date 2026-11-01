# Preview.10 release preparation — 2026-11-01

PR #12 merged as `d7c44cd22534edbfad65464eda7eae273d6f2478` with parents
`ccbd058749e7db49b303168fb13e778343ea2422` and
`871f6d1872fdf1fa40dfaa524ab920fc1c43527e`. PR #13's local integration commit
`483e32da01942098bcc74bbd7b85f6e97f62b76f` preserves that main revision and
`ccb6cfa977c55ea1fbe96636f742815d40bd3e51`, resolving both changelog/roadmap
sections without dropping either increment.

Both manifests select `0.1.0-preview.10`; catalog remains nineteen available
skills with presentation-only sidecars. Release preparation changes documentation,
the two manifest versions and this new evidence group; it does not change the
already reviewed skill/resources, validator code, existing tests, catalog or
historical release pages. Protected blob checks and published changelog-suffix
comparison verify that scope.

All preparation belongs to PR #13 before its merge. Intended publication date:
2026-11-01 in America/Mexico_City, checked against actual GitHub publication time.
The final tag/assets must use the exact merged source tree, not a later source
commit. Native/authenticated invocation remains an independent open track.

## Required release gates

- Fresh combined full suite and both local validators; inspect actual skips.
- Native Claude manifest/catalog parsing, separately from skill activation.
- Independent review of source integration and preparation.
- Fresh target policy, checks/reviews, source SHA and compatible ordinary merge.
- Candidate/merge tree equality, exact ZIP/blob equality, extracted validators
  and all nineteen presentation files.
- Draft asset upload/download digest equality; verified published prerelease,
  tag/merge equality, local publication date and preserved prior releases/tags.

Verification results are appended here only after observation. Final asset
receipts are external release metadata or temporary local artifacts, without
post-merge preparation changes to this source record.

## Fresh prepared-source results

- Full unittest discovery: **222 discovered, 220 passed, two Windows symlink
  privilege skips**, exit 0 in **538.800 seconds**. [Full output](premerge-tests.log)
  replaces workspace-specific path prefixes with `<workspace>`; outcomes and
  exception codes are preserved.
- Repository and distribution validators passed, as did `git diff --check`.
- Claude Code 2.1.300 passed strict parsing of the marketplace and the explicit
  `.claude-plugin/plugin.json` file. [Native parse receipts](claude-validation.json)
  retain their actual selected manifest types and checked-file hashes. Empty
  contents lists do not establish skill discovery or invocation.
- The [independent review](review.md) found no confirmed Critical, Important or
  Minor source issue. Its parse-scope caveat was resolved by the explicit plugin
  manifest check; post-merge and publication gates remain separate.
- All **476 protected existing files** remain unchanged from the integrated
  baseline, and the complete preview.9-and-older changelog suffix is preserved.
  Existing manifests change only their version values.
- All **213 local Markdown targets** checked in current consumer/release
  documentation exist. This is not remote URL validation.

The active main ruleset requires a PR and ordinary merge commit, with zero
required formal approvals/status checks and no bypass actor. Repository settings
preserve source branches. These observations are refreshed against the final
prepared source before merge; an empty status/check list is not called a pass.

Candidate/exact-merge ZIP, draft asset roundtrip, preserved old releases/tags and
actual publication-date checks run after the source is frozen. Their receipts do
not add a later source-preparation commit to main. Temporary local packaging
artifacts are removed after independently verified publication.
