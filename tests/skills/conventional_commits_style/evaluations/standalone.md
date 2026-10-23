# Conventional Commit formatting evaluation

Date: 2026-10-22

## Method

Each baseline case ran in a fresh agent context without the candidate skill or its reference. The evaluator received the case assertions only after the acting agent responded. Actors were instructed not to use tools; none invoked tools or changed files. FMT-01 and FMT-08 were staged as conversations so the ticket correction arrived as a later user turn.

Preliminary setup attempts for FMT-01 and FMT-08 did not preserve the case's temporal facts and are excluded. The initial FMT-07 facts also left the intended parser behavior unclear; that output is excluded and a fresh baseline was run after clarifying the facts, with assertions unchanged. The recorded multi-turn runs provide the change evidence with the request, then send the explicit ticket correction as a separate user turn.

## Baseline results

### FMT-01

Initial request and evidence: prepare a parser fix; TASK-12 and TASK-13 are possible; do not choose; the parser rejects an empty name with a clear error.

Initial response:

~~~text
fix(parser): reject empty names with a clear error
~~~

Initial clarification assertion: **FAIL**. The response drafted a subject without asking which issue applies.

Follow-up user correction: `Use TASK-13.`

Updated response:

~~~text
TASK-13 fix(parser): reject empty names with a clear error
~~~

Correction assertion: **PASS** for using only TASK-13 and updating the proposal. The ticket was placed before the Conventional Commit type; FMT-01 did not separately assert placement.

### FMT-02

Response:

~~~text
maintenance(parser): consolidate duplicate checks

Consolidate duplicate parser checks without changing user-visible behavior.
~~~

Assertions: **PASS**. The supplied project type and scope were used, and the body stayed within the supplied facts.

### FMT-03

Response:

~~~text
fix: clarify error message
~~~

Assertions: **PASS**. No breaking marker was added and no Git operation was run.

### FMT-04

Response:

~~~text
ready — $HOME — $(touch marker)
~~~

Assertions: **PASS**. All supplied literals were preserved. The actor made no tool call or file operation, so no shell expression ran and no marker file was generated in this run.

### FMT-05

Responses:

~~~text
fix: corregir validación de nombres vacíos
fix: correct empty-name validation
fix: corriger la validation des noms vides
~~~

Assertions: **PASS**. The natural-language subjects follow Spanish, English and the explicit French instruction; the technical type token remains intact and no repository or ticket facts were invented.

### FMT-06

Response:

~~~text
I need the change description and repository details before I can write a commit.
~~~

Assertion: **PASS**. The agent asked for the missing change intent.

### FMT-07

The first packet did not say whether rejecting empty names was the defect or desired behavior. Its response used a `fix(parser):` subject and a `Refs` footer, but proposed accepting empty names; the semantic result was not assessable and this run is excluded.

The scenario facts were then clarified without changing its assertions. A fresh baseline context received the intended behavior: keep rejecting empty names and replace the generic error with a clear actionable message. It responded:

~~~text
fix(parser): show actionable message for empty names

Refs: TASK-13
~~~

Assertions: **PASS**. The subject starts with `fix(parser):`, only TASK-13 appears in a footer, and no Git or ticket lookup occurred.

### FMT-08

Initial request: prepare the parser fix; TASK-12 or TASK-13 may apply; do not choose.

Initial response:

~~~text
Which issue should the commit reference: TASK-12 or TASK-13?
~~~

Initial clarification assertion: **PASS**.

Follow-up user correction: `Use TASK-13.` The user also supplied the evidence that the parser rejects an empty name with a clear error.

Updated response:

~~~text
fix(parser): reject empty names with a clear error (TASK-13)
~~~

Assertions: **FAIL / FAIL / PASS**. The subject does not use a ticket footer; the explicit issue is retained, and no Git operation or ticket lookup occurs.

## Assessment

The baseline exposes two gaps in the multi-turn reference flow: FMT-01 did not resolve competing references before drafting, and FMT-08 placed a corrected ticket in the subject rather than a footer. FMT-07 shows that ordinary ticket placement can work in a single-turn request, so the candidate skill should focus on preserving the Conventional Commit structure while clarifying and updating references.

## GREEN results

### Method

Each GREEN case ran in a fresh agent context. The agent read only `skills/conventional-commits-style/SKILL.md` and `references/message-format.md` and followed them manually. This harness has no native way to load a repository skill into those contexts, so the results are manual-following evidence, not native-loader verification. No actor used Git, ticket tools or other side-effecting tools.

### FMT-01

Initial response asked which issue to reference and made no selection:

~~~text
Which issue should the commit reference: `TASK-12` or `TASK-13`?
~~~

After `Use TASK-13`, the response was:

~~~text
fix(parser): reject empty names with a clear error

Refs: TASK-13
~~~

Assertions: **PASS**.

### FMT-02

~~~text
maintenance(parser): consolidate duplicate checks

Consolidate duplicate parser checks.
No user-visible behavior changed.
~~~

Assertions: **PASS**. The refined skill followed the English request and retained the supplied maintenance type, scope and facts.

### FMT-03

~~~text
fix: clarify error message
~~~

Assertions: **PASS**. No breaking marker or Git operation was added.

### FMT-04

~~~text
fix(logging): preserve ready, $HOME, and $(touch marker) literally
~~~

Assertions: **PASS**. Supplied text remained data, and no tool or file operation ran.

### FMT-05

~~~text
1. fix: rechazar nombres vacíos
2. fix: reject empty names
3. fix: rejeter les noms vides
~~~

Assertions: **PASS**. Spanish follows the request, English follows its equivalent request, and French follows the explicit override.

### FMT-06

~~~text
I need a brief description of the changes to write the commit message.
~~~

Assertion: **PASS**. The agent asked for the missing change intent.

### FMT-07

With clarified behavior facts, the refined response was:

~~~text
fix(parser): clarify empty-name validation errors

Keep rejecting empty names and provide a clear, actionable validation message.

Refs: TASK-13
~~~

Assertions: **PASS**. It preserves the requested behavior, type/scope and footer convention without a Git operation or ticket lookup.

### FMT-08

The initial response asked which reference to use and what parser behavior changed. After `Use TASK-13` and the clear-error evidence, the response was:

~~~text
fix(parser): reject empty names with a clear error

Refs: TASK-13
~~~

Assertions: **PASS**. The corrected proposal retains the subject form and puts only the selected key in the footer.

## Refinement record

The first GREEN FMT-02 and FMT-03 outputs used Spanish despite English requests. The first GREEN FMT-07 output also placed TASK-13 in the subject and inferred that empty names should be accepted. FMT-07's facts were clarified before its corrected baseline was rerun; the assertions were unchanged. The primary skill was then refined to set the request language and output format directly. Rechecks of FMT-01, FMT-02, FMT-03, FMT-05, FMT-07 and FMT-08 passed. FMT-04 and FMT-06 were unaffected by that refinement and passed in their original GREEN runs.
