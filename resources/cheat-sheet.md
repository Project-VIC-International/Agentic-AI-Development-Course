# Quick Reference — Agentic AI Development Course

*Print this page. Keep it at your desk during the lab.*

---

## The Four Doors Into Any Application

| Door | What It Is | Who Uses It |
|------|-----------|-------------|
| **UI** | Graphical interface — buttons, menus, forms | Everyone |
| **CLI** | Command line — text commands, scriptable | Power users, batch processing |
| **API** | Application-to-application — structured data exchange | Other software, integrations |
| **MCP** | Agent-to-application — AI discovers and uses capabilities | AI agents |

---

## Ontology Building Blocks

| Concept | What It Is | Example |
|---------|-----------|---------|
| **Class** | A type of thing | `Device`, `Person`, `File`, `Investigation` |
| **Property** | A description of a thing | `name`, `hashValue`, `timestamp` |
| **Relationship** | A named connection between things | `contains`, `extractedBy`, `hasAccount` |
| **Facet** | A group of related properties on an object | `FileFacet` (fileName, filePath), `HashFacet` (hashMethod, hashValue) |
| **Namespace** | A topic-specific vocabulary prefix | `uco-observable:`, `case-investigation:`, `cac:` |

---

## The Three Ontology Layers

```
┌──────────────────────────┐
│     CAC Ontology         │  Your mission (crimes against children)
├──────────────────────────┤
│     CASE                 │  Your work (cyber-investigations)
├──────────────────────────┤
│     UCO                  │  The foundation (all cyber domains)
└──────────────────────────┘
```

---

## Data Formats

| Format | File Extension | Best For |
|--------|---------------|----------|
| **JSON-LD** | `.jsonld` | Machine processing, API exchange |
| **Turtle** | `.ttl` | Human reading, compact hand-editing |

Both carry identical information — just different syntax.

---

## Spec-Driven Development Workflow

```
Constitution ──► Specify ──► Plan ──► Tasks ──► Implement
    │               │          │         │          │
"The rules"    "What &     "How to   "Atomic    "Agent
 of the game    why"       build it"  work       executes"
                                      units"
```

| Phase | What You Produce | Who Decides |
|-------|-----------------|-------------|
| Constitution | Project rules (tech, security, compliance) | You |
| Specify | What the tool does and why | You (agent helps draft) |
| Plan | Architecture and data model | Agent proposes, you approve |
| Tasks | Ordered work units with "done" criteria | Agent proposes, you approve |
| Implement | Working code and tests | Agent builds, you review |

---

## Agent Rules

Rules live in `.cursor/rules/` and the agent reads them every prompt.

```
---
description: Short description of the rule
alwaysApply: true
---

# Rule Title

Plain-language instructions the agent must follow.
```

---

## Key Technologies

| Tool | What It Does |
|------|-------------|
| **Cursor** | IDE with built-in AI agent |
| **rdflib** | Python library for reading/writing knowledge graphs |
| **pyshacl** | Python library for validating graphs against SHACL shapes |
| **SPARQL** | Query language for asking questions of knowledge graphs |
| **SHACL** | Grammar rules for graph data — ensures interoperability |

---

## Validation Essentials

| What | Why |
|------|-----|
| SHACL validation | Ensures your graph follows the rules (required fields, correct types) |
| Cross-model review | Use a second AI model as a peer reviewer |
| NIST CFTT | NIST program for forensic tool validation |
| CJIS compliance | Mandatory for any tool handling Criminal Justice Information |
| Independent T&V | Non-negotiable before operational use |
