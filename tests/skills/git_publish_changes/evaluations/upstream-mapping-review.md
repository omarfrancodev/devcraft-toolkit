# Usable upstream review follow-up — 2026-10-25

Scope: F002 from the [PR #8 review](https://github.com/omarfrancodev/devcraft-toolkit/pull/8#issuecomment-6405229539), reviewed source 030faf65935e2625fa58735e4f5b976454634d34. The requirement is self-contained: requested upstream setup must resolve to the expected local tracking ref/commit, not merely store two branch keys. Git documents that [branch.merge must match a fetched ref](https://git-scm.com/docs/git-config#Documentation/git-config.txt-branchname.merge).

## Real regression and correction

The [RED run](upstream-mapping-red.log) reproduced two missing prerequisites. A real clone --single-branch published feature/demo normally and independently verified the remote OID. The old two-key recipe returned configured although Git could not resolve its upstream because remote.origin.fetch covered main only. A second fixture had a wildcard mapping but no local tracking ref for an already equal remote; it also incorrectly completed setup.

The revised reference requires an existing safe unambiguous mapping and a usable direct local tracking ref before either key write. Missing prerequisites return upstream needs_decision, preserve the verified publication and keys, and grant no fetch, ref creation or mapping repair. Successful setup additionally resolves the expected full upstream ref and commit. Cached tracking OIDs remain distinct from independently observed remote state. Post-write resolution failure is partial and preserves actual state.

The [GREEN run](upstream-mapping-green.log) passed both regressions plus ordinary new-branch setup and equality/config-only setup. Snapshot assertions preserve local content/index/config and server state when setup is blocked; publication still succeeds independently in the single-branch fixture. The test-only recipe is outside installed resources and uses Git prospective resolution for its known positive-refspec fixtures. It is not a general runtime mapping parser; maintained instructions also cover exclusions, ambiguous mappings and effective scopes.

## Behavior evaluation

The [baseline actor](upstream-mapping-baseline.json) already recognized the missing mapping and safely declined incomplete key writes. Retain that success: this is an explicit-contract correction supported by a reproduced Git failure, not evidence that every old-guidance actor fails. A fresh [candidate](upstream-mapping-candidate.json) handled four supplied-fact cases: absent mapping, absent tracking ref, usable cached ref at an older commit, and failed final resolution after keys. All four evaluator assertions passed. No actual skill loader, network or Git execution occurred in those actor cases; writes were separately authorized instrumentation.

## Environment and validation limits

The reviewer reported missing PyYAML and Windows Git/path restrictions in their own run; those outcomes are not rewritten as passing. This run uses Python 3.14.3, PyYAML 6.0.3 and Git 2.45.0.windows.1. PyYAML was already declared in requirements-dev.txt. Repository/distribution and skill structural validators passed in this environment. Local bare repositories do not establish authenticated transport or native activation. Full-suite results are appended after execution.

## Final verification

Fresh full command: `python -B -m unittest discover -s tests -p "test_*.py" -v` — **140 tests, 139 passed, one existing Windows symlink privilege skip**, 202.301 seconds. [Raw log](upstream-mapping-full-suite.log). Both repository/distribution validators and publication skill quick validation passed. The instruction body is 448 whitespace-delimited words. Complete-base whitespace passed. The correction adds no runtime dependency, extra configuration permission, authenticated transport or native compatibility claim.

Whole-PR changed-document local target check: 138 targets, zero missing.
