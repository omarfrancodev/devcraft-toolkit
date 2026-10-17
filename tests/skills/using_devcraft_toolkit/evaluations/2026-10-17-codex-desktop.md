# Evaluation: using-devcraft-toolkit

- Date: 2026-10-17
- Harness: Codex desktop task; this harness does not expose dynamic activation of repo-local skills, so the authored entry was followed directly against the scenario inputs. Harness version was not exposed.
- Method: self-evaluation of routing and language outcomes in the current task. This is not an independent evaluator result.

## Scenario outcomes

- English, Spanish, and French requests preserve the same scope decision while translating explanatory text.
- An explicit Spanish preference overrides an English request; an indeterminate request defaults to English; a later explicit preference updates the execution language.
- Repository context routes to `git-working-directory-policy`; read-only preflight routes to `git-safety-check` with its declared dependency.
- Commit coordination, publication coordination, and activity reporting are described as planned/unavailable in this distribution.
- An unrelated request remains outside toolkit scope, and an individual skill installation does not require the root catalog.

## Limitations

- No independent harness invocation was available, and no cross-harness compatibility is claimed.
- Missing progress/question tools and an external standalone skill installation were checked against the written routing rules, not dynamically simulated.
