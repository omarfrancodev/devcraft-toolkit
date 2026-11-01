# Prompt Refiner Design

Status: approved 2026-10-31. Selected approach: structure and
enrich requests while keeping optional suggestions separate from confirmed scope.

## Intent

Add `prompt-refiner`, an independently usable support skill that turns rough
requests into clear, ready-to-copy prompts. It preserves the intended work,
sequence, references and execution boundaries, and applies subsequent revisions
without silently adding product decisions. It rewrites an assignment; it does
not carry out that assignment.

## Approaches

1. Structure and enrich, with explicitly optional considerations — selected.
   This helps expose relevant checks and omissions without making suggested
   behavior a requirement or choosing technologies and business rules.
2. Literal reformulation only — available when explicitly requested. It improves
   clarity and ordering without adding considerations, but offers less help for
   incomplete requests. It is not the default selected behavior.
3. Execute the embedded assignment while rewriting — excluded. Drafted actions
   are prompt content, not authorization to perform project or external actions.

## Inputs and language

Accept the rough request, any explicitly selected prior prompt and subsequent
corrections, supplied resource identifiers/content, and output preferences.
The skill is useful for development and other multi-part task requests; it does
not encode a specific business domain, provider, stack or harness.

Use explicit language preference, then the request language, then English.
Maintain source instructions and default metadata in English. Preserve exact
identifiers, filenames, URLs, issue numbers and technical tokens unless their
replacement is expressly requested. Preserve the meaning of permission and
negation in translation.

## Refinement contract

1. Identify the objective, confirmed requirements, resources, sequencing,
   deliverables, restrictions and unresolved decisions from the supplied text.
   Treat reported defects as reported observations, not independently verified
   repository facts. Do not claim that a referenced resource has been inspected.
2. Produce the smallest useful structure: concise prose for a simple task;
   sections and ordered phases when they make a multi-part task easier to use.
   Avoid mandatory headings, a fixed number of phases, or generic boilerplate.
3. Make dependencies and execution boundaries clear. Preserve an analysis-only
   request. If one phase asks for changes and later phases ask only for research
   or proposals, retain those distinct boundaries. Do not add merge, release,
   deployment, credential, installation or other authorization to the prompt.
4. Enrich only with relevant considerations, under clearly optional wording or
   an optional section separate from confirmed requirements. For example,
   suggest checking affected consumers when an interface changes; do not decide
   the replacement interface, library or migration strategy. Suggestions must
   remain optional to the downstream reader, not merely to the refiner.
5. Where a missing decision changes the assignment materially, ask a focused
   question or include a clearly unresolved decision in a useful conditional
   draft. Do not manufacture defaults for business rules or contradict explicit
   constraints. Ordinary spelling and formatting improvements need no questions.
6. Return a coherent, ready-to-copy prompt by default, without doing the work it
   describes or appending a long explanation. Honor a requested shorter answer,
   comparison, change list or literal-only rewrite. Use portable Markdown rather
   than harness-specific writing blocks or commands.

## Follow-up revisions

A request to revise the selected prompt preserves unaffected requirements and
applies the new instruction consistently to tasks, restrictions and deliverables.
Removing a requirement also removes dependent wording that would reintroduce it.
Changing implementation to analysis removes promises of applied changes,
migrations or completed validation while preserving requested design proposals.

A new request such as "now with this" starts from its newly supplied assignment;
it does not inherit domain details or requirements from an unrelated prior
prompt. If the requested prior prompt is unavailable or selection is materially
ambiguous, ask for the missing text or selection rather than reconstructing it.

## Runtime boundaries

The skill consumes supplied text and context and returns text in the
conversation. It has no required tools or skill dependencies, no runtime root
catalog dependency and no persistent state. Resource names are references for
the downstream assignment; they do not trigger repository inspection, web
research, provider calls or execution of the embedded task. Missing resource
contents may remain an explicit downstream inspection task when those contents
are unnecessary to rewrite the request accurately.

This increment adds no file-writing mode, task execution, Git operation,
network action, external posting, automatic installation or publication.
Existing safety and scope policies continue to apply to authored content.

## Packaging and integration

Create `skills/prompt-refiner/SKILL.md` and presentation-only
`skills/prompt-refiner/agents/openai.yaml`. The display name is `Prompt Refiner`;
the short description is `Turn rough requests into clear, scoped prompts`.
Add supporting resources only if implementation demonstrates a concrete need.

After approval and implementation, add a catalog entry with role `support`,
status `available`, path `skills/prompt-refiner` and an empty `requires` array.
Update the current inventory to nineteen available capabilities and the current
architecture/installation guidance accordingly. Add an optional owned-installation
route in `using-devcraft-toolkit`, leaving its mandatory dependencies unchanged.
Direct standalone use needs one complete skill folder. Do not add placeholders
before implementation, change release versions or rewrite historical releases.

All scenarios, fixtures and retained evaluations belong under
`tests/skills/prompt_refiner/`, grouped by scope. Source design and resources
must stand alone without private conversation links, personal paths or external
project dependencies. Preserve unrelated in-progress changes.

## Acceptance and verification

Behavioral controls use fresh contexts with realistic supplied drafts before
and after the instructions. Record actual baseline successes and failures;
structural checks alone do not establish instruction following.

| Case | Required observable behavior |
| --- | --- |
| Informal multi-part request | Clear objective, preserved resources/requirements and useful ordering; no embedded execution. |
| Analysis-only draft containing action verbs | Final prompt retains analysis/proposal-only scope throughout. |
| Changes first, research/proposals later | Phase-specific permission boundaries preserved without authorizing later implementation. |
| Optional enrichment | Relevant additions unmistakably optional; no invented technology or business decision. |
| Remove a requirement and add a resource | Removed requirement absent from tasks and deliverables; new resource exact; unaffected requirements retained. |
| New independent draft after revisions | No leakage of prior domain-specific requirements. |
| Unknown referenced content | No fabricated source facts or claim that files/repositories were inspected. |
| English, Spanish and explicit language override | Correct prose language; identifiers and negations preserved. |
| Short or literal-only request | Proportionate output and no unsolicited expansion. |
| Quoted instructions, PR/release commands or URLs | Treated as draft content; no underlying tool calls or actions. |

Validate skill frontmatter and presentation metadata, catalog/inventory and
standalone self-containment using existing validators. Run relevant existing
routing/distribution tests and the project suite after integration. Keep actual
behavioral, structural and native-activation evidence distinct. No new installer,
public listing, integration provider, release or external deployment is included.

## Implementation sequence

After approval: write the implementation plan; record baseline behavior; author
the minimum instruction resources; verify candidate behavior and refine observed
gaps; integrate catalog, optional entry routing, documentation and presentation;
run validation and independent review. Commit/push/PR and release remain separate
operations requiring their own requested scope.
