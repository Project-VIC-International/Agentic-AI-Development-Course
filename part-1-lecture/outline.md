# Lecture Outline — Detailed Timing and Speaker Notes

## The Future Is Here: Building Interoperable Crimes Against Children Mission Tools with Agentic AI and Open Standards

---

## Section 1: Welcome & Why This Matters (0:00–0:05)

**Key message:** The digital evidence landscape is exploding. The tools you need don't exist yet — or they don't talk to each other. You can change that, starting today.

### Speaker Notes

- Open with scale: the volume of CyberTips, the number of devices per case, the explosion of online platforms. The data is growing faster than the workforce.
- Acknowledge the audience: you are the front line. You know the gaps better than anyone. You've wished for a tool that doesn't exist. You've spent hours reformatting data from one tool to paste into another.
- Set the promise: by the end of today's session and the lab that follows, you will have seen a working tool built from scratch using AI — and you'll understand how to do it yourself.
- Clarify: you do NOT need to be a programmer. If you can describe what you need in plain language, you can build it.

### Transition

> "To understand how AI can help you build tools, let's first understand what AI actually is — and what it isn't."

---

## Section 2: AI Foundations (0:05–0:14)

**Key message:** AI is a tool, not magic. Understanding the basics — including where models come from and what hardware runs them — helps you use them effectively.

### Speaker Notes

- **What is AI?** Software that can perform tasks that typically require human intelligence — recognizing patterns, making predictions, generating text.
- **What is a Large Language Model (LLM)?** A program trained on enormous amounts of text that can understand and generate human language. ChatGPT, Claude, Gemini — these are LLMs.
- **Not all LLMs are the same.** Walk through the types:
  - **Instruction-following LLMs** — follow directions precisely. Good for building tools and formatting data.
  - **Reasoning LLMs** — think step-by-step through complex problems. Good for analyzing evidence chains and legal reasoning.
  - **Dense models** — every part of the model activates for every query. Thorough but expensive.
  - **Mixture of Experts (MoE)** — only activates relevant "expert" parts. Faster and cheaper at scale.
  - **Visual LLMs** — can see and understand images alongside text. Useful for processing screenshots and documents.
  - **Multimodal** — combines text, vision, audio, code. The most versatile.
  - Key takeaway: different models excel at different tasks. Choose the right model for the job, just like you choose the right forensic tool.
- **How do they work (conceptual)?** They predict what comes next. Given context, they generate the most likely continuation. This is why *context* matters — the more relevant information you give them, the better their output.
- **What can they do?** Summarize, analyze, write, code, explain, translate, reason through problems.
- **What can't they do?** They don't have memory between sessions (unless you give them context or use memory tools). They can be confidently wrong ("hallucinate"). They don't have agency — they respond, they don't act (unless they're agents with tools).
- **Solving the memory problem.** LLMs forget everything when a session ends. Open-source agent memory tools fix this:
  - [Mem0](https://github.com/mem0ai/mem0) — universal memory layer for AI agents. Remembers preferences, decisions, and context across sessions. Works with any LLM. Self-hosted option. Apache 2.0.
  - [MemPalace](https://github.com/MemPalace/mempalace) — structured memory using the "memory palace" metaphor. Stores verbatim conversations. 96.6% recall on benchmarks. Runs entirely locally. 19 MCP tools so agents can search and store memories automatically. MIT license.
  - For investigators: imagine an agent that remembers every case, every tool decision, every investigation pattern. Agent memory turns a forgetful assistant into an experienced partner.
  - These are open-source tools on GitHub — search before you build.
- **Key concept: prompting.** The quality of your input determines the quality of the output. "Garbage in, garbage out" applies. This is why structured approaches (like spec-driven development) matter.
- **AI/ML models beyond LLMs.** LLMs are just one type of AI model. There are models for image classification, object detection, age estimation, perceptual hashing, and more. These are the models that power your forensic tools.
- **Where to get models:**
  - [HuggingFace](https://huggingface.co) — the GitHub of AI/ML models. Thousands of pre-trained models, free to download.
  - The research community — academic papers often publish models alongside their research.
  - Project VIC International — provides models and hash intelligence specifically for CAC investigations.
  - Your state university — universities have AI/ML labs, GPU clusters, and graduate students who can train custom models for your mission. Partner with them.
- **GPUs and hardware acceleration.** AI models require enormous amounts of math. A regular CPU processes tasks one at a time. A GPU has thousands of cores that process in parallel. The difference: classifying one image on a CPU might take 5-10 seconds; on a GPU, milliseconds. For 10,000 images: CPU = hours, GPU = minutes. GPUs are what make AI fast enough to be useful in real investigations.

### Transition

> "So LLMs can understand and generate language. But they just sit there and wait for you to type. What if they could actually *do things*? That's where agentic AI comes in."

---

## Section 3: What Is Agentic AI? (0:14–0:20)

**Key message:** Agentic AI doesn't just answer questions — it does work. It can think, plan, act, observe results, and iterate.

### Speaker Notes

- **From chatbot to agent.** A chatbot waits for your question and gives an answer. An agent takes a goal and works toward it — using tools, reading files, searching the web, writing code, testing, and iterating.
- **The agent loop:** Think → Plan → Act → Observe → Repeat. The agent doesn't just generate one answer — it works through a problem step by step, checking its own work.
- **Tools.** An agent has access to tools: a terminal to run commands, a file system to read and write files, a web browser to search for information, and more. This is what makes it an *agent* rather than a chatbot.
- **Why this matters for you.** You don't need to learn to code. You need to learn to describe what you want clearly. The agent does the implementation. You review, guide, and iterate.
- **"Vibe coding" vs. disciplined development.** Letting an AI build whatever it wants with no structure leads to chaos. That's "vibe coding." We'll show you a disciplined approach called spec-driven development that keeps you in control.

### Transition

> "So an agent can use tools, read files, write code, and browse the web. But how does any software actually get used? Let's talk about the four doors into any application."

---

## Section 4: The Four Doors Into Any Application (0:20–0:28)

**Key message:** Every application has multiple interfaces — UI, CLI, API, and MCP. Agents can use all of them, and they can work *on* and *in* an application simultaneously.

### Speaker Notes

This section uses the "building with four doors" metaphor.

- **Door 1: UI (Front Door).** The graphical interface. Buttons, menus, forms. What everyone uses. Welcoming but limited — you can only do what the designer planned for. If you need to process 500 CyberTips, you're clicking 500 times.

- **Door 2: CLI (Staff Entrance).** The command line. Text commands, no buttons. Power users and system administrators use this. Scriptable and repeatable — one command can process all 500. Like the staff entrance: no lobby, but you can go places the front door doesn't reach.

- **Door 3: API (Loading Dock).** Application Programming Interface. How applications talk to each other. Each API is a documented set of endpoints — one for each type of question or action — with a schema that defines what data goes in and what comes back. Like a loading dock: standardized containers, manifests, no humans needed. When your case management system pulls CyberTip data automatically, that's an API call.

- **Door 4: MCP (The Agent's Door).** Model Context Protocol. A standardized way for AI agents to discover and use an application's capabilities. MCP is to agents what APIs are to applications. The agent reads a directory of available capabilities and uses them. This is purpose-built for AI interaction.

- **The superpower: agents use ALL four doors.**
  - Multimodal agents can see and interact with UIs
  - Agents can type CLI commands and read output
  - Agents can make API calls and process responses
  - Agents use MCP natively as their primary interface

- **The game-changer: working ON and IN simultaneously.**
  - Working ON: the agent writes code, adds features, fixes bugs — it's a developer
  - Working IN: the agent uses the application, queries data, generates reports — it's a user
  - Both at once: the agent builds a feature, tests it against real data, finds an issue, fixes it, re-tests — all in one continuous loop
  - This has never been possible before. The builder and the user are the same entity.

### Transition

> "Now you know how agents interact with applications. Before we have an agent build something, let's talk about the world's largest library of things that have already been built."

---

## Section 5: GitHub as a Library & The Open-Source Mindset (0:28–0:33)

**Key message:** Before you build anything, look at what already exists. GitHub is a library of solutions, and open source is a mindset.

### Speaker Notes

- **GitHub is not just for coders.** It's a library. Millions of projects, searchable, browsable, with documentation. You wouldn't write a report without checking if someone already wrote one on the same topic. Same principle.
- **Live demo (if feasible) or screenshots:** Search GitHub for "ICAC," "CyberTip," "digital forensics," "CASE ontology." Show what comes up. Point out READMEs, stars, recent activity as signals of quality.
- **The open-source mindset:**
  - Don't reinvent — extend. If someone solved 80% of your problem, build on their work.
  - Read the license. Apache 2.0, MIT, GPL — these determine what you can do with the code.
  - Contribute back. If you improve something, share it. The community gets stronger.
- **Key organizations to know:**
  - [casework](https://github.com/casework) — CASE examples and tools
  - [Cyber-Domain-Ontology](https://github.com/Cyber-Domain-Ontology) — CDO governance
  - [ucoProject](https://github.com/ucoProject) — UCO ontology
  - [Project-VIC-International](https://github.com/Project-VIC-International) — CAC Ontology
- **The principle for this course:** Every tool you build should check what already exists first, use existing work where possible, and contribute improvements back.

### Transition

> "So we have a library of existing work. Now we need a workshop to build in. Let me introduce you to Cursor and a method called spec-driven development."

---

## Section 6: Cursor & Spec-Driven Development (0:33–0:40)

**Key message:** Cursor is an AI-powered workshop, and spec-driven development keeps you in control of what gets built.

### Speaker Notes

- **Cursor overview.** An IDE (Integrated Development Environment) with an AI agent built in. The agent can read your files, write code, run commands, search the web, and use tools — all from a chat panel.
- **The agent panel.** Show or describe the interface: you type in natural language, the agent responds with actions. It asks clarifying questions. It shows you what it's about to do. You approve or redirect.
- **Why spec-driven development?**
  - "Vibe coding" = telling an AI "build me a CyberTip tool" and hoping for the best
  - Spec-driven development = defining exactly what you want *before* the AI writes a single line of code
  - You stay in control. The AI implements your intent, not its own.
- **GitHub's spec-kit workflow:**
  1. **Constitution** — the rules of the game. Tech stack, security standards, design principles, interoperability requirements (CASE/UCO/CAC compliance goes here)
  2. **Specify** — describe *what* you want and *why*. User stories, outcomes, constraints. No technical details yet.
  3. **Plan** — the AI generates a technical blueprint: architecture, data model, components
  4. **Tasks** — the plan is broken into atomic, testable units of work
  5. **Implement** — the agent executes tasks one by one, checking its work
- **The key insight:** The specification is the source of truth, not the code. If the code doesn't match the spec, the code is wrong.

### Transition

> "We've talked about building tools with AI. But if everyone builds tools their own way, we end up with the same problem we have today — tools that can't talk to each other. Let's talk about why interoperability matters and how we solve it."

---

## Section 7: The Interoperability Journey (0:40–0:44)

**Key message:** You already believe in interoperability — VICS proved it for hashes. CASE/UCO/CAC extends that to everything.

### Speaker Notes

- **Start with what they know.** Project VIC hash intelligence. The VICS schema. 36 tool developers have adopted it. When you run a hash lookup, the results are interoperable across Griffeye, NetClean, NPS, and dozens more.
- **The 14-year reality check.** It took 14 years to get 36 tool developers to adopt one schema for one type of data. That schema exchanges *observations* — hash values, categories, identifiers. It answers: "Have we seen this file before?"
- **What it doesn't capture.** Investigation context. Who found it, on what device, connected to which suspect, in which jurisdiction, as part of which operation, leading to what legal outcome. That context lives in spreadsheets, reports, emails, and investigators' heads.
- **The daily pain.** Ask the room:
  - How many hours do you spend normalizing data from different tools into a common format?
  - How often do you re-type information from a forensic report into a case management system?
  - How many times has a prosecutor asked you to show the evidence chain, and you had to reconstruct it manually?
- **This is data janitorial work.** It's not investigation. It's where cases stall and mistakes creep in.
- **The vision:** What if every tool you use spoke the same language — not just for hashes, but for *everything*?

### Transition

> "That's exactly what CASE, UCO, and the Cyber Domain Ontology were built to do."

---

## Section 8: CASE/UCO & the Cyber Domain Ontology (0:44–0:48)

**Key message:** Open standards are how your tools talk to everyone else's tools.

### Speaker Notes

- **The Cyber Domain Ontology (CDO).** A Linux Foundation project that governs the development of CASE and UCO. Open governance, community-driven, international.
- **UCO — Unified Cyber Ontology.** The foundation layer. Provides a shared vocabulary for the entire cyber domain: devices, accounts, files, network connections, actions, relationships, identities, locations.
- **CASE — Cyber-investigation Analysis Standard Expression.** Extends UCO specifically for cyber-investigations: evidence items, chain of custody, provenance (who did what, when, with which tool), investigative actions, tool results.
- **What is an ontology?** In plain language: a shared vocabulary that machines can understand. It defines what things exist (classes), how they are described (properties), and how they connect (relationships). Think of it as a language — if everyone speaks it, everyone understands each other.
- **Show a simple example.** A device → contains → a file → has hash → matches known CSAM → found by → forensic tool → during → investigation. All of that expressed as a connected graph, in a format any CASE-aware tool can read.
- **Why this matters for interoperability:**
  - Tools that output CASE data can share information automatically
  - No more manual normalization between tool outputs
  - New tools are interoperable from day one if they speak CASE
  - Prosecutors, analysts, and partner agencies can consume the same data

### Transition

> "CASE and UCO give us the general language for cyber-investigations. But our mission has specialized needs. That's why the CAC Ontology exists."

---

## Section 9: The CAC Ontology (0:48–0:52)

**Key message:** CAC Ontology captures the full semantic picture of a child exploitation investigation as a connected graph.

### Speaker Notes

- **What is the CAC Ontology?** A domain-specific extension of UCO and CASE, built specifically for crimes against children investigations. Shepherded by Project VIC International, open to all participants.
- **What it models:**
  - Investigations and case lifecycles
  - CyberTip processing and NCMEC integration
  - Digital forensics and evidence handling
  - Online grooming, enticement, sextortion
  - CSAM production and distribution
  - Offender tradecraft and behavioral patterns
  - Victim impact and recovery services
  - Legal processes and outcomes
  - Multi-jurisdictional and international operations
  - Task force organization and coordination
- **Scale:** 35+ specialized modules, 2,154 classes, 2,443 properties, 97 ontology files. This is comprehensive.
- **Real examples:** 56 example knowledge graphs based on actual law enforcement cases.
- **The AI modeling workflow.** You can take a press release, a report, or a tool export and use an AI agent to model it as a CAC Ontology knowledge graph. The agent reads the ontology, understands the concepts, and produces the graph. You review and refine.
- **The democratization moment:**
  - You no longer need to be a software developer to produce interoperable investigation data
  - Use the CASE/UCO/CAC SDK — pre-built libraries that handle the technical plumbing
  - Use a capable agent like Opus 4.6 in Cursor — it understands the ontology and can generate compliant output
  - Use multiple LLM services as a review team — have one model generate, another review, a third validate. They catch different things, just like human peer reviewers.
- **International reach.** Coordination frameworks supporting 120+ countries. When you build on CAC Ontology, your data can cross borders.

### Transition

> "CASE, UCO, and CAC Ontology give us the language. But languages need a place to be spoken. Let's talk about where your investigation graphs actually live — graph databases."

---

## Section 10: Graph Databases (0:52–0:56)

**Key message:** CASE/UCO/CAC are languages for graphs that get stored and queried in graph databases. Graph databases also have UI, CLI, API, and MCP — and agents can put data in and query it.

### Speaker Notes

- **From language to storage.** We've been talking about CASE/UCO/CAC as languages for expressing investigation data. But a language needs a place to be written and read. Graph databases are where knowledge graphs live.
- **What is a graph database?** A database designed to store and query connected data — nodes (entities) and edges (relationships). Unlike traditional databases that use flat tables, graph databases preserve the connections between things. They store data the way you already think about investigations.
- **Why graphs are powerful for investigations:** When you describe a case — "the CyberTip led to the suspect, who owned the device, which contained the file" — that's already a graph. Every noun is a node, every verb is an edge. Graph databases let you query those connections naturally.
- **Four doors apply here too.** Graph databases have all four doors:
  - UI — visual graph exploration tools (Neo4j Browser, GraphDB Workbench) — investigators can see and navigate the graph
  - CLI — command-line interfaces for batch queries and scripting
  - API — REST endpoints and query protocols for application integration
  - MCP — some graph databases already have MCP servers, meaning **your AI agent can store data in and query the database directly**
- **The complete picture.** You describe your need → the agent builds a tool using CASE/UCO/CAC → the tool outputs knowledge graphs → the graphs are stored in a graph database → the agent queries the database to answer investigative questions, find patterns, and generate reports.
- **Cross-case intelligence.** The real power comes when you have multiple investigations in the same database: find connections between cases, identify repeat offenders, detect networks, track patterns over time. This is intelligence analysis at machine speed.
- **Popular options for CASE/UCO/CAC:** GraphDB (Ontotext), Apache Jena Fuseki (free, open source), Amazon Neptune, Stardog. RDF/SPARQL databases are the natural fit because CASE/UCO/CAC are RDF-based.

### Transition

> "So we have the language, we have the storage, and we have agents that can use both. But before any of this goes into an operational environment, there are critical guardrails. Let's talk about testing, validation, and security."

---

## Section 11: Testing, Validation & Cybersecurity (0:56–1:04)

**Key message:** Any tool you build MUST be independently tested and validated before operational use. It MUST meet CJIS security requirements. Your agent can help you plan for all of this — just point it at the standards.

### Speaker Notes

- **The non-negotiable rule.** State it clearly and directly: any new application, model, or tool you build MUST be independently tested and validated before it can be used in real digital forensics or law enforcement operations. No exceptions.
- **Why this matters in law enforcement:**
  - Evidence must withstand legal challenge — defense attorneys will question your tools
  - Results must be reproducible — another examiner should get the same result
  - Tools must be accurate — false positives and false negatives have real consequences for victims and for justice
  - The NIST Computer Forensics Tool Testing (CFTT) program exists specifically for forensic tool validation
- **What validation looks like:**
  - For software tools: unit testing, integration testing, validation on known datasets, peer review, documentation for court
  - For AI/ML models: benchmark testing, error rate analysis, bias evaluation, adversarial testing, independent third-party validation
  - Who can validate: your agency QA, NIST CFTT, university research partners, peer agencies, commercial testing labs
- **Cybersecurity requirements — CJIS Security Policy:**
  - Any tool that handles Criminal Justice Information must comply with the FBI CJIS Security Policy
  - Key areas: access control, encryption, auditing, personnel security, incident response
  - This is a legal requirement, not a best practice
- **Encryption at all times:**
  - Data at rest: AES-256 or equivalent. All databases, files, backups.
  - Data in transit: TLS 1.2+ for all connections. No unencrypted HTTP.
  - Key management: secure storage, regular rotation, never hardcoded.
- **NIST 800-53 and cybersecurity overlays:**
  - NIST SP 800-53 defines comprehensive security controls organized into families (Access Control, Audit, Encryption, etc.)
  - NIST cybersecurity overlays customize these controls for specific missions — law enforcement and CJIS have specific overlays
  - Use these as your security planning framework
- **How the agent helps:**
  - Point the agent at the CJIS Security Policy, NIST 800-53, or any security standard
  - Ask it to generate a compliance checklist for your tool
  - Ask it to audit your application against specific control families
  - Ask it to implement encryption, access controls, or audit logging
  - Put these requirements in your constitution — the agent inherits them automatically
  - All they have to do is point their agent at this repository and it will help them plan everything accordingly.

### Transition

> "You've now seen the complete picture: AI agents, open standards, graph databases, and the security and validation guardrails. Let's go build something."

---

## Section 12: Bridge to Lab (1:04–1:08)

**Key message:** You just went from "what is AI" to "how to build interoperable, secure, validated tools with it." Now you're going to do it.

### Speaker Notes

- **Preview the lab.** In the lab session, you will:
  1. Set up your environment (Cursor, GitHub, Python)
  2. Explore GitHub to find existing projects
  3. Have your first conversation with an AI agent
  4. Use spec-driven development to define a CAC mission tool — with CJIS, NIST, and T&V requirements baked into the constitution
  5. See CASE/UCO data structures in action
  6. Model an investigation scenario using CAC Ontology
  7. Watch an agent build a working prototype end-to-end
- **Set expectations.** The prototype won't be production-ready. It will be a working proof of concept that demonstrates the workflow. Remember: any tool you build must go through independent testing and validation before operational use. The goal is for you to leave here knowing *you can do this* — and knowing the guardrails.
- **Encouragement.** If you can write an email, you can write a specification. If you can write a specification, the AI can help you build the tool. If you build the tool on CASE/UCO/CAC, it's interoperable from day one. If you put CJIS and NIST requirements in the constitution, security is built in from the start.
- **The agent works for you.** Point the agent at this course repository, at the CJIS Security Policy, at NIST 800-53, at the CAC Ontology — it reads the standards and helps you plan, build, and validate accordingly.
- **Call to action.** Think about a tool you've wished existed. A gap in your workflow. A report you wish was automated. A data connection you wish you could make. Bring that idea to the lab.
