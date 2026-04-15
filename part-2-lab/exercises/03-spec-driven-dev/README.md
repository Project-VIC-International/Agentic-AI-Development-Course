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

Pick one (or bring your own idea) and use the starter template to write a specification.

### Use the Starter Template

Open the spec template:

```
part-2-lab/exercises/03-spec-driven-dev/templates/spec-template.md
```

This template has every section you need, with placeholders to fill in. You don't need to invent the structure from scratch — just fill in the blanks.

In Cursor's agent panel:

> Read the template at part-2-lab/exercises/03-spec-driven-dev/templates/spec-template.md and the constitution at part-2-lab/exercises/03-spec-driven-dev/example-spec/constitution.md.
>
> I want to build a [YOUR TOOL IDEA]. Help me fill in the spec template for this tool. Save the completed specification as spec.md in this directory.

The agent will generate a specification document using the template structure. Review it:
- Does it capture what you actually want?
- Is anything missing?
- Is anything wrong?

Tell the agent to revise until you're satisfied.

## Step 3: Generate a Plan

Once your specification is solid, use the plan template:

> Read the plan template at part-2-lab/exercises/03-spec-driven-dev/templates/plan-template.md and the spec we just wrote.
>
> Generate a technical plan for this tool using the template structure. Include architecture, data model, components, CASE/UCO/CAC integration approach, and testing strategy.
>
> Save the plan as plan.md.

Review the plan. This is where the agent translates your "what" into "how." Check:
- Does the architecture make sense?
- Does it use CASE/UCO/CAC from the beginning (not as an afterthought)?
- Is the testing approach adequate?

## Step 4: Generate Tasks

Use the tasks template to break the plan into work units:

> Read the tasks template at part-2-lab/exercises/03-spec-driven-dev/templates/tasks-template.md and the plan we just wrote.
>
> Break the plan into an ordered list of atomic, testable tasks using the template structure. Each task should have a clear description and a "done when" criterion.
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

## Done When

You should have these artifacts saved in your project:

- [ ] `constitution.md` — reviewed and discussed as a class
- [ ] `spec.md` — your tool specification, reviewed and revised
- [ ] `plan.md` — technical plan generated from the spec
- [ ] `tasks.md` — ordered list of atomic tasks
- [ ] Consistency check — agent reviewed all four documents for alignment

## What You Just Did

You used spec-driven development to go from a vague idea to a complete, verified project plan — without writing a single line of code:

1. **Constitution** — guaranteed interoperability requirements are baked in
2. **Specification** — captured your intent in plain language
3. **Plan** — translated intent into architecture
4. **Tasks** — broke architecture into executable work
5. **Verification** — checked everything for consistency

The agent did the heavy lifting. You made the decisions. This is how you stay in control while leveraging AI to do the implementation work.

In Exercise 6, we'll pick up where this left off and actually build the tool.
