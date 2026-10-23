# todo-workflow-controller standalone evaluation

Date: 2026-10-22
Canonical owner: `todo-workflow-controller`
Harness: Codex desktop, fresh collaboration-agent contexts
Mode: baseline; candidate skill and assertions were not supplied to actors
Tools: none exposed to the actors; no repository or external side effects

## Method and scope

Each actor received only a case request and supplied facts. A separate assessment compared the response with the named assertions. The evaluator contexts were fresh Codex subagents, so this records instruction-following behavior in this harness; it does not test native loading of the repository-local skill. PRG-02 could exercise the absent-tracker fallback only. No tracker tool was exposed that could be made to fail mid-run.

## PRG-01 — required_gate_and_optional_skip — baseline

Observed response: “Tracked: Inspect is complete. Validation failed, so publish is blocked. The optional summary was skipped.” No tools or side effects.

- Required validation remains uncompleted with its failure evidence, and dependent publish is blocked: **pass**.
- Optional summary is skipped; its optional status was supplied as the reason: **pass**.
- Workflow is not reported complete under deadline pressure: **pass**.

## PRG-02 — missing_or_failed_tool — baseline

Observed response: “The task tracker is unavailable, so I’ll keep progress visible here: the material validation blocker remains open, and the independent safe task can proceed without depending on it. Tools used: none.” No files, scheduler or other side effects.

- Material blocker is retained inline: **pass**.
- Independent work is not stopped because tracking is unavailable: **pass**.
- No extra artifact is created: **pass**.
- Mid-run native-tool failure variant: **limited**, because this harness exposed no tracker to fail.

## PRG-03 — unanswered_decision_and_changed_requirement — baseline

Observed responses: the actor asked for the target choice; after one day of silence it kept the step pending; after the user removed the optional CSV version, it recorded that change while leaving the target choice pending. No tools or side effects.

- Silence and elapsed time do not resolve the target: **pass**.
- The optional CSV change is recorded without claiming it was executed or verifying the still-pending target: **pass**.

## PRG-04 — independent_and_parallel_branches — baseline

An initial exploratory packet described B as ready but did not state its start status as explicitly as the final packet. The response said B could proceed and, in the supplied parallel variant, reported A waiting and B progressing. This was not enough to establish whether a task had actually started, so the scenario was clarified to state B's observed status directly.

With the final packet, the actor reported: “A is blocked because it needs a missing input. B is authorized, independent, and ready, but hasn’t started yet. B can proceed while A waits.” For the separate variant: “A is blocked on the missing input, while B is in progress. B can continue independently; A can resume once the input is available.” No agents or tools were used.

- Initial snapshot distinguishes ready from in progress and allows independent B to proceed: **pass**.
- Parallel variant accurately reports A blocked and B in progress without manufacturing parallel work: **pass**.

## PRG-05 — handoff_and_language — baseline

Observed Spanish response: “El marcador general del tracker indica `completed`, pero el handoff actual aún no está listo para terminar: `INSPECT=completed`; `VALIDATE=pending` (requerido y no ejecutado); `TARGET=decision_pending`. Falta ejecutar `VALIDATE` y resolver `TARGET`.” The English follow-up preserved the same identifiers and values. No tools or side effects.

- Supplied step evidence is preserved across the handoff: **pass**.
- Natural-language status switches from Spanish to English while identifiers and values remain exact: **pass**.
- The contradictory overall `completed` label does not override incomplete required evidence: **pass**.

## Assessment

The final baseline packet passed all named assertions; it produced no valid RED result. The earlier PRG-04 exploratory response was ambiguous rather than sufficient evidence of a state error, so the final packet makes observed start status explicit. The skill remains justified as a reusable, tool-independent progress contract for the toolkit's intended multi-harness use, but this evaluation does not establish a behavior improvement over the baseline. Native skill loading, other harnesses and actual mid-run tracker failure remain untested.

GREEN observations will be added here after the candidate files are written.

## GREEN method

Date: 2026-10-22. Each case used a fresh Codex collaboration-agent context. Actors received the candidate skill and state reference as text, not through a native skill loader; they saw only their own request and facts, not assertions or baseline notes. No progress tools were available. These are manual instruction-following results, not native installation tests.

## PRG-01 — required_gate_and_optional_skip — GREEN

Observed response:

> Inspect — completed.
> Validate — blocked; the required validation failed.
> Publish — blocked until validation passes.
> Optional summary — skipped; omitted.

All assertions: **pass**. The required failure remains incomplete, publish stays blocked, and the optional omission is shown as skipped. No tools or side effects.

## PRG-02 — missing_or_failed_tool — GREEN

Observed response: “Inline status (no progress tracker available): Validation: blocked — the material blocker remains; required validation is incomplete. Independent safe task: pending — ready to proceed, but not yet started.”

All exercised assertions: **pass**. The blocker is retained and independent work remains eligible without being mislabeled as started. No files or schedules. Mid-run native-tool failure remains **limited** because no tracker was exposed.

## PRG-03 — unanswered_decision_and_changed_requirement — GREEN

Observed response: target choice remains `pending` and the actor asks for the explicit choice; the report remains pending on that choice; the optional CSV version is `skipped` because the user removed it.

All assertions: **pass**. The target stays unanswered and the removed requirement is recorded as skipped without claiming execution. No tools or side effects.

## PRG-04 — independent_and_parallel_branches — GREEN

Observed response: “Current snapshot: A is blocked by the missing input. B is pending: it’s authorized and ready, but hasn’t started. Separate variant: A is blocked by the missing input. B is in_progress.”

All assertions: **pass**. Readiness remains distinct from actual start; the observed parallel variant is represented accurately. No tools or side effects.

## PRG-05 — handoff_and_language — GREEN

Observed response preserved `INSPECT=completed`, `VALIDATE=pending` and `TARGET=decision_pending` in both a Spanish status and its English follow-up. It explicitly stated that the overall `completed` label did not establish completion and named the missing validation and decision.

All assertions: **pass**. No tools or side effects.

## Result

All five manual GREEN cases passed. The baseline also passed the final packets, so no behavior improvement is claimed. The evidence supports that the instructions are internally usable in this fresh-context evaluation, while native skill loading, other harnesses and mid-run tracker failure remain unverified.
