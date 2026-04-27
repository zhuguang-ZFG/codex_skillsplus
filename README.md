# Codex Skills Plus

English | [简体中文](./README.zh.md)

[![Skills](https://img.shields.io/badge/skills-2-1f6feb)](./skills)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

Curated Codex skills for more reliable coding workflows. This repository packages reusable skill folders that help coding agents think more clearly, change less, and verify more.

## Highlights

- Ready-to-use Codex skill folders
- Focus on practical coding workflows
- English and Chinese documentation
- Lightweight skill bodies with on-demand references

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

Example:

```text
使用 $karpathy-guidelines-zh 先审视这个改动方案，再开始实现。
```

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
├─ skills/
│  ├─ karpathy-guidelines/
│  │  ├─ SKILL.md
│  │  ├─ agents/openai.yaml
│  │  └─ references/examples.md
│  └─ karpathy-guidelines-zh/
│     ├─ SKILL.md
│     ├─ agents/openai.yaml
│     └─ references/examples.md
├─ README.md
├─ README.zh.md
└─ LICENSE
```

## Installation

### Option 1: Copy into your Codex skills directory

Copy any skill folder into:

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

### Option 2: Reference the skill by repository path

If your Codex environment supports filesystem-path invocation, use:

```text
<repo>/skills/karpathy-guidelines
<repo>/skills/karpathy-guidelines-zh
```

## Usage Notes

Use these skills when you want the agent to slow down slightly and produce cleaner, lower-risk changes.

The two skills share the same core mindset:

1. Think before coding.
2. Keep it simple.
3. Make surgical changes.
4. Drive toward verifiable success.

Choose:

- `karpathy-guidelines` for English prompts and English-facing workflows
- `karpathy-guidelines-zh` for Chinese prompts and Chinese-facing workflows

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

## License

MIT
