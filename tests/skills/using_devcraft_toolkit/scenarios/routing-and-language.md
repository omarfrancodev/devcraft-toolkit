# Behavioral scenarios: using-devcraft-toolkit

Canonical owner: `using-devcraft-toolkit`.

## Language resolution

For each request, resolve one response language using explicit user preference first, then the language of the request, then English when indeterminate. Keep technical identifiers, catalog keys, status labels, and commands unchanged.

1. English request, no preference: route and respond in English.
2. Spanish request, no preference: route and respond in Spanish, translating explanatory labels while preserving skill names and commands.
3. French request, no preference: respond in French with the same identifier preservation.
4. English request with “responde en español”: respond in Spanish.
5. Language-indeterminate input: use English.
6. A later explicit language instruction during the same execution changes the resolved language for subsequent output.

Expected evidence: the same scope decision is applied regardless of language; only natural-language content and visible template labels change.

## Routing and availability

- A repository-context request can use `git-working-directory-policy` when that skill is installed.
- A Git preflight request can use `git-safety-check` and its declared `git-working-directory-policy` dependency.
- Commit, publish, and activity-report requests must clearly state that the target capability is planned or not installed in this distribution. Do not emulate a missing coordinator or claim completion.
- An unrelated request, such as explaining a Python expression, must not auto-load the toolkit entry.
- When an individual skill is installed without the repository checkout, it must not try to open the development-only `catalog.json` or root documentation.

Expected evidence: route only within the requested scope, report actual installed capabilities, and retain any unresolved user decision without performing an unrelated operation.
