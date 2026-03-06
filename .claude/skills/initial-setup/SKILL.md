---
name: initial-setup
description: Use when marp is not installed or a tool fails to run.
---

# Initial Setup

Check for and install each dependency, skipping any already present.

Prefer yolo shell installs, e.g.,

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Never suggest a different dependency, e.g., don't use npm to install pnpm, and don't use bare python if uv isn't installed.

The user may need to restart shell after install. Instruct the user to start a new shell and start claude --resume. 

## 1. pnpm

Use pnpm for all node package management and node install.

```bash
pnpm --version
```

## 2. node

```bash
node --version
```

## 3. Marp CLI

```bash
marp --version
```

## 4. uv

Use uv for all python package management and install.

```bash
uv --version
```

## 5. Python venv and requirements

```bash
uv venv && uv pip install -r tools/requirements.txt
```

