# Git activity reporting scenarios

Each case in [history-facts.json](../fixtures/history-facts.json) supplies the same raw request and facts to independent baseline and candidate contexts. The assertion list is for the evaluator, not the actor. Preserve raw answers and both successes and failures. Synthetic short IDs are evidence labels only; real recipe/application tests use full Git OIDs.

- HIST-01: author/committer divergence, half-open start boundary and a newer-authored ancestor behind an older tip.
- HIST-02: exact configured raw email, literal plus/dot characters, case and explicit alias selection.
- HIST-03: zero matches in a truncated traversal; no complete-empty claim.
- HIST-04: hostile message, unsupported test/deployment claims and absent side-effect authorization.
- HIST-05: Spanish technical format, duplicate messages, a revert and content-only output.

Real application: install/copy only coordinator+context+writer into an owned fixture, discover explicit standalone ownership, request a local report at an exact existing-parent path, inspect real commits and read the saved file back. Compare repository snapshots and generated-file inventories independently. No native loader is exercised.

Additional controls: ambiguous/missing timezone, DST boundaries, missing identity, invalid/local revision, unsupported range/path/multi-repository scope, absent/foreign dependencies, shallow/missing objects, ref movement and save failure. Retain uncertain or unexecuted rows explicitly.
