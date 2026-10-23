---
name: natural-language-report-writer
description: Use when a user asks to turn supplied facts or evidence into an activity report, progress update, or summary for a specific audience or format, including a report requested as a local file.
---

# Natural-Language Report Writer

Turn the evidence supplied with the request into a clear report. Resolve the report's language, audience, purpose, structure, level of detail, and destination before composing.

- Use an explicit language instruction for the report when present. Otherwise use the language of the user's request; use English only when the language is indeterminate. An explicit instruction such as “answer in Spanish” takes precedence even when the surrounding request is in English.
- Use only supplied facts or information deliberately inspected within the user's authorized scope. Keep completed work, ongoing work, open items, and uncertainty distinct. Preserve dates, numbers, names, filenames, identifiers, and technical details without inventing impact, authorship, tests, or completion.
- Follow the user's requested format and audience first. When no structure is requested, use the bundled English template as a starting point, translate visible headings into the resolved language, and omit optional sections that have no supported content. Keep template placeholder keys unchanged in the source file and replace them in rendered output.
- Return report content in the conversation by default. A request for content alone does not authorize file creation. Write a local report only when the user explicitly asks to save it and selects a destination. Create or update only that report file; do not choose a path, create additional files or directories, or post the report externally. Ask before replacing an existing file unless the user explicitly authorized replacement. Read the selected file back and verify it before claiming success.
- If evidence is missing or conflicting, state the limitation or preserve the conflict. Ask a focused question only when the uncertainty prevents a useful, accurate report. A failed write or readback is reported as a failure.

Use [report-quality.md](references/report-quality.md) for evidence, language, structure, and file-output decisions. The starter structure is in [report.md](assets/report.md).
