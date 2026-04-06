---
marp: true
theme: default
paginate: true
---

<!-- _class: lead -->

# Agentic AI with Claude Code

James Rowland
Cape Fear Makers Guild
April 7, 2026
[github.com/rowland-208/marp-decks](https://github.com/rowland-208/marp-decks)

---

# Setup

1. **Claude desktop app** — [claude.ai/download](https://claude.ai/download)
2. **Claude subscription** — [claude.ai/upgrade](https://claude.ai/upgrade)
4. **Obsidian** — [obsidian.md](https://obsidian.md)

---

<!-- _class: lead -->

# Demo: Claude in the Browser

Chat with Claude on claude.ai — ask it to create a Connections puzzle:

> Create a 4x4 grid of 16 words. These words must be divisible into four groups of four that share a common, hidden theme. The themes should be: 1. Equipment at a makerspace, 2. Synonyms for 'fast', 3. Words that follow 'Book', 4. Movie characters that are engineers

**Why this works**: no search engine can do this — the answer requires creative synthesis over novel constraints

---

<!-- _class: lead -->

# Demo: Walled Garden vs Terminal

> Create and serve a hello world webpage

**Browser** — can write the HTML, but can't serve it. The browser is a walled garden.

**Claude Code** — writes the file, starts a server, and it works. The terminal is how you break out.

---

<!-- _class: lead -->

# Demo: Build a Game

> Build a multiplayer top-down dungeon crawler using React, Phaser, Express, and SQLite. 8-bit pixel art style with a muted color palette, pixel art avatar editor, NPC monsters, weapon/health/mana loot, and a small set of spells. The full dungeon map should be visible with multiple rooms. Start by making a plan.

We'll use `--dangerously-skip-permissions` — don't try this at home

Claude can `rm -rf /`, install malware, or push to your repos without asking

---

<!-- _class: lead -->

# Demo: Knowledge Base

1. New folder, open in **Obsidian**, add some markdown
2. Ask Claude to summarize

Agent brain: markdown is the data, Obsidian is the viewer

---

<!-- _class: lead -->

# Demo: CLAUDE.md & Skills

- Create two notes with related content

> Create a /link skill that finds related notes and adds wikilinks between them

- Use the `/link` skill
- Add a **CLAUDE.md** with a wikilinks preference

---

# Claude Ecosystem

- **Multiple harnesses**: chat, code, remote code, desktop
- **CLAUDE.md & skills** for project-level config and automation
- **Built-in tools**: task management, planning, memory
- **Remote control**: interact from your phone, like Open Claw but terminal-native
- **Sub-agents**: spin up parallel workers for complex tasks
- **Hooks**: trigger shell commands on agent events

---

# Iteration Makes Problem Solving Work

- **LLM alone** — can think, write, answer, but stuck in a box
- **Agent** — LLM + tools + feedback loop — it can *act*, observe results, and adjust
- **Building requires testing** — thinking isn't enough, you have to run the code, see what breaks, fix it — agents do this automatically
- Everything we just built used an **agent**, not just a chatbot

---

![w:900 center](tool-iteration.png)

---

![w:900 center](length-of-tasks-log.png)

---

# Runtime Environment

- Agents need a world to act in
- **Linux shell** is the best
- **CLI tools** give broader access
- The runtime is the house; the tools are the furniture

---

# Agentic Operating System

Pick and choose the parts

- **Model**: Claude → open models
- **Harness**: Claude Code → Open Code, Codex, GitHub Copilot, etc.
- **Text format**: Markdown — the standard, works everywhere
- **Version control**: Git — the standard, GitHub is just one host
- **Viewer**: Obsidian is open, but any markdown viewer works

---

# CFMB — Our Discord Bot

<style scoped>section { position: relative; } section img[alt="logo"] { position: absolute; top: 30px; right: 30px; width: 120px; }</style>

![logo](cfmg.png)

Claude Code and the other harnesses are just wrappers around models — you can build your own

- Custom agent tailored to our community
- [github.com/rowland-208/cfmb](https://github.com/rowland-208/cfmb/tree/main/cfmb)

---

# Beyond Localhost

Our hello world demo only works on **localhost** — no one else can see it

- **GitHub Pages** solves this for static sites
- For self-hosted apps that need a network, **Tailscale** is a great option
- Encrypted mesh VPN — no port forwarding, no firewall config
- Your devices and friends' devices on one private network


