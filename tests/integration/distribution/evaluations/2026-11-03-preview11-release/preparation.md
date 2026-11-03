# Preview.11 release preparation

Date: 2026-11-03. Source implementation: e8ef80fa12440c6c00128364f6149c4309377ba9.
PR #14 targets main at be68a988f62f5697274af3664b46f664203c3f43.
Both manifests select 0.1.0-preview.11; the inventory remains twenty available
skills, with no new runtime change in release preparation. Source skills,
validators, existing tests and historical release pages stay unchanged.

The review of the implementation found no confirmed defects. Its independent
full run reported 194 passing tests, 29 long-path fixture setup errors before
the behavior under test, and two symlink privilege omissions. That environment
reservation remains recorded; it does not override or falsify another run.
Fresh release-source checks below must be observed before merge.

All version/changelog/current-pointer/release records belong to PR #14 before
its merge. Intended publication date: 2026-11-03 in America/Mexico_City, verified
against the actual published timestamp. No later preparation commit on main.

## Gates

- Fresh full suite, both validators, whitespace and local Markdown targets.
- Claude strict plugin/marketplace parsing, distinct from activation.
- Independent review of release-only source scope and historical preservation.
- Fresh policy/check/review/source gates and ordinary source-conditional merge.
- Candidate/merge tree equality and exact archive/blob/resource validation.
- Draft asset roundtrip, public release/date/tag verification and old-state preservation.

Results are appended only after observation. Post-merge receipts remain in the
release or ignored packaging area rather than changing this preparation source.

## Fresh results

- Complete suite: **225 discovered, 223 passed, two Windows symlink privilege
  omissions**, exit zero; unittest 521.973 seconds (wrapper 523.247 seconds).
  [Actual output](premerge-tests.log) retains all outcomes with personal path
  prefixes sanitized. All 29 Git fixture cases left unvalidated by the external
  long-path run passed here. This does not turn that other run into a success.
- Repository/distribution validators and `git diff --check` passed.
- Claude Code 2.1.300 strictly parsed the explicit plugin and marketplace
  manifests: [receipts](claude-validation.json). No warnings/errors were gating;
  empty contents lists are not evidence of skill discovery or activation.
- All 535 protected baseline files outside the eleven allowed release documents
  and manifests remain unchanged after checkout EOL normalization. Both manifests
  differ only in version. Preview.10-and-older changelog content is preserved.
- The initial current-document check found 172 existing local Markdown file
  targets. This does not validate external URLs or establish native compatibility.

Policy before preparation requires a PR/ordinary merge, zero formal approvals,
no required status-check rule and no bypass actor; legacy protection is absent.
These facts and head/check/review observations are refreshed on the prepared
source immediately before merge. Empty check lists are not called passed.

Independent source review found no supported Critical, Important or Minor issue;
its actual outcomes and limits are retained in [review.md](review.md). Exact candidate
archive, final merge, assets, public timestamp and old-state preservation remain
later gates whose receipts are not added in a post-merge source-preparation commit.
