# Seven-client expansion evidence

## Interface inspection

Consulted 2026-10-23: official Copilot plugin/settings documentation, Microsoft
VS Code plugin guide, Kiro V3 features/2.25 changelog, and Crew skill/agent docs.
Installed Windows help reported Copilot CLI 1.0.91 and kiro-cli-chat 2.28.0.
Only version/help were run against host clients; no host installation, model,
account store, security setting or credentials were changed.

Crew documents complete GitHub skill import and its default agent's on-demand
catalog. No toolkit template or App is delivered. CLI/IDE Power sharing is not
proof of Crew Power consumption; use Crew's own imported complete skill set.
Project trust and existing restricted-agent mappings remain explicit gates.

## Actual remote Copilot probe

Disposable Linux container using image
node@sha256:06d7adf3e0ef61a13f1d28682726366f97a15aa1888c934d3ecec86c33918b53,
Node 24.22.1, Git 2.54.0 and Copilot CLI 1.0.91. Public Git/npm acquisition
required network. The owned tool prefix used npm lifecycle scripts disabled;
no personal homes/authentication were mounted and no model was invoked.

The corrected run executed **20 commands, all exit 0**. Copilot registered the
remote marketplace, installed/listed/reinstalled the suite, changed its user
enable state, refreshed the marketplace, updated at the same ref and uninstalled.
All seven installed skill folders and every resource hash matched a separately
fetched immutable b05a8c4367dc02e33ac9d19a8eb98e0bdb31c04e payload. Control-project
and unrelated-skill sentinels survived. These are test-process resource reads,
not model-driven reads or proof of active-session isolation.

[Attempt 1](attempt-1.json) retained the actual rejected #SHA recipe:
Copilot cloned with git clone --branch and expected a branch/tag. The corrected
source was the existing mutable docs/distribution-installation branch, resolved
and asserted as 218aea8d180a17f2cb6d321c9141f2979191b8e0. Package contents still
matched b05a8c4. The retained runner rejects a different preview HEAD until its
expectation is reviewed. It archives this run, not branch-tracking CI.

[Results/commands/hashes](results.json), [executed runner](runner.mjs),
[container setup](run.sh) and [npm dependency lock](toolchain-lock.json) are retained.
The runner assumes disposable /root, /reference, /projects and /tool directories
plus a writable /output mount; never execute it in a personal user environment.

This does not verify repository declarative auto-install, model activation,
version-changing update or VS Code crossover. Kiro CLI version/help inspection
is not an installation/session check. No isolated authenticated IDE or Crew
environment was available.

## Expanded native gates

These rows describe actual execution status, not inferred compatibility.
Each row includes user and project expectations; copied resources are separate.

| Client | Complete delivery | Current evidence | Native gates still open |
| --- | --- | --- | --- |
| Codex | Marketplace plugin | Historical limited registration/resources | Authenticated reads, active scope and full lifecycle |
| Claude Code | Marketplace plugin | Historical limited registration/resources | Authenticated reads, active scope and version-changing lifecycle |
| Copilot CLI | Same marketplace plugin | Limited remote registration/resources and same-ref lifecycle | Authenticated reads, repository auto-install/isolation and lifecycle |
| Copilot VS Code | Marketplace UI / CLI discovery | blocked: no isolated IDE session | User/workspace activation, CLI crossover, resources and lifecycle |
| Kiro CLI V3 | Shared IDE Power / CLI-only full skill set | Help inspected; session blocked | Shared Power activation; selected/control skill sessions |
| Kiro IDE | Remote Power | blocked: no isolated IDE session | Remote import, resources, user activation and lifecycle |
| Kiro Crew | Native complete skill import | blocked: no isolated Crew instance | Imports, source metadata, default/restricted agent discovery, trust and lifecycle |

Kiro CLI/IDE project-only Power is not_supported under this contract; full
project skill sets are distinct delivery rows. Crew's full import is not a Power
or atomic plugin, and its trusted-project route is not a user import.
The [expanded per-delivery/scope matrix](matrix.md) has 28 primary rows and three separately labeled Kiro full-set fallback rows. Historical results and Task 4 Step 3 remain unchanged. See
[scenario packets](../../scenarios/client-expansion.md) for exact assertions.

## Repository verification

The current tree discovered 75 Python tests: 74 passed and one Windows symlink
privilege case was skipped. Both repository/distribution validators, 185 local
Markdown links (including anchors) and git diff --check passed. Canonical skills,
catalog, manifests and scripts are unchanged from 218aea8. These checks do not
close native session gates.
