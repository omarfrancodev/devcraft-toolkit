# Independent whole-branch review — 2026-10-25

Reviewer: fresh gpt-6-astra/high; pinned range c6871ca..f9f07bb. Read-only review; no reviewer subagents or source/index/HEAD changes.

## Strengths

Implementation matches the approved design and addresses all five review-focus areas: unknown evidence, canonical fork/request identity, GitLab interpreted text effects, uncertain mutation receipts and source/target provenance. Dependency closures, entry routes and unpublished preview.7 documentation agree. Evidence distinguishes supplied facts, emulated effects and prepared real Git objects from hosting/native activation.

## Findings

Critical: none. Important: none.

Minor (deferred): tests/support/hosted_provider_fixtures.py:50 invents merge provenance when a merged fixture record lacks merge_oid. The expression request.get("merge_oid") or "c"*40 applies the hypothetical fallback to every lifecycle state. A read-only in-memory reproduction with state="merged" and merge_oid=None normalized to merged=True with cccc... as actual result. Installed instruction-only skills and the retained real-result application are unaffected, but future unknown-provenance fixture coverage could falsely appear conclusive. Recommended repair: preserve missing result for merged records, restrict hypothetical fallback to explicitly unmerged records and add a regression. The executor agrees with Minor severity; no material fix pass is needed.

## Declined to judge and executor rulings

- Authenticated GitHub/GitLab execution and native client activation are deferred validation tracks. Executor keeps them explicitly unverified within the approved emulated/manual scope. Cost if wrong: hidden service/client incompatibility until authenticated/native checks.
- Full provider-policy enforcement by the emulator is outside its contract. Executor retains separate protocol/graph versus instruction-following claims. Cost if wrong: future consumers could overestimate policy coverage and miss defects.

## Assessment

Ready to merge: yes, with the minor fixture correction recommended before expanding unknown-provenance coverage. Reviewer confirmed matching clean worktree and complete-range whitespace, inspected both full-suite receipts (160 discovered, 159 passed, one existing Windows symlink skip; 254.700 and 185.562 seconds), and ran only the concrete in-memory reproduction. The full suite was not rerun during review.

## Subsequent requested correction

The original review above remains unchanged. The later explicit request to fix its Minor finding is completed through two reproduced RED/GREEN regressions and a fresh full-suite gate (162 discovered, 161 passed, one existing Windows skip). See fixture-follow-up.md and review-follow-up-suite.log. No additional independent re-review is claimed; the Minor is now resolved.
