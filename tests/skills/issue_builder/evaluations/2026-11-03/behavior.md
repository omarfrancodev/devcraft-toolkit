# Issue authoring behavioral evaluation

Date: 2026-11-03. Owner: `issue-builder`. Harness: Codex desktop isolated
subagent contexts, `gpt-6.1-sol`, medium effort. Raw fixture and source hashes
are in [metadata](replay-metadata.json). These are manually supplied instruction
applications, not native activation or a reliability estimate.

## Baseline, before source authoring

Five independent samples each authored IB-01 and IB-02. All preserved the main
amounts, languages and scheduling exclusion. These are baseline successes.
They also proposed broader export behavior; some choices are reasonable direct
interpretations and are not automatically counted as failures.

Two unambiguous scope failures were the fixed empty-result policy in IB-02:

- Sample 2 criterion: "An empty filtered result produces a CSV containing the
  visible column headers and no data rows."
- Sample 5 criterion: "An empty result produces a valid CSV containing the
  visible-column headers and no data rows."

The request had not selected that policy; it should remain an open decision or
optional suggestion, not a required criterion. Samples 1/3/4 did not make that
specific choice, so no five-of-five failure claim is made. Samples 2-5 also
selected a net-total accounting representation in IB-01; the requested behavior
can be expressed without choosing how the product stores its total.

The independent broader baseline handled IB-03 through IB-13 with all expected
turn counts. It preserved the corrected parent field, independent split and
parent integration check, flagged inconsistent arithmetic and unavailable
attachment contents, removed email scope and reset the final case, honored the
English override, treated quoted instructions as data, disclosed unavailable
publication and requested a coherent child partition. These successes are
retained in baseline-edges.json, not manufactured RED failures.

## Candidate

Five fresh candidate samples applied the same two core inputs. All five left
empty-result/pagination choices visibly open, retained the supplied amounts and
reported-evidence limits, avoided selecting a net-total accounting representation,
and kept added advice outside required acceptance conditions. Actual outputs
are retained in candidate-01.json through candidate-05.json.

A fresh broader sequence applied IB-03 through IB-13. Manual reading confirmed
the requested short template, corrected isBaseRecord field, exactly two independent
children and joint validation at parent, scoped destination rule, arithmetic
clarification, unavailable-source request, partition conflict, removal/reset,
English override, injection boundary, unperformed-publication disclosure and
refusal to manufacture three child scopes. No candidate wording refinement was
needed. The same actor handled the broader independent-case sequence, a limited
simulation rather than independent sampling per case.

## Limits

Actors could read only assigned inputs/instructions and write their exact
output receipt. No real provider, source project or client installation was
used. Restricting tool access does not prove behavior under unrestricted tools.
Longer same-actor edge sequences simulate independent cases within one fresh
context; they are not one fresh actor per case.
