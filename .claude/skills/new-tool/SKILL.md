---
name: new-tool
description: Create a new tool in the tools/ directory. Use this when the user asks to create or add a new tool.
---

## Checklist

[ ] Identify tool language: python, bash, or javascript
[ ] Create a script file in tools/<script-name>.py
[ ] Update requirements.txt etc.
[ ] Create claude SKILL.md file

## Claude skills

Keep the skill simple and brief. The tool name should match the skill name. Use `uv run` in code snippets to encourage uv usage. Check existing skills for consistency.

## Package management

Use uv for python package management. Put requirements in tools/requirements.txt. Create a venv in the repo root.

Use pnpm for node package management. Create an env in the repo root.
