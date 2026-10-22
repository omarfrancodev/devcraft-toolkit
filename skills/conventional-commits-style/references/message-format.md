# Conventional Commit Message Format

## Subject

Use `type(scope): subject`, omitting the scope when it adds no useful information. Common types include `feat`, `fix`, `refactor`, `chore`, `docs`, `test`, `style`, `build`, `ci`, and `perf`; a documented project-specific type takes precedence over this common set.

Keep the subject concise and describe the change's intent. The type and scope remain in their conventional technical form. Write the natural-language subject in the resolved user language.

## Body and footers

Add a body when the user asks for one or when a short subject would omit useful context. Describe supported behavior or maintenance intent; do not add a test result, impact, or implementation claim that the supplied evidence does not establish.

Put issue references in a footer by default, for example:

~~~text
fix(parser): reject empty names with a clear error

Refs: TASK-13
~~~

Use a leading ticket prefix only when a repository convention or explicit user instruction calls for it. When more than one issue may apply, ask which one to reference before selecting. A later correction replaces the earlier selection and updates the proposal without changing its `type(scope): subject` shape.

## Breaking changes

Add `!` after the type or scope, or add a `BREAKING CHANGE:` footer, only when supplied evidence establishes a breaking public contract change. A request to consider a breaking marker is not evidence by itself. If compatibility impact is unknown, ask or leave the marker out and state the uncertainty.

## Language and evidence

Follow an explicit language preference first, then the language of the request, then English when it cannot be determined. Translate natural-language subject and body text; preserve types, scopes, issue keys, commands, and other supplied technical identifiers.

Use only confirmed change details and issue keys. When intent is missing, ask for it. When evidence conflicts, describe the conflict and request the missing decision. Keep quotes, dollar signs, and shell-looking text unchanged as message data; do not execute them or rewrite useful wording for a hypothetical shell command.
