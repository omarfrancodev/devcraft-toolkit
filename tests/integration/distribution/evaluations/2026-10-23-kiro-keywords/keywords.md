# F001: Kiro activation keywords

## Finding and chosen correction

The PR review identified that Kiro's Power authoring guide marks keywords as
required while the Agent Plugins 1.0 schema treats them as optional. The toolkit's
initial finite contract rejected that field. No actual Kiro load failure had
been established, so this record does not claim to repair an observed runtime
failure.

The revised contract adopts root activation metadata: git, commit, report and
validation. The validator accepts non-empty arrays of non-empty strings and
reports distribution-keywords for missing/empty/malformed values. Unknown or
component-override fields remain rejected. The Claude compatibility manifest,
shared identity/version, marketplace sources, seven skills and catalog remain
unchanged. No template or App is added.

## Regression observations

Before changing the validator, three focused tests failed (ten assertions,
including eight invalid-input subcases). A valid keywords array produced
distribution-metadata, missing keywords was accepted, and malformed keywords
had no dedicated diagnostic.

After the correction, all 21 distribution tests passed against real temporary
packages. The accepted-keywords case supplies a valid different non-empty list;
it does not mirror the manifest's exact tags. Negative cases include missing
keywords, null, an empty array, scalar/object values, numbers and empty strings.
This proves the finite local contract, not the upstream native loader.

## Final local verification

The full suite discovered 78 tests: 77 passed and one Windows symlink privilege
case was skipped. Both repository/distribution validators, 192 local Markdown
file/anchor links and git diff --check passed. No real user installation was
modified. Native activation is not established by these checks.

## Native boundary

The historical b05a8c4/218aea8 remote acquisition and managed-resource probes
predate this metadata correction and remain historical evidence. They do not
establish native acceptance of the revised root manifest. Kiro IDE/CLI loading,
keyword trigger matching, model resource reads and active scope remain pending
because no safely isolated authenticated Kiro session was available. Task 4
Step 3 remains open. Future execution follows
[NATIVE-KIRO-KEYWORDS](../../scenarios/native-loading.md#native-kiro-keywords-corrected-power-activation).

Official sources consulted 2026-10-23:
[Kiro required fields](https://kiro.dev/docs/powers/create/) and
[portable schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json).
