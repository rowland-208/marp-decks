## Overview

This repository contains presentation slide decks built with [Marp](https://marp.app/), a Markdown-based slide framework. Each deck is a single `.md` file at the repository root.

## Session Guide

Start every editing session by rendering the slide deck for the user. Use marp --watch for live rendering in html.

Give the user a clickable file:// link to the html file.

## Common Marp Commands

```bash
# Export a deck to HTML
marp deck.md --output deck.html

# Export a deck to PDF
marp deck.md --pdf --output deck.pdf

# Watch mode (live preview)
marp --watch deck.md
```

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

Assume requirements are already installed. Try to run tools first. If that fails then use the initial-setup skill.
