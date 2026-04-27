# Codex Skills Plus

English | [简体中文](./README.zh.md)

Curated Codex skills for more reliable coding workflows. This repository currently includes a Karpathy-inspired skill that helps coding agents avoid common LLM failure modes such as hidden assumptions, overengineering, broad unrelated edits, and weak verification.

## Included Skill

### `karpathy-guidelines`

Path: [skills/karpathy-guidelines](./skills/karpathy-guidelines)

This skill is a behavioral guardrail for coding tasks. It is designed for situations where the agent should:

- surface assumptions before implementing
- prefer the simplest viable solution
- keep diffs narrow and directly tied to the request
- define success in testable, verifiable terms

It is especially useful for:

- implementation planning
- code review
- bug fixing
- refactoring
- debugging
- any non-trivial task where minimal, surgical changes matter

## Why This Exists

Andrej Karpathy has pointed out a set of recurring problems in LLM-assisted coding:

- models silently choose an interpretation and run with it
- models overcomplicate simple tasks
- models touch adjacent code that was not part of the request
- models complete work without strong success criteria

This repository packages those ideas into a Codex-compatible skill so they can be reused directly in agent workflows.

## Repository Structure

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

## Installation

### Option 1: Copy into your Codex skills directory

Copy the skill folder into your local Codex skills path:

```text
$CODEX_HOME/skills/karpathy-guidelines
```

If `CODEX_HOME` is not set, the common fallback is:

```text
~/.codex/skills/karpathy-guidelines
```

### Option 2: Use directly from this repository

If your Codex setup supports referencing a skill by filesystem path, point it at:

```text
<repo>/skills/karpathy-guidelines
```

## How to Use

Invoke the skill explicitly when you want the agent to slow down, simplify, and verify:

```text
Use $karpathy-guidelines to review this coding task before making changes.
```

Example prompts:

- `Use $karpathy-guidelines to fix this bug with the smallest safe change.`
- `Use $karpathy-guidelines to review this refactor plan and trim unnecessary complexity.`
- `Use $karpathy-guidelines to define verification steps before implementing the API change.`

## What the Skill Teaches

The skill centers on four principles:

1. Think before coding.
State assumptions, surface ambiguity, and ask when missing details would change the implementation.

2. Keep it simple.
Implement the minimum code needed for the current requirement, with no speculative architecture.

3. Make surgical changes.
Touch only the lines required by the request, match existing style, and avoid unrelated cleanup.

4. Drive toward verifiable success.
Turn vague tasks into concrete checks, tests, or measurable outcomes.

## Included References

The skill keeps the main `SKILL.md` lightweight and places concrete examples in:

- [skills/karpathy-guidelines/references/examples.md](./skills/karpathy-guidelines/references/examples.md)

Load that file only when you need examples of:

- hidden assumptions
- overengineered implementations
- drive-by refactors
- vague versus verifiable execution plans

## Attribution

This skill is inspired by Andrej Karpathy's public observations on common LLM coding pitfalls and adapted into a Codex-native skill format for reusable agent workflows.

## License

MIT
