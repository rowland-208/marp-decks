---
marp: true
theme: default
paginate: true
style: |
  :root {
    --color-background: #1a1b26;
    --color-foreground: #c0caf5;
    --color-highlight: #7aa2f7;
    --color-dimmed: #565f89;
  }
  section {
    background: linear-gradient(180deg, #1a1b26 0%, #1e2030 40%, #24283b 100%);
    color: #c0caf5;
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
  }
  section::after {
    color: #565f89;
  }
  h1 {
    color: #7aa2f7;
    text-shadow: 0 0 30px rgba(122, 162, 247, 0.3);
  }
  h2 {
    color: #7aa2f7;
    border-bottom: 2px solid #3b4261;
    padding-bottom: 8px;
  }
  h3 {
    color: #9aa5ce;
  }
  strong {
    color: #bb9af7;
  }
  a {
    color: #7aa2f7;
  }
  li {
    color: #a9b1d6;
  }
  code {
    background: #292e42;
    color: #9ece6a;
  }
  pre code {
    background: transparent;
  }
  pre {
    background: #292e42;
    border: 1px solid #3b4261;
    border-radius: 8px;
  }
  table {
    border-collapse: collapse;
    width: 100%;
  }
  th {
    background: #292e42;
    color: #7aa2f7;
    border: 1px solid #3b4261;
    padding: 10px;
  }
  td {
    background: rgba(30, 32, 48, 0.7);
    border: 1px solid #3b4261;
    padding: 10px;
    color: #a9b1d6;
  }
  blockquote {
    border-left: 4px solid #bb9af7;
    color: #9aa5ce;
    font-style: italic;
  }
  section.title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: radial-gradient(ellipse at 50% 120%, #292e42 0%, #1e2030 50%, #1a1b26 100%);
  }
  section.title h1 {
    font-size: 2.5em;
    border: none;
  }
  section.light h2 {
    color: #1a1b26;
    border-bottom-color: #ccc;
  }
  section.light strong {
    color: #7c3aed;
  }
  section.light li {
    color: #333;
  }
  section.closing {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: radial-gradient(ellipse at 50% 120%, #292e42 0%, #1e2030 50%, #1a1b26 100%);
  }
---

<!-- _class: title -->
<!-- _paginate: false -->
<!-- _backgroundColor: #121525 -->

![w:300](title.png)

# Skills as Code
### Claude Skills Are a New Kind of Programming

---

## What Is a Skill?

- A **reusable unit of functionality** — invoked by name, like calling a function
- Written in natural language, stored as markdown files
- Takes input, performs work, produces output
- Lives in `.claude/skills/` — version-controlled alongside your code

```
.claude/skills/
├── generate-deck/SKILL.md
├── verify/SKILL.md
├── publish/SKILL.md
└── generate-image/SKILL.md
```

---

## Skills Are Functions

| Programming Concept | Skill Equivalent |
|---|---|
| Function definition | `SKILL.md` file with instructions |
| Function call | `/skill-name` invocation |
| Parameters | Arguments passed in the user prompt |
| Return value | The artifact produced (file, commit, output) |
| Library / module | A directory of related skills |

The mental model maps directly — skills **are** functions for an AI runtime.

---

<!-- _backgroundColor: #080b1b -->

## Layered Abstractions

![bg right:35% fit](abstractions.png)

Skills can call other skills — just like functions calling functions.

```
/generate-deck
  ├── Creates draft slides
  ├── /verify         ← fact-checks all claims
  ├── /generate-image ← creates visuals
  └── /publish        ← exports, commits, pushes
```

- Each skill is **self-contained** but composable
- Higher-level skills orchestrate lower-level ones
- You build **complex workflows from simple primitives**

---

## CLAUDE.md Is Your Config File

- `CLAUDE.md` sets the **runtime environment** — conventions, paths, preferences
- Like `.bashrc`, `tsconfig.json`, or `pyproject.toml`
- Every conversation loads it automatically
- Global `~/.claude/CLAUDE.md` for user-wide defaults
- Project-level `CLAUDE.md` for repo-specific behavior

**The config shapes the runtime. The skills define the operations.**

---

<!-- _backgroundColor: #0e0f12 -->

## The Interactive REPL

![bg right:40% fit](repl.png)

Using Claude interactively is a **Read-Eval-Print Loop**:

1. **Read** — you type a prompt
2. **Eval** — Claude interprets and executes
3. **Print** — results appear (files, code, output)
4. **Loop** — you iterate based on what you see

- Immediate feedback, fast iteration
- Prototype a workflow, then **extract it into a skill**
- The REPL is where skills are born

---

<!-- _backgroundColor: #0d0d1b -->

## But the Language Is Fuzzy

![bg right:40% fit](fuzzy.png)

`2 + 2` → always `4`
Same skill, same input → **different outputs each time**

- The runtime is **non-deterministic**
- This isn't a bug — it's a **fundamental property**
- You're programming a system that **interprets intent**

> "The skill says what to do. The model decides how."

---

## Testing Skills

If skills are code, they need **testing** — but testing looks different here.

- **Behavioral testing** — does the skill produce the right *kind* of output?
- **Boundary testing** — what happens with unusual inputs?
- **Regression testing** — does it still work after you change the prompt?
- **Composition testing** — do layered skills interact correctly?

You can't assert exact equality. You assert **properties and patterns**.
Like property-based testing, but for natural language.

---

## The Implications

- **Prompt engineering is programming** — just in a fuzzy, intent-based language
- **Skills are your codebase** — they grow, refactor, and need maintenance
- **CLAUDE.md is infrastructure** — it defines the platform your skills run on
- **Version control matters** — skills evolve, and you need to track changes
- **Composition is power** — small skills combine into sophisticated workflows

We're not replacing programming. We're **adding a new layer to it**.

---

<!-- _class: closing -->
<!-- _paginate: false -->

## The Best Programming Language Is the One That Understands You

### Skills turn conversation into automation.
