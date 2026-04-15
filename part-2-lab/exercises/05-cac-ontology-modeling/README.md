# Exercise 5: CAC Ontology Modeling

**Duration:** 25 minutes
**Goal:** Model a crimes against children investigation scenario using the CAC Ontology with AI-assisted workflow

## The Scenario

You will model a realistic (but entirely synthetic) investigation scenario as a CAC Ontology knowledge graph. This exercise uses the same AI-assisted modeling workflow that practitioners use in the field.

## Step 1: Read the Scenario

Open and read the synthetic press release:

```
part-2-lab/exercises/05-cac-ontology-modeling/examples/synthetic-press-release.md
```

This is a fictional press release describing the conclusion of an ICAC investigation. It contains the kinds of details that a real press release would: suspect information, charges, evidence, agencies involved, and outcomes.

## Step 2: Model with AI

In the Cursor agent panel, provide the scenario and ask the agent to model it:

> Read the file part-2-lab/exercises/05-cac-ontology-modeling/examples/synthetic-press-release.md
>
> Model this investigation as a CASE/UCO/CAC Ontology knowledge graph in Turtle format. Include:
> 1. The investigation itself
> 2. All persons mentioned (suspect, investigators, victims — use synthetic identifiers only)
> 3. All devices and digital evidence
> 4. All forensic actions and tools used
> 5. Legal processes (charges, arrest, prosecution)
> 6. The CyberTip that initiated the investigation
> 7. All relationships between these entities
>
> Use proper UCO, CASE, and CAC Ontology namespaces. Save the output as investigation-graph.ttl.

Watch the agent work. It will:
1. Read the press release
2. Identify the entities (people, devices, evidence, actions)
3. Map them to the appropriate ontology classes
4. Create the relationships between them
5. Produce a valid Turtle file

## Step 3: Review the Graph

Ask the agent to summarize what it created:

> Summarize the knowledge graph you just created. How many entities are there? What types? How are they connected? Draw me an ASCII diagram showing the key relationships.

Compare the summary to the original press release. Did the agent capture everything? Did it miss anything?

## Step 4: Query the Graph

Ask the agent to demonstrate what you can do with structured data that you can't do with a press release:

> Using the knowledge graph, answer these investigative questions:
> 1. What devices were seized and what evidence was found on each?
> 2. What is the chain of custody for each piece of evidence?
> 3. What timeline of events can be constructed?
> 4. What agencies and personnel were involved?
> 5. What charges resulted from what evidence?

These questions would require manual reading and note-taking with a flat document. With a knowledge graph, they can be answered programmatically.

## Step 5: Cross-Model Review

This step demonstrates the "AI review team" concept from the lecture.

Copy the graph the agent generated. Open a different AI service in your browser (ChatGPT, Gemini, or another model). Paste the graph and ask:

> Review this CASE/UCO/CAC Ontology knowledge graph for completeness and correctness:
> 1. Are all entities properly typed with the correct ontology classes?
> 2. Are relationships complete — did I miss any connections?
> 3. Are there any CASE/UCO modeling best practices I violated?
> 4. What additional information from the source document could be captured?

Compare the feedback from the second model. Different models catch different issues — this is why using multiple models as peer reviewers improves quality.

## Step 6: Compare to Flat Data

Ask the Cursor agent:

> If this investigation data were in a CSV spreadsheet instead of a knowledge graph, what would be lost? Show me what a typical CSV export would look like versus what the knowledge graph captures.

The contrast drives home the value of structured, standards-based data:
- **CSV:** flat rows, no relationships, no provenance, no context
- **Knowledge graph:** connected data, full provenance, queryable, shareable, machine-readable

## Done When

- [ ] You read the synthetic press release and identified key entities
- [ ] The agent produced `investigation-graph.ttl` from the press release
- [ ] You reviewed the graph summary and ASCII diagram
- [ ] You answered investigative questions using the graph
- [ ] You used a second AI model to review the graph (cross-model review)

**Artifact:** `investigation-graph.ttl` — a CASE/UCO/CAC knowledge graph of the synthetic scenario.

## What You Just Did

You completed the AI-assisted CAC Ontology modeling workflow:

1. **Started with a document** — a press release describing an investigation
2. **Used an AI agent** to model it as a knowledge graph
3. **Reviewed** the output for completeness
4. **Queried** the graph to answer investigative questions
5. **Used a second AI model** as a peer reviewer
6. **Compared** structured data to flat data to understand the value

This same workflow works with:
- Real press releases (for training)
- Tool exports (for integration)
- Case reports (for standardization)
- Investigation plans (for operational modeling)

The CAC Ontology captures the full semantic picture of your investigation — not just observations, but the complete context of who, what, when, where, how, and why.
