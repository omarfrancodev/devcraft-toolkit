# Installation environment

Date: 2026-10-23. Package source: e4965443613f1407ce4b18100564e810e39d227b (local snapshot of the seven skills and package metadata).

- Host: Windows, Node.js 24.15.0, npm 11.5.1, Docker Engine 29.9.2.
- Disposable environment: Linux container, Node.js 24.22.1, actual container user home /root.
- Image: node@sha256:06d7adf3e0ef61a13f1d28682726366f97a15aa1888c934d3ecec86c33918b53.
- Skills CLI: 1.7.4, acquired in a dedicated tool directory with npm lifecycle scripts disabled. Declared Node requirement: >=22.20.0.
- Registry integrity: sha512-lHZJksE8UImNAr+LL6unqq7jERjdFw5EJasm17srycwL7rXHGdCmgu1L1ttLxUO9i3rdH+QQig+px0icHqLmRw==.
- Installation runs: network disabled, source/toolchain/runner read-only, only evidence output mounted writable. No personal profiles or authentication stores mounted.
- Native clients observed on host: Codex CLI 0.162.0, Claude Code 2.1.300, VS Code 1.143.0. No Kiro executable found. These versions are inventory, not activation evidence.

The retained [runner](filesystem-matrix.mjs) expects /source (package snapshot), /tool (pinned CLI npm prefix), and writable /output mounts. Run only inside a disposable container: it resets its container-owned /root skill directories and writes case fixtures. Do not execute it against a real user's home. Its stdout reports matrix totals; [raw results](filesystem-results.json) retain commands, byte inventories and effects.
