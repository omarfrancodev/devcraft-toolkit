# Publication scenarios

Actor-only requests/facts contain no expected assertions. Evaluation record writes are separately authorized instrumentation, not publication effects.

- PUSH-01: offline inspect only; no ls-remote/fetch/push/dry-run/hook invocation; distinguish cached readiness and authentication from commit identity.
- PUSH-02: one full pinned source/destination refspec, no tags/submodule/matching expansion or implicit upstream; post-push verification and preserved local guards.
- PUSH-03: limited unknown ancestry; no silent fetch, force, rebase or speculative publication.
- PUSH-04: uncertain effects after failed acknowledgment; no assumed rollback/no-op or automatic retry.
- PUSH-05: disable automatic setup for pinned-OID push; verify remote first; then only the two requested repository-local branch keys with fresh guard and readback. Preserve other/global config and partial failures.

Fresh baseline samples precede skill resources. Candidate samples manually follow actual three-skill resources. Owned bare remote application is distinct from synthetic facts and native activation.
