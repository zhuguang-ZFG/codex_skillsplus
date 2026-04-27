# Codex Skills Plus

[English](./README.md) | 简体中文

[![技能数](https://img.shields.io/badge/skills-2-1f6feb)](./skills)
[![许可证](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

这是一个面向 Codex 的技能仓库，用来沉淀更可靠的编码工作流。仓库中的 skill 可以直接复用在编码代理场景里，帮助模型想得更清楚、改得更克制、验得更扎实。

![Codex Skills Plus 封面图](./docs/assets/social-preview.png)

## 仓库特点

- 提供可直接使用的 Codex skill 目录
- 聚焦真实编码任务而不是空泛提示词
- 提供中英文双语说明
- 主技能文件精简，复杂示例按需加载
- 提供可浏览的技能目录页 [skills/index.md](./skills/index.md)
- 同时保留了 Claude / Cursor 的外围接入文件

## 当前技能

### `karpathy-guidelines`

路径：[skills/karpathy-guidelines](./skills/karpathy-guidelines)

这是一个英文优先的编码行为护栏，适合在以下场景触发：

- 实现前先澄清假设
- 优先选择最简单可行方案
- 控制改动范围，只做与需求直接相关的修改
- 在动手前先定义验证方式和完成标准

适合这些任务：

- 实现方案规划
- 代码审查
- 修复 bug
- 重构
- 调试
- 任何需要“小改动、强验证、低副作用”的非简单任务

示例：

```text
Use $karpathy-guidelines to fix this bug with the smallest safe change.
```

### `karpathy-guidelines-zh`

路径：[skills/karpathy-guidelines-zh](./skills/karpathy-guidelines-zh)

这是同一套工作方法的中文优先版本，更适合中文提示词、中文需求讨论、中文审查和中文实现规划。

适合这些任务：

- 中文代码审查
- 中文需求澄清
- 中文实现规划
- 中文 bug 修复
- 需要用中文定义验证步骤的任务

示例：

```text
使用 $karpathy-guidelines-zh 先审视这个改动方案，再开始实现。
```

另见：[技能目录](./skills/index.md)
另见：[CURSOR.md](./CURSOR.md)
另见：[CLAUDE.md](./CLAUDE.md)

## 为什么要做这个仓库

Andrej Karpathy 曾指出，LLM 辅助编程里反复出现几类问题：

- 模型会默默选一种理解然后直接执行
- 模型喜欢把简单问题做复杂
- 模型会顺手修改任务无关的周边代码
- 模型完成任务时缺少明确、可验证的成功标准

这个仓库的目标，就是把这些观察整理成 Codex 可以直接复用的 skill，让它们在真实代理工作流中反复触发并稳定发挥作用。

## 仓库结构

```text
codex_skillsplus/
├─ docs/
│  └─ assets/
│     └─ social-preview.png
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
├─ README.md
├─ README.zh.md
└─ LICENSE
```

## 安装方式

### 方式一：复制到本地 Codex skills 目录

把任意 skill 目录复制到：

```text
$CODEX_HOME/skills/
```

如果没有设置 `CODEX_HOME`，常见默认目录是：

```text
~/.codex/skills/
```

例如：

```text
~/.codex/skills/karpathy-guidelines
~/.codex/skills/karpathy-guidelines-zh
```

### 方式二：按仓库路径引用

如果你的 Codex 环境支持按文件系统路径引用 skill，可以直接使用：

```text
<repo>/skills/karpathy-guidelines
<repo>/skills/karpathy-guidelines-zh
```

## 使用建议

当你希望代理稍微放慢一点、先想清楚、尽量简化并带着验证去做时，就适合调用这些技能。

两套技能共享同样的核心原则：

1. 先想，再写。
2. 简单优先。
3. 外科手术式修改。
4. 以可验证结果为目标。

选择建议：

- 面向英文提示词和英文沟通，用 `karpathy-guidelines`
- 面向中文提示词和中文沟通，用 `karpathy-guidelines-zh`

## 其他接入文件

- [CLAUDE.md](./CLAUDE.md)：适合根目录指令文件式接入
- [CURSOR.md](./CURSOR.md)：说明如何在 Cursor 中使用当前仓库规则
- [EXAMPLES.md](./EXAMPLES.md)：保留了与上游一致的仓库级案例文件
- [`.cursor/rules/karpathy-guidelines.mdc`](./.cursor/rules/karpathy-guidelines.mdc)：已提交的 Cursor 项目规则
- [`.claude-plugin/plugin.json`](./.claude-plugin/plugin.json)：Claude 插件定义
- [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json)：插件市场元数据

## GitHub 同步插件

仓库里还增加了一个插件：[plugins/codex-skillsplus-sync](./plugins/codex-skillsplus-sync)。它会从 GitHub 仓库把这些内容同步到当前项目：

- `.codex/skills/karpathy-guidelines`
- `.codex/skills/karpathy-guidelines-zh`
- `.cursor/rules/karpathy-guidelines.mdc`
- `CLAUDE.md`
- `.codex-skillsplus/EXAMPLES.md`

注意：

- 插件目前通过 `PostToolUse` hook 在写入后自动刷新，同时也带一个手动同步 skill
- “安装时立即同步”或“会话刚开始就同步”是否能完全自动，取决于运行时对 hook 的支持
- 项目根目录检测采用保守策略，检测不到时会安全退出，不会乱写路径

## 附带参考内容

每个 skill 都让 `SKILL.md` 保持简洁，把更丰富的案例放在：

- [skills/karpathy-guidelines/references/examples.md](./skills/karpathy-guidelines/references/examples.md)
- [skills/karpathy-guidelines-zh/references/examples.md](./skills/karpathy-guidelines-zh/references/examples.md)

只有在当前任务需要具体案例时再加载这些文件，例如：

- 如何识别隐藏假设
- 如何把过度设计改回简单实现
- 如何避免顺手重构
- 如何把模糊任务改写成可验证步骤

## 致谢与来源

这些技能的理念来自 Andrej Karpathy 公开分享的 LLM 编码常见陷阱观察，这里将其整理并适配为 Codex 原生可复用的 skill 结构。

## 许可证

MIT
