Both cases use reported evidence only. The request authorizes creating `feature/parser` and continuing to commit, subject to successful branch verification. Repository root, Git/common directories, original branch, identity and complete preservation checks were not supplied.

**Case 1 — source changes before writing**

- **Outcome:** `stopped`.
- Pinned source: `cccccccccccccccccccccccccccccccccccccccc`.
- Fresh source: `dddddddddddddddddddddddddddddddddddddddd`.
- Target: literal `feature/parser`.
- The refreshed source guard failed. Do not attempt branch creation or commit, and do not silently repin to the new source.
- Next operations: read-only inspection through the selected `git-working-directory-policy` context to establish what moved. Resolve whether to restart from the new current commit or pursue a separately decided alternate-base workflow. Any authorized continuation requires fresh guards, effect review and preservation evidence.

**Case 2 — switch attempted once; post-checkout fails**

- **Outcome:** `partial`.
- Reported attempt exited `1`; post-checkout printed failure.
- Reported actual HEAD is `feature/parser` at `cccccccccccccccccccccccccccccccccccccccc`.
- Reported index and files are unchanged. These facts establish actual selection despite the failed command; they do not establish complete success or rollback.
- Stop dependent commit work. Do not retry creation, switch back, delete the branch, reset, restore, stash or clean.
- Next operations: read-only inspection of the failed hook and its helpers, independently verify HEAD/target, original and unrelated refs/config, index semantics and complete file preservation, and determine any additional effects. Those postconditions remain unverified from the supplied facts.
- A later explicit continuation requires resolution of the failed gate and fresh inspection. The existing branch must be treated as an actual partial effect, not automatically recreated.