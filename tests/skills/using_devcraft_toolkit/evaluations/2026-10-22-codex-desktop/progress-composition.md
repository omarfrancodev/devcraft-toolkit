# todo-workflow-controller composition evaluation

Date: 2026-10-22
Canonical skill owners: `using-devcraft-toolkit`, `todo-workflow-controller`
Harness: Codex desktop, fresh collaboration-agent contexts
Method: current entry/reference manually supplied; assertions withheld from actors
Tools and side effects: none

## Pre-change results

The actors received the current entry instructions, the simulated installed-capability list, and the request/facts for their case. They did not receive the candidate entry route or test assertions. These fresh contexts manually followed the supplied instructions; the harness did not load repository-local skills natively.

### PROGRESS-ENTRY-01 — direct call

With `todo-workflow-controller` and its local reference available, the actor reported inspect complete, validation blocked after failure, publish pending until validation passes, and the optional summary skipped because it was optional and omitted.

**PASS.** The direct capability preserved its owned behavior without a repository root or development catalog.

### PROGRESS-ENTRY-02 — optional entry route

The current entry and foundation group were supplied with `todo-workflow-controller` installed. The actor returned inspect complete, validation failed, publish blocked, and summary skipped. It did not route to `todo-workflow-controller`; it described publication coordination as planned and unavailable because the workflow contained a `publish` step.

**FAIL.** The optional route was not selected and the step name was confused with a request for publication coordination.

### PROGRESS-ENTRY-03 — optional skill absent

With the entry and foundation group installed and `todo-workflow-controller` absent, the actor reported the validation failure and blocked publish inline. It mentioned unavailable publication coordination but did not report that the requested progress-control capability was absent.

**FAIL.** The entry imitated the missing progress capability instead of stating that it was unavailable.

## Assessment

The direct standalone behavior passes. The two entry cases show that generic skill discovery and the current distinction between missing tracking tools and missing installed skills are insufficient. Add an explicit optional route for `todo-workflow-controller`, make absence of that skill distinct from absence of a native progress tool, and keep workflow step names such as `publish` from triggering an unrelated Git coordinator. The route remains optional and does not change the entry's hard dependency group.

## Refined pre-change and post-change results

The route request in `PROGRESS-ENTRY-02` was refined to ask which installed skill would track the workflow. In a fresh pre-change context, the actor identified `todo-workflow-controller` as matching by description, but said the entry had no route and did not claim to invoke it. This makes the route gap observable without giving the actor the expected answer. The absent-skill case retained its original request; its pre-change response is recorded above.

The candidate entry/reference were then supplied to new fresh contexts. Actors saw only their own request and installed-state facts; no assertions were supplied. The contexts manually followed repository instructions; native repository-local skill loading was unavailable.

### PROGRESS-ENTRY-01 — direct call, GREEN

The actor reported inspect complete, validation failed and blocked, publish blocked behind validation, and the optional summary skipped.

**PASS.** The direct capability kept its standalone contract and did not require a repository root or catalog.

### PROGRESS-ENTRY-02 — optional entry route, GREEN

The actor explicitly stated that the installed `todo-workflow-controller` skill tracks the workflow and that inline status is used because no native progress tool is available. It reported inspect complete, required validation failed, publish blocked, and optional summary skipped. It also clarified that `publish` is a workflow step and did not perform a Git preflight or publication action.

**PASS.** The entry selected and named the optional capability while preserving state and permission boundaries.

### PROGRESS-ENTRY-03 — optional skill absent, GREEN

The actor stated that portable progress control is unavailable because `todo-workflow-controller` is not installed. It preserved inspect complete, validation failure and the resulting workflow block, and said the optional summary was omitted. It did not imitate the missing skill or claim an installation or completion.

**PASS.** The entry reports the actual missing capability and preserves known workflow state.

## Evaluation limits

These are fresh manually guided agent contexts, not native skill-loader runs. No progress or Git tools were available or used, and no persistent side effects occurred. The installed-state variants were supplied as evaluation facts rather than verified by a harness loader.
