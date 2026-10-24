# Preview.4 release preparation — 2026-10-24

## Scope and review

PR #6 contains the staging/commit construction increment and its release preparation. The [approving review](https://github.com/omarfrancodev/devcraft-toolkit/pull/6#issuecomment-6390925352) evaluated `c6a27b128d6fdec640c02f41984d487287086fbd..38d376648fdbb067721f12eea5ced1eb835825d2` with no actionable findings. Subsequent preparation changes documentation and retained verification only; skill resources, scripts, tests, catalog and manifests retain their reviewed behavior. Both manifests already select `0.1.0-preview.4`.

The versioned changelog, release page, installation source pointers and roadmap are prepared before merging. The release tag and ZIP/checksum assets must target PR #6's exact merge commit. The ZIP is checked file-for-file against that Git tree with command-local LF settings; package validators must pass before publication. These post-merge artifact checks do not require a later source commit.

## Fresh pre-merge verification

- `python -B -m unittest discover -s tests -p "test_*.py" -v`: 100 discovered, 99 passed, one existing Windows symlink privilege skip; exit 0. See [premerge-tests.log](premerge-tests.log).
- `python -B scripts/validate_repository.py --root .`: exit 0, repository catalog valid.
- `python -B -m scripts.validate_distribution --root .`: exit 0, distribution contract valid; native loading is not verified.
- Complete-base whitespace check against `c6a27b128d6fdec640c02f41984d487287086fbd`: exit 0.
- Local links in the changed documentation resolve, including the release page and this evidence.
- The earlier release pages and historical installation probes remain byte-identical to the reviewed head. Preview.3 tag and published assets were inspected unchanged before preparation.
- Remote status/workflow queries returned empty lists at the reviewed head; this is local verification, not a claim of passing hosted CI.

## Limits and publication boundary

This is an experimental eleven-skill prerelease with six planned capabilities. Native authenticated invocation and lifecycle gates remain open. Supplied-fact evaluations and owned disposable Git executions do not prove universal model adherence or client activation. See [implementation verification](../../../evaluations/2026-10-24-git-staging-commits/final.md) and [compatibility](../../../../../docs/compatibility.md).

This record is retained before the merge. The GitHub release and its assets provide the subsequent publication result; no future result is asserted here. Previous release tags and assets must remain unchanged.
