# Commit Message Formatting Design

Date: 2026-10-22
Status: Proposed; product implementation has not started.
Capability: conventional-commits-style

## Product goal

Produce clear commit messages from supplied change intent and repository conventions without inspecting or modifying Git unless a separate requested operation supplies that context.

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

## Files and test ownership

- skills/conventional-commits-style/SKILL.md
- skills/conventional-commits-style/references/message-format.md
- tests/skills/conventional_commits_style/scenarios/formatting.md
- tests/skills/conventional_commits_style/evaluations/<run>.md when explicitly retained

Tests use the canonical owner conventional-commits-style; the Python-compatible test package is conventional_commits_style. Introduce unit/integration test code only for a real executable contract, not to check whether instructions contain a chosen sentence. Scenario fixtures and evidence remain outside the installed skill folder.

## Catalog, routing and documentation

After actual verification, mark only conventional-commits-style available and leave requires=[] in catalog.json. Add its installed-capability route to using-devcraft-toolkit without widening the entry's hard dependency group. Route only when the skill is actually installed; a missing optional capability remains a visible limitation.

Update README.md, docs/architecture.md, docs/composition.md, docs/installation.md, docs/compatibility.md and docs/roadmap.md to match observed availability. Derive current counts from catalog.json instead of assuming that other increments have already landed. Keep the foundation spec's historical three-skill delivery record intact.

Foundation context/preflight stay read-only. If this capability allows explicit file output or check execution, document those effects precisely in AGENTS.md and the scenario protocol; do not change the permissions of unrelated skills.

## Acceptance and evidence

Run the existing repository suite and structural validator. Execute the owned behavioral scenarios on the actual available harness; use the common protocol and record executed/limited outcomes. Structural success alone is not a behavioral pass. A manually followed skill is recorded as a self-evaluation, not a dynamically loaded or independent evaluation.

No network connection, unrelated source tree or tool absent from the environment is needed to understand the requirements. A limited scenario remains limited and must not become a blanket compatibility claim. Leave future coordinators planned.

## References

- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/): message structure, optional scope/body/footers and breaking markers.

The maintained implementation requirements are fully stated above. References explain standards or existing project contracts; they do not substitute for missing product decisions.
