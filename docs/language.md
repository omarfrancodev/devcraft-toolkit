# Language behavior

Toolkit source instructions, documentation, examples, and default templates are written in English. User-facing content follows this precedence:

1. An explicit language preference from the user.
2. The language of the current request.
3. English when the request language is indeterminate.

Resolve language once for an execution. A later explicit user instruction can change it. Translate natural-language explanations and visible template labels while preserving technical identifiers, schema keys, status values, and command syntax.

Do not infer response language from machine locale, repository location, Git identity, or branch name. Behavioral scenarios are maintained under the owning skill's subtree in `tests/skills/` and evaluated in the requesting user's language.
