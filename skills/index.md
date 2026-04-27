# Skill Catalog

English | [简体中文说明请见仓库首页](../README.zh.md)

This directory contains Codex-ready skills that can be copied into a local skills folder or referenced directly by path.

## Available Skills

### `karpathy-guidelines`

Path: [./karpathy-guidelines](./karpathy-guidelines)

English-first behavioral guidelines for coding tasks. Use it when you want an agent to:

- surface assumptions before implementing
- prefer the simplest viable solution
- keep changes narrow and request-driven
- define verification steps before or during implementation

Good fit for:

- planning implementation
- reviewing code
- fixing bugs
- refactoring with restraint
- debugging tasks that need clear success criteria

Example:

```text
Use $karpathy-guidelines to review this task and define the smallest safe implementation plan.
```

### `karpathy-guidelines-zh`

Path: [./karpathy-guidelines-zh](./karpathy-guidelines-zh)

Chinese-first version of the same workflow. Use it when the surrounding task, conversation, or deliverable should stay in Chinese.

适合：

- 中文需求澄清
- 中文代码审查
- 中文实现规划
- 中文 bug 修复
- 中文验证步骤整理

示例：

```text
使用 $karpathy-guidelines-zh 先梳理假设和验证步骤，再开始修改代码。
```

## Installation Reminder

Copy a skill folder into:

```text
$CODEX_HOME/skills/
```

Common fallback location:

```text
~/.codex/skills/
```

Or reference a skill directly from this repository path if your setup supports it.
