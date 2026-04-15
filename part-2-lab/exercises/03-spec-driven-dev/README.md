# Exercise 3: Spec-Driven Development

**Duration:** 30 minutes
**Goal:** Use GitHub's spec-kit workflow to define a CAC mission tool — from constitution to tasks — before any code is written

## Why Spec-Driven Development?

In the lecture, we distinguished between "vibe coding" (telling AI to build whatever) and spec-driven development (defining what you want first, then having AI build it).

This exercise puts that into practice. You will:
1. Define the rules of your project (Constitution)
2. Describe what you want and why (Specification)
3. Let the agent generate a technical plan (Plan)
4. Break the plan into atomic work units (Tasks)

Only then does implementation begin.

## Step 1: Understand the Constitution (Group Activity)

The constitution defines the rules every tool built in this project must follow. We've provided a starter constitution for CAC mission tools.

Open and read the file:

```
part-2-lab/exercises/03-spec-driven-dev/example-spec/constitution.md
```

This constitution includes:
- Technology requirements (Python, JSON-LD)
- A mandate for CASE/UCO/CAC compliance
- Security and privacy requirements for law enforcement data
- Open-source and interoperability principles

**Discussion:** As a class, review the constitution. Does it capture the rules your tools should follow? What would you add or change?

## Step 2: Write a Specification

Now it's your turn. Think of a tool you wish existed for your work. Here are some ideas:

- **CyberTip Triage Helper** — Takes CyberTip XML exports and produces a prioritized summary with timeline
- **Evidence Chain Tracker** — Models the chain of custody from seizure to courtroom
- **Case Timeline Generator** — Takes multiple tool outputs and generates a unified timeline
- **Investigation Graph Builder** — Converts a case report into a CASE/UCO/CAC knowledge graph
- **Device-Account Mapper** — Maps relationships between seized devices and associated online accounts

Pick one (or bring your own idea) and ask the agent to help you write a specification.

In Cursor's agent panel:

> I want to create a specification for a [YOUR TOOL IDEA]. Using the spec-driven development approach, help me write a specification that describes:
> 1. What the tool does (in plain language)
> 2. Who uses it (the user persona)
> 3. What problem it solves
> 4. What inputs it takes
> 5. What outputs it produces
> 6. Key constraints (must be CASE/UCO/CAC compliant, must handle sensitive data appropriately)
>
> Reference the constitution in part-2-lab/exercises/03-spec-driven-dev/example-spec/constitution.md for project rules.

The agent will generate a specification document. Review it:
- Does it capture what you actually want?
- Is anything missing?
- Is anything wrong?

Tell the agent to revise until you're satisfied.

## Step 3: Generate a Plan

Once your specification is solid, ask the agent to plan:

> Based on the specification we just wrote, generate a technical plan. Include:
> 1. Architecture overview
> 2. Data model (what objects, properties, and relationships are needed)
> 3. Component breakdown
> 4. CASE/UCO/CAC integration approach
> 5. Testing strategy
>
> Save the plan as plan.md.

Review the plan. This is where the agent translates your "what" into "how." Check:
- Does the architecture make sense?
- Does it use CASE/UCO/CAC from the beginning (not as an afterthought)?
- Is the testing approach adequate?

## Step 4: Generate Tasks

Ask the agent to break the plan into tasks:

> Break this plan into a list of atomic, testable tasks. Each task should:
> 1. Have a clear description
> 2. Be completable independently
> 3. Have a clear "done" criteria
> 4. Be ordered by dependency (what must come first)
>
> Save the task list as tasks.md.

You now have a complete roadmap: Constitution → Specification → Plan → Tasks.

## Step 5: Review the Full Pipeline

Look at what you've created:
1. `constitution.md` — the rules
2. A specification — what and why
3. `plan.md` — how to build it
4. `tasks.md` — step-by-step work units

Ask the agent:

> Review the constitution, specification, plan, and tasks for consistency. Are there any contradictions, gaps, or misalignments? Does the plan honor the constitution's requirements for CASE/UCO/CAC compliance?

This is the **verification step** — catching problems before code is written, not after.

## What You Just Did

You used spec-driven development to go from a vague idea to a complete, verified project plan — without writing a single line of code:

1. **Constitution** — guaranteed interoperability requirements are baked in
2. **Specification** — captured your intent in plain language
3. **Plan** — translated intent into architecture
4. **Tasks** — broke architecture into executable work
5. **Verification** — checked everything for consistency

The agent did the heavy lifting. You made the decisions. This is how you stay in control while leveraging AI to do the implementation work.

In Exercise 6, we'll pick up where this left off and actually build the tool.
