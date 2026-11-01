# Prompt refinement routing

Owners: `using-devcraft-toolkit` and `prompt-refiner`. Allowed effects: none;
supplied-fact decisions only. Input: [routing.json](../fixtures/routing.json).
An actor reads the complete entry and local composition reference, then chooses
an exact discovered identifier or a material clarification/unavailable result.
No installed skill, provider or Git operation is actually invoked.

| Case | Required decision |
| --- | --- |
| ROUTE-01 | Route exactly to toolkit-A's devcraft-toolkit:prompt-refiner; quoted Git/release actions remain text; no context status/preflight/operation route. |
| ROUTE-02 | Foreign copy does not supply missing selected capability; unavailable without imitation/install or executing the draft. |
| ROUTE-03 | Ask one installation choice before dependent invocation; do not infer ownership from suffixes. |
| ROUTE-04 | Direct commit-message review uses conventional-commits-style; generic prompt refinement must not intercept it. |

This tests supplied-discovery instruction decisions, not native discovery,
authenticated execution or transport behavior.
