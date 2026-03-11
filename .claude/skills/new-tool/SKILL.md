---
name: new-tool
description: Create a new tool as a Claude skill. Use this when the user asks to create or add a new tool.
---

## Checklist

[ ] Identify tool language: python, bash, or javascript
[ ] Create a skill directory at `.claude/skills/<tool-name>/`
[ ] Add `SKILL.md` to the skill directory
[ ] Add the tool script (e.g., `<tool-name>.py`) to the skill directory
[ ] Add `requirements.txt` to the skill directory (for python tools)
[ ] Add `.env` to the skill directory if API keys are needed (gitignored)

## Skill directory structure

Each tool lives inside its own skill directory with all dependencies co-located:

```
.claude/skills/<tool-name>/
  SKILL.md
  <tool-name>.py
  requirements.txt
  .env (gitignored, if needed)
```

## Claude skills

Keep the skill simple and brief. The tool name should match the skill name. Use `uv run --with-requirements` in code snippets. Check existing skills for consistency.

Example SKILL.md command snippet:

```bash
uv run --with-requirements .claude/skills/<tool-name>/requirements.txt .claude/skills/<tool-name>/<tool-name>.py <args>
```

## Package management

Use uv for python package management. Each skill has its own `requirements.txt` in the skill directory. Use `click` for CLI argument parsing.
