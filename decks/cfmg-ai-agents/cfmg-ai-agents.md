---
marp: true
theme: default
paginate: true
style: |
  :root {
    --color-background: #faf9f5;
    --color-foreground: #141413;
    --color-highlight: #d97757;
    --color-dimmed: #b0aea5;
  }
  section {
    background: #faf9f5;
    color: #141413;
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
  }
  section::after {
    color: #b0aea5;
  }
  h1 {
    color: #d97757;
  }
  h2 {
    color: #d97757;
    border-bottom: 2px solid #e8e6dc;
    padding-bottom: 8px;
  }
  h3 {
    color: #141413;
  }
  strong {
    color: #d97757;
  }
  a {
    color: #6a9bcc;
  }
  li {
    color: #141413;
  }
  code {
    background: #e8e6dc;
    color: #141413;
  }
  pre code {
    background: transparent;
  }
  pre {
    background: #e8e6dc;
    border: 1px solid #b0aea5;
    border-radius: 8px;
  }
  table {
    color: #141413;
  }
  th {
    background: #e8e6dc;
    color: #d97757;
  }
  td {
    background: #faf9f5;
  }
---

<!-- _class: lead -->

# Agentic AI with Claude Code

James Rowland
Cape Fear Makers Guild
April 7, 2026
[github.com/rowland-208/marp-decks](https://github.com/rowland-208/marp-decks)

---

# Setup

Who will follow along?

1. **Install Claude Code** — open a terminal and run:
   ```bash
   curl -fsSL https://claude.ai/install.sh | bash
   ```
2. **Authenticate** — run `claude` and follow the prompts

**Note**: Claude Code requires a paid subscription $17/mo
If you're interested in alternatives please ask after the talk

---

# AI Pricing

- Pricing is **variable** right now — the market is still shaking out
- **Claude Code** — reasonable $17/mo, but you can burn through limits fast
- **Cursor** — $20/mo with free tier available, subsidized by vc funding
- **GitHub Copilot** — $10/mo with free tier available, subsidized by microsoft
- **API** — pay for what you use, unlimited usage but may encounter throttling
- **OpenCode + OpenRouter** — often totally free but models are highly variable, non-trivial setup
- **Key insight**: get used to shifting sands, models are commodities not secret sauce

---

<!-- _class: lead -->

# What Should We Build?

Let's brainstorm an app together

---

# Build It

Don't be afraid of the terminal — it's just a **text interface** to your computer

- You type a command, it does something, it shows you the result
- Everything you do with a mouse, you can do with text
- **Why agents need it**: agents act by running commands — the terminal is how they interact with your computer
- Technically agents can use GUIs but it burns through limits faster and is clunky

```bash
ls               # list files and directories
cd repos         # move to a directory
mkdir <app-name> # make a new directory
cd <app-name>
claude           # start claude and prompt it
```

---

# What Just Happened?

- Claude **wrote files**, **ran commands**, **hit errors**, **fixed them**, and **iterated**
- Exactly what you would do with terminal commands
- It read error messages, adjusted its approach, and tried again
- This is what makes it an **agent**, not just a chatbot

---

# Tokens & Context

**Tokens** — chunks of text the model reads and writes
- "hello" = 1 token, "unbelievable" = 3 tokens
- ~4 characters per tokens
- Code is more token-dense than prose

**Context** — the window of text the model can see at once
- Too much = slow and expensive
- Too little = the agent forgets what it's doing

```bash
/context   # run this in Claude Code to see current usage
```

---

<!-- _class: lead -->

# CLAUDE.md

Project-level instructions that Claude reads **every session**

- Lives in your project root
- Tell Claude your preferences, conventions, and constraints
- E.g. "Yes Caption"
- Claude follows them automatically

---

<!-- _class: lead -->

# Build a Skill

A skill is a **reusable prompt** you invoke with a slash command

```
/my-skill
```

- Saved as a markdown file in `.claude/skills/`
- Can control tool use, include files, run scripts
- Think of it as a recipe Claude follows, or **pseudocode** that claude executes
- Or like coding scripts with LLM as the interpreter

**What skill should we add?**

---

<!-- _class: lead -->

# Superpowers Plugin

A collection of skills for **planning**, **TDD**, **debugging**, and more

```bash
/plugin install superpowers@claude-plugins-official
```

Let's rebuild our app with superpowers active and see the difference:
- Brainstorming before building
- Step-by-step planning
- Review checkpoints


Select plugins carefully, build your own skills, vanilla models+harnesses are getting better over time

---

# What Changed?

- Same tool, same model, same terminal
- Brainstorming helped us make a better plan
- Subagent development keeps the main agent on task and keeps context clean
- The agent didn't change — **we changed how we directed it**

---

# Agentic OS Architecture

Analogy: linux is a collection of components

```
              ┌────────────────┐
              │  User Input    │
              │ terminal, chat │
              └───────┬────────┘
 ┌───────────┐  ┌─────▼─────┐   ┌──────────┐
 │  Config   │  │ Harness   │   │  Model   │
 │ CLAUDE.md,│─►│           │◄─►│ Claude,  │
 │ skills,   │  │ Claude    │   │ GPT,     │
 │ hooks     │  │ Open Claw │   │ Gemini   │
 └───────────┘  └─────┬─────┘   └──────────┘
          ┌───────────▼────────────┐
          │    Runtime + Tools     │
          │ terminal,     git, gh, │
          │  files       npm, cli  │
          └────────────────────────┘
```

---

# Agent

**LLM + tools + iteration loop**

- **LLM** — the brain, generates text and decisions
- **Tools** — terminal, file editor, memory, web search, Discord, WhatsApp, etc.
- **Iteration** — run a command, read the output, decide what to do next

The loop is what separates an agent from a chatbot:
a chatbot answers; an agent **acts, observes, and adjusts**

Humans need iteration to get it right too. A good idea is only as good as your ability to try it.

---

# Harness

The code that **connects the AI to tools**

| Harness | Who makes it | Open source | Coding First | Hands Off |
|---------|-------------|--------------|----------------------|-----------|
| Claude Code | Anthropic | No | Yes | Kind of |
| Cursor | Cursor | No | Yes | No |
| Open Code | Community | Yes | Yes | No |
| Open Claw | OpenAI | Yes | No | Yes |
| Cowork | Anthropic | No | No | Yes |

The harness determines what the agent **can do** — same model, different harness, different capabilities, e.g. terminal, gui, files, memory, connect to discord/whatsapp

---

# Model

The AI brain itself — you have choices

- **Big labs** — OpenAI (GPT), Anthropic (Claude), Google (Gemini)
- **OpenRouter** — one API, access to many models
- **Self-hosted** — run models on your own hardware (Gemma, Qwen)

**Harness + model interact**: Claude Code works best with Claude models, Copilot works best with OpenAI models

Pick based on your task, budget, and privacy needs 

---

# Skills & Config

How you customize agent behavior — multiple layers:

| Config | Scope | Standard? |
|--------|-------|-----------|
| **CLAUDE.md** / **AGENTS.md** | Project instructions | Most harnesses |
| **Skills** | Reusable workflows | Claude format spreading |
| **Hooks** | Shell triggers on events | Claude Code only |
| **settings.json** | Harness settings | Claude Code only |

---

# Skills & Config

Skills:
- Control **which tools** the agent can use
- **Inherit files** for context
- **Combine with scripts** for complex workflows
- Use the **skill builder skill** to create new skills
- Or just ask vanilla Claude to write one for you

---

# Cloud vs Local

Where does the harness run

**Local** (your laptop)
- Easier to manage
- Great for hobby projects
- No monthly server costs

**Cloud** (remote server)
- Runs all the time, accessible from anywhere
- Needed for bots, APIs, shared apps

Self hosting is a talk in its own right

---

# Markdown

The universal data format for agents

- **Config** is markdown — CLAUDE.md, skills, docs
- **Data store** — use markdown files as a lightweight database
- **Open format** — no vendor lock-in, works everywhere
- **Obsidian** — great viewer/editor for markdown vaults
- Agents read and write markdown natively — it's their first language
- Claude can work in your obsidian knowledgebase, e.g., organizing, linking, summarizing

---

# Git

Your **safety net** and collaboration layer

- Agents can use it on your behalf, just ask "set up a git repo" 
- Version control means you can always undo agent mistakes
- A **git repo** is a .git folder in your project, that's all there is to it
- **GitHub** is a way to publish a git repo online for sharing
- Use GitHub instead of dropbox/google drive/etc.
- Not great for video, photos, etc.; history is expensive

---

# Safety

Claude's bash tool can do **almost anything** on your machine

- By default, Claude **asks permission** before running commands
- `--dangerously-skip-permissions` — skips all prompts
  - Useful for demos, risky for real work
  - Better to specify explicit allow permissions in .claude/settings.json
  - Difficult but more secure to run in a docker container

Rule of thumb: if you wouldn't let a stranger run the command, don't skip permissions

---

# CLI Tools

**Token-efficient** — commands are short by design (~60 characters)
- Built for humans in small terminals — naturally concise for agents too

**Better than MCP** for personal projects
- MCP adds complexity for access control you don't need solo
- CLI tools are simpler: install, authenticate, use

**Auth once, agent uses it forever**
```bash
gh auth login        # authenticate GitHub CLI
```

Skip MCP for personal projects — just use the CLI
