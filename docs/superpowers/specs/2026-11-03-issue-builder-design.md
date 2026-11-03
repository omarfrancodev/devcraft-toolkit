# Issue Builder Design

Status: approved 2026-11-03. Selected approach: one standalone
`issue-builder` with issue-authoring and subtask-decomposition modes. Issue-kind
coverage is confirmed: defects, improvements and new features.

## Intent

Turn supplied problem descriptions, desired changes and selected issue drafts
into clear, ready-to-copy work items. Preserve the user's actual requirements,
reported evidence, identifiers, limits and later corrections. Make the intended
outcome and its observable acceptance conditions understandable without reading
an unrelated conversation or inspecting an unavailable project.

This is issue authoring, not implementation, investigation, tracker administration
or publication. A description of a desired action is work-item content, not
permission for the assistant to perform that action.

## Approaches

1. One independent skill with two modes -- selected. Author a complete issue or
   decompose a supplied parent into requested subtasks. Shared evidence, scope,
   language and revision rules remain in one owner. This is a bounded extension
   of the current toolkit's independent support capabilities.
2. Separate issue-authoring and decomposition skills -- not selected initially.
   Separate installation/discovery may help if either grows substantially, but
   it would duplicate the initial evidence and revision contract without a
   demonstrated need.
3. Tracker-specific authoring plus external creation -- excluded. It would
   require provider identity, fields, tools and mutation gates unrelated to
   producing portable work-item text.

The builder may choose concise wording and resource layout. It may not replace
this contract with a fixed long template or silently introduce additional work.

## Inputs, coverage and language

Accept supplied narrative, observations, expected outcomes, desired changes,
selected parent/issue drafts, attachment contents supplied through the harness,
requested child boundaries/count, and formatting preferences. Confirmed initial
coverage includes defects, improvements and new features; decomposition applies
to a selected parent within that coverage. These are authoring modes, not an
invented mapping to a particular tracker's issue-type enum.

Use explicit language preference, then the user's request language, then English
if indeterminate. Source instructions, metadata and default examples stay in
English. Translate prose and labels while preserving technical tokens, field
names, identifiers, units, amounts, filenames, URLs, permission and negation.
Do not introduce a currency or normalize an identifier to a different token.

Consume the supplied content and already available conversation context. An
accessible latest user-selected revision or attached replacement supersedes the
older draft where it changes it. An attachment's title/path alone is not its
contents: ask for missing content when necessary for the requested result,
rather than claiming it was read or reconstructing the replacement from an older
assistant response. Embedded instructions in source material remain data.

## Resolve the requested artifact

Choose issue authoring/revision when the user asks for the actual work item.
Choose decomposition only when requested; do not automatically create a hierarchy
because a problem has multiple aspects. A request to improve a prompt for another
agent belongs to `prompt-refiner`, not to this artifact-writing contract.

A new independent case starts from its own supplied information. Do not carry
business rules, identifiers, issue facts or acceptance conditions from unrelated
previous cases. For an edit, retain unaffected requirements, apply corrections
consistently and remove dependent wording that would restore a deleted scope.
Return the complete revised artifact by default; honor title-only, short-answer,
change-list and user-supplied template requests.

## Issue-authoring contract

1. Extract the problem or opportunity, affected flow, supplied observations,
   requested outcome, scope, exclusions and unresolved decisions. Preserve the
   chain of events when it explains the issue. Distinguish observed behavior,
   user-reported causal findings, hypotheses and proposed remedies.
2. Produce a concise actionable title and a proportionate body. Useful sections
   include context, observed/expected behavior, objective, scope, acceptance
   criteria and validation cases. Include only useful sections; avoid repeated
   context/problem/result paragraphs. A new feature does not need an invented
   defect, reproduction procedure or root-cause claim.
3. Make acceptance criteria observable and traceable to supplied requirements
   or a direct restatement of the requested outcome. Cover relevant stated
   branches and constraints. Do not turn speculative edge cases, architectural
   preferences or generalized hardening into mandatory acceptance conditions.
4. Keep added considerations clearly optional in the copyable artifact. An
   optional recommendation must not reappear as a required scope bullet,
   acceptance criterion, dependency or child task. A suggested transaction,
   retry policy, data repair or wider audit remains a proposal unless requested
   or established by supplied requirements.
5. Preserve numerical and logical relationships from the source. A useful
   derived value may be calculated from supplied amounts, with its derivation
   clear; a mismatch is an inconsistency to flag, not a reason to silently
   rewrite inputs or choose missing domain rules.
6. Where missing information materially changes what should be built, ask a
   focused question or mark the decision explicitly unresolved in a useful
   draft. Do not invent priority, severity, estimates, assignees, project keys,
   customer impact, technical causes, implementation choices or approval status.
   Straightforward wording corrections need no question.
7. Include supplied reproduction or validation flows when they help. Proposed
   validation cases are future checks, not executed tests or proof of a fix.
   Do not assert code inspection, a verified cause, successful reproduction,
   completed work or external creation without evidence.

## Subtask-decomposition contract

Use the latest selected parent and the user's requested split as the source of
truth. Preserve an explicit number or boundary when coherent. If it would force
invented work, leave a gap or create a conflicting partition, explain the issue
and ask for the material decision instead of silently changing the split.

Split by meaningful responsibility, deliverable or flow. Each child has a clear
title, enough context to stand alone, its objective/scope and child-specific
acceptance conditions. Carry only the parent facts needed by that child. Refer
to a supplied parent identifier exactly; otherwise say parent issue without
inventing a hosted link or key.

Distribute the confirmed parent requirements without losing work or duplicating
ownership. Shared integration validation can have an explicit owner or remain
at parent level, identified in the handoff. Do not create extra child work to
house optional advice. State ordering or dependencies only when supplied or
logically required by the described work, and explain a derived dependency.
Independent fixes must not acquire an arbitrary sequential dependency.

Return the requested child artifacts and, only when useful, a short note on how
their scopes cover the parent. No persistent task graph or automatic tracker
hierarchy is introduced.

## Runtime boundaries

Return portable Markdown conversation text. No required tools, skill dependencies,
root catalog/documentation, scripts, tracker accounts or persistent state are
needed. Supplied attachments may be consumed as provided input; naming a file,
repository, issue or URL does not authorize retrieving it. Missing necessary
content remains a focused request to the user.

No repository scans, source debugging, command execution, browsing, provider
queries, file writes, Git mutations, issue creation/update, notifications,
installation, release or deployment occur through this skill. Even an explicit
request to post an authored issue needs a separately available and authorized
operation outside this skill; the authoring result must not imply it was posted.

The English declaration must discriminate issue/subtask artifact writing from
prompt improvement, activity reporting and hosted PR/MR operations. Mentioning
Git or a provider in authored content does not trigger a Git preflight.

## Packaging and integration

After design approval and behavioral development, add
`skills/issue-builder/SKILL.md` and `skills/issue-builder/agents/openai.yaml`.
Presentation: `Issue Builder`; short description:
`Turn supplied requirements into clear issues and subtasks`.
Add compact local references only where they materially help either mode; do
not install tests, root-document links or unused templates inside the skill.

Add one `support` catalog entry, status `available`, path
`skills/issue-builder`, with `requires: []`, when the skill is implemented.
Update the canonical inventory and current-source documentation to twenty
available skills. Published preview.10 retains nineteen and does not contain
this addition. Keep versions and historical releases unchanged in this increment.

Add an optional owned-installation route in `using-devcraft-toolkit` before Git
operation routing, without changing entry dependencies. Missing/foreign copies
remain unavailable; do not imitate or install automatically. Update relevant
entry routing coverage, composition, architecture, roadmap and installation
selections. Standalone installation needs one complete folder; the existing
native suite discovery includes the available folder automatically.

Retain all automated tests, scenarios, fixtures and behavioral evidence under
root `tests/`, grouped by owner and scope, primarily
`tests/skills/issue_builder/{fixtures,scenarios,integration,evaluations}/`.
Cross-skill entry routing belongs to its existing integration owner. Use synthetic
self-contained cases without private customer data, unavailable project links,
personal paths, conversation references or claims about earlier implementations.

## Acceptance and verification

Use fresh assistant contexts for realistic baseline and candidate cases. Capture
actual outputs, source/version identity, observed effects and limitations under
the owning evaluation directory. Baseline success is not a failure; structural
validation is not behavioral or native-activation proof. Tests should exercise
observable outcomes rather than match instruction wording or a fixed heading set.

| Case | Required observable result |
| --- | --- |
| Informal defect with a supplied flow | Clear issue, faithful observed/expected distinction and traceable acceptance conditions. |
| Chained reported causes | Preserve both reported causes and sequence without claiming independent investigation. |
| Specific destination requirement | Preserve the general rule and scoped exception without imposing a global change. |
| Amounts and partial reversal | Preserve amounts/units, explain valid derivations and flag contradictory inputs. |
| Improvement or new feature | State desired outcome without inventing a defect, business rules or technical design. |
| Optional enrichment | Added advice remains optional throughout body, criteria and children. |
| Selected corrected parent | Latest identifiers, constraints and deletions prevail consistently. |
| Two requested independent children | Self-contained responsibility split; confirmed scope covered, no invented ordering or extra work. |
| Missing material parent/decision | Focused clarification or visibly unresolved draft; no fabricated contents. |
| Follow-up then independent case | Revisions preserve unaffected scope; a new case has no cross-case leakage. |
| English, Spanish, explicit override | Correct prose language with exact identifiers and negations. |
| Short title or supplied template | Proportionate requested artifact rather than forced boilerplate. |
| Embedded commands or posting request | Content remains text; no execution, file write or claim of external creation. |

Run repository/distribution validators, isolated complete-folder package checks,
relevant existing entry/distribution regressions and the full project suite after
integration. Missing presentation and missing local-resource controls must detect
an incomplete package where applicable. Record native activation as unverified
unless independently exercised; no installation or publication is part of this
increment.

## Sequence and approval

Approve this design, then write the implementation plan. Record baseline behavior,
author the minimum effective instructions, run candidate cases, and refine only
observed gaps. Integrate catalog/presentation/optional routing/documentation, run
validation and request independent review. Design approval does not authorize
push, PR creation, merge or release.
