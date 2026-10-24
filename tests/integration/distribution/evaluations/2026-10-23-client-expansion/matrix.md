# Expanded native validation matrix

Snapshot: 2026-10-23. Status is native session evidence, not documentation availability.
Historical observations retain their original source/version; new Copilot observations
use the client-expansion record. No row claims authenticated invocation.

| Client | Delivery | Scope | Native status | Evidence or remaining gate |
| --- | --- | --- | --- | --- |
| Codex | complete | user | limited | Historical local/remote registration or registry observation; authenticated invocation, active scope and version-changing lifecycle open. |
| Codex | complete | project | limited | Historical local/remote registration or registry observation; authenticated invocation, active scope and version-changing lifecycle open. |
| Codex | individual | user | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Codex | individual | project | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Copilot CLI | complete | user | limited | Remote registration/resources and same-ref lifecycle observed; no authenticated activation. |
| Copilot CLI | complete | project | blocked | Repository declarations documented; auto-install and selected/control active-session isolation not run. |
| Copilot CLI | individual | user | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Copilot CLI | individual | project | blocked | Selected complete folders under .agents/skills/ with explicit dependencies; native discovery/resource reads, selected/control scope and copy lifecycle unverified. |
| Copilot VS Code | complete | user | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Copilot VS Code | complete | project | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Copilot VS Code | individual | user | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Copilot VS Code | individual | project | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Claude Code | complete | user | limited | Historical local/remote registration or registry observation; authenticated invocation, active scope and version-changing lifecycle open. |
| Claude Code | complete | project | limited | Historical local/remote registration or registry observation; authenticated invocation, active scope and version-changing lifecycle open. |
| Claude Code | individual | user | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Claude Code | individual | project | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Kiro CLI V3 | complete | user | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Kiro CLI V3 | complete | project | not_supported | Project-only native Power is not established; distinct full-set fallback below. |
| Kiro CLI V3 | individual | user | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Kiro CLI V3 | individual | project | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Kiro IDE | complete | user | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Kiro IDE | complete | project | not_supported | Project-only native Power is not established; distinct full-set fallback below. |
| Kiro IDE | individual | user | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Kiro IDE | individual | project | blocked | No isolated authenticated client/session; discovery, resources, scope and lifecycle remain open. |
| Kiro Crew | complete | user | blocked | Own native skill snapshot import (complete or selected set); no isolated Crew instance. Project route also needs enablement/trust. |
| Kiro Crew | complete | project | blocked | All seven complete folders under the active project's .kiro/skills/; project enablement/trust, discovery/resource reads, control isolation and folder lifecycle unverified. |
| Kiro Crew | individual | user | blocked | Own native skill snapshot import (complete or selected set); no isolated Crew instance. Project route also needs enablement/trust. |
| Kiro Crew | individual | project | blocked | Selected complete folders with explicit dependency closure under the active project's .kiro/skills/; project enablement/trust, discovery/resource reads, control isolation and folder lifecycle unverified. |
| Kiro CLI V3 | complete skill-set fallback | user | blocked | Shared-folder resource copying has separate historical evidence; native session not passed. |
| Kiro CLI V3 | complete skill-set fallback | project | blocked | Shared-folder resource copying has separate historical evidence; native session not passed. |
| Kiro IDE | complete skill-set fallback | project | blocked | Shared-folder resource copying has separate historical evidence; native session not passed. |

A blocked row has a documented route but lacks required native execution; it is not
a package failure. Kiro CLI help is interface evidence only. Copilot CLI does not
pass VS Code discovery, and neither Kiro CLI nor IDE passes Crew.

See [client observations](clients.md), [historical native details](../2026-10-23-installation/native.md)
and [scenario assertions](../../scenarios/client-expansion.md).
