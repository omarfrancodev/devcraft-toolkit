# Path-specific filter applicability evaluation

Date: 2026-10-31. Owner: `git-analyze-changes`.

## Method

Codex desktop dispatched five fresh-context baseline actors and five different
fresh-context candidate actors, each using `gpt-6.1-sol` at medium effort.
Each read the complete analyzer entry/reference and its selected context
instruction. The [fact record](replay-facts.json) captures inputs and candidate
resource hashes. Actors received the same five cases and were forbidden to
inspect unrelated source, execute Git, mutate files, use network or delegate.
No patches were supplied; decisions must be conditional rather than claims of
completed collection. These are manually loaded instruction replays, not native
plugin activation, live LFS execution or a statistical reliability estimate.

This is a regression evaluation: the control loaded the previous instructions
at the recorded source commit, without the candidate applicability recipe.
It is not a claim that a skill-free assistant was tested. Behavioral RED is the
unnecessary limitation of safe paths under the old rule; the real Git controls
below characterize command behavior independently of agent decisions.

## Baseline (before instruction edits)

All five controls returned `limited` for A and B and suppressed worktree
comparison even though the selected README had no applicable filter. For C,
they also suppressed the safe README comparison together with the filtered
binary. Their D/E conservative handling was correct baseline behavior, not a
failure. Their cited cause was the unconditional configured-command gate.

Retained verbatim excerpts:

| Sample | Excerpt | Observed failure |
| --- | --- | --- |
| 1 | “Aunque `README.md` no tenga filtro efectivo, los comandos globales no vacíos activan la puerta conservadora.” | Unused registration limits A. |
| 2 | “los atributos de cada ruta no levantan esa barrera.” | Excluded-path registration limits B. |
| 3 | “Que README no use filtros no elimina la puerta global” | No selected-path distinction in A. |
| 4 | “No depende de que el filtro resulte aplicable a los archivos seleccionados ni de que provenga del ámbito system.” | Registration rather than applicability is decisive. |
| 5 | “la regla actual aplica el bloqueo a todo el worktree” | No selected-path recovery. |

## Candidate

All five candidate outputs were read manually. Each permitted protected
literal README comparison for A/B; retained safe README evidence alongside
limited filtered-binary coverage for C; kept unknown applicability limited for
D; and discarded invalidated composition with at most one protected retry for
E. Each deferred the context dependency's broad status until its complete
potential scan was proven safe, rejected filter/configuration bypass, and
withheld an observed `analyzed` result until actual patches and stable guards
exist. Differences were presentation and conditional wording, not decisions.

Retained verbatim excerpts:

| Sample | Excerpt | Assessment |
| --- | --- | --- |
| 1 | “LFS registrado pero sin aplicación no bloquea.” | A recovery, conditional coverage. |
| 2 | “El filtro de una ruta excluida no limita README.” | A/B recovery, conditional outcome. |
| 3 | “No es automáticamente `blocked`, porque quedan lecturas seguras.” | D retains independent evidence. |
| 4 | “Su LFS no limita la cobertura seleccionada.” | B recovery without broad status. |
| 5 | “A changed decision or source invalidates the combined evidence: discard it, retry the protected collection at most once or return limited.” | E invalidation understood. |

## Independent review refinement

A fresh reviewer identified that Git serializes `-filter` and `filter=unset`
identically, and likewise `!filter` and `filter=unspecified`. A real fixture
confirmed both collisions. The recipe now checks winning commands for those
possible driver names before interpreting the output as absence; ambiguous
executable conversions remain limited. A separate real-Git regression control
pins the serialization and first verifies that metadata-only inspection preserves
repository state. A deliberate positive control then runs an inspected clean-only
fixture helper, expecting only its local sentinel write, proving that both
colliding names can actually execute a driver. No installed LFS program runs. The initial five candidate replays preceded this refinement; final
edge replay and verification results are recorded separately below.

## Real Git controls and limitations

The owner integration suite exercises real temporary Git repositories with
sentinel conversion commands that would create `filter-sentinel` if executed.
The new controls cover unused inherited registration, a dirty filtered sibling,
mixed safe/filtered selections, `info/attributes`, external attributes, index
fallback, nested precedence, empty higher-precedence command overrides,
commandless named drivers, NUL/literal untracked paths and changed attributes
with unchanged HEAD/index. Repository snapshots verify preservation around
protected reads; the separately identified reserved-word positive control
intentionally creates its owned sentinel after the preservation assertion. Fixture setup performs owned local writes before observation;
no actual installed LFS program, remote server or authentication is exercised.

The full project suite and structural validators are recorded separately in
[verification.md](verification.md). Existing historical evaluations are retained
as evidence of the instructions they tested, not silently rewritten as current
behavior. Native plugin loading/invocation and multi-client scope/lifecycle
validation remain open.

## Final edge replay

One additional fresh-context actor read the final analyzer/context resources
and answered A-E plus five cases: ambiguous executable `unset`, ambiguous
executable `unspecified`, a commandless named driver, an empty winning process
command overriding an inherited command, and staged-only inspection with unknown
worktree attributes. Each decision matched the final recipe. Ambiguous names
stayed limited; absent/empty effective conversions allowed exact protected
comparison; staged-only evidence remained available. No commands or writes
were performed by this actor.

Retained excerpts: “Que sea un `echo` inspeccionado no lo exime”; “La definición
inferior no vacía queda sobreescrita y no constituye un comando efectivo”; “La
incertidumbre de filtros, por sí sola, no limita una cobertura staged completa.”
These conclusions describe the replay, not native runtime activation.

A separate [local application](local-application.json) manually followed the
final source recipe on one selected modified project file with the actual
system LFS commands registered. It collected a protected exact-path patch with
unchanged HEAD/index/selected-content/configuration/attribute observations.
The application did not update the installed plugin or its cache.
