# Behavioral scenario protocol

Scenarios evaluate what a skill does when followed in an actual assistant harness. Structural tests do not establish behavior or harness compatibility.

For each run, record:

- Date, canonical skill owner(s), assistant harness, and observed version when available.
- The user request and the exact fixture state before invocation.
- The evidence the assistant used, the decision it returned, and whether repository snapshots changed.
- Missing tools, unsupported fixture features, and any behavior that could not be observed.

Run only the scenario's requested, read-only operation. Use temporary fixtures, never a developer repository. Keep retained skill-only notes in `tests/skills/<skill_package>/evaluations/<run>/` and cross-skill notes in `tests/integration/evaluations/<run>/`. State `limited` when an input or harness capability was unavailable; do not turn an unrun scenario into a pass. Follow the user's language while preserving canonical skill names, commands, and schema keys.
