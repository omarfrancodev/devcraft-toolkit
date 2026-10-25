# Preview.5 release preparation — 2026-10-25

## Scope and review

PR #7 includes the history-report coordinator and its release preparation. The [approving review](https://github.com/omarfrancodev/devcraft-toolkit/pull/7#issuecomment-6395249264), ID `CR-d9d12f66e50545dc8d01`, evaluated `613ffebe3f15a7d0e42e55330d5742ad8f96bb4d..6e3706272cccfa704c59382343c7c4363dff7968` with no actionable findings. Its PyYAML/MSYS environment failures and successful repeats remain in the discussion; they are not product defects or broader compatibility evidence.

Subsequent release preparation changes documentation and retained verification only. Runtime resources, scripts, tests, catalog and existing manifest values remain as reviewed; both manifests already select `0.1.0-preview.5`. The versioned changelog, release page, source pointers and roadmap are prepared before merging. The ZIP/checksum assets and tag must use the exact merge commit; no later source-preparation commit is required.

## Fresh pre-merge verification

- `python -B -m unittest discover -s tests -p "test_*.py" -v`: 114 discovered, 113 passed, one existing Windows symlink privilege skip; exit 0. See [premerge-tests.log](premerge-tests.log).
- Repository and distribution validators: exit 0; native loading is not verified.
- Complete-base whitespace check against `613ffebe3f15a7d0e42e55330d5742ad8f96bb4d`: exit 0.
- All changed-document local targets resolve, including this record and the release page.
- Historical release pages and installation probes remain unchanged. Published preview.1–4 tags, asset identities/digests and publication metadata were captured before preparation for comparison after publication.
- Hosted status/check-run queries at the reviewed head returned zero records. This is local verification, not a claim of passing hosted CI.

## Publication boundary

Build a candidate archive from the prepared head, then require the expected head when merging. Verify that the merge tree equals the prepared tree. Build the final ZIP with command-local LF settings, compare every file with Git blobs, run extracted-package checks and verify uploaded/downloaded asset hashes. Publish as a prerelease at the exact merge revision and preserve older releases.

This record precedes the merge; the GitHub release records the later publication result. See [implementation verification](../../../evaluations/2026-10-24-git-activity-report/final.md) and [compatibility limits](../../../../../docs/compatibility.md). Twelve skills are available and five remain planned; authenticated native activation/lifecycle and universal model adherence remain unverified.
