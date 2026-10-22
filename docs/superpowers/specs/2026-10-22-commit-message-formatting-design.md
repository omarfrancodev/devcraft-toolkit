# Commit Message Formatting Design

Date: 2026-10-22
Status: Draft for written-spec review.
Capability: conventional-commits-style

## Goal

Produce clear commit messages from supplied change intent and repository conventions without inspecting or modifying Git unless a separate requested operation supplies that context.

## Scope and non-goals

Deliver one independently usable instruction-first capability. Keep requires=[]; the toolkit entry is an optional consumer, not a prerequisite. Do not implement another planned capability or change catalog availability by writing this design.

The capability's persistence and execution boundaries are stated below. CCR/Jira, coordinators, native plugin packaging and releases are outside scope.

## Approaches considered

| Approach | Tradeoff and decision |
| --- | --- |
| Fixed language and fixed vocabulary | Small surface, but fails user-language requirements and project-specific conventions. |
| Executable formatter and parser | Useful for strict machine enforcement, but adds a runtime and cannot infer functional intent from supplied facts alone. |
| Instruction-first formatting with explicit input boundaries | Selected: supports independent proposals, project conventions and ambiguity without becoming a commit executor. |

## Architecture and components

| Component | Responsibility |
| --- | --- |
| SKILL.md | Trigger, language resolution, formatting sequence and no-write boundary. |
| references/message-format.md | Subject/body/footer decisions, ticket conventions, breaking changes and ambiguity handling. |

Installed resources are local to skills/conventional-commits-style/. Tests and fixtures are owned by tests/skills/conventional_commits_style/. Root validation tooling is not an installed runtime dependency.

## Data flow and contracts

Supplied change intent and conventions -> resolve language and confirmed references -> choose type/scope -> compose subject/body/footers -> expose unresolved decisions -> return a proposal. No stage invokes Git or creates a commit.

The interfaces are request/evidence/result records interpreted by the assistant; no callable runtime API or persisted state schema is introduced. The implementation plan supplies exact test packets, source paths and execution checks.

## Inputs and output

Inputs are the supplied change summary, intended grouping, repository conventions when available, optional confirmed issue references, and the already resolved output language. Missing information stays unknown; the skill does not invent an issue, scope, breaking change, author or validation result.

Return a proposed subject and optional body/footers, a concise grouping question only when needed, and any unresolved material decision. Formatting completion is not a created commit. No required machine-readable runtime schema is introduced.

## Formatting behavior

Default to type(scope): subject, omitting scope when it adds no useful information. Common types are feat, fix, refactor, chore, docs, test, style, build, ci and perf; honor a documented project-specific type instead of treating this list as an exhaustive standard. A breaking-change marker or footer is included only when the supplied behavior establishes a breaking contract.

Keep type syntax and technical scope conventions intact; write the natural-language subject/body in the resolved language. Explain functional intent, not a list of filenames or generic "changes". Use a short subject by default; add a body or footers when requested or needed to preserve relevant context.

Conventional Commit syntax starts with the type. Issue references normally belong in a requested/project-defined footer. A leading ticket prefix is an explicit repository convention or user override, not a universal rule or a claim of strict standard conformance. Use only provided or confirmed references; resolve competing applicable references before selecting one. A later user correction replaces the earlier formatting decision.

Treat quotation marks, apostrophes, dollar signs and shell-looking text as message data. Do not distort useful wording to accommodate a future shell command. A future commit executor must pass message data safely; this skill executes no commit command.

## Boundaries and acceptance

The skill has no required skill dependencies and works without a Git repository. It never stages, commits, renames a branch, queries a ticket platform, publishes a message or adds unsolicited attribution.

Behavioral cases cover English/Spanish/another language, explicit override, indeterminate language, meaningful/omitted scope, a project-specific type, confirmed versus ambiguous references, a later reference correction, unsupported breaking claims, mixed unrelated changes and quote-bearing text. Check semantics and side effects rather than exact prose. Do not infer a type-to-version release outcome as an executed release.

## Error handling and authorization

Missing change intent requires the missing fact. Competing applicable references require selection; a later explicit correction updates the proposal. An unsupported breaking claim is omitted or identified as unresolved. No repository is an acceptable input condition, not an error.

No progress status, formatting result, drafted report or discovered command is authorization for another operation. Preserve unknown facts, unresolved choices and limitations. Do not mutate unrelated files or claim work was executed without evidence.

## Testing strategy and acceptance criteria

Use the following exact request/evidence packets as behavioral cases. The baseline evaluator sees only the request, supplied facts and actual permitted tools, without the candidate skill or expected answer. A separate assessment compares the observed behavior with the assertions below. The same inputs and tool restrictions are used for GREEN with the candidate skill supplied.

Use a fresh supported evaluation context when available; record whether execution was independent, manual or limited. Missing evaluation capability is a limitation, not invented independence. An absent skill is not a RED result. If the baseline meets all cases, inspect the unproven requirement or necessity of the capability; do not force a failure by changing expectations after seeing results.

### FMT-01: ambiguous_reference_then_correction

- Request: Prepare a commit for the parser fix. Relevant issues may be TASK-12 or TASK-13. Do not choose one for me.
- Supplied evidence: The parser rejects an empty name with a clear error. Later response: Use TASK-13.
- Assertions:
  - Initial output asks which applicable issue to use and invents neither selection nor extra issue.
  - After the explicit response, only TASK-13 is referenced and the decision is updated.

### FMT-02: project_specific_type_scope_and_body

- Request: Our project uses maintenance for internal cleanup. Draft a maintenance(parser) commit with a body.
- Supplied evidence: Consolidated duplicate parser checks; no user-visible behavior changed.
- Assertions:
  - Use the supplied maintenance type and parser scope; do not force feat or fix.
  - The body describes the supplied cleanup without a fabricated functional change or test result.

### FMT-03: breaking_marker_requires_evidence

- Request: Draft a commit; add a breaking marker only if justified.
- Supplied evidence: An error message was clarified; no public input/output contract changed.
- Assertions:
  - No ! marker or BREAKING CHANGE footer is invented.
  - Return a proposal without running Git.

### FMT-04: quoted_subject_is_data

- Request: Propose a subject that mentions the literal strings "ready", $HOME and $(touch marker). Do not execute anything.
- Supplied evidence: Logging preserves these literal values.
- Assertions:
  - Preserve the supplied literals as data; no shell command or file named marker is created.
  - Do not drop useful wording merely to fit a future command-line quoting style.

### FMT-05: language_without_repository

- Request: Redacta un commit para corregir la validación de nombres vacíos; no hay repositorio disponible.
- Supplied evidence: The input rejects empty names. Repeat with an English request and with: Answer in French.
- Assertions:
  - Natural-language subject follows Spanish, English and the explicit French override respectively.
  - Technical Conventional Commit tokens remain intact; no Git repository, ticket or validation result is invented.

### FMT-06: missing_intent

- Request: Write the commit.
- Supplied evidence: No change description, repository or evidence was provided.
- Assertions:
  - Ask for the change intent instead of producing a generic unsupported completion claim.

Capture actual observations and assertion outcomes in tests/skills/conventional_commits_style/evaluations/standalone.md. Where a required evaluation could not run, record the limitation and leave the availability decision open. No new script is required merely to turn prose into keyword tests.

## File structure

- skills/conventional-commits-style/SKILL.md
- skills/conventional-commits-style/references/message-format.md
- tests/skills/conventional_commits_style/scenarios/formatting.md
- tests/skills/conventional_commits_style/evaluations/standalone.md

Create optional directories only when an actual file needs them. Python packages normalize hyphens to underscores, while scenario ownership retains the canonical skill name.

## Catalog and composition

After principal behavior and structural validation succeed, change only conventional-commits-style to available with requires=[] in the same complete standalone delivery. Update its availability documentation from the actual catalog counts. The other independently delivered capabilities may or may not already be available.

A separate complete task adds the optional installed-capability route to using-devcraft-toolkit and verifies direct, composed and absent-installation cases. It does not widen the entry's hard dependency group or emulate an absent skill. Standalone capability failure and entry-composition failure remain separate results.

Preserve the read-only foundation context/preflight contracts. A report's explicit file output or a requested validation execution needs its exact side-effect policy in AGENTS.md and tests/scenarios/README.md; that exception does not grant writes to other skills.

## Global Constraints

- Source instructions, documentation, examples and default templates are English; user-facing output uses explicit user preference, then request language, then English when indeterminate.
- Technical identifiers, schema keys, command syntax and supplied data identifiers remain unchanged by translation.
- Tests, fixtures, scenarios and retained evaluations live under tests/skills/<normalized_skill_name>/; root tests/integration/ is only for multiple named skills.
- Installed skills use only their bundled resources and explicitly declared skill dependencies; repository tooling and catalog.json are development resources.
- Implementation must be understandable from repository-local requirements and accessible official technical references, without private conversations, personal paths or unavailable files.
- Catalog status stays planned until structural checks and actual behavioral evaluation justify available; record unexecuted cases as limitations.
- No new coordinator, CCR/Jira integration, plugin manifest, installer, release automation or runtime orchestration engine is included.
- Use Python 3.11+ and the existing PyYAML>=6.0,<7.0 development setup; add no dependencies or helpers without a demonstrated need.
- Behavioral RED means an observed baseline violation without the candidate skill; a missing SKILL.md or planned catalog entry is not a failing behavior test.

## Risks and review focus

1. FMT-01: competing references and a later correction preserve the actual user decision.
2. FMT-02: project-specific types, optional scope and requested bodies remain usable.
3. FMT-03: breaking syntax is never inferred from a request alone.
4. FMT-04: shell-looking message data is preserved without execution.
5. FMT-05: no repository and language changes do not alter the requested formatting scope.

The implementation plan maps every item above to a named case and a concrete task. Source/content checks do not replace observed behavior. Limited harness coverage remains explicitly limited.

## References

- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/): message structure, optional scope/body/footers and breaking markers.

Project requirements are stated in this document; links provide accessible standards or in-repository contracts. Review this spec before treating its companion plan as ready for execution.
