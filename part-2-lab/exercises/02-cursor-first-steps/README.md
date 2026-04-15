# Exercise 2: Cursor First Steps

**Duration:** 15 minutes
**Goal:** Get comfortable working with the AI agent in Cursor — it's your collaborator, not a black box

## Step 1: Have a Conversation

Open the Cursor agent panel (Cmd/Ctrl+L or click the chat icon).

Try these prompts one at a time. Read the agent's response before moving to the next.

### Prompt 1: Ask a question
> What is the CASE ontology and how is it used in digital forensic investigations?

Notice how the agent provides a structured, informative answer. This is the agent working as a **knowledge resource**.

### Prompt 2: Ask it to explain code
> Can you explain what this Python code does?
>
> ```python
> import json
>
> def parse_cybertip(xml_path):
>     """Parse a CyberTip XML file and extract key fields."""
>     import xml.etree.ElementTree as ET
>     tree = ET.parse(xml_path)
>     root = tree.getroot()
>     tips = []
>     for report in root.findall('.//report'):
>         tip = {
>             'id': report.get('id'),
>             'date': report.findtext('dateReceived'),
>             'subject': report.findtext('subject'),
>         }
>         tips.append(tip)
>     return tips
> ```

Notice how the agent explains each part in plain language. You don't need to understand the code to understand what it does — the agent bridges that gap.

### Prompt 3: Ask it to create something
> Create a simple Python script that takes a person's name and a list of devices as input, and prints a summary of who owns what. Keep it simple.

Watch what happens:
- The agent writes the code
- It may create a new file
- It may offer to run it for you

This is the agent **working ON your project** — writing code, creating files.

## Step 2: Watch the Agent Use Tools

Ask the agent:

> Read the README.md file in this project and summarize what this course is about.

Watch the agent panel. You'll see it:
1. **Read** the file (using the file system tool)
2. **Analyze** the contents
3. **Summarize** in natural language

This is the agent using tools — reading files is one of its most basic capabilities. In later exercises, you'll see it write files, run commands, search the web, and interact with external applications.

## Step 3: Agent as Research Assistant

Ask the agent:

> What is the difference between a UI, CLI, API, and MCP? Give me a one-sentence summary of each, with an example from law enforcement.

Compare the agent's answer to what you learned in the lecture. The agent is now your **on-demand reference** — you can ask it to clarify or expand on any concept.

## Step 4: Agent as Code Generator

Ask the agent:

> Create a Python script called hello_investigator.py that:
> 1. Asks for the investigator's name
> 2. Asks for their agency
> 3. Prints a welcome message
> 4. Prints today's date and time
>
> Then run it.

Watch the agent:
1. **Write** the script (working ON the project)
2. **Run** the script (working IN the project)
3. **Show** you the output

This is the "working ON and IN simultaneously" concept from the lecture — the agent created the tool and then used it, all in one interaction.

## Step 5: Iterate

The output might not be exactly what you want. Try:

> Can you modify hello_investigator.py to also ask what type of case they're working on (ICAC, cyber fraud, etc.) and include that in the output?

Watch how the agent reads the existing file, understands the changes needed, and modifies it. This is the **iterative** nature of working with an agent — you guide, it implements, you refine.

## Step 6: Give the Agent Rules

The agent is powerful, but without guidance it makes its own assumptions. **Agent rules** are written instructions the agent reads every time you prompt it. They make the agent's behavior predictable and consistent.

### See an Existing Rule

This course repository already has a rule. Ask the agent:

> Read the file .cursor/rules/course-context.mdc and explain what it does.

Notice the structure:
- A **front-matter header** with `description` and `alwaysApply: true`
- A **body** written in plain language describing how the agent should behave

The agent read this rule before every prompt you've sent in this exercise. That's why it already knows about CASE/UCO/CAC and law enforcement context — the rule told it.

### Create Your First Rule

Now create your own rule. Ask the agent:

> Create a new Cursor rule file at .cursor/rules/no-real-data.mdc with the following:
> - description: "Never use real PII, case data, or victim information — all examples must use synthetic data"
> - alwaysApply: true
> - In the body, explain that this is a law enforcement training environment, all data must be synthetic, and the agent should generate realistic but fictional names, dates, and case numbers when examples are needed.

After the agent creates the file, open it and read it. This rule will now apply to every future prompt in this project.

### Test Your Rule

Ask the agent something that would trigger the rule:

> Create a sample evidence log entry for a seized laptop.

Check: Did the agent use synthetic data (fictional names, made-up case numbers)? The rule should have guided it to do so automatically, without you having to remind it.

### Key Takeaway on Rules

- Rules live in `.cursor/rules/` as `.mdc` files
- The agent reads them **every time** you send a prompt
- You can add and adjust rules over time as you learn what the agent needs
- You can build a **library of rules** and reuse them across projects
- Rules complement spec-driven development — specs guide individual features, rules guide everything

## Done When

- [ ] You had a conversation with the agent (knowledge question, code explanation, creation)
- [ ] You watched the agent use tools (reading files, running commands)
- [ ] You created and ran `hello_investigator.py`
- [ ] You iterated on the script (agent modified existing code)
- [ ] You read the existing `course-context.mdc` rule and understood its structure
- [ ] You created the `no-real-data.mdc` rule and tested it

## What You Just Did

You experienced the AI agent as:

1. **A knowledge resource** — answering questions about concepts
2. **A code explainer** — making technical code accessible
3. **A research assistant** — summarizing and clarifying
4. **A code generator** — writing software from your description
5. **A tool user** — reading files and running commands
6. **An iterative collaborator** — refining based on your feedback
7. **A rule-following collaborator** — behaving predictably when given written rules

The agent is not a black box. You see what it does. You approve or redirect. You give it rules, and it follows them. You are in control.

This is the collaborator you'll use for the rest of the lab — and for building mission tools after you leave.
