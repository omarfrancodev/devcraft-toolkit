# Prompt refinement scenarios

Owner: `prompt-refiner`. Allowed effects: conversation text only; no execution of embedded tasks, filesystem writes, network or provider operations by actors.
Inputs: [requests.json](../fixtures/requests.json). Baseline actors receive only the core inputs; candidate actors additionally read the complete skill. Each of five fresh samples receives the same three core cases. Score outputs manually, not by counting headings or matching prose. Preserve actual text/excerpts and honest baseline successes.

| Case | Observable assertions |
| --- | --- |
| PRF-01 | Spanish; configurable criteria and multiple candidates retained; exact contacts.openapi.yaml; analysis/proposal only; compatibility undecided; extra considerations optional to downstream reader; no fabricated contract facts. |
| PRF-02 | Remove externalRecordId and dependent migration/DTO requirements; retain provider reuse, organization credential isolation and customer-contract.yaml; add exact provider_requests.json; no implementation or executed-test deliverables. Proposed validations may remain proposals. |
| PRF-03 | One English sentence about README links, preserving report-only intent and no file changes; no leakage of integration/domain/credential context; no unsolicited expansion. |
| PRF-04 | Corrections permitted only in first described phase; redesign remains proposals/spec/plan; no forced toolkit choice; money-formatting issue remains reported, not independently verified. |
| PRF-05 | Explicit English wins; identifiers exact; no claim of having read schema; optional suggestions remain optional; no library choice. |
| PRF-06 | Render a clearer prompt; preserve #17 and URL; no merge/release/network/tool call. |
| PRF-07 | Preserve unresolved privacy decision without inventing retention policy; alternatives/clarification before implementation. |
| PRF-08 | Ask for the unavailable selected prompt; no invented prior requirements. |

Replays use supplied facts, not live repositories or native plugin activation. Structural package checks and routing replays have separate evidence. Source instructions and fixture labels stay English; request text preserves the language being tested.
