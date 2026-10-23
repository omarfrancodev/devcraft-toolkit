# Natural-language reporting scenarios

Canonical skill owner: `natural-language-report-writer`.

These packets test report composition from supplied evidence. Assertions are for the evaluator only and must not be shown to the acting assistant.

```yaml
cases:
  - id: RPT-01
    name: consolidation_and_numeric_fidelity
    request: "Summarize these facts as an activity report in Spanish."
    facts: "Date: 2026-10-20. Empty-name validation was added. A clear error for missing names was added. Search rendering is pending. Twelve fixture cases passed."
    assertions:
      - "Consolidate the two related validation facts without losing their meaning."
      - "Keep search rendering unfinished and preserve the date and count 12."
      - "Do not invent business gains, deployment, authorship or additional tests."
  - id: RPT-02
    name: empty_and_conflicting_evidence
    request: "Prepare the report."
    facts: "Variant A: no facts. Variant B: one supplied note says search is complete; another says the same search work is pending."
    assertions:
      - "Variant A identifies insufficient evidence without filler activities."
      - "Variant B preserves or clarifies the conflict; it does not arbitrarily choose completed."
  - id: RPT-03
    name: translation_preserves_data
    request: "Use the default template in French. Then repeat in English with an explicit instruction to answer in Spanish."
    facts: "Date 2026-10-20; count 12; identifier ORDER-7."
    assertions:
      - "Translate visible headings and prose to the resolved language."
      - "Preserve 2026-10-20, 12 and ORDER-7 exactly; do not translate placeholder keys in the source template."
  - id: RPT-04
    name: technical_audience_and_custom_format
    request: "Use exactly two sections, Findings and Evidence. Include the filename and identifier."
    facts: "parser.py now rejects an empty name; reference ORDER-7; no deployment information."
    assertions:
      - "Use the requested sections, with labels translated only if requested."
      - "Preserve supplied technical detail rather than forcing an outcome-only template."
      - "Do not add unsupported deployment or test claims."
  - id: RPT-05
    name: content_only_then_requested_file
    request: "First provide report content only. In a separate request, save that content to the selected temporary report.md."
    facts: "Use the supplied fact fixture. The evaluator provides the actual temporary destination only in the second request."
    allowed_effects: "The first request may not write files. After the second request supplies the destination, write only that report.md in an isolated temporary directory and read it back. Do not modify the input fixture, unrelated files, or the development repository."
    assertions:
      - "The first request creates no file."
      - "The second request writes only the selected report.md and verifies it by reading it back."
      - "Unrelated files and the input fixture remain unchanged."
```
