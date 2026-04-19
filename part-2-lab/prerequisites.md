# Prerequisites & Setup Guide

Complete these steps **before** the lab session. If you run into issues, bring your laptop to the session and we'll help you during Exercise 0.

## Participation Modes

Not everyone has the same laptop or the same technical background. Choose the mode that fits your situation:

| Mode | What You Need | What You Do |
|------|--------------|-------------|
| **Hands-On** (recommended) | Your own laptop with Git, Python, and Cursor installed | Follow every exercise yourself |
| **Paired** | A seat next to someone in Hands-On mode | Work together — one drives, one navigates. Switch roles between exercises |
| **Observer** | A web browser and a GitHub account | Follow along on the projector, explore GitHub repos in your browser, take notes. The instructor walks through every step live |

All three modes are full participation. You will learn the concepts regardless of which mode you choose. If your agency laptop has restrictions that prevent installs, **Observer mode is designed for you** — bring the laptop anyway and follow along in your browser.

## Required Software (Hands-On Mode)

### 1. GitHub Account (Free)

1. Go to [github.com](https://github.com)
2. Click "Sign up" and create a free account
3. Verify your email address
4. Remember your username and password — you'll need them

### 2. Git

Git is the version control tool that lets you download and share code.

**Check if you already have it:**
```bash
git --version
```

If you see a version number (e.g., `git version 2.43.0`), you're good.

**If not installed:**
- **Windows:** Download from [git-scm.com/downloads](https://git-scm.com/downloads)
- **Mac:** Open Terminal and type `git --version` — macOS will prompt you to install it
- **Linux:** `sudo apt install git` (Ubuntu/Debian) or `sudo dnf install git` (Fedora)

### 3. Python 3.10+

Python is the programming language we'll use for exercises and prototyping.

**Check if you already have it:**
```bash
python3 --version
```

> **Windows users:** If `python3` is not recognized, try `python --version` instead. On Windows, Python is often available as `python` rather than `python3`. Either is fine as long as the version is 3.10 or higher.

If you see version 3.10 or higher, you're good.

**If not installed:**
- **All platforms:** Download from [python.org/downloads](https://www.python.org/downloads/)
- During installation on Windows, **check "Add Python to PATH"** — this is critical

### 4. Cursor IDE

Cursor is the AI-powered development environment we'll use throughout the lab.

1. Go to [cursor.com](https://cursor.com)
2. Download the installer for your operating system
3. Run the installer
4. Launch Cursor and sign in (you can use your GitHub account)
5. The free tier is sufficient for this lab. A $20/month subscription will help you build a simple tool every month. A $200/month subscription will help you build a lot. You can add a budget on top of that as you need.

### 5. GitHub CLI (Optional but Recommended)

The GitHub CLI (`gh`) makes it easy to interact with GitHub from the command line.

**Install:**
- **Windows:** `winget install --id GitHub.cli`
- **Mac:** `brew install gh`
- **Linux:** See [cli.github.com/manual/installation](https://cli.github.com/manual/installation)

**Authenticate:**
```bash
gh auth login
```

Follow the prompts to log in with your GitHub account.

## Pre-Lab Setup

Once all software is installed, clone the course repository and run the preflight check:

```bash
git clone https://github.com/Project-VIC-International/Agentic-AI-Development-Course.git
cd Agentic-AI-Development-Course
```

Run the preflight check to verify everything at once:

```bash
python3 part-2-lab/preflight.py
```

> **Windows users:** Use `python part-2-lab/preflight.py` if `python3` is not recognized.

The script checks Python version, Git, pip, and optional dependencies. Fix any items marked `FAIL` before the lab. Items marked `WARN` are optional and won't block you.

Open the project in Cursor:

```bash
cursor .
```

Or open Cursor manually and use File → Open Folder to open the `Agentic-AI-Development-Course` directory.

## What You Do NOT Need

- **No programming experience.** We will explain everything as we go.
- **No AI experience.** The lecture (Part 1) covers the fundamentals.
- **No ontology knowledge.** We build understanding step by step.
- **No paid subscriptions.** Free tiers of all tools are sufficient.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `git` command not found | Reinstall Git, ensure it's added to PATH |
| `python3` command not found | Try `python --version` (Windows). If still missing, reinstall Python and check "Add to PATH" |
| Cursor won't launch | Check system requirements at [cursor.com](https://cursor.com) |
| GitHub authentication fails | Run `gh auth login` and follow prompts |
| Can't clone the repository | Check internet connection, verify GitHub credentials |
| Agency laptop blocks installs | Use Observer mode — follow along in your browser and pair with a neighbor |
| Cursor free-tier rate limit | Pair up — two people share one Cursor session. This also models real collaboration |

If you arrive at the lab without completing setup, don't worry — pair with someone who has, and we'll help you get set up during Exercise 0.
