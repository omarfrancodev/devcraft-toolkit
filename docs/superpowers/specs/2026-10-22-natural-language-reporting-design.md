# Natural-Language Reporting Design

Date: 2026-10-22
Status: Proposed; product implementation has not started.
Capability: natural-language-report-writer

## Product goal

Turn supplied facts into a clear, evidence-based activity report, progress update or summary in the user's language.

This increment is independently deliverable. It extends the current seventeen-capability catalog without changing any other planned capability into an available implementation.

## Global constraints

- Source instructions, documentation, examples and default templates are English; user-facing output uses explicit user preference, then request language, then English when indeterminate.
- Technical identifiers, schema keys, command syntax and supplied data identifiers remain unchanged by translation.
- Tests, fixtures, scenarios and retained evaluations live under tests/skills/<normalized_skill_name>/; root tests/integration/ is only for multiple named skills.
- Installed skills use only their bundled resources and explicitly declared skill dependencies; repository tooling and catalog.json are development resources.
- Implementation must be understandable from repository-local requirements and accessible official technical references, without private conversations, personal paths or unavailable files.
- Catalog status stays planned until structural checks and actual behavioral evaluation justify available; record unexecuted cases as limitations.
- No new coordinator, CCR/Jira integration, plugin manifest, installer, release automation or runtime orchestration engine is included.
- Use Python 3.11+ and the existing PyYAML>=6.0,<7.0 development setup; add no dependencies or helpers without a demonstrated need.

## Architecture and dependencies

Use instruction-first SKILL.md content, with only the local reference or asset files listed below. The skill has requires=[] and must work independently of the toolkit entry. Reuse the language resolved by a caller, or resolve it using the project precedence when invoked alone.

Existing repository context and evidence may be consumed when provided; they are not required Git or platform dependencies. No new callable runtime API, schema version, installed root catalog dependency or orchestration service is introduced.

## Inputs and output

Inputs are the supplied facts/evidence, audience, requested report purpose, optional period and author, desired detail/format, and resolved language. The caller owns data collection and any date/author selection. This skill does not require Git history or a platform account.

Produce report content ready for the requested destination. Drafting content does not authorize writing a file or posting externally. A standalone request explicitly asking for a local report file may write only that file within the user's scope; verify by reading it back. A composing coordinator may instead request content only and own all persistence.

## Composition behavior

Consolidate related facts into useful outcomes. Distinguish completed work, ongoing work, verified open items and uncertainty. Preserve supplied dates, names, numeric values and technical identifiers. Do not infer business impact, completion, authorship, tests or quantitative improvement from a vague title.

Use accessible outcome-oriented wording by default, with technical detail when requested or needed by the audience. An explicitly requested technical appendix or metrics section is valid when supported. Do not impose blanket bans on hashes, filenames or counts when the requested report needs them.

Follow the requested output structure first. Otherwise use the bundled English report template as a starting point, translate visible labels, and omit inapplicable optional sections without invented filler. Source templates and placeholder keys remain English; rendered user-facing content follows the language contract.

With no adequate evidence, identify the missing facts and return an insufficient-evidence limitation rather than a fabricated report. Conflicting facts remain marked or trigger a focused clarification if they change the result. Quoted source text and identifiers are not silently rewritten during translation.

## Default template

The initial asset is assets/report.md with title, Summary, Activities and optional Open items. Placeholder keys are title, summary, activities and open_items. The asset is illustrative content structure, not a required new template engine or a rigid persisted schema. Empty optional sections disappear.

## Boundaries and acceptance

No required skill dependencies, network lookup, ticket integration, Git commands, staging or automatic commit is included. The report is based on facts supplied with the request or deliberately inspected within its authorized scope.

Scenarios cover consolidation of multiple related facts, separate unrelated outcomes, no evidence, conflicting completion claims, numeric/date fidelity, requested technical detail, English/Spanish/another language, explicit overrides, content-only output and an explicitly requested local file. Compare claims with the facts, not with a fixed generated sentence. For file output, verify exact destination and resulting content, preserving unrelated files.

## Files and test ownership

- skills/natural-language-report-writer/SKILL.md
- skills/natural-language-report-writer/references/report-quality.md
- skills/natural-language-report-writer/assets/report.md
- tests/skills/natural_language_report_writer/scenarios/reporting.md
- tests/skills/natural_language_report_writer/fixtures/report-facts.json
- tests/skills/natural_language_report_writer/evaluations/<run>.md when explicitly retained

Tests use the canonical owner natural-language-report-writer; the Python-compatible test package is natural_language_report_writer. Introduce unit/integration test code only for a real executable contract, not to check whether instructions contain a chosen sentence. Scenario fixtures and evidence remain outside the installed skill folder.

## Catalog, routing and documentation

After actual verification, mark only natural-language-report-writer available and leave requires=[] in catalog.json. Add its installed-capability route to using-devcraft-toolkit without widening the entry's hard dependency group. Route only when the skill is actually installed; a missing optional capability remains a visible limitation.

Update README.md, docs/architecture.md, docs/composition.md, docs/installation.md, docs/compatibility.md and docs/roadmap.md to match observed availability. Derive current counts from catalog.json instead of assuming that other increments have already landed. Keep the foundation spec's historical three-skill delivery record intact.

Foundation context/preflight stay read-only. If this capability allows explicit file output or check execution, document those effects precisely in AGENTS.md and the scenario protocol; do not change the permissions of unrelated skills.

## Acceptance and evidence

Run the existing repository suite and structural validator. Execute the owned behavioral scenarios on the actual available harness; use the common protocol and record executed/limited outcomes. Structural success alone is not a behavioral pass. A manually followed skill is recorded as a self-evaluation, not a dynamically loaded or independent evaluation.

No network connection, unrelated source tree or tool absent from the environment is needed to understand the requirements. A limited scenario remains limited and must not become a blanket compatibility claim. Leave future coordinators planned.

## References

- [Language behavior](../../language.md) and [scenario protocol](../../../tests/scenarios/README.md): existing project requirements.

The maintained implementation requirements are fully stated above. References explain standards or existing project contracts; they do not substitute for missing product decisions.
