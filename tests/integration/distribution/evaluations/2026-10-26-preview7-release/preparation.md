# Preview.7 release preparation — 2026-10-26

PR #9 includes hosted PR/MR management/promotion and all source release preparation. The approving [review](https://github.com/omarfrancodev/devcraft-toolkit/pull/9#issuecomment-6409747976), CR-ef5304ed4e3b4cd79227, assessed c6871ca4e078b7fae33c2506d72906420a616245..8913ed42fdf91efe4cc2b7575679fd270ce26153 with zero confirmed findings. Its C012 gate passed 162 tests (161 passed, one Windows symlink skip), following documented environment failures and corrections; those remain review evidence, not product defects or broader compatibility claims.

Preparation changes current documentation and adds release verification only; original skills/catalog/manifests/scripts/tests/historical releases retain their reviewed blobs. Existing manifests already select 0.1.0-preview.7. Versioned changelog, notes and consumer source pointers are prepared before merge. Sixteen skills are available and git-publish-work alone remains planned.

The selected ruleset permits ordinary merge commits and requires zero formal approvals; no required status-check rule is active. Legacy branch protection returns 404 because rulesets supply the restrictions. Source cleanup is disabled. Revalidate before the expected-head merge; do not bypass policy. Capture prior release/tag metadata for preservation.

Verify a candidate archive from the prepared head, merge with its expected source SHA, require prepared/merge tree equality, and build final ZIP/checksums from that exact merge. Verify every archive entry against Git blobs, extracted-package validation, draft uploaded/downloaded digests and the published tag target. No follow-up preparation commit on main or release automation is introduced. This record precedes merge; publication metadata records the eventual result.

## Fresh pre-merge verification

- Full unittest discovery: 162 tests, 161 passed and one existing Windows symlink privilege skip; exit 0 in 376.245 seconds. See [premerge-tests.log](premerge-tests.log).
- Repository/distribution validators and both new-skill structural checks pass; full-range whitespace is clean.
- The protected inventory confirms all 362 original files outside the explicitly modified current documentation preserve their reviewed blobs, including skills/catalog/manifests/scripts/tests/historical release pages. Existing manifest versions remain preview.7.
- Whole-PR changed-document local targets resolve without missing files; the exact final count is reported by the preparation gate.
- Publishing identity is omarfrancodev; repository-local commit identity is omarfrancodev <fofe2803@gmail.com>. No global identity change.

The prepared-head archive and exact-merge archive are checked after this source/evidence commit, without a later preparation commit. Final release metadata records the merge SHA, ZIP digest and uploaded/downloaded asset checks. Native/authenticated provider execution remains unverified; implementation publication does not close those gates.
