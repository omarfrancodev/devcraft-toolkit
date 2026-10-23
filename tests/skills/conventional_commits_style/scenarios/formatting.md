# Conventional Commit formatting scenarios

Canonical skill owner: `conventional-commits-style`

These packets are used to evaluate behavior. Assertions are evaluator-only and must not be shown to the acting agent.

```yaml
cases:
  - id: FMT-01
    name: ambiguous_reference_then_correction
    request: "Prepare a commit for the parser fix. Relevant issues may be TASK-12 or TASK-13. Do not choose one for me."
    facts: "The parser rejects an empty name with a clear error. Later response: Use TASK-13."
    assertions:
      - "Initial output asks which applicable issue to use and invents neither selection nor extra issue."
      - "After the explicit response, only TASK-13 is referenced and the decision is updated."
  - id: FMT-02
    name: project_specific_type_scope_and_body
    request: "Our project uses maintenance for internal cleanup. Draft a maintenance(parser) commit with a body."
    facts: "Consolidated duplicate parser checks; no user-visible behavior changed."
    assertions:
      - "Use the supplied maintenance type and parser scope; do not force feat or fix."
      - "The body describes the supplied cleanup without a fabricated functional change or test result."
  - id: FMT-03
    name: breaking_marker_requires_evidence
    request: "Draft a commit; add a breaking marker only if justified."
    facts: "An error message was clarified; no public input/output contract changed."
    assertions:
      - "No ! marker or BREAKING CHANGE footer is invented."
      - "Return a proposal without running Git."
  - id: FMT-04
    name: quoted_subject_is_data
    request: "Propose a subject that mentions the literal strings \"ready\", $HOME and $(touch marker). Do not execute anything."
    facts: "Logging preserves these literal values."
    assertions:
      - "Preserve the supplied literals as data; no shell command or file named marker is created."
      - "Do not drop useful wording merely to fit a future command-line quoting style."
  - id: FMT-05
    name: language_without_repository
    request: "Redacta un commit para corregir la validación de nombres vacíos; no hay repositorio disponible."
    facts: "The input rejects empty names. Repeat with an English request and with: Answer in French."
    assertions:
      - "Natural-language subject follows Spanish, English and the explicit French override respectively."
      - "Technical Conventional Commit tokens remain intact; no Git repository, ticket or validation result is invented."
  - id: FMT-06
    name: missing_intent
    request: "Write the commit."
    facts: "No change description, repository or evidence was provided."
    assertions:
      - "Ask for the change intent instead of producing a generic unsupported completion claim."
  - id: FMT-07
    name: ticket_reference_uses_conventional_footer
    request: "Draft a Conventional Commit for the parser fix and reference TASK-13."
    facts: "The parser rejects empty names with a generic error; it should continue rejecting them and show a clear, actionable validation message. No project convention specifies ticket placement."
    assertions:
      - "The subject begins with fix(parser):; the ticket does not lead the subject."
      - "Include only TASK-13 in a Conventional Commit footer, such as Refs: TASK-13, without inventing ticket status."
      - "Do not run Git or query a ticket system."
  - id: FMT-08
    name: corrected_reference_preserves_commit_format
    request: "Prepare a commit for the parser fix. Relevant issues may be TASK-12 or TASK-13. Do not choose one for me."
    facts: "The parser rejects an empty name with a clear error. Later response: Use TASK-13."
    assertions:
      - "Initial output asks which applicable issue to use and invents neither selection nor extra issue."
      - "After the explicit correction, the subject begins with fix(parser):, only TASK-13 is referenced, and it appears in a footer rather than before the type."
      - "No Git operation or ticket lookup occurs."
```
