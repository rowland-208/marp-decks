---
marp: true
theme: default
paginate: true
---

<!-- _class: lead -->

# Agentic AI with Claude Code and Open Claw

Cape Fear Makers Guild

---

# What is an AI Agent?

A model that doesn't just respond — it **acts**

- Receives a goal, not just a prompt
- Plans a sequence of steps
- Uses **tools** to interact with the world
- Observes results and adjusts

> "Give an AI a hammer and it will try to use it"

---

# The Agent Loop

```
┌─────────────────────────────────┐
│  Goal / Task                    │
└────────────────┬────────────────┘
                 ↓
          [ Think / Plan ]
                 ↓
          [ Use a Tool   ]  ← read files, run code,
                 ↓             search the web, call APIs
          [ Observe Result ]
                 ↓
         Done? ──→ Yes: respond
           ↓
           No: loop back
```

---

# Tools Are the Superpower

| Tool | What it does |
|------|-------------|
| Read / Write files | Access the codebase |
| Run shell commands | Execute code, tests |
| Web search / fetch | Get current info |
| Call APIs | Talk to external systems |

An agent with the right tools can do in seconds what takes humans minutes.

---

# Claude Code

Anthropic's agentic coding assistant — runs in your terminal

- Reads your entire codebase
- Writes, edits, and refactors files
- Runs tests and fixes failures
- Searches the web for docs
- Asks clarifying questions when needed

```bash
claude "add input validation to the login form"
```

---

# How Claude Code Works

1. You describe a task in plain English
2. It explores your repo (reads files, searches)
3. It makes a plan
4. It executes — editing files, running commands
5. It shows you what changed

All steps visible. You approve risky actions.

---

# Open Claw

An **open-source** Claude Code-compatible client

- Same tool protocol, your own front end
- Runs locally — full control over data
- Extensible: add custom tools, integrations
- Great for makers: hack it, extend it, embed it

---

# What Can You Build?

- **Coding assistants** tailored to your stack
- **Home automation agents** (read sensors, trigger actions)
- **Document pipelines** (ingest, summarize, file)
- **Repair shop helpers** (diagnose from symptoms)
- **Anything with a clear goal + tools**

The pattern is always the same: goal → tools → loop

---

# Live Demo

- Ask Claude Code to add a feature to a small project
- Watch the agent loop in action
- See tool calls, observations, and edits live

---

# Try It Yourself

**Claude Code**
```bash
npm install -g @anthropic-ai/claude-code
claude
```

**Anthropic API**
- claude.ai/api — free tier available

**Open Claw**
- github.com/open-claw/open-claw

---

# Key Takeaways

1. Agents = LLM + tools + a loop
2. The tools define what's possible
3. Claude Code is a polished example you can use today
4. Open Claw lets you go deeper and customize
5. Makers are well-positioned — you already think in systems

---

<!-- _class: lead -->

# Questions?

Cape Fear Makers Guild — March 2026

cfmg.io
