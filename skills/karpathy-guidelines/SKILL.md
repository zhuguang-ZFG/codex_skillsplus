---
name: karpathy-guidelines
description: Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, debugging, or refactoring code to avoid hidden assumptions, overengineering, broad unrelated edits, and vague success criteria. Trigger this skill for implementation planning, code review, bug fixes, and any task where simple, surgical, verifiable changes matter.
---

# Karpathy Guidelines

Use this skill as a default execution policy for non-trivial coding work when it is active. Treat the principles below as mandatory operating constraints unless the user explicitly asks for an exception. Bias toward clarity, simplicity, and verification instead of silently making assumptions or producing broad speculative changes.

These guidelines are inspired by Andrej Karpathy's observations about common LLM coding failure modes. For trivial edits, apply them with judgment rather than forcing a heavyweight process.

## Follow the Core Principles

### 1. Think Before Coding

Surface uncertainty before implementation.

- State assumptions explicitly instead of acting on them silently.
- Present multiple plausible interpretations when the request is ambiguous.
- Name tradeoffs when there is more than one reasonable path.
- Pause and ask for clarification when missing information would change the implementation materially.

Prefer a short clarification or assumption list over confident guessing.

### 2. Keep It Simple

Implement the minimum code that solves the current problem.

- Avoid abstractions for single-use code.
- Avoid optional configuration, extensibility, or flexibility that was not requested.
- Avoid speculative error handling for impossible or unsupported scenarios.
- Prefer the shortest implementation a strong senior engineer would still consider clean.

If a solution feels "architected" rather than needed, simplify it.

### 3. Make Surgical Changes

Edit only what the request requires.

- Match the surrounding code style.
- Do not refactor adjacent code unless the request requires it.
- Do not rewrite comments, formatting, or naming outside the necessary change set.
- Remove unused code only when your own changes created it.
- Mention unrelated problems if needed, but do not fix them opportunistically.

Every changed line should trace back to the user's request or to verification for that request.

### 4. Drive Toward Verifiable Success

Turn vague tasks into checks that can be proven complete.

- For bugs, reproduce the issue first when practical.
- For behavior changes, write or identify the check that proves the new behavior.
- For refactors, verify behavior before and after.
- For multi-step work, state a short plan where each step has a concrete verification point.

Prefer "write failing test, fix code, make test pass" over "make it work."

## Use This Execution Pattern

When using this skill, structure the work in this order:

1. Restate the task in concrete terms.
2. List assumptions or ambiguities that could change the implementation.
3. Choose the simplest viable approach.
4. Define success criteria or verification steps.
5. Implement only the necessary change.
6. Run the narrowest useful verification.
7. Report what changed, what was verified, and any remaining uncertainty.

For multi-step tasks, use this compact template:

```text
1. [step] -> verify: [check]
2. [step] -> verify: [check]
3. [step] -> verify: [check]
```

## Load Examples Only When Needed

Read [references/examples.md](references/examples.md) when the task would benefit from concrete examples of:

- hidden assumptions that should be surfaced
- overengineered solutions that should be simplified
- broad edits that should be narrowed
- vague goals that should be rewritten into verifiable checks

Do not load the examples file for every task. Keep it as on-demand reference material.
