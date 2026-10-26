# Missing merge provenance follow-up

## Defect and reproduced failures

The original independent review identified a Minor development-fixture defect: raw_request fabricated a hypothetical merge SHA for a merged record whose actual result was null or absent. The explicitly requested follow-up adds test_merged_request_without_result_preserves_unknown_provenance; all four GitHub/GitLab null/absent subcases failed before correction, observing cccc... as actual merge provenance.

A related observation-path regression, test_unknown_merge_result_does_not_borrow_prepared_graph_evidence, then used an owned real Git graph. With a null result, read incorrectly returned prepared parents and containment; with an absent key, it raised KeyError. These were observed RED before the observation guard changed.

## Correction and scope

raw_request keeps missing actual merge results unknown and supplies the hypothetical fallback only for explicitly unmerged open/closed records. read emits prepared commit evidence only when the selected merged result equals the graph's actual merge OID. It does not borrow prepared parents/containment for an unknown result. Both regressions passed after these changes; existing real-result and hypothetical-state controls remain applicable.

The installed instruction resources are unchanged. The earlier successful copied-resource applications used known real merge results, so their evidence remains scoped to those operations; they were not repeated for this fixture correction. No authenticated provider or native activation claim is added.

## Verification

Final full-suite results are recorded in verification.md and review-follow-up-suite.log after the complete correction. An intermediate run started before the related observation-path regression was added; its separate log does not establish coverage of the final source. Repository/distribution validation and complete-base whitespace are checked before publication.

Final follow-up verification: 162 tests discovered, 161 passed and one existing Windows symlink privilege skip, 452.625 seconds; see review-follow-up-suite.log. Both repository/distribution validators and complete-base whitespace pass.

The intermediate 161-test run passed in 344.779 seconds and is retained separately; it predates the second regression and observation guard. The final 162-test gate supersedes it for current-source verification.
