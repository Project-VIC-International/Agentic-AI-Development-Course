# Exercise 1: GitHub Exploration

**Duration:** 15 minutes
**Goal:** Learn to use GitHub as a library — search for existing projects before building something new

## The Principle

> Before you build anything, search for what already exists.

GitHub hosts millions of projects. Many are directly relevant to your mission. Learning to search effectively saves time and connects you to a global community of practitioners.

## Step 1: Search GitHub for ICAC-Related Projects

Open your browser and go to [github.com](https://github.com).

In the search bar, try these searches:

1. `ICAC investigation`
2. `CyberTip processing`
3. `digital forensics tool`
4. `child exploitation detection`

For each search:
- Look at the results. How many repositories come up?
- Click on one that looks interesting
- Read the README — does it explain what the project does?
- Check: when was it last updated? How many stars does it have?

**Write down one project that looks interesting or useful.**

## Step 2: Explore the CDO Ecosystem Organizations

Visit each of these GitHub organizations and explore their repositories:

### CASE Community
**URL:** [github.com/casework](https://github.com/casework)

- What kinds of projects are here?
- Find the CASE ontology repository — what does the README say?
- Look for example files — these show how CASE data is structured

### Cyber Domain Ontology
**URL:** [github.com/Cyber-Domain-Ontology](https://github.com/Cyber-Domain-Ontology)

- This is the governance organization for CASE and UCO
- Look at CDO-Shapes repositories — these define validation rules
- Notice the consistent structure: each repo has documentation, tests, and examples

### UCO Project
**URL:** [github.com/ucoProject](https://github.com/ucoProject)

- UCO is the foundation that CASE and CAC Ontology build on
- Find the main UCO ontology repository
- Look at the namespace structure — this is the vocabulary of the cyber domain

### CAC Ontology
**URL:** [github.com/Project-VIC-International/CAC-Ontology](https://github.com/Project-VIC-International/CAC-Ontology)

- This is the domain-specific extension for crimes against children
- Read the README — what modules does it include?
- Look at the `examples/` directory — these are real investigation models
- Look at `agent.md` — this is how AI agents are guided to use the ontology

## Step 3: Evaluate a Repository

Pick one repository from the organizations above. Answer these questions:

1. **What does it do?** (Read the README)
2. **Is it active?** (Check the last commit date)
3. **Is it well-documented?** (Is there a README, docs folder, examples?)
4. **What license does it use?** (Look for a LICENSE file)
5. **Could you use it in your work?** (Does it solve a problem you have?)

## Step 4: Ask the Agent

Go back to Cursor and ask the agent:

> Search GitHub for open-source tools related to ICAC investigations or CyberTip processing. What projects exist? Which ones look most mature and well-maintained?

Watch how the agent searches, evaluates, and summarizes. This is the agent using **Door 3 (API)** and **Door 4 (MCP)** to interact with GitHub — the same doors we discussed in the lecture.

## Done When

- [ ] You searched GitHub and found at least one ICAC-related project
- [ ] You visited all four CDO ecosystem organizations (casework, CDO, ucoProject, CAC Ontology)
- [ ] You evaluated one repository for activity, documentation, and licensing
- [ ] You asked the agent to search GitHub and reviewed its findings

## What You Just Did

You learned to treat GitHub as a library:

- **Search first** — don't reinvent what already exists
- **Evaluate quality** — activity, documentation, licensing
- **Explore ecosystems** — CASE, UCO, CDO, and CAC Ontology are maintained communities
- **Use the agent to search** — it can find and summarize projects faster than manual browsing

This mindset — **search → evaluate → build on existing work** — is the foundation of the open-source approach we'll use for the rest of the lab.
