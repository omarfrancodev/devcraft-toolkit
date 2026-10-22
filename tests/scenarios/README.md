# Behavioral scenario protocol

Scenarios evaluate what a skill does when followed in an actual assistant harness. Structural tests do not establish behavior or harness compatibility.

For each run, record:

- Date, canonical skill owner(s), assistant harness, and observed version when available.
- The user request and the exact fixture state before invocation.
- The evidence the assistant used, the decision it returned, and whether repository snapshots changed.
- Missing tools, unsupported fixture features, and any behavior that could not be observed.

Run only the scenario's requested operation. Scenarios are read-only unless `allowed_effects` names an exact temporary output; use temporary fixtures, never a developer repository. Validation-discovery cases may execute only the exact inspected checks requested by the case, inside its owned temporary project copy; disclose expected artifacts and preserve any unexpected file or state change. Do not run package installation, autofix, network, cleanup, or unrelated commands. For the report-writer file-output case, record the fixture state before and after, write only the selected report file after the explicit save request, read it back, and verify that unrelated files remain unchanged. Keep retained skill-only notes in `tests/skills/<skill_package>/evaluations/<run>/` and cross-skill notes in `tests/integration/evaluations/<run>/`. State `limited` when an input or harness capability was unavailable; do not turn an unrun scenario into a pass. Follow the user's language while preserving canonical skill names, commands, and schema keys.
