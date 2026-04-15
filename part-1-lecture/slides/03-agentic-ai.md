# What Is Agentic AI?

---

## From Chatbot to Agent

| Chatbot | Agent |
|---------|-------|
| Waits for your question | Takes a goal and works toward it |
| Gives one answer | Iterates through multiple steps |
| Can only talk | Can use tools |
| Generates text | Takes action |

---

## The Agent Loop

```
    ┌──────────┐
    │  THINK   │ ← Understand the goal
    └────┬─────┘
         │
    ┌────▼─────┐
    │   PLAN   │ ← Break it into steps
    └────┬─────┘
         │
    ┌────▼─────┐
    │   ACT    │ ← Execute a step (write code, run command, search)
    └────┬─────┘
         │
    ┌────▼─────┐
    │ OBSERVE  │ ← Check the result
    └────┬─────┘
         │
         └──────── Repeat until done
```

The agent doesn't just generate one answer — it works through a problem step by step, checking its own work along the way.

---

## What Makes an Agent an Agent: Tools

An AI agent has access to tools:

- **File system** — read and write files
- **Terminal** — run commands and scripts
- **Web browser** — search for information and documentation
- **MCP servers** — interact with external applications
- **Code execution** — write, run, test, and debug code

Without tools, it's a chatbot. With tools, it's a collaborator.

---

## Why This Matters for Your Mission

You don't need to learn to code.

You need to learn to **describe what you want clearly**.

The agent handles the implementation. You review, guide, and iterate.

---

## "Vibe Coding" vs. Disciplined Development

| Vibe Coding | Spec-Driven Development |
|-------------|------------------------|
| "Hey AI, build me a tool" | Define requirements first, then build |
| Hope for the best | Verify against the spec |
| No structure | Constitution → Spec → Plan → Tasks |
| Hard to reproduce | Reproducible and auditable |
| Fragile results | Reliable results |

We'll show you the disciplined approach shortly.
