# Filesystem installation evaluation

Status: passed for file placement and resources; native discovery/activation is not established by this evaluation.

Source and tools: [environment](environment.md). Packets: [FS-01–05](../../scenarios/installation.md). Retained observations: [JSON](filesystem-results.json) and [runner](filesystem-matrix.mjs).

| Method | Targets | Scopes | Selections per combination | Passed |
| --- | --- | --- | --- | --- |
| Skills CLI 1.7.4, explicit selection, copy | codex, github-copilot, claude-code, kiro-cli | project, global | seven closures and full set | 64/64 |
| Complete-folder manual copying | same four targets | project, global | seven closures and full set | 64/64 |
| CLI lifecycle | same four targets | project, global | report writer | 8/8 |

All selected files, references and assets matched source SHA-256 hashes. Selected directory sets were exact; no planned skill appeared. Copy mode contained no symlinks. Project, control-project and container-user sentinels survived; other-scope directories were absent.

Observed destinations:

| Target | Project, both methods | Global CLI | Global manual |
| --- | --- | --- | --- |
| codex | .agents/skills | /root/.agents/skills | /root/.agents/skills |
| github-copilot | .agents/skills | /root/.agents/skills | /root/.copilot/skills |
| claude-code | .claude/skills | /root/.claude/skills | /root/.claude/skills |
| kiro-cli | .kiro/skills | /root/.kiro/skills | /root/.kiro/skills |

Skills CLI 1.7.4 uses the shared .agents/skills global destination for github-copilot. Manual copying independently exercised the documented .copilot/skills user root. This observed version-specific difference is intentional in the recipes; selectors do not isolate clients from shared discovery roots. CLI lock artifacts include project skills-lock.json and user .agents/.skill-lock.json; full inventories identify actual writes.

A bare entry selection installed only using-devcraft-toolkit. The CLI did not resolve catalog dependencies. The entry trio and preflight pair passed when explicitly selected.

FS-04 inspected a same-name collision and stopped before invoking the CLI; existing content and an unrelated sentinel were unchanged. This proves the documented pre-install gate, not an overwrite-protection feature of the CLI. FS-05 then explicitly authorized replacement in that disposable fixture: repeated installation was byte-identical, explicit re-add from a changed local source updated the copy, and named removal preserved unrelated content. The local update is not evidence of automatic remote updates.

No host personal skill store was changed. A target selector, correct directory or successful CLI exit is not evidence of native harness loading, ownership discovery, language behavior, or native scope. Those checks have a [separate native matrix](native.md).
