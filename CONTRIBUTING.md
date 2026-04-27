# Contributing

English | [简体中文](./CONTRIBUTING.zh.md)

This repository stores reusable Codex skills. Each contribution should be easy to discover, easy to understand, and easy to reuse in real agent workflows.

## What to Contribute

Good contributions usually add one of these:

- a new skill folder under `skills/`
- better references for an existing skill
- improved bilingual documentation
- preview assets or repository organization improvements

Avoid adding general notes or extra docs that are not directly useful to a skill or to repository contributors.

## Skill Requirements

Each skill should follow this minimum structure:

```text
skills/
└─ skill-name/
   ├─ SKILL.md
   ├─ agents/openai.yaml
   └─ references/        (optional)
```

Required expectations:

- The folder name should be lowercase hyphen-case.
- `SKILL.md` must include YAML frontmatter with `name` and `description`.
- The description should clearly explain what the skill does and when it should be used.
- `agents/openai.yaml` should include a clear display name, short description, and default prompt.
- Keep `SKILL.md` concise and move richer examples into `references/` when useful.

## Writing Guidelines

- Prefer practical instructions over abstract theory.
- Write for another Codex instance, not for a human end user.
- Keep trigger descriptions explicit.
- Include example prompts when they help the skill trigger correctly.
- Use imperative guidance such as `Do X` or `Prefer Y`.
- Avoid unnecessary files like `CHANGELOG.md`, `NOTES.md`, or extra process docs inside a skill folder.

## Bilingual Documentation

If a contribution is user-facing at the repository level, prefer updating both:

- `README.md`
- `README.zh.md`

If a skill is specifically designed for Chinese workflows, consider whether it should have:

- a Chinese-first `SKILL.md`
- Chinese examples in `references/`
- an English repository description so non-Chinese readers can still discover it

## Validation

Before opening a PR or pushing changes, check:

1. The skill folder structure is correct.
2. `SKILL.md` renders cleanly and the trigger description is specific.
3. Links inside the repository resolve correctly.
4. Preview assets render correctly in GitHub.
5. If possible, run the local skill validator.

Note for Windows contributors:

- The upstream validation script may read files using the local default encoding.
- UTF-8 Chinese files can display correctly on GitHub while still failing a local validator that assumes `gbk`.
- When that happens, document the limitation in the PR rather than rewriting good repository text into broken encoding.

## Suggested Workflow

1. Add or update files in a focused change set.
2. Keep the diff directly tied to the contribution.
3. Update repository docs if discoverability changed.
4. Validate locally where practical.
5. Commit with a descriptive message.

## Pull Request Checklist

- The new skill has a clear purpose.
- The trigger description is specific.
- The repository docs still match the current skill list.
- New images or assets are stored in sensible paths.
- The change does not add unnecessary clutter.

## License

By contributing, you agree that your contributions will be released under the repository's MIT license.
