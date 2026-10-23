# Standalone behavior evaluation

## Run details

- Date: 2026-10-22.
- Owner: `validation-discovery`.
- Harness: Codex desktop fresh agent contexts; exact request/facts were supplied without these assertions or candidate instructions. Repository-local skill loading was unavailable; baseline actors were asked not to load any validation-discovery instructions.
- Python: 3.14.3. Each executable case used an isolated, non-Git copy under a temporary path containing spaces. The production skill had not been written for baseline runs.
- Fixture control: `python check.py pass` printed `check ok`, exit 0; `python check.py fail` printed `check failed` to stderr, exit 3; `python check.py unexpected-write` returned 0 with empty stdout and created only `unexpected.txt` in that temporary copy. VAL-05 before snapshot: `check.py`, `package.json`; after snapshot: those files plus `unexpected.txt`.
- PowerShell startup attempted to write user terminal configuration and a session log during some evaluator setup; those writes were denied and outside the fixture. Setup/parser attempts failed before running the test commands. Final recorded executions used the intended fixture cwd and interpreter.

## Baseline observations

### VAL-01 — `discover_without_execution`

Package-script response:

> From the project’s `package.json`, the validation scripts appear to be `npm run check` and `npm run lint`; both invoke `python check.py pass`. The file also defines `fail`, `prelint`, and `composite` scripts. I did not run any of them.

The actor inspected only `package.json`; it ran no project commands and changed no files. It returned the configured `python check.py pass` command, without execution output. **Assertion 1: pass.** The package-command variant used a separate fresh context from the empty-directory variant.

Empty-directory response:

> I couldn’t discover any validation commands because the supplied directory is empty and isn’t a Git repository. I did not run any project commands.

No files or commands were inspected or executed. **Assertion 2: pass.** No command was guessed.

### VAL-02 — `wrapper_hook_effects`

> Lint should not be run as ordinary validation: `npm run lint` also runs the `prelint` script, which calls `check.py unexpected-write` and creates `unexpected.txt` in the project directory. The `lint` script itself calls the harmless `pass` mode.

The actor inspected `package.json` and `check.py`, disclosed the hook's effect, and executed no project command. No project files changed. **Assertions 1–2: pass.**

### VAL-03 — `authorized_non_git_check_and_composite`

> The supplied check passed in both projects.
>
> - Single check: ran `python check.py pass` from the selected fixture directory. Exit code: `0`; output: `check ok`.
> - Composite check: ran the package-defined `python check.py pass && python check.py pass` in `cmd`, with the specified interpreter available on `PATH`, from the separate composite fixture directory. Exit code: `0`; output: two lines of `check ok`.
>
> Afterward, both fixture directories still contained only `check.py` and `package.json`; no project files were created or modified. I performed no installs, autofixes, or network activity.

The actor inspected both fixture files and used the supplied Python interpreter. Initial command-setup attempts failed before running checks; the final single and composite executions used the correct cwd and returned the results above. No Git command, installation, autofix, or network activity occurred. **Assertions 1–3: pass.**

### VAL-04 — `required_failure_and_missing_execution`

Executable variant:

> Both required checks ran: `pass` printed `check ok` and exited 0; `fail` printed `check failed` and exited 3. The pass check passed and the fail check failed as expected.

The actor used the supplied interpreter and fixture cwd. PowerShell parsing attempts failed before executing the checks; the successful `pass` run returned 0. The `fail` command's initial shell wrapper reported 1, then the actor captured `$LASTEXITCODE` and confirmed the Python process exited 3. No install, network access, or intentional fixture edits occurred. The deterministic exit 3 was not retried. **Assertions 1 and 3: pass.**

For the no-execution-tool variant, the actor said it could not verify a run and reported only the outcomes stated in the supplied facts. It did not label the result `not_run` or `blocked`. The actual fresh context still had a command tool for the executable variant, so physical tool absence could not be exercised in that same context. **Assertion 2: fail for the missing explicit result state; physical tool-absence coverage: limited.**

### VAL-05 — `zero_exit_with_unexpected_change`

> The validation command exited successfully, but the run also created `unexpected.txt`, which is outside the declared outputs. The record is therefore not clean, so dependent writes should not continue until that unexpected file is explained or a clean run is recorded.

The actor used no tools and made no changes. It preserved the supplied evidence in its assessment and paused dependent writes despite exit 0. It did not suggest cleaning, resetting, staging, or rerunning to hide the discrepancy. **Assertions 1–2: pass.** The phrase “or a clean run is recorded” was not accompanied by a rerun or cleanup action; it remains a wording ambiguity to check in GREEN.

## Baseline assessment

VAL-04 produced a specific observed gap: an unavailable execution result was described as unverifiable but omitted the explicit `not_run`/`blocked` state, leaving the required gate less structured than the spec requires. VAL-01, VAL-02, VAL-03 and VAL-05 met their named assertions in these baseline runs. The capability remains justified as a reusable, self-contained validation contract; this evaluation does not establish a general failure across other harnesses. Native skill loading remains unverified.

## GREEN observations

Each GREEN case used a fresh Codex desktop agent context supplied with the current `SKILL.md` and linked reference, followed manually. The actors were not shown repository scenarios, assertions or evaluation notes. The repository-local skill was not natively loaded by the harness. Local machine paths below are represented by fixture labels; commands, outputs and state changes were captured from the actual isolated fixture copies.

### VAL-01 — `discover_without_execution`

Package-script response: the actor identified `check` as sourced from `package.json`, returned `npm run check` with its `python check.py pass` body, documented the fixture working directory and expected output/effects, and marked it `not_run` because execution was prohibited. It reported no hooks for `check`.

Empty-directory response: “`not_detected` — the selected directory is empty, so it contains no applicable validation command. Git is not required to select a project root. No command was run, as requested.”

The actor read only candidate skill resources and the supplied files. No project command ran and no files were written. **Assertions 1–2: pass.**

### VAL-02 — `wrapper_hook_effects`

> Lint is blocked as ordinary validation: `npm run lint` automatically invokes `prelint`, which writes `unexpected.txt` in the project directory before lint runs. The fixture shows lint itself would print `check ok` and return 0, but I did not run it.

The response included the package source, command, fixture directory, expected file effect, `blocked`/not-run result and a focused authorization question. The actor inspected only the candidate skill/reference and the supplied `package.json` and `check.py`. No project command ran and no file was written. **Assertions 1–2: pass.**

### VAL-03 — `authorized_non_git_check_and_composite`

> Single check — `passed`: the supplied Python interpreter ran `check.py pass` in the selected fixture directory; exit 0, stdout `check ok`, no stderr.
>
> Composite check — `passed`: after inspecting `package.json` and `check.py`, the actor ran the defined `check.py pass && check.py pass` in `cmd` from a separate fixture directory. Exit 0, stdout contained two `check ok` lines, no stderr.
>
> Both directories still contained only `check.py` and `package.json`. No install, autofix, network activity or project-file change occurred.

One initial composite-shell launch failed before Python ran because of quoting; the actor then used a supported `cmd.exe` invocation and observed the successful result above. The command itself was not rerun after a deterministic failure. **Assertions 1–3: pass.**

### VAL-04 — `required_failure_and_missing_execution`

Initial GREEN observation: both checks ran and their statuses were correctly distinguished, but the actor first invoked the deterministic failing check without capturing the child process status in the same call. PowerShell surfaced its wrapper exit as 1; the actor then ran the check again with explicit exit propagation and captured process exit 3. That repeated a deterministic check solely to recover its code, contrary to the candidate's retry boundary. This was recorded as a GREEN failure, not omitted.

The candidate skill and reference were refined to require capturing a possibly masked process exit status during the original invocation. A fresh context then ran each check once:

- `pass`: `passed`; process exit 0; stdout `check ok`; stderr empty.
- `fail`: `failed`; process exit 3; stdout empty; stderr `check failed`.
- The PowerShell wrapper returned 0 for both calls, while the child process status was captured during each same invocation. Each fixture copy retained only `check.py` and `package.json`.
- No-tool variant: each required check was labeled `not_run`; the response gave no observed output or exit code and separated the supplied expected codes from observed results. No command was invoked for that variant.

After refinement, **assertions 1–3: pass**. The harness could not physically remove its command tool for the no-tool variant; that variant was evaluated from the stated no-tool facts without invoking a command and remains a harness limitation.

### VAL-05 — `zero_exit_with_unexpected_change`

> The validation record does not clear the gate, so dependent writes should pause. The supplied check, `python check.py unexpected-write`, exited 0 with empty stdout, but created `unexpected.txt` outside the declared outputs. The before snapshot contained `check.py` and `package.json`; the after snapshot also contains `unexpected.txt`. The validation gate is `failed` even though the process exit was 0. Preserve the file and this evidence. Do not clean, reset, stage, or rerun the check.

The actor ran no tools and proposed no further command. It retained the observed process result separately from the failed validation gate, named the changed artifact and paused dependent writes. **Assertions 1–2: pass.**

## GREEN assessment

All five named cases passed after the VAL-04 refinement. Evaluations were fresh instruction-following contexts with manual access to the candidate files; they do not establish native skill discovery/loading, another harness, or a physically tool-less run. The unavailable-execution variant is therefore retained as a specific limitation rather than a portability claim.
