# Remote suite installation evaluation

Date: 2026-10-23. Status: remote acquisition and package/file assertions passed; native activation remains limited/blocked.

## Source and environment

- Repository: https://github.com/omarfrancodev/devcraft-toolkit.git.
- Immutable reference payload: b05a8c4367dc02e33ac9d19a8eb98e0bdb31c04e, candidate 0.1.0-preview.2, not a release tag.
- Codex source: repository marketplace with explicit --ref at that SHA.
- Claude source: published branch docs/distribution-installation, which resolved to that SHA during this run. Branch tracking is mutable; the archive runner deliberately rejects a different HEAD until a maintainer reviews/updates the expectation. This is a recorded snapshot, not a continuously tracking CI test.
- Optional CLI source: GitHub tree URL containing that SHA.
- The default branch observed at setup was 4fe4174ceb91de8964a1f1391b599b9c3a820141, the source-only preview state. Normal default-source recipes become applicable after metadata integration.
- Disposable Linux container, Node.js 24.22.1, Git 2.54.0; Codex CLI 0.162.0, Claude Code 2.1.300, Skills CLI 1.7.4.
- Image: node@sha256:06d7adf3e0ef61a13f1d28682726366f97a15aa1888c934d3ecec86c33918b53.
- Native tools were acquired in an owned prefix with npm lifecycle scripts disabled. [Dependency lock/integrities](toolchain-lock.json) are retained. Git/CA certificates were installed only in the disposable container.
- Public Git/npm network access was necessary. No host homes, credentials or authentication stores were mounted; no TLS/trust/approval protections were disabled and no model was invoked.

The package manifests, catalog and skill resources in the documentation revision are unchanged from the reference payload. This comparison prevents presenting a local checkout test as a remote acquisition pass.

## Observed packets

| Packet | Result | Evidence level |
| --- | --- | --- |
| REMOTE-FS-01 | Fetched exact SHA; both manifests and seven canonical skill directories verified | Git source/filesystem passed |
| REMOTE-NATIVE-01 | Codex remotely registered, installed/listed the suite; all installed skill resources matched source SHA-256; Git marketplace refresh and removal exited 0 | limited native; no authenticated invocation |
| REMOTE-NATIVE-02 user | Claude registered the remote preview branch, installed/listed seven skills, inspected components and matched all resources; update and scoped uninstall exited 0 | limited native |
| REMOTE-NATIVE-02 project | Same package/resource checks; control-project registry reported disabled; scoped update/uninstall exited 0 | limited native; active-session scope unverified |
| REMOTE-ALT-01 Codex | Independent formatter copied from remote source into one project | filesystem passed |
| REMOTE-ALT-01 Kiro | All seven explicitly selected skills copied from remote source into one project | filesystem passed; Kiro IDE not exercised |
| REMOTE-LIMIT-01 | Authentication/IDE sessions absent; Kiro pinned-ref interface not established | blocked/unverified, not passed |

The corrected run executed 29 commands, all exit 0. Project/control sentinels were preserved. Resource matches were computed from actual native managed cache files and actual optional copies against a separately fetched Git reference. These are test-process reads, not model-driven resource reads.

[Exact results, commands and hashes](results.json), [executed runner](runner.mjs) and [container setup](run.sh) are retained. The runner assumes a disposable /root, /reference, /projects and mounted /tool and /output paths; do not execute it on a personal user account. Its source-ref assertion is intentionally tied to the recorded snapshot.

## Preserved failed attempt and correction

[Attempt 1](attempt-1.json) succeeded through Codex remote installation/resource checks, then Claude rejected Git URL#SHA: its clone requested a remote branch named after the SHA, which did not exist. This was a recipe error, not evidence that the package failed metadata validation. The preview recipe now uses the existing branch, verifies its resolved revision and explicitly labels it mutable. No tag or release was created to conceal the distinction.

## Remaining gates

No authenticated invocation, model resource read, complete version-changing native lifecycle, Copilot session or Kiro IDE session passed here. Existing [local native matrix](../2026-10-23-installation/native.md) and Task 4 Step 3 remain open. Default-source production examples are conditional on integration; the source-only published preview is not a native package. A client-managed clone/cache is expected and is different from requiring the consumer to maintain a local checkout.
