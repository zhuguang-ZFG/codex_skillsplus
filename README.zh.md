# Codex Skills Plus

[English](./README.md) | 简体中文

这是一个面向 Codex 的技能仓库，用来沉淀更可靠的编码工作流。当前仓库包含一个受 Andrej Karpathy 观点启发的技能，重点减少 LLM 在编程时常见的几类问题：隐藏假设、过度设计、顺手乱改，以及缺少可验证的成功标准。

## 当前技能

### `karpathy-guidelines`

路径：[skills/karpathy-guidelines](./skills/karpathy-guidelines)

这个技能本质上是一套“编码行为护栏”，适合在以下场景触发：

- 实现前先澄清假设
- 优先选择最简单可行方案
- 控制改动范围，只做与需求直接相关的修改
- 在动手前先定义验证方式和完成标准

尤其适合这些任务：

- 实现方案规划
- 代码审查
- 修复 bug
- 重构
- 调试
- 任何需要“小改动、强验证、低副作用”的非简单任务

## 为什么要做这个技能

Andrej Karpathy 曾指出，LLM 辅助编程里常出现这些模式：

- 模型会默默选一种理解然后直接执行
- 模型喜欢把简单问题做复杂
- 模型会顺手修改任务无关的周边代码
- 模型完成任务时没有明确、可验证的成功标准

这个仓库的目标，就是把这些观察整理成 Codex 可直接复用的 skill，让它能在真实代理工作流里反复触发和生效。

## 仓库结构

```text
codex_skillsplus/
├─ skills/
│  └─ karpathy-guidelines/
│     ├─ SKILL.md
│     ├─ agents/openai.yaml
│     └─ references/examples.md
├─ README.md
├─ README.zh.md
└─ LICENSE
```

## 安装方式

### 方式一：复制到本地 Codex skills 目录

把技能目录复制到本地 Codex skills 路径：

```text
$CODEX_HOME/skills/karpathy-guidelines
```

如果没有设置 `CODEX_HOME`，常见的默认目录是：

```text
~/.codex/skills/karpathy-guidelines
```

### 方式二：直接从仓库路径引用

如果你的 Codex 环境支持按文件路径引用 skill，可以直接使用：

```text
<repo>/skills/karpathy-guidelines
```

## 如何使用

当你希望代理放慢一点、先想清楚、尽量简化并带着验证去做时，可以显式调用这个技能：

```text
Use $karpathy-guidelines to review this coding task before making changes.
```

示例提示词：

- `Use $karpathy-guidelines to fix this bug with the smallest safe change.`
- `Use $karpathy-guidelines to review this refactor plan and trim unnecessary complexity.`
- `Use $karpathy-guidelines to define verification steps before implementing the API change.`

## 这个技能教什么

技能围绕四个核心原则展开：

1. 先想，再写。
先把假设、不确定点和歧义摊开，避免带着误解直接实现。

2. 简单优先。
只实现当前需求真正需要的最小代码，不提前为未来需求造架构。

3. 外科手术式修改。
只碰必须改的代码，保持原有风格，不做顺手“优化”。

4. 以可验证结果为目标。
把模糊任务转成可检查、可测试、可证明完成的目标。

## 附带参考内容

主文件 `SKILL.md` 保持轻量，具体案例放在这里：

- [skills/karpathy-guidelines/references/examples.md](./skills/karpathy-guidelines/references/examples.md)

只有在需要具体例子时再读取这个文件，比如：

- 如何识别隐藏假设
- 如何把过度设计改回简单实现
- 如何避免顺手重构
- 如何把模糊目标改写成可验证步骤

## 致谢与来源

这个技能的理念来自 Andrej Karpathy 公开分享的 LLM 编码常见陷阱观察，这里将其整理并适配为 Codex 原生可复用的 skill 结构。

## 许可证

MIT
