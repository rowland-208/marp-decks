---
name: initial-setup
description: Use when marp is not installed or a tool fails to run.
---

# Initial Setup

Check for and install each dependency, skipping any already present.

## 1. pnpm

```bash
pnpm --version
```

## 2. uv

```bash
uv --version
```

## 3. Python venv and requirements

```bash
uv venv && uv pip install -r tools/requirements.txt
```

## 4. Marp CLI

```bash
marp --version
```
