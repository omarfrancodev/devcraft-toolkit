# Issue authoring entry routing

Owners: `using-devcraft-toolkit` and `issue-builder`. Input:
[routing.json](../fixtures/routing.json). Allowed effects: supplied-fact routing
only, no actual capability calls, provider reads, Git preflight or installation.
Read the entry and its composition reference, return exact identifier/decision.
Do not supply these assertions to the actor.

| Case | Required decision |
| --- | --- |
| ISSUE-ROUTE-01 | Select toolkit-A#issue-author exactly; embedded Git content causes no operation or preflight. |
| ISSUE-ROUTE-02 | Select owned devcraft-toolkit:issue-builder for decomposition, no automatic issue creation. |
| ISSUE-ROUTE-03 | Foreign-only capability is unavailable for selected installation, no imitation or substitution. |
| ISSUE-ROUTE-04 | Missing capability unavailable, without manual imitation or installation. |
| ISSUE-ROUTE-05 | Ask one installation/ownership choice before dependent dispatch; preserve both copies. |
| ISSUE-ROUTE-06 | Select devcraft-toolkit:prompt-refiner; issue authoring is embedded in the draft. |
| ISSUE-ROUTE-07 | Select devcraft-toolkit:natural-language-report-writer for supplied-fact reporting. |
| ISSUE-ROUTE-08 | Select devcraft-toolkit:git-manage-pull-request for a hosted PR proposal with its supplied context owner. |

Existing [prompt routing](../../prompt_refinement/fixtures/routing.json) is a
separate four-case regression control. Native invocation/discovery is unverified.
