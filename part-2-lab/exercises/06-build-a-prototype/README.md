# Exercise 6: Build a Prototype

**Duration:** Remaining lab time
**Goal:** Build a working, interoperable CAC mission tool end-to-end using spec-driven development and agentic AI

## Overview

This is the capstone exercise. Everything you've learned comes together here:

- **Exercise 0:** You set up your environment
- **Exercise 1:** You learned to search before building
- **Exercise 2:** You learned to work with an AI agent
- **Exercise 3:** You learned spec-driven development
- **Exercise 4:** You learned CASE/UCO data structures
- **Exercise 5:** You learned CAC Ontology modeling

Now you build a real tool.

## Step 1: Choose a Tool (Group Decision)

As a class, pick one tool to build. Here are the candidates — or propose your own:

### Option A: CyberTip Triage Helper

**What it does:** Takes a batch of synthetic CyberTip-style records and produces:
- A prioritized triage list (sorted by severity indicators)
- A timeline of reported incidents
- A CASE/UCO/CAC-compliant knowledge graph of all tips and their relationships

**Why it matters:** Triage is the bottleneck. Prioritizing the right tips first saves time and protects more children.

### Option B: Evidence Chain Tracker

**What it does:** Takes a list of evidence items (devices, files, accounts) and produces:
- A chain of custody graph showing who handled what, when
- Provenance records for every forensic action
- A CASE/UCO-compliant output suitable for court presentation

**Why it matters:** Chain of custody errors can sink a prosecution. Automating the record-keeping reduces risk.

### Option C: Investigation Graph Builder

**What it does:** Takes a plain-text case summary (like the press release from Exercise 5) and produces:
- A complete CASE/UCO/CAC knowledge graph
- A visual summary of entities and relationships
- Answers to standard investigative questions (who, what, when, where)

**Why it matters:** Every investigation generates documents. Converting them to structured, queryable graphs makes analysis faster.

### Option D: Your Idea

Bring the idea you thought of during the lecture. Describe it to the class. If the group picks it, we build it.

## Step 2: Adopt the Constitution and Cursor Rules

Before writing the spec, give your AI agent the standing orders it needs to build a CAC mission tool the right way. From your project root:

```bash
mkdir -p .cursor/rules .specify/memory
cp ../03-spec-driven-dev/example-spec/constitution.md .specify/memory/constitution.md
cp ../03-spec-driven-dev/example-cursor-rules/*.mdc .cursor/rules/
```

(Adjust the relative paths if your project lives somewhere else in the course tree.)

You now have:

- A **constitution** at `.specify/memory/constitution.md` — the rules of your project
- Eight **Cursor rules** at `.cursor/rules/` — the standing orders the AI agent reads on every prompt (CASE/UCO/CAC alignment, CJIS security, four-surface coverage, no stubs, etc.)

Open a couple of the rule files and read them. They are written in plain English and you can edit them to fit your project (look for `[FILL IN]` placeholders).

## Step 3: Define the Specification

Using the constitution from Exercise 3, ask the agent to help write a specification for the chosen tool:

> We're building [CHOSEN TOOL]. Using the constitution in part-2-lab/exercises/03-spec-driven-dev/example-spec/constitution.md, help me write a specification that covers:
> 1. What the tool does
> 2. Who uses it
> 3. What inputs it accepts
> 4. What outputs it produces (must include CASE/UCO/CAC-compliant graph)
> 5. Key constraints and requirements
>
> Save it as spec.md in this directory.

## Step 4: Generate the Plan

> Based on the spec we just wrote, generate a technical plan. Include architecture, data model, components, and testing approach. Save it as plan.md.

## Step 5: Generate Tasks

> Break the plan into an ordered list of atomic tasks. Save as tasks.md.

## Step 6: Build

This is where the agent builds the tool. Work through the tasks one at a time:

> Let's start building. Execute task 1 from tasks.md. Show me what you're doing and let me review before moving to the next task.

For each task:
1. The agent implements it
2. You review the implementation
3. You approve or ask for changes
4. Move to the next task

**Key things to watch for:**
- Is the agent following the constitution?
- Is CASE/UCO/CAC compliance built in from the start (not bolted on at the end)?
- Does each task produce testable output?
- Are examples using synthetic data only?

## Step 7: Test the Prototype

Once the core tasks are done, test the prototype:

> Run the tool with the example input data. Show me the output. Is the output valid CASE/UCO/CAC? Run any validation checks.

The agent should:
1. Run the tool (working IN the application)
2. Inspect the output
3. Validate against SHACL shapes if available
4. Fix any issues (working ON the application)
5. Re-test

This is the "working on and in simultaneously" concept in action.

## Step 8: Cross-Model Review (If Time Permits)

Take the tool's output and paste it into a different AI model:

> Review this CASE/UCO/CAC knowledge graph output for correctness and completeness. Does it follow CASE modeling best practices? Are there any issues?

## Done When

- [ ] Tool chosen and specification written (`spec.md`)
- [ ] Technical plan generated (`plan.md`)
- [ ] Tasks broken down (`tasks.md`)
- [ ] Prototype runs on synthetic input data
- [ ] Output is CASE/UCO/CAC-compliant (validated or agent-reviewed)
- [ ] (If time) Cross-model review completed

**Artifacts:** `spec.md`, `plan.md`, `tasks.md`, working prototype code, sample output graph, and validation results.

## What You Just Built

In one lab session, you:

1. **Chose** a mission-relevant tool to build
2. **Specified** what it should do using spec-driven development
3. **Planned** the architecture with AI assistance
4. **Tasked** the work into executable units
5. **Built** a working prototype with an AI agent
6. **Tested** it against real (synthetic) data
7. **Validated** the output for standards compliance

The prototype outputs **interoperable data** — CASE/UCO/CAC-compliant knowledge graphs that any other CASE-aware tool can consume.

You did this without writing code by hand. You described what you wanted, guided the agent, and reviewed the results.

**This is the workflow you can take home and use tomorrow.**

## After the Lab

### Continue Building
- Iterate on the prototype — add features, improve the output
- Use the spec-driven workflow for any new tool idea
- Use multiple AI models to review and improve

### Connect with the Community
- **CAC Ontology:** [site.cacontology.projectvic.org/community](https://site.cacontology.projectvic.org/community)
- **CASE Community:** [caseontology.org](https://caseontology.org/)
- **CDO Project:** [cyberdomainontology.org](https://cyberdomainontology.org/)

### Share Your Work
- If you build something useful, consider open-sourcing it
- Contribute improvements back to the projects you build on
- Share your experience with colleagues at your agency

### Keep Learning
- Check the [resources](../../../resources/) directory for further reading
- Explore the GitHub organizations from Exercise 1
- Practice with the AI-assisted modeling workflow from Exercise 5
