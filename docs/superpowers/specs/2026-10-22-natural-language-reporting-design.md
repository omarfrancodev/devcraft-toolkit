# Natural-Language Reporting Design

Date: 2026-10-22
Status: Draft for written-spec review.
Capability: natural-language-report-writer

## Goal

Turn supplied facts into a clear, evidence-based activity report, progress update or summary in the user's language.

## Scope and non-goals

Deliver one independently usable instruction-first capability. Keep requires=[]; the toolkit entry is an optional consumer, not a prerequisite. Do not implement another planned capability or change catalog availability by writing this design.

The capability's persistence and execution boundaries are stated below. CCR, coordinators, native plugin packaging and releases are outside scope.

## Approaches considered

| Approach | Tradeoff and decision |
| --- | --- |
| Fixed business-only report | Predictable output but cannot honor technical audiences, custom structures or user language. |
| Automatic data collection and report publication | Broader automation, but couples reporting to Git/platform access and expands authorization. |
| Evidence-to-report composition with optional explicit persistence | Selected: keeps data collection separate, honors audience/format and permits only a requested local file. |

## Architecture and components

| Component | Responsibility |
| --- | --- |
| SKILL.md | Evidence selection, language, audience and content-only versus explicit file-output flow. |
| references/report-quality.md | Consolidation, uncertainty, claim fidelity and user-format precedence. |
| assets/report.md | English starter structure with title, summary, activities and open_items placeholders. |

Installed resources are local to skills/natural-language-report-writer/. Tests and fixtures are owned by tests/skills/natural_language_report_writer/. Root validation tooling is not an installed runtime dependency.

## Data flow and contracts

Supplied facts and audience -> resolve language and requested structure -> group supported outcomes -> retain uncertainties -> render content -> return content or write/read back one explicitly requested local file.

The interfaces are request/evidence/result records interpreted by the assistant; no callable runtime API or persisted state schema is introduced. The implementation plan supplies exact test packets, source paths and execution checks.

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

## Error handling and authorization

Absent facts return an insufficient-evidence limitation. Conflicting completion claims remain visible or require clarification. An unspecified destination never authorizes persistence. A file-write/readback failure is reported as a failure instead of claiming a created report.

No progress status, formatting result, drafted report or discovered command is authorization for another operation. Preserve unknown facts, unresolved choices and limitations. Do not mutate unrelated files or claim work was executed without evidence.

## Testing strategy and acceptance criteria

Use the following exact request/evidence packets as behavioral cases. The baseline evaluator sees only the request, supplied facts and actual permitted tools, without the candidate skill or expected answer. A separate assessment compares the observed behavior with the assertions below. The same inputs and tool restrictions are used for GREEN with the candidate skill supplied.

Use a fresh supported evaluation context when available; record whether execution was independent, manual or limited. Missing evaluation capability is a limitation, not invented independence. An absent skill is not a RED result. If the baseline meets all cases, inspect the unproven requirement or necessity of the capability; do not force a failure by changing expectations after seeing results.

### RPT-01: consolidation_and_numeric_fidelity

- Request: Summarize these facts as an activity report in Spanish.
- Supplied evidence: Date: 2026-10-20. Empty-name validation was added. A clear error for missing names was added. Search rendering is pending. Twelve fixture cases passed.
- Assertions:
  - Consolidate the two related validation facts without losing their meaning.
  - Keep search rendering unfinished and preserve the date and count 12.
  - Do not invent business gains, deployment, authorship or additional tests.

### RPT-02: empty_and_conflicting_evidence

- Request: Prepare the report.
- Supplied evidence: Variant A: no facts. Variant B: one supplied note says search is complete; another says the same search work is pending.
- Assertions:
  - Variant A identifies insufficient evidence without filler activities.
  - Variant B preserves or clarifies the conflict; it does not arbitrarily choose completed.

### RPT-03: translation_preserves_data

- Request: Use the default template in French. Then repeat in English with an explicit instruction to answer in Spanish.
- Supplied evidence: Date 2026-10-20; count 12; identifier ORDER-7.
- Assertions:
  - Translate visible headings and prose to the resolved language.
  - Preserve 2026-10-20, 12 and ORDER-7 exactly; do not translate placeholder keys in the source template.

### RPT-04: technical_audience_and_custom_format

- Request: Use exactly two sections, Findings and Evidence. Include the filename and identifier.
- Supplied evidence: parser.py now rejects an empty name; reference ORDER-7; no deployment information.
- Assertions:
  - Use the requested sections, with labels translated only if requested.
  - Preserve supplied technical detail rather than forcing an outcome-only template.
  - Do not add unsupported deployment or test claims.

### RPT-05: content_only_then_requested_file

- Request: First provide report content only. In a separate request, save that content to the selected temporary report.md.
- Supplied evidence: Use the supplied fact fixture. The evaluator provides the actual temporary destination only in the second request.
- Assertions:
  - The first request creates no file.
  - The second request writes only the selected report.md and verifies it by reading it back.
  - Unrelated files and the input fixture remain unchanged.

Capture actual observations and assertion outcomes in tests/skills/natural_language_report_writer/evaluations/standalone.md. Where a required evaluation could not run, record the limitation and leave the availability decision open. No new script is required merely to turn prose into keyword tests.

## File structure

- skills/natural-language-report-writer/SKILL.md
- skills/natural-language-report-writer/references/report-quality.md
- skills/natural-language-report-writer/assets/report.md
- tests/skills/natural_language_report_writer/scenarios/reporting.md
- tests/skills/natural_language_report_writer/fixtures/report-facts.json
- tests/skills/natural_language_report_writer/evaluations/standalone.md

Create optional directories only when an actual file needs them. Python packages normalize hyphens to underscores, while scenario ownership retains the canonical skill name.

## Catalog and composition

After principal behavior and structural validation succeed, change only natural-language-report-writer to available with requires=[] in the same complete standalone delivery. Update its availability documentation from the actual catalog counts. The other independently delivered capabilities may or may not already be available.

A separate complete task adds the optional installed-capability route to using-devcraft-toolkit and verifies direct, composed and absent-installation cases. It does not widen the entry's hard dependency group or emulate an absent skill. Standalone capability failure and entry-composition failure remain separate results.

Preserve the read-only foundation context/preflight contracts. A report's explicit file output or a requested validation execution needs its exact side-effect policy in AGENTS.md and tests/scenarios/README.md; that exception does not grant writes to other skills.

## Global Constraints

- Source instructions, documentation, examples and default templates are English; user-facing output uses explicit user preference, then request language, then English when indeterminate.
- Technical identifiers, schema keys, command syntax and supplied data identifiers remain unchanged by translation.
- Tests, fixtures, scenarios and retained evaluations live under tests/skills/<normalized_skill_name>/; root tests/integration/ is only for multiple named skills.
- Installed skills use only their bundled resources and explicitly declared skill dependencies; repository tooling and catalog.json are development resources.
- Implementation must be understandable from repository-local requirements and accessible official technical references, without private conversations, personal paths or unavailable files.
- Catalog status stays planned until structural checks and actual behavioral evaluation justify available; record unexecuted cases as limitations.
- No new coordinator, CCR integration, plugin manifest, installer, release automation or runtime orchestration engine is included.
- Use Python 3.11+ and the existing PyYAML>=6.0,<7.0 development setup; add no dependencies or helpers without a demonstrated need.
- Behavioral RED means an observed baseline violation without the candidate skill; a missing SKILL.md or planned catalog entry is not a failing behavior test.

## Risks and review focus

1. RPT-01: several related facts consolidate without invented completion or impact.
2. RPT-02: empty/conflicting evidence remains explicit instead of producing filler.
3. RPT-03: translated headings preserve dates, numbers and identifiers.
4. RPT-04: a technical audience and custom format override the starter template.
5. RPT-05: content-only and explicit local-file output have different side-effect boundaries.

The implementation plan maps every item above to a named case and a concrete task. Source/content checks do not replace observed behavior. Limited harness coverage remains explicitly limited.

## References

- [Language behavior](../../language.md) and [scenario protocol](../../../tests/scenarios/README.md): existing project requirements.

Project requirements are stated in this document; links provide accessible standards or in-repository contracts. Review this spec before treating its companion plan as ready for execution.
