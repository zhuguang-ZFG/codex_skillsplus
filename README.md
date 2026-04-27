# Codex Skills Plus

English | [简体中文](./README.zh.md)

[![Skills](https://img.shields.io/badge/skills-2-1f6feb)](./skills)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

Curated Codex skills for more reliable coding workflows. This repository packages reusable skill folders that help coding agents think more clearly, change less, and verify more.

![Codex Skills Plus social preview](./docs/assets/social-preview.png)

## Quick Start

If you are new, do this:

1. Choose one skill folder:
   - `skills/karpathy-guidelines` for English
   - `skills/karpathy-guidelines-zh` for Chinese
2. Copy the whole folder into your local Codex skills directory:
   - `$CODEX_HOME/skills/` if `CODEX_HOME` is set
   - otherwise `~/.codex/skills/`
3. If you want these rules to apply by default in one project, also copy:
   - [CLAUDE.md](./CLAUDE.md) into the project root
   - or [`.cursor/rules/karpathy-guidelines.mdc`](./.cursor/rules/karpathy-guidelines.mdc) if you use Cursor
4. Start with one of these prompts:
   - `Use $karpathy-guidelines to review this task before coding.`
   - `使用 $karpathy-guidelines-zh 先梳理假设和验证步骤，再开始实现。`

If you want the repository to copy guidance into a project from GitHub, see [GitHub Sync Plugin](#github-sync-plugin).

## Highlights

- Ready-to-use Codex skill folders
- Focus on practical coding workflows
- English and Chinese documentation
- Lightweight skill bodies with on-demand references
- Browseable skill catalog
- Claude/Cursor compatibility files copied from the upstream layout
- Repository preview assets for GitHub sharing

## Included Skills

### `karpathy-guidelines`

Path: [skills/karpathy-guidelines](./skills/karpathy-guidelines)

An English-first behavioral guardrail for coding tasks. Use it when the agent should:

- surface assumptions before implementing
- choose the simplest viable solution
- keep diffs narrow and directly tied to the request
- define success in testable, verifiable terms

Best for:

- implementation planning
- code review
- bug fixing
- refactoring
- debugging
- non-trivial changes where minimal, surgical edits matter

When active, treat it as a default execution policy rather than optional advice.

Example:

```text
Use $karpathy-guidelines to fix this bug with the smallest safe change.
```

### `karpathy-guidelines-zh`

Path: [skills/karpathy-guidelines-zh](./skills/karpathy-guidelines-zh)

A Chinese-first version of the same working style, designed for Chinese prompts and Chinese discussion during planning, review, and implementation.

Best for:

- 中文代码审查
- 中文需求澄清
- 中文实现规划
- 中文 bug 修复
- 需要用中文定义验证步骤的任务

激活后应将其视为默认执行策略，而不是仅供参考的建议。

Example:

```text
使用 $karpathy-guidelines-zh 先审视这个改动方案，再开始实现。
```

See also:

- [Skill Catalog](./skills/index.md)
- [Contribution Guide](./CONTRIBUTING.md)
- [Cursor Setup](./CURSOR.md)
- [Root Claude Instructions](./CLAUDE.md)

## Why This Exists

Andrej Karpathy has pointed out several recurring problems in LLM-assisted coding:

- models silently pick an interpretation and run with it
- models overcomplicate simple tasks
- models touch adjacent code that was not part of the request
- models complete work without strong success criteria

This repository turns those observations into Codex-compatible skills that can be reused directly in agent workflows.

## Repository Structure

```text
codex_skillsplus/
├─ docs/
│  └─ assets/
│     └─ social-preview.png
├─ .claude-plugin/
│  ├─ marketplace.json
│  └─ plugin.json
├─ .cursor/
│  └─ rules/
│     └─ karpathy-guidelines.mdc
├─ skills/
│  ├─ karpathy-guidelines/
│  │  ├─ SKILL.md
│  │  ├─ agents/openai.yaml
│  │  └─ references/examples.md
│  ├─ karpathy-guidelines-zh/
│  │  ├─ SKILL.md
│  │  ├─ agents/openai.yaml
│  │  └─ references/examples.md
│  └─ index.md
├─ CLAUDE.md
├─ CONTRIBUTING.md
├─ CONTRIBUTING.zh.md
├─ CURSOR.md
├─ EXAMPLES.md
├─ README.md
├─ README.zh.md
└─ LICENSE
```

## Installation

### Option 1: Copy into your Codex skills directory

Copy one or both whole skill folders into:

```text
$CODEX_HOME/skills/
```

If `CODEX_HOME` is not set, a common fallback is:

```text
~/.codex/skills/
```

For example:

```text
~/.codex/skills/karpathy-guidelines
~/.codex/skills/karpathy-guidelines-zh
```

Important:

- Copy the whole folder, not only `SKILL.md`
- Keep the internal files such as `agents/openai.yaml` and `references/`
- After copying, your local path should look like:

```text
~/.codex/skills/karpathy-guidelines/SKILL.md
~/.codex/skills/karpathy-guidelines-zh/SKILL.md
```

### Option 2: Reference the skill by repository path

If your Codex environment supports filesystem-path invocation, use:

```text
<repo>/skills/karpathy-guidelines
<repo>/skills/karpathy-guidelines-zh
```

## Choose a Skill

- Use `karpathy-guidelines` for English prompts and English-facing workflows.
- Use `karpathy-guidelines-zh` for Chinese prompts and Chinese-facing workflows.
- Read `references/examples.md` only when the task needs concrete examples.

## First Use Examples

If you are not sure what to type first, copy one of these exactly:

English:

```text
Use $karpathy-guidelines to fix this bug with the smallest safe change. First list assumptions, then define verification.
```

Chinese:

```text
使用 $karpathy-guidelines-zh 修复这个 bug。先列出假设和验证步骤，再做最小修改。
```

You know it is working when the agent:

- explains assumptions before changing code
- prefers the smallest reasonable implementation
- avoids unrelated cleanup
- explains how success will be verified

## Other Integration Files

- [CLAUDE.md](./CLAUDE.md): root instruction file for project-default coding behavior
- [CURSOR.md](./CURSOR.md): how to use the committed Cursor rule as an always-apply default policy
- [EXAMPLES.md](./EXAMPLES.md): repository-level example set mirroring the upstream layout
- [`.cursor/rules/karpathy-guidelines.mdc`](./.cursor/rules/karpathy-guidelines.mdc): committed Cursor project rule
- [`.claude-plugin/plugin.json`](./.claude-plugin/plugin.json): Claude plugin definition
- [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json): marketplace metadata

## GitHub Sync Plugin

This repository also includes a plugin at [plugins/codex-skillsplus-sync](./plugins/codex-skillsplus-sync) that pulls guidance directly from the GitHub repository into the current project.

What it syncs:

- `.codex/skills/karpathy-guidelines`
- `.codex/skills/karpathy-guidelines-zh`
- `.cursor/rules/karpathy-guidelines.mdc`
- `CLAUDE.md`
- `.codex-skillsplus/EXAMPLES.md`

Important notes:

- the plugin uses a `PostToolUse` hook after file edits, plus a manual sync skill
- install-time or session-start auto-sync depends on what the runtime exposes to hooks
- project-root detection is best effort and will fail safely if the runtime does not expose a usable target directory

Beginner workflow:

1. Install the plugin.
2. Point it at a real project.
3. Run the sync once manually.
4. Confirm these now exist inside the project:
   - `.codex/skills/karpathy-guidelines`
   - `.codex/skills/karpathy-guidelines-zh`
   - `.cursor/rules/karpathy-guidelines.mdc`
   - `CLAUDE.md`
5. Start coding normally.

## Usage Notes

Use these skills when you want the agent to slow down slightly and produce cleaner, lower-risk changes. When installed as project guidance or explicitly activated as skills, they should be treated as default execution policy for non-trivial work, not as optional style suggestions.

Strongest setup:

1. Install the skill under `~/.codex/skills/`
2. Put `CLAUDE.md` in the project root or use the Cursor rule
3. Explicitly invoke the skill on important tasks

The two skills share the same core mindset:

1. Think before coding.
2. Keep it simple.
3. Make surgical changes.
4. Drive toward verifiable success.

## Included References

Each skill keeps `SKILL.md` concise and stores richer examples in:

- [skills/karpathy-guidelines/references/examples.md](./skills/karpathy-guidelines/references/examples.md)
- [skills/karpathy-guidelines-zh/references/examples.md](./skills/karpathy-guidelines-zh/references/examples.md)

Load those files only when the current task needs concrete examples of:

- hidden assumptions
- overengineered implementations
- drive-by refactors
- vague versus verifiable execution plans

## Attribution

These skills are inspired by Andrej Karpathy's public observations on common LLM coding pitfalls and adapted into a Codex-native skill format for reusable agent workflows.

## Contributing

New skills are welcome. Follow [CONTRIBUTING.md](./CONTRIBUTING.md) for naming, layout, documentation, and validation expectations.

## License

MIT
