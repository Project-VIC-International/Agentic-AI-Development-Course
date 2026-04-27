# Part 1: The Future Is Here

## Building Interoperable Crimes Against Children Mission Tools with Agentic AI and Open Standards

**Format:** 1-hour lecture
**Audience:** Law enforcement investigators, forensic examiners, crime intelligence analysts, and prosecutors working CAC/ICAC cases
**Prerequisites:** None — this is the introductory session that sets up Part 2

## Lecture Goals

By the end of this lecture, attendees will understand:

1. What AI, ML models, and agentic AI are — and where to get models (HuggingFace, Project VIC, universities)
2. Why GPUs matter for running models at speed
3. The four ways humans and agents interact with applications (UI, CLI, API, MCP)
4. How to use GitHub as a library of existing solutions
5. What spec-driven development is and why it keeps you in control of AI
6. The CASE/UCO/CAC Ontology ecosystem and why interoperability matters
7. That CASE/UCO/CAC data lives in graph databases — which also have four doors, including MCP for agents
8. That any new tool MUST be independently tested and validated before operational use
9. How to meet cybersecurity requirements (CJIS Security Policy, NIST 800-53, encryption)
10. That they — without being software developers — can build interoperable, secure, validated tools today

## Delivery Notes

### Tone

This audience is composed of investigators who protect children. They are pragmatic, skeptical of hype, and time-constrained. Every concept must be tied to a concrete benefit for their mission. Avoid jargon without explanation. Use law enforcement examples exclusively.

### Pacing

The lecture moves through 12 sections. With the addition of AI/ML models, graph databases, testing & validation, and cybersecurity/CJIS, the lecture runs slightly longer than 60 minutes (~68 min). If time is tight, the AI/ML models content is integrated into the AI Foundations section, and T&V + cybersecurity can be compressed. Transitions between sections should feel like chapters in a story, not disconnected topics. The narrative arc is:

> Here's a problem you live with every day → Here's why it exists → Here's the solution → Here's why *you* can use it now → Let's go build something

### Materials

- Slide content is in the [slides/](slides/) directory as markdown files
- The [outline](outline.md) contains detailed timing, speaker notes, and transition cues
- Slides can be converted to presentation format using [Marp](https://marp.app/), [reveal.js](https://revealjs.com/), or copied into PowerPoint/Google Slides
- Instructor visuals from NotebookLM are exported in [../graphics/](../graphics/) and cataloged in [../graphics/README.md](../graphics/README.md)

## Slide Deck Overview

| # | File | Section | Time |
|---|------|---------|------|
| 01 | [01-welcome-and-why.md](slides/01-welcome-and-why.md) | Welcome & Why This Matters | 0:00–0:05 |
| 02 | [02-ai-foundations.md](slides/02-ai-foundations.md) | AI Foundations (includes AI/ML models & GPUs) | 0:05–0:14 |
| 03 | [03-agentic-ai.md](slides/03-agentic-ai.md) | What Is Agentic AI? | 0:14–0:20 |
| 04 | [04-four-doors.md](slides/04-four-doors.md) | The Four Doors Into Any Application | 0:20–0:28 |
| 05 | [05-github-as-library.md](slides/05-github-as-library.md) | GitHub as a Library & Open-Source Mindset | 0:28–0:33 |
| 06 | [06-cursor-and-spec-driven-dev.md](slides/06-cursor-and-spec-driven-dev.md) | Cursor & Spec-Driven Development | 0:33–0:40 |
| 07 | [07-interoperability-journey.md](slides/07-interoperability-journey.md) | The Interoperability Journey | 0:40–0:44 |
| 08 | [08-case-uco-cdo.md](slides/08-case-uco-cdo.md) | CASE/UCO & the Cyber Domain Ontology | 0:44–0:48 |
| 09 | [09-cac-ontology.md](slides/09-cac-ontology.md) | The CAC Ontology | 0:48–0:52 |
| 10 | [10-bridge-to-lab.md](slides/10-bridge-to-lab.md) | Bridge to Lab | 1:04–1:08 |
| 11 | [11-ai-ml-models-and-gpus.md](slides/11-ai-ml-models-and-gpus.md) | AI/ML Models & GPUs (deep dive supplement) | — |
| 12 | [12-testing-and-validation.md](slides/12-testing-and-validation.md) | Testing & Validation | 0:56–1:00 |
| 13 | [13-cybersecurity-and-cjis.md](slides/13-cybersecurity-and-cjis.md) | Cybersecurity, NIST & CJIS Compliance | 1:00–1:04 |
| 14 | [14-graph-databases.md](slides/14-graph-databases.md) | Graph Databases: Where Your Data Lives | 0:52–0:56 |

**Recommended delivery order:** 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 14 → 12 → 13 → 10

Slide 11 (AI/ML Models deep dive) is supplementary — the key concepts are already integrated into Slide 02. Use Slide 11 for extended sessions or as a handout.
