# Codex Skills Plus Sync Plugin

This plugin syncs project-local guidance files from the GitHub repository:

- `https://github.com/zhuguang-ZFG/codex_skillsplus`

## What it syncs

- `.codex/skills/karpathy-guidelines`
- `.codex/skills/karpathy-guidelines-zh`
- `.cursor/rules/karpathy-guidelines.mdc`
- `CLAUDE.md`
- `.codex-skillsplus/EXAMPLES.md`

## Behavior

- A manual sync is available through the bundled skill `codex-skillsplus-project-sync`.
- A `PostToolUse` hook refreshes the project after file edits.
- The sync script skips refreshes for 6 hours unless forced.

## Limitations

- The hook uses best-effort project root detection.
- If the runtime does not expose a usable project root, the script exits safely without writing.
