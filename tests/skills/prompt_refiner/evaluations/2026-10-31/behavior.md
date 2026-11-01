# Prompt refinement behavioral evaluation

Date: 2026-10-31. Owner: `prompt-refiner`. Harness: Codex desktop fresh isolated
contexts, `gpt-6.1-sol`, medium effort. [Inputs](../../fixtures/requests.json)
and [resource hashes/sample counts](replay-metadata.json) are retained locally.
Actors returned actual rewritten prompts, not answers about intended rules.
They could read assigned text only; no source project was attached to the
resource names and no embedded work was executed. These are manually loaded
instruction evaluations, not native activation or a reliability estimate.

## Baseline: five fresh samples before source authoring

Each sample handled the same three core cases without candidate instructions.
All preserved the resource names, analysis-only restriction, provider/organization
constraint and independent one-sentence English reset. Removing the field also
removed dependent implementation deliverables; samples using an explicit negative
exclusion were accepted. These are baseline successes, not claimed failures.

All five nevertheless expanded mandatory work without labeling additions as
optional. In PRF-01, examples included validation planning and migration options;
PRF-02 commonly acquired a new implementation/validation plan. The gap is against
the selected refinement contract, rather than a claim that ordinary assistants
cannot rewrite prompts. No skill-free execution-safety effect is inferred from
the harness's tool restrictions.

Retained baseline excerpts:

| Sample | Verbatim excerpt | Observed issue |
| --- | --- | --- |
| 1 | “Un plan de implementación y validación para las alternativas propuestas” | Extra validation planning coupled to a required plan. |
| 2 | “un plan de implementación y pruebas” | Added planning scope in revised analysis prompt. |
| 3 | “Un plan de implementación y validación para las alternativas propuestas” | No optional marker for added validation. |
| 4 | “Opciones de compatibilidad y migración” | Migration consideration not labeled optional. |
| 5 | “una propuesta de integración con los pasos necesarios para implementarla y validarla posteriormente” | Future validation added without optional wording. |

## Initial candidate and refinement

Five different actors read the first complete skill. They preserved the baseline
successes and used explicit optional advice, but three PRF-01 samples still added
mandatory validation planning alongside an implementation plan. The issue was
not fixed by labeling only other additions as optional. Examples were candidate
1's “un plan de implementación y validación” and candidate 4's “un plan de
implementación y validación futura”. Candidate 2 and 5 made future validation
explicitly optional in PRF-01.

The source gained a final imperative/deliverable trace: keep equivalent
clarifications, but move added work to the optional part or remove it. A concrete
example distinguishes a requested implementation plan from an additional
validation plan. Analysis-only revisions do not automatically require replacement
implementation/test plans.

## Final core samples

Five new contexts read the refined skill and the identical three core inputs.
Every output was manually inspected. They preserved confirmed requirements,
references, undecided compatibility, analysis-only revisions and the one-sentence
English reset. No final sample made new validation planning mandatory. Samples
2-4 offered optional future validation; samples 1 and 5 omitted that addition.
Neither omission is a failure: enrichment is useful advice, not a required
amount of text. PRF-02 no longer automatically gained a mandatory replacement
implementation/validation plan.

| Sample | Verbatim excerpt | Assessment |
| --- | --- | --- |
| 1 | “Limita el trabajo al análisis y las propuestas” | Revised task stays analysis-only. |
| 2 | “Opcionalmente, propone futuras validaciones del contrato y del comportamiento elegido.” | Optionality visible to downstream reader. |
| 3 | “Opcionalmente, propone cómo validar en el futuro el contrato elegido y su impacto en los consumidores.” | No added mandatory validation. |
| 4 | “Opcionalmente, propone cómo validar el contrato y la compatibilidad cuando se elija una alternativa.” | Future decision remains pending. |
| 5 | “Limita el trabajo a análisis y propuestas; no apliques código, crees migraciones ni ejecutes pruebas.” | No replacement execution/plan mandate. |

## Final edge application

A separate fresh actor handled PRF-04 through PRF-08 with the final skill:

- PRF-04 preserved fixes in the first described phase and proposals-only redesign
  afterward; the money-formatting report remained unverified, without choosing
  ComponentKit as the solution.
- PRF-05 used explicit English and preserved all three identifiers; it wrote
  “which we have not yet reviewed” rather than inventing schema findings.
- PRF-06 returned the refined merge/release prompt as text, preserving the PR
  number and URL. The actor did not merge, publish or query a provider.
- PRF-07 retained the unresolved privacy rule and alternatives before implementation.
- PRF-08 asked for the unavailable prior prompt: “Comparte el texto del prompt
  anterior”. It did not reconstruct a hidden assignment.

Behavioral decisions, package copying and entry ownership routing are different
evidence levels. See [verification.md](verification.md) for actual commands,
results and review limits. Native loading/invocation remains unverified.
