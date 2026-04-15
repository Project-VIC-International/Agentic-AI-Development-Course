# Project Constitution — CAC Mission Tools

This constitution defines the governing principles, constraints, and standards for all tools built in this project. Every specification, plan, and implementation must comply with these rules.

## Mission

Build interoperable, open-source tools that support Crimes Against Children investigations. Every tool must produce data that can be shared, combined, and analyzed across agencies, jurisdictions, and tools without manual normalization.

## Interoperability Requirements

### Mandatory Standards Compliance

All tools MUST produce output that is compliant with:

1. **UCO (Unified Cyber Ontology)** — for foundational cyber domain concepts
2. **CASE (Cyber-investigation Analysis Standard Expression)** — for investigation-specific concepts
3. **CAC Ontology** — for crimes-against-children-specific concepts

### Data Format

- Primary output format: **JSON-LD** (JavaScript Object Notation for Linked Data)
- Secondary output format: **Turtle** (.ttl) where appropriate
- All output MUST include proper namespace declarations for UCO, CASE, and CAC Ontology
- All output MUST be valid against the relevant SHACL shapes

### Integration

- Tools SHOULD use the CASE/UCO/CAC SDK where available
- Tools MUST NOT invent custom schemas when a UCO, CASE, or CAC Ontology class exists
- Tools SHOULD reference existing ontology classes by IRI rather than duplicating definitions

## Technology Stack

### Required

- **Language:** Python 3.10+
- **Data serialization:** `rdflib` for RDF/JSON-LD handling
- **Validation:** SHACL validation via `pyshacl`
- **Dependency management:** `requirements.txt` with pinned versions

### Recommended

- **CLI interface:** `click` or `argparse`
- **Testing:** `pytest`
- **Documentation:** Markdown in a `docs/` directory

## Security and Privacy

### CJIS Security Policy Compliance

All tools that access, store, or transmit Criminal Justice Information (CJI) MUST comply with the [FBI CJIS Security Policy](https://www.fbi.gov/services/cjis/cjis-security-policy-resource-center):

- **Access Control** — authentication, authorization, and role-based access required
- **Auditing** — log who accessed what data, when, and what actions were taken
- **Personnel Security** — background check requirements for anyone with CJI access
- **Media Protection** — secure handling and disposal of storage devices
- **Physical Security** — controlled access to systems processing CJI
- **Incident Response** — documented plan for security breaches
- **Configuration Management** — track all changes to systems and software

### NIST Cybersecurity Standards

Tools SHOULD reference and implement controls from:

- **NIST Cybersecurity Framework** (Identify, Protect, Detect, Respond, Recover)
- **NIST SP 800-53 Rev. 5** — security and privacy control catalog
- **NIST cybersecurity overlays** appropriate for law enforcement environments

The agent SHOULD be used to audit the application against relevant NIST 800-53 control families (AC, AU, CM, IA, SC, SI).

### Encryption Requirements

- **Data at rest:** All stored data MUST be encrypted using AES-256 or equivalent
- **Data in transit:** All network communication MUST use TLS 1.2 or higher
- **No unencrypted HTTP** — always HTTPS
- **Key management:** encryption keys MUST be stored securely, rotated regularly, and NEVER hardcoded in source code

### Sensitive Data Handling

- Tools MUST NOT embed real PII (personally identifiable information) in examples, tests, or documentation
- All example data MUST use synthetic/fictional identifiers
- Tools that process real investigation data MUST include appropriate access control guidance
- No real case data, victim information, or suspect information in any committed file

### Code Security

- No hardcoded credentials, API keys, or encryption keys
- Dependencies must be from trusted sources
- Input validation on all user-provided data
- Secrets management via environment variables or secure vaults

## Open Source

- License: **Apache 2.0**
- All code must be suitable for public release
- README must explain what the tool does, how to install it, and how to use it
- Contributing guidelines must be provided for community contributions

## Testing and Validation

### Mandatory Independent Testing

All tools MUST undergo independent testing and validation before operational deployment in any law enforcement or digital forensics environment.

### Validation Requirements

- **Unit tests** — every component must have automated tests
- **Integration tests** — components must be tested together
- **Validation on known datasets** — tool output must be verified against ground truth
- **SHACL validation** — all CASE/UCO/CAC output must pass SHACL validation
- **Peer review** — code must be reviewed by someone other than the original developer (or AI agent)
- **Documentation for court** — tool methodology must be documented sufficiently for court admissibility

### For AI/ML Models

Any AI/ML model used in a tool MUST have:

- Documented benchmark performance (accuracy, precision, recall)
- Documented false positive and false negative rates
- Bias evaluation across relevant data types
- Independent third-party validation before operational use

### Validation Partners

- Agency quality assurance processes
- NIST Computer Forensics Tool Testing (CFTT) program
- University research partners
- Peer agencies (cross-validation)
- Commercial testing laboratories

## Quality Standards

- All tools must include automated tests
- All CASE/UCO/CAC output must pass SHACL validation
- Code must include meaningful error messages
- Documentation must be kept up to date with code changes

## Design Principles

1. **Interoperable from day one** — not as an afterthought
2. **Secure from day one** — CJIS and encryption requirements in every design
3. **Validated before deployment** — independent T&V is non-negotiable
4. **Search before you build** — check existing projects first
5. **Extend, don't reinvent** — use existing ontology classes
6. **Victim-centric** — tools serve the mission of protecting children
7. **Accessible** — usable by investigators, not just developers
