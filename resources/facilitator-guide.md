# Facilitator Guide

This guide is for instructors delivering the Agentic AI Development Course. It covers preparation, delivery notes, fallback plans, and common issues.

---

## Before the Session

### Room Setup

- [ ] Projector connected and tested
- [ ] Wi-Fi credentials posted visibly (students will need internet)
- [ ] Power strips available — this is a laptop-heavy session
- [ ] Cheat sheets printed ([resources/cheat-sheet.md](cheat-sheet.md)) — one per student

### Technical Preparation

- [ ] Clone the course repo on your own machine and verify exercises work end-to-end
- [ ] Run `python3 part-2-lab/preflight.py` on your own machine — it should pass
- [ ] Run the validator: `python3 part-2-lab/exercises/04-case-uco-introduction/validation/validate_graph.py`
- [ ] Run the validator on the bad graph to confirm it fails: `python3 part-2-lab/exercises/04-case-uco-introduction/validation/validate_graph.py part-2-lab/exercises/04-case-uco-introduction/validation/graph_with_errors.jsonld`
- [ ] Test Cursor agent panel — send at least one prompt to verify you can connect
- [ ] Have a second AI service open in a browser (ChatGPT, Gemini) for cross-model review demos
- [ ] Verify you can access all four GitHub organizations (casework, CDO, ucoProject, Project-VIC-International)

### Fallback Materials

Prepare these in case of Wi-Fi failure, rate limits, or install issues:

- [ ] Pre-recorded demo of Exercise 6 (build-a-prototype) — 5-10 minutes showing spec → plan → tasks → build → validate flow
- [ ] Screenshot set of key Cursor interactions (agent panel, tool use, file creation, terminal)
- [ ] A completed example output from Exercise 5 (investigation-graph.ttl) saved locally
- [ ] Zipped copy of the course repository on a USB drive — for students who can't clone

### Participant Preparation

- Send the [prerequisites guide](../part-2-lab/prerequisites.md) at least one week before the session
- Emphasize: Observer mode is full participation — no one should feel left out if their laptop can't run installs
- For groups with many restricted laptops, consider providing 3-4 pre-configured machines that pairs can share

---

## Part 1: Lecture Delivery

### Timing

See the [timing table in the lecture outline](../part-1-lecture/outline.md) for core vs. stretch guidance. Key points:

- **Strict 50 min:** Compress testing/validation/security to 2 min headline, summarize agent memory briefly
- **Standard 60 min:** Deliver as written, watch the clock at section 8 (CASE/UCO) — it's easy to run long on facets and SPARQL
- **Extended 75+ min:** Add live SPARQL examples and detailed NIST walkthrough

### Audience Engagement Points

These are the moments where the audience is most likely to engage. Lean into them:

1. **Section 7 (Interoperability Journey):** Ask the room about data normalization pain. This is their daily frustration. Let them vent briefly — it validates the problem.
2. **Section 4 (Four Doors):** The "AI agent working ON and IN simultaneously" concept surprises people. Pause and let it land.
3. **Section 8 (Reasoning):** The three-hop inference example (person → account → IP → location) always gets a reaction from investigators. They immediately see the value.
4. **Section 6 (Agent Rules):** Investigators understand rules and policies. This section clicks fast with this audience.

### Common Questions

| Question | Answer |
|----------|--------|
| "Can the AI access our case data?" | Not unless you give it access. Cursor runs locally. You control what files are in the project. For sensitive data, use local models behind your firewall. |
| "Is this admissible in court?" | The tool itself must be independently tested and validated. CASE/UCO compliance helps with structured, auditable output. But no tool is automatically admissible — T&V is mandatory. |
| "What if the AI makes a mistake?" | It will. That's why we use spec-driven development (catch errors before code), SHACL validation (catch errors in data), and cross-model review (second opinion). You always review. |
| "Our agency won't let us install software." | Observer mode today. For production: work with your IT team, use local models, pursue authorized tool procurement channels. |
| "How is this different from ChatGPT?" | ChatGPT is a chatbot — it answers questions. An agent in Cursor has tools: it can read files, write code, run commands, search the web, and interact with databases. It acts, not just responds. |

---

## Part 2: Lab Delivery

### Exercise-by-Exercise Notes

#### Exercise 0: Environment Setup (15 min)

- Walk the room while students run the preflight check
- Common issue: Windows `python3` vs `python` — tell them up front
- If >30% of the room has install problems, switch to a paired model immediately
- Have your own screen showing the preflight output as a reference

#### Exercise 1: GitHub Exploration (15 min)

- This exercise works even in Observer mode (browser only)
- Live-demo the GitHub search on the projector while students follow along
- Point out the CAC Ontology's `agent.md` file — this is relevant to the Rules concept

#### Exercise 2: Cursor First Steps (15 min)

- Walk the room — first agent interactions often have confusion about which panel to type in
- The "create and run a script" step (Step 4) is the "aha" moment for most students
- If Cursor rate limits hit, pair up immediately

#### Exercise 3: Spec-Driven Development (30 min)

- This is the most important exercise conceptually
- Start with a group read of the constitution — have someone read each section aloud
- The templates reduce prompt fragility — students fill in blanks rather than inventing structure
- Common issue: students pick overly ambitious tool ideas. Guide them toward simpler options
- Review 2-3 specs as a class before moving to plan generation

#### Exercise 4: CASE/UCO Introduction (20 min)

- The validation step is the concrete payoff — make sure every student sees the validator run
- If rdflib/pyshacl won't install, demo it on the projector and show both pass and fail
- The "modify the graph" step (add a second device) is where students see the agent write real ontology data

#### Exercise 5: CAC Ontology Modeling (25 min)

- The cross-model review step is important — have ChatGPT or Gemini open in a browser
- Students are often impressed by how much the agent extracts from the press release
- Common issue: agent may use incorrect namespace URIs — this is a teaching moment about validation

#### Exercise 6: Build a Prototype (remaining time)

- This is instructor-led as a class — one person drives while others navigate
- Pick the tool as a group vote. Option C (Investigation Graph Builder) is the safest default because it builds on Exercise 5.
- Don't try to finish everything — getting through spec + plan + first 2-3 tasks is a success
- End with a validation run even if the tool isn't complete — closing on "the output validates" is a strong finish

### When Things Go Wrong

| Problem | Fallback |
|---------|----------|
| Wi-Fi down | Use USB drive with pre-cloned repo. Exercises 1 and web-search features won't work, but Cursor agent, file editing, and validation all work offline |
| Cursor rate limits | Pair up. Two students per Cursor session. This actually improves learning through discussion |
| Can't install Python packages | Demo validation on projector. Students watch and take notes |
| Agent produces bad output | This is a teaching moment. Show the error, discuss why it happened, fix it together |
| Running behind schedule | Skip Exercise 1 (students can explore GitHub later). Jump from Ex 0 → Ex 2 → Ex 3 |

---

## After the Session

### Follow-Up Resources

Direct students to:
- The course repository — they keep it forever
- [resources/further-reading.md](further-reading.md) — curated reading list
- [resources/links.md](links.md) — links to communities, standards, and tools
- CAC Ontology community — [site.cacontology.projectvic.org/community](https://site.cacontology.projectvic.org/community)

### Collecting Feedback

Ask students (verbally or via quick survey):
1. What was the most useful thing you learned?
2. What would you change about the course?
3. Do you plan to try building a tool using this workflow?
4. Would you want a follow-up session focused on [graph databases / validation / specific tool building]?

### Reporting

For organizational reporting:
- Number of participants and agencies represented
- Participation mode breakdown (hands-on / paired / observer)
- Which prototype was built in Exercise 6
- Any tools or follow-up projects that participants plan to pursue
