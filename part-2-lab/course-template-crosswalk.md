# Course-to-Template Crosswalk

The course repository teaches the workflow. The template repository is where students apply it in their own private project.

| Course concept | Course location | Template location | Student action |
| --- | --- | --- | --- |
| Environment setup | `exercises/00-environment-setup/` | `QUICKSTART.md`, `docs/tooling-setup.md`, `scripts/`, `.devcontainer/devcontainer.json` | Verify tools, run setup scripts if needed, or use Codespaces |
| First agent conversation | `exercises/02-cursor-first-steps/` | `START-HERE.md`, `prompts/START-AGENT-HERE.md`, `AGENTS.md`, `policies/` | Ask the agent to explain the template and its policies before editing |
| Spec-driven development | `exercises/03-spec-driven-dev/` | `docs/spec-kit-workflow.md`, `policies/speckit-workflow.md` | Use `specify -> clarify -> plan -> tasks -> analyze -> implement -> converge` |
| CASE/UCO introduction | `exercises/04-case-uco-introduction/` | `docs/case-uco-cac-guidance.md`, `examples/synthetic-data/` | Identify where CASE/UCO concepts fit the project |
| CAC ontology modeling | `exercises/05-cac-ontology-modeling/` | `docs/case-uco-cac-guidance.md`, `policies/ontology-alignment.md` | Identify CAC concepts and reuse them where practical |
| Prototype build | `exercises/06-build-a-prototype/` | `intake/`, `planning/`, `.github/ISSUE_TEMPLATE/`, `examples/` | Build one small reviewed issue at a time with synthetic data |

## Recommended Student Flow

1. Open this course guide.
2. Create a private repository from the template.
3. Open the template-based project in your AI coding agent (see the template's `docs/agent-setup.md`).
4. Paste `prompts/START-AGENT-HERE.md`.
5. Complete `intake/problem-intake.md`.
6. Review the intake.
7. Draft a milestone plan.
8. Work one approved issue at a time.

## Safety Reminder

Do not paste real case data into your AI agent, GitHub, issues, logs, screenshots, test files, or sample data. Use synthetic data only.
