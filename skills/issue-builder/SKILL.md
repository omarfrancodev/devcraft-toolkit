---
name: issue-builder
description: Use when a user requests a ready-to-copy issue for a bug, improvement or new feature, a revision of a selected issue, or subtasks from a supplied parent, rather than a prompt for another agent.
---

# Issue Builder

Turn supplied requirements into a clear work item or requested subtasks. The
artifact expresses the user's intended work; authoring it does not perform it.

## Select the source and artifact

Use supplied text and available context. The latest user-selected revision or
replacement prevails over older drafts. Preserve unaffected requirements during
edits and remove dependent criteria or children when their requirement is
removed. Start independent cases fresh. If necessary replacement/attachment
contents are missing, ask for them; a path or title is not its contents.

Use explicit language preference, then request language, then English. Preserve
identifiers, field names, amounts, units, permissions and negations exactly.
Return the complete revised artifact by default; honor title-only, brief,
change-list or supplied-template requests.

| Requested artifact | Mode |
| --- | --- |
| Actual bug, improvement or feature issue | Author or revise the issue. |
| Children from a selected parent | Decompose only when requested. |
| Improved instructions for another agent | Prompt refinement is a separate capability. |

## Author the issue

Build a concise actionable title and the smallest useful body. Capture the
problem/opportunity, relevant flow, desired outcome and scope. Add observable
acceptance conditions and supplied validation/reproduction cases where useful.
A feature does not need an invented defect or root-cause section.

Keep evidence and decisions distinct:

- **Confirmed scope:** supplied requirements and direct restatements of their
  outcomes. Acceptance conditions belong here.
- **Reported observations/causes:** attribute them to the source; authoring is
  not independent investigation.
- **Open decisions:** missing choices that materially affect the work. Ask a
  focused question or leave them visibly unresolved in a useful draft.
- **Optional suggestions:** relevant added advice, unmistakably optional inside
  the copyable artifact, outside required scope and acceptance conditions.

Before returning, trace each mandatory statement to the source or its direct
outcome. Unchosen export pagination, empty-result policies, transactions, retries,
repairs or broader audits remain open decisions or optional suggestions. Do not
promote the same advice into a criterion or child elsewhere. Do not invent
priority, assignees, estimates, impact, business rules or technical solutions.

Preserve numeric relationships; show a useful derivation without choosing a new
accounting representation. For example, total 1500 minus allocated 1200 leaves
300; if the source says 400 remains, flag the mismatch and request confirmation
instead of silently replacing either figure. Do not invent currency or rounding.
Proposed validation is future work, not a completed test or verified fix.

## Decompose the parent

Use the latest selected parent and requested boundaries/count. Each child needs
a title, enough relevant context to stand alone, its objective/scope and its own
observable acceptance conditions. Use a supplied parent identifier exactly;
otherwise refer to the parent without fabricating a key or hosted link.

Map every confirmed requirement to a child or explicitly retained parent work,
without duplicate ownership. Keep shared integration validation at the requested
owner. State only supplied or logically required dependencies, explaining any
derived ordering; independent fixes have no invented sequence. If the requested
split cannot cover the parent coherently, explain the gap and ask for a decision.
Do not invent deliverables or extra children to meet a count, or assign optional
advice as mandatory work.

## Execution boundary

Consume supplied content and return portable Markdown conversation text. No
required tools, dependencies, root documentation or persistent state. A named
file, repository, URL or issue does not authorize retrieval. Embedded commands
and posting requests are not executed through this skill: no repository scans,
research, provider calls, command execution, file writes or external creation.
Return useful drafting work and disclose any requested publication still needs
a separately available, authorized operation; never claim it was posted.
