# Natural-language report writer evaluation

Date: 2026-10-22
Canonical skill owner: `natural-language-report-writer`
Harness: Codex desktop; fresh collaboration-agent contexts, version unavailable
Method: each baseline actor received only the user request and supplied facts; no candidate instructions or assertions were shown. RPT-01 through RPT-04 used no tools or file effects. RPT-05 used an isolated operating-system temporary directory, not the development repository.

## Baseline results

### RPT-01 — consolidation and numeric fidelity

The actor returned a Spanish activity report. It combined the two validation facts, rendered the supplied date as “20 de octubre de 2026,” reported twelve fixture cases, and kept search rendering pending. It made no business-impact, deployment, authorship, or additional-test claims.

**PASS.** All assertions hold; the date and count retain their meaning in the requested language.

### RPT-02 — empty and conflicting evidence

For Variant A, the actor said no factual information was supplied and there were no findings or status updates. For Variant B, it stated that the notes conflict and that current search status cannot be determined.

**PASS.** No filler activity was introduced, and neither conflicting status was selected as true.

### RPT-03 — translation preserves data

For the French request, the actor produced French labels and preserved `2026-10-20`, `12`, and `ORDER-7`. For the second request, it returned English labels (`Date`, `Count`, `Identifier`) and appended “Instruction: Answer in Spanish,” while the user had explicitly asked for Spanish output.

**FAIL.** The explicit language override was not applied to the second report. The failure is specific to RPT-03's second variant; the data values remained intact.

### RPT-04 — technical audience and custom format

The actor used exactly the requested headings, `Findings` and `Evidence`, included `parser.py` and `ORDER-7`, and made no deployment claim.

**PASS.** The custom structure and supplied technical evidence were preserved.

### RPT-05 — content only, then requested local file

The first request returned report content only. The evaluator observed that no output file existed; the isolated directory still contained only `report-facts.json` and `unrelated.txt`. In a separate request, the actor saved the report to the selected `report.md` and reported a matching readback. Independent inspection confirmed that the output bytes exactly matched the prior response. Only `report.md` was added; the fixture hash remained `7b383fde0601ee473e59cd547617e8407b6fd3a36c492d6ce8338c7e744a04f4`, and the unrelated-file hash remained `c5d3e37410c775e378293d545b255df091bbec3c2e6eeddb32bae706a4fe9430`.

**PASS.** The first request caused no persistence; the explicit second request wrote and verified only the selected file.

## Baseline assessment

The baseline exposes a concrete language-resolution failure in RPT-03 while meeting the other named behaviors. The independent product need remains a reusable, evidence-bound reporting contract: user language and explicit overrides must resolve reliably, supplied structure and identifiers must survive rendering, and content generation must remain separate from requested local persistence. The candidate skill will address those boundaries without adding automatic data collection or publication.

No repository files or user data were changed by the behavioral actors. The RPT-05 temporary fixture was isolated from the development repository.
## GREEN results

### RPT-01 — consolidation and numeric fidelity

The fresh actor returned a Spanish report with translated template headings. It grouped the two name-validation changes, retained 2026-10-20 and the value 12, and marked search rendering as pending without adding unsupported impact or completion claims.

**PASS.** All three scenario assertions hold.

### RPT-02 — empty and conflicting evidence

For the empty variant, the actor said there was insufficient information and omitted unsupported activities. For the conflicting variant, it retained the conflict and left the resolution/status open.

**PASS.** Both variants preserved the evidence boundary without filler or arbitrary resolution.

### RPT-03 — translation preserves data

The actor produced a French report for the first request and a Spanish report after the explicit Spanish override in the second. The exact values `2026-10-20`, `12`, and `ORDER-7` remained unchanged; the source placeholder keys were not exposed.

**PASS.** Language resolution and data preservation assertions hold for both variants.

### RPT-04 — technical audience and custom format

The actor used exactly `Findings` and `Evidence`, included `parser.py` and `ORDER-7`, and stated that no deployment information was provided.

**PASS.** The requested format and technical details were retained without unsupported deployment or test claims.

### RPT-05 — content only, then requested local file

On the first request, the actor read the fixture and returned:

> # Activity Report — ORDER-7
>
> ## Summary
> On 2026-10-20, empty-name validation and a clear error for missing names were added. Search rendering remains pending.
>
> ## Activities
> - Added empty-name validation.
> - Added a clear error for missing names.
> - Twelve fixture cases passed.
>
> ## Open items
> - Search rendering is pending.

The evaluator confirmed that no `report.md` existed after the first request. On the separate second request, the actor wrote only the selected `report.md`, read the same file back, and reported an exact match. Independent inspection found exactly three files in the evaluation folder: the unchanged fixture, unchanged unrelated file, and selected report. The fixture SHA-256 stayed `21D344078DD1FD4E6386016DE7BF73A19553B48DFCF3DBDE34A0B862CE02FE46`; the unrelated file SHA-256 stayed `194E7C460F519A3107D87413EA97D5571BE05D2D47C25B366C09AFE797025F96`. The saved report content matched the response.

**PASS.** The initial content-only request caused no file effect; the explicit save wrote and verified only the selected path; both other files remained unchanged.

## Final assessment

All five GREEN cases passed when fresh actors manually followed the actual candidate resources. No instruction refinement was needed. Native repository-local skill loading was not available, and the RPT-05 target was an isolated ignored worktree evaluation folder rather than an OS-managed temporary directory; these are harness limits, not claimed coverage. Baseline and GREEN results are behavior evidence, while repository tests remain structural regression checks.
## Repository checks

- `python -m unittest discover -s tests -p "test_*.py" -v`: 57 tests passed; one symlink fixture skipped because Windows denied symlink creation (exit 0).
- `python scripts/validate_repository.py --root .`: passed with `Repository catalog is valid.`
- `git diff --check`: passed with no whitespace errors.
