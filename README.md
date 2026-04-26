# Agentic AI Development Course

## Building Interoperable Crimes Against Children Mission Tools with Agentic AI and Open Standards

Training materials for a two-part session at the [National Cyber Crime Conference (NCCC)](https://www.mass.gov/info-details/national-cyber-crime-conference), hosted by the Massachusetts Attorney General's Office.

### Who This Course Is For

Law enforcement investigators, forensic examiners, crime intelligence analysts, and prosecutors working **Crimes Against Children (CAC)** and **Internet Crimes Against Children (ICAC)** cases. No prior programming experience is required.

### What You Will Learn

By the end of this course, you will be able to:

- Explain what AI, large language models, and agentic AI are — and what they are not
- Understand how humans and agents interact with applications (UI, CLI, API, MCP)
- Use GitHub as a library to find and evaluate existing open-source tools
- Use Cursor as an agentic AI IDE to build software through natural language
- Apply spec-driven development to maintain control over what an AI agent builds
- Understand the Cyber Domain Ontology ecosystem: UCO, CASE, and CAC Ontology
- Produce interoperable investigation data using CASE/UCO/CAC standards
- Build a working prototype of a CAC mission tool in a single session

### Course Structure

| Part | Title | Duration |
|------|-------|----------|
| **Part 1** | [The Future Is Here: Building Interoperable Crimes Against Children Mission Tools with Agentic AI and Open Standards](part-1-lecture/) | 1 hour lecture |
| **Part 2** | [From Idea to Prototype: Live Building an Open-Source Crimes Against Children Mission Capability with Agentic AI](part-2-lab/) | Hands-on lab |

## Hands-On Lab Workspace

This course repository explains the method. The [Project VIC Agentic AI Development Project Template](https://github.com/Project-VIC-International/Agentic-AI-Development-Project-Template) is where students should do their hands-on work.

For the lab, create a private repository from the template and use that repository as your Cursor workspace. Keep this course repository open as the reference guide for the lecture, exercises, and background material.

Start with `START-HERE-NCCC.md` in this repository, then switch into the template-based project for the actual lab work.

### Prerequisites

See the [detailed prerequisites and setup guide](part-2-lab/prerequisites.md) for the lab portion. In summary:

- A laptop with internet access
- A [GitHub](https://github.com) account (free)
- [Cursor](https://cursor.com) IDE installed (free tier is sufficient)
- [Python 3.10+](https://www.python.org/downloads/) installed
- [Git](https://git-scm.com/downloads) installed
- No prior programming experience required
- A private repository created from the [Project VIC template](https://github.com/Project-VIC-International/Agentic-AI-Development-Project-Template)

### Key Resources

| Resource | Description |
|----------|-------------|
| [Cyber Domain Ontology](https://cyberdomainontology.org/) | Linux Foundation project governing CASE and UCO |
| [CASE Ontology](https://caseontology.org/) | Cyber-investigation Analysis Standard Expression |
| [UCO Ontology](https://unifiedcyberontology.org/) | Unified Cyber Ontology — the foundation layer |
| [CAC Ontology](https://site.cacontology.projectvic.org/) | Crimes Against Children Ontology — the domain extension |
| [GitHub spec-kit](https://github.com/github/spec-kit) | Toolkit for spec-driven development with AI |
| [Cursor IDE](https://cursor.com) | Agentic AI-powered development environment |
| [Project VIC International](https://projectvic.org) | Shepherds the CAC Ontology initiative |

### Repository Structure

```
Agentic-AI-Development-Course/
├── README.md                           # This file
├── LICENSE                             # Apache 2.0
├── part-1-lecture/                      # Lecture materials
│   ├── README.md                       # Lecture guide & speaker notes
│   ├── outline.md                      # Detailed outline with timing
│   └── slides/                         # Slide content (markdown)
├── part-2-lab/                         # Hands-on lab materials
│   ├── README.md                       # Lab guide & facilitator notes
│   ├── prerequisites.md               # Setup checklist
│   ├── exercises/                      # Step-by-step exercise guides
│   └── solutions/                      # Reference solutions
├── resources/                          # Glossary, links, further reading
└── .cursor/
    └── rules/                          # Cursor rules for course context
```

### License

This project is licensed under the [Apache License 2.0](LICENSE), consistent with the Cyber Domain Ontology ecosystem.

### Contributing

This is an open-source training initiative. If you would like to contribute improvements, additional exercises, or translations, please open an issue or pull request.

### Acknowledgments

- [Cyber Domain Ontology](https://cyberdomainontology.org/) — a Linux Foundation project
- [Project VIC International](https://projectvic.org) — shepherds the CAC Ontology
- [CASE Community](https://caseontology.org/) — the CASE Ontology community
- [GitHub](https://github.com/github/spec-kit) — spec-kit and spec-driven development
- [Cursor](https://cursor.com) — agentic AI IDE
- The Massachusetts Attorney General's Office — hosts the NCCC
- The law enforcement officers, forensic examiners, and analysts who protect children every day
