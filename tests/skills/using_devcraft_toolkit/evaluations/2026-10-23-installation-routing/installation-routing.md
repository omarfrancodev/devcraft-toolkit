# Installation-aware routing evaluation

Date: 2026-10-23. Method: fresh Codex agent contexts manually following the actual entry and its local reference; synthetic discovery fixtures, simulated invocation records. This is not native skill loading or proof that a client exposes ownership metadata.

Baseline source: dde788a0c3cccd2f14ca33d2257f049834c3adce. Scenarios were defined before entry edits. Each baseline and final packet used a different fresh context; no evaluator read expected assertions. Baseline formatter output was not supplied in packets 02–04, so those observations concern selection and boundaries, not completed capability output.

| Packet | Unchanged-entry baseline | Final instructions |
| --- | --- | --- |
| ROUTE-INSTALL-01 | Selected devcraft-toolkit:conventional-commits-style, Spanish proposal, no Git preflight: pass | Same owned identifier; read formatter and local reference; Spanish proposal: pass |
| ROUTE-INSTALL-02 | Selected foreign-tools:conventional-commits-style: fail | No invocation; reported selected installation's formatter unavailable: pass |
| ROUTE-INSTALL-03 | Selected devcraft-toolkit:conventional-commits-style without a question: fail | No invocation; asked one installation-choice question: pass |
| ROUTE-INSTALL-04 | Selected standalone conventional-commits-style; validation-discovery absent, no substitute: pass | Same standalone identifier; English proposal, missing validation reported: pass |

Observed baseline actions:

- 01: `INVOKE("devcraft-toolkit:conventional-commits-style")`; proposal `fix: validar nombres vacíos`.
- 02: `INVOKE(foreign-tools:conventional-commits-style)`. Evaluator explained: “Current entry and composition route to installed conventional-commits-style without an installation-owner restriction.”
- 03: `INVOKE(devcraft-toolkit:conventional-commits-style)`. Evaluator explained: “Selection based on explicit request to use Devcraft Toolkit and installed namespaced formatter matching that request.”
- 04: `INVOKE(conventional-commits-style)`; “validation-discovery is unavailable in that installation, so I cannot discover validation commands.” No unselected suite identifier invoked.

Observed final responses/actions:

- 01: simulated `INVOKE devcraft-toolkit:conventional-commits-style`; `feat: agregar validación de nombres vacíos`.
- 02: no invocation or imitation. “La capacidad conventional-commits-style no está disponible en la instalación seleccionada de Devcraft Toolkit. La única copia detectada pertenece a foreign-tools, que no está seleccionado para esta solicitud.”
- 03: no invocation. “Hay dos copias del formateador y no está resuelta la instalación que corresponde usar. ¿Cuál eliges: devcraft-toolkit:conventional-commits-style o conventional-commits-style?”
- 04: simulated `INVOKE(conventional-commits-style)`; `feat: add empty-name validation`; “validation-discovery is unavailable in the selected standalone installation, so I couldn’t discover validation commands.”

Final 01 and 04 manually read both formatter files after selecting it; entry/reference paths and skill-local resource paths stayed canonical. No Git preflight, installation, check execution or deliberate repository mutation occurred. Final 01's first read enabled the shell profile and emitted denied cache/log write attempts; subsequent reads disabled profiles. This was not silently counted as native client isolation.

The explicit contract addresses the two observed ownership failures while retaining baseline successes. It adds no runtime catalog/manifest lookup, persistent resolver, dependency installation, or namespace convention. Native registration and activation remain separate checks.

## Existing-behavior regression observations

A separate fresh evaluator read the current entry and four optional skills/local resources. The following twelve requests were independent in-memory runs within that one context, not twelve isolated sessions or native activations.

| Run | Observed selection/result |
| --- | --- |
| R1 direct formatter | conventional-commits-style; `feat: add empty-name validation` |
| R2 routed Spanish formatter | conventional-commits-style; `feat: agregar validación de nombres vacíos` |
| R3 absent formatter | Reported unavailable; no proposal or install |
| R4 progress route | todo-workflow-controller; inspect completed, required validation blocked, dependent publish blocked, optional summary skipped; no Git preflight |
| R5 absent progress | Reported unavailable without tracker imitation |
| R6 supplied-facts report | natural-language-report-writer; Spanish report preserved 2026-10-20, both completed validation/error changes, 12 passed cases and pending search; content only |
| R7 absent writer | Reported unavailable without drafting/file output |
| R8 validation discovery | validation-discovery; identified package.json scripts.check = python check.py pass; status not_run, unverified script effects disclosed |
| R9 absent validation | Reported unavailable without emulation |
| R10 language override | English request with explicit Spanish preference; Spanish Conventional Commit |
| R11 history coordinator | Reported git-activity-report planned/unavailable; no Git history inspection or report substitution |
| R12 unrelated Python | No entry invocation; explained 2**3 = 8 |

No commands beyond read-only instruction reads, file writes, checks, installation or Git operations were performed by the regression evaluator. These twelve observations passed their existing boundary assertions; they are not evidence of tracker failure injection or native clients.

Automated verification: 75 tests discovered, 74 passed, one Windows symlink-privilege skip. Repository and distribution validators passed; native loading remains unverified.
