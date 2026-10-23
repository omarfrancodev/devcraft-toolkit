# Report Quality

## Resolve the request

Identify the report purpose, audience, supplied evidence, requested sections, detail level, language, and destination. The request's format takes precedence over the starter structure. Do not collect Git history or platform data unless the user explicitly requests and authorizes that inspection.

## Make claims traceable to evidence

Combine related facts into clear outcomes while keeping unrelated work separate. Describe whether work is completed, ongoing, blocked, or still unknown only when the supplied evidence supports that status. Retain material caveats and conflicts; do not pick one conflicting claim without evidence. If a missing fact would change the report, ask a focused question or state the uncertainty.

Do not infer business impact, release or deployment, authorship, test coverage, dates, or quantitative improvement from a title or vague note. Preserve exact supplied dates, numeric values, names, filenames, commands, and identifiers. Technical detail belongs in the report when requested or useful to its audience; do not remove it under a generic business-writing rule.

When the evidence is empty, say that there is not enough information for a factual report and name the missing input that would help. Do not fill a template with invented activities or unsupported status.

## Resolve language and structure

Use this precedence for user-facing report content:

1. An explicit language instruction for the report.
2. The language of the user's request.
3. English when the request language cannot be determined.

An explicit override controls even when the surrounding request uses another language. Translate visible prose and section labels, but keep identifiers, filenames, commands, names, exact dates and numeric values unchanged. Do not translate source-template placeholder keys; replace them with rendered content instead of exposing unresolved keys.

Use the user's requested sections, order, headings, and format exactly when feasible. If no structure is supplied, start from `assets/report.md`. Its English source labels are convention only: translate labels such as Summary, Activities, and Open items to the resolved language. Omit an optional section with no evidence rather than adding filler. Do not force an executive summary or business-only style when the user asks for another audience or format.

## Return content or save one file

The default result is report text in the conversation. “Prepare,” “draft,” “summarize,” or “write a report” alone does not request persistence.

For explicit local-file output, use only the destination selected by the user. If no destination is selected, ask for it. Do not create parent directories, companion files, or alternate copies. If the selected file already exists and replacement was not explicitly authorized, ask before overwriting it. Write the report, read the same path back, and compare its content with the intended output. Report the exact limitation if writing or verification fails; never claim success from an attempted write alone. This permission does not authorize Git operations, network access, or external publication.

## Example

Evidence: “Feature-flag checks now reject unknown keys. The migration guide is still being drafted. Fourteen lint checks passed.”

Report:

> Unknown feature-flag keys are rejected. The migration guide remains in progress. Fourteen lint checks passed.
