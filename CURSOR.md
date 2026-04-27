# Using this repo with Cursor

This repository includes a Cursor rule so the Karpathy-inspired coding principles can apply automatically inside Cursor.

## Fastest path for beginners

If you only want the simple version:

1. Open your project in Cursor.
2. Make sure the file [`.cursor/rules/karpathy-guidelines.mdc`](.cursor/rules/karpathy-guidelines.mdc) exists in that project.
3. Re-open the project if Cursor does not notice the rule immediately.
4. Ask for a small code change.
5. Check that the agent starts by clarifying assumptions and verification before changing code.

## In this repository

1. Open this folder in Cursor.
2. The rule [`.cursor/rules/karpathy-guidelines.mdc`](.cursor/rules/karpathy-guidelines.mdc) is already committed with `alwaysApply: true`.
3. You do not need any extra installation steps for Cursor in this repo.
4. In Cursor, confirm it under **Settings -> Rules** or the project rules UI, where `karpathy-guidelines` should appear.

## Use the same rule in another project

### Cursor (recommended)

Copy [`.cursor/rules/karpathy-guidelines.mdc`](.cursor/rules/karpathy-guidelines.mdc) into the target project's `.cursor/rules/` directory.

If the folder does not exist yet:

1. Create `.cursor/`
2. Create `.cursor/rules/`
3. Copy `karpathy-guidelines.mdc` into that folder
4. Re-open the project in Cursor if needed

### Other tools

If your tool does not use Cursor rules but does support a root instruction file, copy [CLAUDE.md](./CLAUDE.md) into the project root instead.

## Optional: personal Agent Skills

If you want reusable skills under `~/.cursor/skills`, use:

- [`skills/karpathy-guidelines/SKILL.md`](skills/karpathy-guidelines/SKILL.md) for English-first workflows
- [`skills/karpathy-guidelines-zh/SKILL.md`](skills/karpathy-guidelines-zh/SKILL.md) for Chinese-first workflows

Copy or symlink the whole skill folder layout you normally use for Cursor skills.

## How to tell it is working

The rule is probably active when the agent:

- explains assumptions before editing code
- proposes the smallest reasonable implementation
- avoids unrelated cleanup or refactors
- explains how success will be verified

## Claude Code vs Cursor

- **Claude Code:** Use [README.md](./README.md), [CLAUDE.md](./CLAUDE.md), or the plugin files depending on your setup.
- **Cursor:** Use the committed `.cursor/rules/` file. Cursor does not read `.claude-plugin/` by default.

## For contributors

When you change the four principles, keep these files in sync:

- [CLAUDE.md](./CLAUDE.md)
- [`.cursor/rules/karpathy-guidelines.mdc`](.cursor/rules/karpathy-guidelines.mdc)
- [skills/karpathy-guidelines/SKILL.md](skills/karpathy-guidelines/SKILL.md)
- [skills/karpathy-guidelines-zh/SKILL.md](skills/karpathy-guidelines-zh/SKILL.md) when the Chinese-first version should mirror the same behavior
