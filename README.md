# marp-decks

Presentation slide decks built with [Marp](https://marp.app/), a Markdown-based slide framework.

## Getting Started

This project is designed to be used with [Claude Code](https://claude.ai/code).

1. Install Claude Code if you haven't already
2. Clone this repo and open it in your terminal
3. Run `claude` and use `/initial-setup` to install dependencies
4. Use `/generate-image` to create images for your decks

## Manual Setup

```bash
pnpm install -g @marp-team/marp-cli
uv venv && uv pip install -r tools/requirements.txt
```

## Usage

```bash
# Export a deck to HTML
marp decks/my-deck/my-deck.md --output decks/my-deck/my-deck.html

# Export a deck to PDF
marp decks/my-deck/my-deck.md --pdf --output decks/my-deck/my-deck.pdf

# Live preview
marp --watch decks/my-deck/my-deck.md
```
