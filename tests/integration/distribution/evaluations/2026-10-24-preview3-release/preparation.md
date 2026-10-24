# Preview.3 release preparation

Date: 2026-10-24. Repository: `omarfrancodev/devcraft-toolkit`. Pull request: #5.
This record describes pre-merge release preparation, not an already published artifact.

## Scope

The approved implementation review covered `b0a36a75da2ea563b1ce0c89ad80ff5704a1dfb7` through `ba2f792b741bd2d2f4baa494a378275246bdbc2a`. Its [public review](https://github.com/omarfrancodev/devcraft-toolkit/pull/5#issuecomment-6389206402) reported no confirmed defects; its initial missing-PyYAML failures were resolved by the recorded reruns.

Subsequent release preparation changes the dated changelog, current consumer/source-version documentation and release procedure. Both manifests already contain `0.1.0-preview.3`; runtime skill contracts remain unchanged. The release must be a prerelease at PR #5's exact merge commit, with ZIP and SHA256SUMS assets. Publication does not require a later source commit on main.

## Observed checks

- Python 3.14.3 and declared PyYAML 6.0.3 were available.
- `python -B -m unittest discover -s tests -p "test_*.py" -v`: 89 discovered, 88 passed, one existing Windows symlink privilege skip, exit 0. See [premerge-tests.log](premerge-tests.log).
- Repository and distribution validators passed; native activation is not verified.
- Changed-document local link targets: 127 verified; new version-pinned-source anchors exist.
- The complete branch whitespace check passed.
- There were no GitHub workflow runs or status records on the reviewed implementation head; this is not a CI pass.
- Historical preview.2 release notes were unchanged. Prior ZIP digest: `4121745501508010908123cceb284f7f73b3597763f7b61a6b96ef735af163b2`; prior checksum-file digest: `af254e952131873f29adc8c7175248c5dd40b2d74353e474ed85ad8007ffae30`. Both assets and the prior tag are to remain unchanged.

## Publication verification

After merge, build the archive from the returned merge SHA, compare archive entries/content with that Git tree, run package repository/distribution checks and syntax-compile Python sources without writing caches. Publish a draft prerelease with its assets, verify its target and checksums, then publish without marking it as a stable latest release. The GitHub release metadata records the actual publication; do not append a post-merge preparation commit merely to change this pre-merge record.

Native client invocation and the unexercised promisor/symlink environments remain the documented limits.

## Pre-merge archive probe

The candidate at `5e79cbe5aaa0ebf90561a0540311940161f520cc` initially failed byte equality: archive output honored global core.autocrlf=true. For the first checked JSON file, the archive contained 390 bytes with 20 CRLF sequences versus the 370-byte LF Git blob; CRLF normalization was the only difference. No changed-byte package was published.

Regenerating with command-local `-c core.autocrlf=false -c core.eol=lf` preserved exact blob bytes. The candidate then verified all 156 tracked files, nine skills and nineteen skill resources; 23 Python sources compiled without caches. Both repository/distribution validators passed from a verified extraction in an owned temporary directory. These are packaging checks, not native client activation. Repeat the same exact-byte verification for the final merge archive before publication.
