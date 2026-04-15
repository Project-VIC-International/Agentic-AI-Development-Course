#!/usr/bin/env python3
"""
Preflight check for the Agentic AI Development Course.

Run this script to verify your environment is ready for the lab.

Usage:
    python preflight.py        (Mac/Linux)
    python preflight.py        (Windows — use 'python' not 'python3')
"""

import sys
import shutil
import subprocess

PASS = "PASS"
FAIL = "FAIL"
WARN = "WARN"

results = []


def check(name, status, detail=""):
    results.append((name, status, detail))
    symbol = {"PASS": "+", "FAIL": "!", "WARN": "~"}[status]
    print(f"  [{symbol}] {name}: {status}" + (f" — {detail}" if detail else ""))


def run_cmd(cmd):
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=10
        )
        return result.stdout.strip() or result.stderr.strip()
    except FileNotFoundError:
        return None
    except subprocess.TimeoutExpired:
        return None


print()
print("=" * 60)
print("  Agentic AI Development Course — Preflight Check")
print("=" * 60)
print()

# Python version
py_version = sys.version_info
if py_version >= (3, 10):
    check("Python version", PASS, f"{py_version.major}.{py_version.minor}.{py_version.micro}")
elif py_version >= (3, 8):
    check("Python version", WARN, f"{py_version.major}.{py_version.minor} (3.10+ recommended)")
else:
    check("Python version", FAIL, f"{py_version.major}.{py_version.minor} (need 3.10+)")

# Git
git_version = run_cmd(["git", "--version"])
if git_version:
    check("Git", PASS, git_version)
else:
    check("Git", FAIL, "not found — install from git-scm.com/downloads")

# pip
pip_check = run_cmd([sys.executable, "-m", "pip", "--version"])
if pip_check:
    check("pip", PASS)
else:
    check("pip", FAIL, "not found — may need to install python3-pip")

# rdflib
try:
    import rdflib
    check("rdflib", PASS, f"v{rdflib.__version__}")
except ImportError:
    check("rdflib", WARN, "not installed — run: pip install rdflib")

# pyshacl
try:
    import pyshacl
    check("pyshacl", PASS, f"v{pyshacl.__version__}")
except ImportError:
    check("pyshacl", WARN, "not installed — run: pip install pyshacl")

# GitHub CLI
gh_version = run_cmd(["gh", "--version"])
if gh_version:
    first_line = gh_version.split("\n")[0]
    check("GitHub CLI (gh)", PASS, first_line)
else:
    check("GitHub CLI (gh)", WARN, "not installed (optional)")

# Cursor
cursor_path = shutil.which("cursor")
if cursor_path:
    check("Cursor in PATH", PASS)
else:
    check("Cursor in PATH", WARN, "not in PATH — you can still open Cursor manually")

print()
print("-" * 60)

fails = sum(1 for _, s, _ in results if s == FAIL)
warns = sum(1 for _, s, _ in results if s == WARN)

if fails == 0 and warns == 0:
    print("  All checks passed. You are ready for the lab!")
elif fails == 0:
    print(f"  {warns} warning(s) — you can proceed, but review the items above.")
else:
    print(f"  {fails} check(s) FAILED — fix these before the lab starts.")

print()
