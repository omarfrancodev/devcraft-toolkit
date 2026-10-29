# Preview.8 release preparation — 2026-10-29

PR #10 contains both work-branch creation and publication coordination plus all release source preparation. The approving [review](https://github.com/omarfrancodev/devcraft-toolkit/pull/10#issuecomment-6502947191), CR-70bbb3843885427ebcc2, covered 319ff5f5624069bfeaf8a0cb14a1f445f82f7436..dc790643d85f72bf7d013eed0a084081b59dd608 with zero confirmed findings. Its dependency/path-length/diagnostic-fixture failures and targeted reruns consolidate to 187 distinct passes and one Windows symlink skip; they are not a claim that the first review run passed.

Preparation changes current documentation only, adds notes and fresh release evidence, and preserves reviewed skills/catalog/manifests/scripts/tests and older release pages. Both existing manifests already select preview.8. Final inventory is eighteen available/zero planned. Current ruleset permits ordinary merge commits with zero formal approvals and no required check rule; no automatic source deletion. Revalidate current policy/source before the guarded merge.

The date 2026-10-29 is the intended publication day in America/Mexico_City and must be confirmed from actual GitHub published_at before completion. A tag/assets release must point to this PR's exact merge. Candidate and merge trees must match. Compare every archived file with Git blobs, validate extraction, upload a draft and independently download/digest both assets before publication. Preserve existing release/tag metadata. Publication receipts are release metadata/local artifacts, with no later preparation commit on main. Native/authenticated capability validation remains separate.

## Fresh prepared-source verification

- Full unittest discovery: 188 discovered, 187 passed and one existing WinError 1314 symlink privilege skip; exit 0 in 263.143 seconds. See [complete output](premerge-tests.log).
- Repository/distribution validators and both new-skill quick validations passed; complete PR whitespace check passed.
- Preparation changes fifteen current documentation files and adds release notes/evidence. All reviewed implementation, manifests, catalog, scripts, tests and older release pages are preserved; the published changelog suffix is unchanged.
- The preparation link pass resolved 185 local targets in seventeen new/changed Markdown documents with no missing files. A whole-PR link pass runs before committing the prepared source; fragments and external pages are not filesystem checks.
- Publishing identity: omarfrancodev; repository-local commit identity: omarfrancodev <fofe2803@gmail.com>. No global identity/configuration change.

Archive candidate/exact-merge equality, Git-blob byte checks, extracted-package validation and uploaded/downloaded asset digests are checked after this source/evidence commit and before publication. Their eventual SHA/digest receipts are recorded in release metadata/local artifacts without a follow-up preparation commit.

Whole-PR final local-target pass: 59 Markdown documents, 199 local targets, zero missing.
