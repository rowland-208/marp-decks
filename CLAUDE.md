# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About

This repository contains presentation slide decks built with [Marp](https://marp.app/), a Markdown-based slide framework. Each deck is a single `.md` file at the repository root.

## Common Commands

```bash
# Export a deck to HTML
marp deck.md --output deck.html

# Export a deck to PDF
marp deck.md --pdf --output deck.pdf

# Watch mode (live preview)
marp --watch deck.md
```

Assume marp is installed. If you encounter an error then install it with

```bash
pnpm install -g @marp-team/marp-cli
```

Assume pnpm is installed. If you encounter an error then guide the user through install. Always use pnpm, never use npm, nvx, etc.

## Slide Format

Marp slides are written in Markdown with YAML front matter:

```markdown
---
marp: true
theme: default
paginate: true
---

# Slide 1

Content here

---

# Slide 2

Content here
```

Slide separators are `---` on their own line. Global directives go in the front matter; per-slide directives use HTML comment syntax (`<!-- _class: lead -->`).

## Repository Structure

Each deck gets a directory. The directory and markdown slide share the same name. Deck directories contain additional images and content referenced by the deck. 

root/
-- decks/
---- cfmg-ai-agents/
------ cfmg-ai-agents.md
------ agents-architecture.png
------ lobster-logo.png
---- laser-cutter-101/
------ laser-cutter-101.md
------ omtech.png
-- tools/
---- generate-image.py
---- upload.sh

## Tools

Try to run tools first. If that fails then guide the user to install and configure. 
