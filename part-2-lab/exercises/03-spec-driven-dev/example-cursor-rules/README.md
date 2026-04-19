# Example Cursor Rules — CAC Mission Tools Starter Pack

This directory contains a **starter pack of Cursor rules** that any Crimes Against Children (CAC) investigator can copy into their own project to get an AI agent (Cursor, Claude Code, Codex, etc.) building tools the right way from the very first prompt.

These rules are generalized from the Cursor rules used by Project VIC International on its own development projects (Forensics, Media Authentication, the CASE/UCO/CAC SDK, the CAC Ontology). The versions here are technology-agnostic and written for investigators with no programming background — pair them with the [project constitution](../example-spec/constitution.md) and you have a complete "ground rules" pack for your AI agent.

## What Are Cursor Rules?

Cursor rules are short Markdown files in `.cursor/rules/` that the AI agent reads **on every prompt**. They are persistent context — they tell the agent things like "always validate output against SHACL" or "never hardcode secrets" without you having to repeat yourself.

Think of them as **standing orders** for your AI investigator-developer.

The format is simple:

```
---
description: Short one-line description shown to the agent
alwaysApply: true
---

# Rule body in plain Markdown
```

`alwaysApply: true` means the agent reads this rule on every turn. Use `alwaysApply: false` plus a `globs:` pattern to scope a rule to specific files (e.g., only `tests/**`).

Cursor's official documentation: https://docs.cursor.com/context/rules

## How to Use This Starter Pack

1. **Create a `.cursor/rules/` directory in your own project.**
2. **Copy the rules you want.** All eight are designed to work together but you can adopt them incrementally.
3. **Customize each rule for your project.** Look for `[FILL IN]` placeholders — these are spots where you should plug in your project's specifics (e.g., the name of your CLI command, the names of your modules, your performance targets).
4. **Commit the rules to your repository.** They become part of your project's source code. Every contributor — human or AI — gets the same standing orders.
5. **Iterate.** Watch what your AI agent does. When it does the wrong thing, the fix is usually a sharper rule.

## The Eight Rules

| Rule | Purpose | Why It Matters for CAC Tools |
|------|---------|-------------------------------|
| [`speckit-workflow.mdc`](speckit-workflow.mdc) | Mandate spec-driven development for every feature | Stops "vibe coding"; produces court-defensible documentation |
| [`no-stubs.mdc`](no-stubs.mdc) | Forbid placeholder / mock implementations | Prevents fake "it works" handlers from shipping |
| [`four-surface-review.mdc`](four-surface-review.mdc) | Require GUI / CLI / API / MCP impact review for every change | Investigators, examiners, integrators, and AI agents all need access |
| [`ontology-alignment.mdc`](ontology-alignment.mdc) | Mandate CASE / UCO / CAC (and optional SOLVE-IT) compliance | True interoperability across agencies and tools |
| [`security-compliance.mdc`](security-compliance.mdc) | Enforce NIST SP 800-53 Rev. 5 and FBI CJIS Security Policy | Required for any tool touching CJI |
| [`cross-platform.mdc`](cross-platform.mdc) | Require Windows / Linux / macOS support from day one | Examiner workstations vary across agencies |
| [`auto-research.mdc`](auto-research.mdc) | Use Karpathy-style measure-then-improve loops | Performance gains that you can defend in court |
| [`release-management.mdc`](release-management.mdc) | Require `CHANGELOG.md` and `README.md` updates per release | Reproducibility, attributability, and audit trail |

## How These Rules Interact with the Constitution

The [constitution](../example-spec/constitution.md) says **what** your project stands for. These rules say **how** the AI agent should behave when it builds toward those values:

- The constitution says "all output must be CASE/UCO/CAC compliant." The `ontology-alignment` rule tells the agent to query the CASE/UCO SDK before writing serialization code.
- The constitution says "tools must comply with CJIS." The `security-compliance` rule tells the agent which control families apply to which features.
- The constitution says "spec-driven development." The `speckit-workflow` rule tells the agent never to write code without a spec.

## Adopting the Rules in Your Own Project

Once you have a project repo, the typical setup is:

```bash
mkdir -p .cursor/rules
cp /path/to/this/course/part-2-lab/exercises/03-spec-driven-dev/example-cursor-rules/*.mdc .cursor/rules/

mkdir -p .specify/memory
cp /path/to/this/course/part-2-lab/exercises/03-spec-driven-dev/example-spec/constitution.md .specify/memory/constitution.md
```

That's it. Cursor will start applying the rules immediately on your next prompt. Edit the placeholders in each rule to match your project, then commit:

```bash
git add .cursor/rules .specify/memory
git commit -m "Adopt CAC mission tool starter rules and constitution"
```

## Contributing Improvements Back

If you sharpen a rule for your agency's workflow, please consider opening a pull request to this course or to Project VIC. The whole community benefits from better standing orders.

## Credit

These rules are derived from the Cursor rules maintained by Project VIC International for its open-source development projects. They are released under the same Apache 2.0 license as the rest of this course.
