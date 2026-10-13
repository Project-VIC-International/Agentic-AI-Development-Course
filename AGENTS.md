# Agent Instructions: Agentic AI Development Course

These instructions apply to every AI coding agent working in this repository (Cursor, Claude Code, Codex, GitHub Copilot, Gemini CLI, OpenCode, Zed, Warp, and others).

This repository contains training materials for the **Agentic AI Development Course**, a two-part session that teaches investigators and examiners to build interoperable mission tools for crimes-against-children and other digital investigations using agentic AI and open standards. It is delivered at events such as the National Cyber Crime Conference (NCCC) and DFRWS APAC.

Students do their hands-on work in a private repository created from the [project template](https://github.com/Project-VIC-International/Agentic-AI-Development-Project-Template). The template's `policies/` folder holds the full development policies; this file covers the course materials themselves.

## Audience

- Law enforcement investigators, digital forensic examiners, intelligence analysts, prosecutors, and researchers from many countries
- Working crimes-against-children cases and other digital investigations
- **No prior programming experience assumed**
- English may be a second or third language
- Explanations must be in plain language with investigation-relevant examples

## Key Standards

All tools and examples in this course must be compliant with:

1. **UCO (Unified Cyber Ontology)**: foundational cyber domain vocabulary
   - Namespace: `https://ontology.unifiedcyberontology.org/uco/`
   - GitHub: https://github.com/ucoProject
2. **CASE (Cyber-investigation Analysis Standard Expression)**: cyber-investigation extension
   - Namespace: `https://ontology.caseontology.org/case/`
   - GitHub: https://github.com/casework
3. **CAC Ontology (Crimes Against Children Ontology)**: domain-specific extension
   - Namespace: `https://cacontology.projectvic.org/`
   - GitHub: https://github.com/Project-VIC-International/CAC-Ontology
4. **SOLVE-IT** (optional): digital forensics techniques, weaknesses, and mitigations knowledge base
   - GitHub: https://github.com/SOLVE-IT-DF/solve-it

## Critical Rules

- **No real personal data, case data, victim information, or suspect information** in any file. All examples use synthetic data.
- **Interoperability is mandatory.** Tool output must be CASE/UCO/CAC compliant.
- **Security follows the student's jurisdiction.** Ask which country and agency the tool is for, then apply that framework. Examples: FBI CJIS Security Policy plus NIST SP 800-53 for US criminal justice information; the ISM, PSPF, Essential Eight, and Privacy Act 1988 in Australia; the NZISM, PSR, and Privacy Act 2020 in New Zealand; GDPR and the Law Enforcement Directive in the EU; UK GDPR and the Data Protection Act 2018 Part 3 in the UK. Use NIST SP 800-53 Rev. 5 and ISO/IEC 27001 as the neutral baseline when the framework is not yet known. Never present one country's rules as universal.
- **Encrypt data at rest (AES-256) and in transit (TLS 1.2+).**
- **Independent testing and validation.** Any tool must be independently tested and validated before operational use in law enforcement or digital forensics.
- **Explanations must be accessible.** Write for investigators, not for software engineers.
- **Search before building.** Check existing projects before creating something new.
- **Apache 2.0 license**, consistent with the Cyber Domain Ontology ecosystem.
- **Agent-neutral wording.** The instructor uses Cursor, but students may use any agent. Say "your AI agent" unless a step is truly specific to one tool.

## Security and Validation References

- **NIST SP 800-53 Rev. 5**: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
- **NIST Cybersecurity Framework**: https://www.nist.gov/cyberframework
- **FBI CJIS Security Policy** (United States): https://www.fbi.gov/services/cjis/cjis-security-policy-resource-center
- **Australian Information Security Manual (ISM)**: https://www.cyber.gov.au/ism
- **New Zealand Information Security Manual (NZISM)**: https://nzism.gcsb.govt.nz/
- **ISO/IEC 27037, 27041, 27042, 27043**: digital evidence handling, method validation, analysis, and investigation process
- **NIST CFTT** (tool validation): https://www.nist.gov/itl/ssd/software-quality-group/computer-forensics-tool-testing-program-cftt

## Technology Stack

- Python 3.11+ (required by current Spec Kit releases)
- JSON-LD and Turtle for data serialization
- rdflib for RDF handling
- pyshacl for SHACL validation
- pytest for testing
- Graph databases (GraphDB, Apache Jena Fuseki, Neo4j, and others) for storing and querying CASE/UCO/CAC knowledge graphs

## Graph Databases

CASE/UCO/CAC data is stored in graph databases. When building tools:

- Use RDF/SPARQL graph databases (GraphDB, Fuseki, Stardog, Amazon Neptune) for native CASE/UCO/CAC support.
- Graph databases have UI, CLI, and API surfaces, and some have MCP servers for agent interaction.
- Agents can store data in and query graph databases directly.

## AI/ML Models

- Models can be sourced from Hugging Face, the research community, Project VIC International, or universities.
- GPU acceleration is often needed for inference at operational speed, but tools must still work on CPU where practical.
- All AI/ML models must be independently validated before operational use (benchmark testing, error rates, bias evaluation).

## Spec-Driven Development

This course teaches GitHub's Spec Kit workflow:

1. Constitution, 2. Specify, 3. Clarify, 4. Plan, 5. Tasks, 6. Analyze, 7. Implement, 8. Converge

Commands are written in Spec Kit's reference form (`/speckit.specify`); agents may show them as `/speckit-specify` or `$speckit-specify`.

The example constitution for CAC mission tools is at `part-2-lab/exercises/03-spec-driven-dev/example-spec/constitution.md`. It includes jurisdiction-aware security, NIST baseline, encryption, and testing and validation requirements, which every spec inherits.
