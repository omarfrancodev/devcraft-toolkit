# Validation discovery composition evaluation

## Run details

- Date: 2026-10-22.
- Owner: `using-devcraft-toolkit`; composed capability: `validation-discovery`.
- Harness: fresh Codex agent contexts; exact requests and installation facts were supplied without the scenario assertions. Repository-local skills could not be natively activated, so GREEN contexts were given the current entry and standalone instructions as resources.
- The scenario is discover-only. No project command may run, no files may be modified, and no Git preflight is requested.

## Baseline observations

### VALIDATION-ENTRY-01 — `direct_call`

> The supplied package.json fact identifies a `check` script whose command is `python check.py pass`. The project root and package manager invocation are unavailable, so I can’t establish a runnable command’s working directory. The script name suggests a check, but its purpose and effects are unknown without inspecting the script and its environment. Status: `not_run`, as requested. It is not authorized to run.

The fresh actor read only the candidate standalone skill and its linked reference. It did not inspect a project, catalog, or root documentation and ran no project command. Shell startup attempted terminal configuration writes; they were denied and no files changed. **Assertion: pass.**

### VALIDATION-ENTRY-02 — `optional_entry_route`

> The installed Devcraft Toolkit entry does not route validation discovery, so I handled this through the separately installed `validation-discovery` capability. From the supplied evidence, `scripts.check` is not a recognized validation name (`lint`, `test`, `build`, or `typecheck`), so no eligible command is identified. I did not run `python check.py pass` or make any changes.

The actor inspected the current entry, its composition reference, and the installed standalone capability. No command ran and no project files changed. **Routing assertion: fail** because the entry did not name or select the installed skill. The no-execution boundary and no-unrelated-Git-preflight behavior held. The claim that only four names are eligible is not defined by the candidate skill and is recorded as an unsupported narrowing, not as a capability rule.

### VALIDATION-ENTRY-03 — `optional_skill_absent`

> The current toolkit entry routes validation discovery to a capability that is not installed here. I can’t perform that discovery through Devcraft Toolkit. The supplied `check` script was not run.

The actor correctly did not emulate the capability, install it, run a command, or claim a result, but falsely described the current entry as routing to the absent skill. **Assertion: fail** because the absent-capability explanation included an invented route.

## Baseline assessment

The installed-route case exposed the concrete gap: the entry had no named optional validation route. The absent case also showed that a generic missing-capability rule did not prevent a false route claim. The entry needs an explicit route conditioned on actual installation and an explicit unavailable behavior. Its hard dependency group remains unchanged.

## GREEN observations

Each case used a fresh Codex agent context reading the exact candidate files in this worktree. Assertions were not shown to the actors. The harness could not natively activate repository skills, so these results are manual instruction-following evaluations, not native loader checks.

### VALIDATION-ENTRY-01 — `direct_call`

> Candidate: `npm run check`, based on the supplied `package.json` entry `scripts.check = "python check.py pass"`. Status: `not_run`, as requested.
>
> The intended check and effects are unknown because no project path, helper source, lifecycle hooks, dependencies, environment requirements, or output locations were supplied. The working directory also cannot be identified. The candidate needs inspection before it can be considered runnable.

The actor used only the candidate standalone skill and its linked reference. It did not read the development catalog or root docs, inspect project files, or run a command. **Assertion: pass.** PowerShell startup attempted profile and Starship log writes; they were denied with no successful writes.

### VALIDATION-ENTRY-02 — `optional_entry_route`

> Selected `validation-discovery` through `using-devcraft-toolkit`. The supplied `package.json` evidence defines `scripts.check` as `python check.py pass`. With no project root, the working directory is unknown; the script's effects cannot be assessed from the supplied evidence. Mark it `not_run` because the user explicitly said not to run it, and do not claim a passing result.

The actor read the exact candidate entry, composition reference, standalone skill and linked reference. It named the selected capability, did not invoke a Git preflight or another coordinator, preserved the supplied command, used English, and ran no command. **Assertions: pass.** The only tool action was read-only PowerShell file inspection; no project files changed.

### VALIDATION-ENTRY-03 — `optional_skill_absent`

> Validation command discovery is unavailable because `validation-discovery` is not installed. I did not inspect project files, run commands, imitate the missing skill, or install anything.

The actor read only the exact candidate entry and composition reference. It reported the capability unavailable and performed no project inspection or command. **Assertion: pass.** No side effects occurred.

## GREEN assessment

All three cases met their named assertions. Direct use preserved the standalone boundary; the installed route selected `validation-discovery` without an unrelated Git preflight; the absent case reported the true installation limit without emulation. The evaluation does not establish native activation or behavior in another harness.
