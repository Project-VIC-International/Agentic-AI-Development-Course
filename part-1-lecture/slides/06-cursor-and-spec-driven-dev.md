# Cursor & Spec-Driven Development

---

## Cursor: An AI-Powered Workshop

Cursor is an IDE (Integrated Development Environment) with an AI agent built in.

**What the agent can do:**
- Read and write files in your project
- Run commands in the terminal
- Search the web for documentation
- Interact with external tools via MCP
- Write, test, and debug code
- All from a natural-language chat panel

You type what you want in plain language. The agent acts.

---

## The Agent Panel

```
┌─────────────────────────────────────────────┐
│  Your Project Files          │  Agent Chat  │
│                              │              │
│  📁 src/                     │  You: "Add   │
│  📁 tests/                   │  a function  │
│  📄 spec.md                  │  that parses │
│  📄 constitution.md          │  CyberTip    │
│                              │  XML files"  │
│                              │              │
│  ┌─ editor ──────────────┐   │  Agent: "I'll│
│  │                       │   │  create a    │
│  │  (your code here)     │   │  parser..." │
│  │                       │   │  [writes code│
│  └───────────────────────┘   │   and tests] │
│                              │              │
│  ┌─ terminal ────────────┐   │              │
│  │ $ python test.py      │   │              │
│  │ All tests passed ✓    │   │              │
│  └───────────────────────┘   │              │
└─────────────────────────────────────────────┘
```

---

## Why Spec-Driven Development?

Without structure, AI development is gambling:

| "Vibe Coding" | Spec-Driven Development |
|----------------|------------------------|
| "Build me a CyberTip tool" | Define exactly what the tool does first |
| Hope it works | Verify against written requirements |
| One long prompt | Structured phases with review points |
| No audit trail | Every decision documented |
| Impossible to reproduce | Fully reproducible |

**The specification is the source of truth, not the code.**

---

## The spec-kit Workflow

[GitHub's spec-kit](https://github.com/github/spec-kit) provides a structured 4-phase workflow:

```
  Constitution ──► Specify ──► Plan ──► Tasks ──► Implement
       │               │          │         │          │
   "The rules"    "What &     "How to   "Atomic    "Agent
    of the game    why"       build it"  work       executes"
                                         units"
```

---

## Phase 1: Constitution

The rules of the game. Set once for your project.

**Includes:**
- Technology choices (Python, JSON-LD, etc.)
- Security requirements
- Design principles
- **Interoperability mandate: all output must be CASE/UCO/CAC compliant**
- Coding standards and conventions

This is where you guarantee interoperability from the start.

---

## Phase 2: Specify

Describe **what** you want and **why** — not how.

**Example:**
> "I need a tool that takes NCMEC CyberTip XML exports and produces a timeline of all reported incidents, organized by suspect, with evidence provenance. The output must be a CASE/UCO-compliant knowledge graph."

The AI helps you refine this into a complete specification.

---

## Phase 3: Plan

The AI generates a technical blueprint:

- Architecture decisions
- Data model design
- Component breakdown
- Integration points (CASE/UCO/CAC libraries)
- Testing strategy

**You review every decision.** The AI proposes, you approve.

---

## Phase 4: Tasks → Implement

The plan breaks into small, testable units of work:

1. Set up project structure and dependencies
2. Build CyberTip XML parser
3. Create CASE/UCO graph builder
4. Add timeline generation logic
5. Write validation tests
6. ...

The agent executes tasks one by one, testing each before moving to the next.

---

## Agent Rules: Persistent Guardrails

Specifications guide individual features. But some rules apply to **everything** the agent does in your project — every file it writes, every command it runs, every decision it makes.

These are **agent rules** — written instructions the agent reads every time you prompt it.

---

## What Are Agent Rules?

In Cursor, rules live in `.cursor/rules/` as `.mdc` files. Other agentic AI tools have equivalent mechanisms.

```
your-project/
├── .cursor/
│   └── rules/
│       ├── ontology-alignment.mdc    ← "All data must be CASE/UCO compliant"
│       ├── no-stubs.mdc              ← "Never create placeholder code"
│       ├── four-surface-review.mdc   ← "Check GUI, CLI, API, and MCP impact"
│       ├── speckit-workflow.mdc      ← "Follow the spec pipeline"
│       └── auto-research.mdc         ← "Experiment and measure improvements"
├── src/
├── tests/
└── ...
```

Every time you send a prompt, the agent reads these rules before acting.

---

## Why Rules Matter

Without rules, the agent makes its own assumptions every time:

| Without Rules | With Rules |
|---------------|------------|
| Agent guesses your preferred format | Rule says "all output must be CASE/UCO JSON-LD" |
| Agent writes stub code to "get it working" | Rule says "never create placeholder functions" |
| Agent skips security considerations | Rule says "CJIS compliance is mandatory, encrypt everything" |
| Agent builds for one surface only | Rule says "check impact on GUI, CLI, API, and MCP" |
| Different results every time | **Predictable, consistent behavior** |

Rules make the agent **predictable**. Same rules → same behavior → reproducible outcomes.

---

## Anatomy of a Rule

A rule has a front-matter header and a body written in plain language:

```markdown
---
description: No stubs — always implement real functionality
alwaysApply: true
---

# No Stubs

Never create stub implementations, placeholder functions, or mock returns.
Every function, tool handler, API endpoint, and CLI command must contain
real, working logic that performs its documented purpose.

- If a function is defined, it must do what its name says.
- If a dependency isn't available yet, surface an actionable error
  rather than returning a fake response.
- Test with real data, not synthetic stubs.
```

That's it. Plain language. The agent reads it and follows it.

---

## Real Example: Ontology Alignment Rule

This rule ensures every piece of data stays CASE/UCO/CAC compliant:

> "Every artifact, relationship, provenance record, and analysis result must serialize to valid CASE/UCO JSON-LD. Use the most specific class available. Properties must reference the correct ontology term — do not create synonyms or aliases. If no mapping exists, create a formal extension — do not ship untyped data."

One rule. Written once. Applied to every prompt, every file, every decision.

---

## Real Example: Four-Surface Impact Review

This rule ensures nothing gets missed when a project has multiple interfaces:

> "Every change — feature, fix, refactor — MUST be reviewed for its impact on all four surfaces: GUI, CLI, API, and MCP. A change that improves one surface while leaving another broken is incomplete."

The agent checks all four surfaces every time, without you having to ask.

---

## Rules + Specs = Constrained Agent

Rules and specs work together to keep the agent focused:

```
  ┌─────────────────────────────────────────────────┐
  │                 AGENT RULES                     │
  │  (.cursor/rules/)                               │
  │                                                 │
  │  Applied to EVERYTHING the agent does:          │
  │  • Ontology compliance                          │
  │  • Security standards                           │
  │  • No stubs                                     │
  │  • Four-surface review                          │
  │                                                 │
  │  ┌───────────────────────────────────────┐      │
  │  │           SPECIFICATION               │      │
  │  │  (spec.md for a specific feature)     │      │
  │  │                                       │      │
  │  │  Applied to THIS feature:             │      │
  │  │  • What it does                       │      │
  │  │  • Who it's for                       │      │
  │  │  • Input/output requirements          │      │
  │  │  • Acceptance criteria                │      │
  │  └───────────────────────────────────────┘      │
  └─────────────────────────────────────────────────┘
```

Rules are the **outer boundary**. Specs are the **inner focus**. Together, they constrain the agent from both directions.

---

## Building a Rule Library

Rules are **reusable**. Build a collection over time and copy them between projects:

| Rule | What It Does | Reusable? |
|------|-------------|-----------|
| `no-stubs.mdc` | Prevents placeholder code | Any project |
| `ontology-alignment.mdc` | Enforces CASE/UCO/CAC compliance | Any CAC mission tool |
| `speckit-workflow.mdc` | Requires spec-driven development | Any spec-kit project |
| `four-surface-review.mdc` | Checks all interface surfaces | Multi-surface apps |
| `auto-research.mdc` | Drives experiment-based optimization | Performance-critical tools |

Start small. Add rules when the agent does something wrong. Over time, your rule library becomes your team's institutional knowledge — captured in files, not in someone's head.

---

## How to Write Good Rules

1. **Start from mistakes** — When the agent does something wrong, write a rule to prevent it
2. **Be specific** — "Never create stub code" is better than "write good code"
3. **Use plain language** — The agent reads English, not code
4. **Set `alwaysApply: true`** for rules that apply to every file
5. **Keep rules focused** — One concern per rule, not a wall of text
6. **Evolve over time** — Add and adjust rules as you learn what the agent needs

---

## The Key Insight

> **If you can write an email describing what you need, you can write a specification. If you can write a specification, the AI can build it.**

> **If you can describe how you want the agent to behave, you can write a rule. If you write the rule, the agent will follow it — every time.**

You stay in control at every phase. The AI does the implementation work. Rules and specs keep it on track.
