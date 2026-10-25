# Independent whole-branch review — 2026-10-25

Reviewer: fresh gpt-6-astra/high, read-only range `36a224d..6041da1`, all five plan Review Focus items. No reviewer subdelegation, checkout mutation or duplicate suite run. Verdict: with fixes; two Important findings, no Critical or Minor findings.

## Findings

1. The original fast-forward recipe inherited overwrite-ignore. A clean status omitted local ignored content newly tracked by the target; the reviewer's separate temporary fixture showed a successful FF replacing it. `--no-overwrite-ignore` instead stopped and preserved content/HEAD. Correction: exact recipe/helper/spec now require that flag and preserve/report earlier fetch/metadata effects.
2. A selected symbolic tracking ref could dereference into an unrelated local branch during fetch; the original exact fetch succeeded and moved that branch while leaving the pointer/HEAD unchanged. Correction: direct-or-absent destination gate before fetch and equivalent pre-push checks for every matching opportunistic tracking destination. Unrelated symbolic aliases are still compared by pointer, not rejected merely because they exist.

The executor reproduced three failing regressions before fixes: ignored FF collision, symbolic fetch target and symbolic push tracking. All three passed after one correction pass, preserving bytes/HEAD/index or preventing remote/local writes as applicable. These are real Git controls under owned fixtures, not installed runtime code.

## Matters deliberately outside this validation

- Authenticated SSH/HTTPS and hosting behavior remain unexercised; transport-specific gaps await authenticated validation.
- Native skill activation and cross-client lifecycle remain deferred; supplied discovery/manual resources do not prove client compatibility.
- Concurrent remote exclusion and server deployment effects are not normal-push guarantees; observed guards are not locks and races may leave partial/uncertain state.

The executor recorded an explicit ruling and cost for each limitation in the retained ledger. No minor findings were deferred. No second review was dispatched: corrected behavior is verified by RED/GREEN and the post-fix full suite. Actual copied-resource application evidence preceded these last preservation corrections; new Git regressions and fresh supplied-fact behavior cover the added gates rather than claiming those applications were repeated.
