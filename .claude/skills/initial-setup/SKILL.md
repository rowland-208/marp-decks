---
name: initial-setup
description: Walk the user through installing project dependencies (pnpm, uv, marp). Use when the user is setting up the project for the first time.
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
