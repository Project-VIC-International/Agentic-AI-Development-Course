# Exercise 0: Environment Setup

**Duration:** 15 minutes
**Goal:** Verify your development environment is working and get oriented in Cursor

## Step 1: Verify Your Tools

Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and run:

```bash
git --version
python3 --version
```

You should see version numbers for both. If not, see the [prerequisites guide](../../prerequisites.md).

## Step 2: Clone the Course Repository

If you haven't already:

```bash
git clone https://github.com/YOUR-ORG/Agentic-AI-Development-Course.git
cd Agentic-AI-Development-Course
```

## Step 3: Open in Cursor

Launch Cursor and open the `Agentic-AI-Development-Course` folder:

- **Option A:** In the terminal, type `cursor .` (if Cursor is in your PATH)
- **Option B:** Open Cursor → File → Open Folder → select the folder

## Step 4: Orient Yourself in Cursor

Take a minute to explore the interface:

1. **File Explorer (left panel):** Shows your project files. Click on any file to open it.
2. **Editor (center):** Where files are displayed and edited.
3. **Terminal (bottom):** Click Terminal → New Terminal. This is where you run commands.
4. **Agent Panel (right or via Cmd/Ctrl+L):** This is where you chat with the AI agent.

Try opening the agent panel now. You should see a text input where you can type messages.

## Step 5: Your First Agent Interaction

In the agent panel, type:

> What files are in this project? Give me a brief overview of the repository structure.

The agent will read the project files and explain what it finds. This is your first taste of working with an AI agent — you ask in natural language, it explores and answers.

## Step 6: Verify Python Environment

In the Cursor terminal, run:

```bash
python3 -c "print('Environment is ready!')"
```

You should see `Environment is ready!` printed.

## Checkpoint

Before moving on, confirm:

- [ ] Git is installed and working
- [ ] Python 3.10+ is installed and working
- [ ] The course repository is cloned
- [ ] Cursor is open with the project loaded
- [ ] You've opened the agent panel and sent a message
- [ ] The terminal works inside Cursor

If any of these aren't working, ask the instructor for help now — everything that follows depends on this setup.

## What You Just Did

You set up a complete agentic AI development environment. You have:

- **Git** — for version control and collaboration
- **Python** — for running and building tools
- **Cursor** — an IDE with an AI agent that can read files, write code, and run commands
- **The course repository** — containing all exercises and examples

You also had your first interaction with an AI agent. It read your project files and answered your question in natural language. That's the foundation everything else builds on.
