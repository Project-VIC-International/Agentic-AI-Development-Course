# Glossary

Terms and definitions used throughout this course, explained for a law enforcement audience.

---

### Agent (AI Agent)

An AI system that can take a goal and work toward it by using tools — reading files, running commands, searching the web, writing code, and iterating. Unlike a chatbot (which only responds), an agent *acts*.

### Agentic AI

AI that operates with agency — the ability to make decisions, use tools, and take actions to accomplish a goal. The agent loop is: Think → Plan → Act → Observe → Repeat.

### API (Application Programming Interface)

A documented set of endpoints that allows applications to exchange data programmatically. Each endpoint handles a specific type of request. The schema defines what data goes in and what comes back. Think of it as a loading dock where applications exchange standardized containers.

### CAC Ontology (Crimes Against Children Ontology)

A domain-specific extension of UCO and CASE that provides classes, properties, and relationships for modeling crimes against children investigations. Covers investigations, CyberTip processing, forensics, legal processes, victim services, offender tradecraft, and international coordination. Shepherded by Project VIC International.

### CASE (Cyber-investigation Analysis Standard Expression)

An ontology extending UCO specifically for cyber-investigation concepts — evidence, chain of custody, provenance, investigative actions, and tool results. Part of the Cyber Domain Ontology ecosystem.

### CDO (Cyber Domain Ontology)

A Linux Foundation project that provides open governance for CASE and UCO development. Ensures that these standards are community-driven and vendor-neutral.

### CFTT (Computer Forensics Tool Testing)

A NIST program that provides a methodology for testing digital forensics tools. Produces test results that help validate tools for use in criminal investigations. Reference: [NIST CFTT](https://www.nist.gov/itl/ssd/software-quality-group/computer-forensics-tool-testing-program-cftt).

### CJIS Security Policy

The FBI's Criminal Justice Information Services Security Policy — defines security requirements for any system that accesses, stores, or transmits Criminal Justice Information (CJI). Covers access control, encryption, auditing, personnel security, incident response, and more. Compliance is mandatory for law enforcement tools handling CJI.

### Class

In an ontology, a class represents a type of thing — like `Device`, `Person`, `File`, `Investigation`. Think of it as a category or concept.

### CLI (Command Line Interface)

A text-based interface where you interact with software by typing commands. More powerful than a GUI for batch operations and scripting. The "staff entrance" to an application.

### Constitution (spec-kit)

In spec-driven development, the constitution defines the rules of the project — technology choices, security requirements, design principles, and compliance mandates (like CASE/UCO/CAC interoperability).

### CyberTip

A report submitted to NCMEC (National Center for Missing & Exploited Children) by an electronic service provider regarding apparent child sexual exploitation. CyberTips are a primary trigger for ICAC investigations.

### Encryption

The process of converting data into a coded form to prevent unauthorized access. **Encryption at rest** protects stored data (AES-256). **Encryption in transit** protects data moving over networks (TLS 1.2+). Required by CJIS for all Criminal Justice Information.

### Facet

In UCO/CASE, a facet is a group of related properties attached to an object. For example, a `File` object might have a `ContentDataFacet` (containing hash and size) and a `FileFacet` (containing filename and path).

### Fork

A copy of a GitHub repository under your own account. You can modify a fork without affecting the original project. If you make improvements, you can submit them back via a pull request.

### GPU (Graphics Processing Unit)

A processor originally designed for rendering graphics, now essential for running AI/ML models at speed. GPUs have thousands of cores that process data in parallel, making them orders of magnitude faster than CPUs for AI inference tasks. Without GPU acceleration, many AI models are too slow for practical use in forensic investigations.

### Graph Database

A database designed to store and query connected data — nodes (entities) and edges (relationships). Unlike relational databases that use flat tables, graph databases preserve and optimize for the connections between things. Examples include Neo4j, GraphDB, Apache Jena Fuseki, Amazon Neptune, and Stardog. CASE/UCO/CAC knowledge graphs are stored in graph databases.

### gUFO (Unified Foundational Ontology)

A lightweight implementation of the Unified Foundational Ontology that provides fundamental ontological distinctions (entities, events, situations, roles, phases). CAC Ontology uses gUFO for enhanced semantic precision.

### HuggingFace

A platform and community for sharing AI/ML models, datasets, and tools. Think of it as the "GitHub of AI models." Thousands of pre-trained models are available for download, covering tasks like image classification, text analysis, and object detection. URL: [huggingface.co](https://huggingface.co)

### Hallucination

When an AI model generates information that is confident-sounding but factually incorrect. This is why verification is essential — always check AI output, especially for legal or evidentiary matters.

### ICAC (Internet Crimes Against Children)

A national network of task forces dedicated to investigating and prosecuting individuals who exploit children through the internet.

### IDE (Integrated Development Environment)

A software application that provides tools for writing, testing, and debugging code in one place. Cursor is an AI-powered IDE.

### Inference

The process of using a trained AI/ML model to make predictions or classifications on new data. For example, running an image through a trained classifier to determine its category. Inference requires computational power, which is why GPU acceleration matters.

### Interoperability

The ability of different tools, systems, and organizations to exchange and use data without manual reformatting. CASE/UCO/CAC achieve interoperability by providing a shared language for investigation data.

### JSON-LD (JavaScript Object Notation for Linked Data)

A format for encoding linked data (knowledge graphs) using JSON syntax. One of the primary output formats for CASE/UCO/CAC data. Human-readable and machine-processable.

### Knowledge Graph

A structured representation of information as a network of entities (nodes) connected by relationships (edges). CASE/UCO/CAC data is expressed as knowledge graphs.

### LLM (Large Language Model)

A type of AI model trained on large amounts of text that can understand and generate human language. Examples include GPT (OpenAI), Claude (Anthropic), and Gemini (Google). There are multiple types of LLMs — see Instruction-Following LLM, Reasoning LLM, Dense Model, Mixture of Experts, Visual LLM, and Multimodal LLM.

### LLM Types

Different LLMs are designed for different strengths:
- **Instruction-Following LLM** — follows directions precisely. Best for building tools, formatting data, and executing clear tasks.
- **Reasoning LLM** — thinks step-by-step through complex problems. Best for analyzing evidence chains, legal reasoning, and complex planning.
- **Dense Model** — every part of the model activates for every query. Thorough and high-quality but computationally expensive.
- **Mixture of Experts (MoE)** — only activates the relevant "expert" parts for each query. Faster and cheaper at scale while maintaining quality.
- **Visual LLM** — can see and understand images in addition to text. Useful for analyzing screenshots, reading documents, examining photos.
- **Multimodal LLM** — combines multiple capabilities (text, vision, audio, code). The most versatile type, handles whatever you need.

### Mem0

An open-source universal memory layer for AI agents. Enables agents to remember user preferences, decisions, and context across sessions. Supports multi-level memory (user, session, agent state). Works with any LLM and offers a self-hosted option. URL: [github.com/mem0ai/mem0](https://github.com/mem0ai/mem0)

### MemPalace

An open-source structured AI memory system using the "memory palace" metaphor. Stores verbatim conversations organized into wings (people/projects), rooms (topics), and halls (memory types). Runs entirely locally with no cloud dependency. Provides 19 MCP tools for agent interaction. URL: [github.com/MemPalace/mempalace](https://github.com/MemPalace/mempalace)

### MCP (Model Context Protocol)

A standardized protocol that allows AI agents to discover and use an application's capabilities. MCP is to agents what APIs are to applications — the purpose-built door for agent interaction.

### ML Model (Machine Learning Model)

A program trained on data to perform a specific task — image classification, object detection, text analysis, pattern recognition, etc. Unlike LLMs (which are general-purpose language models), ML models are typically specialized for one task. Available from HuggingFace, Project VIC, universities, and the research community.

### Namespace

In ontologies, a namespace is a topic-specific vocabulary identified by a URI prefix. For example, `uco-observable:` is the namespace for observable objects (devices, files, accounts) in UCO.

### NCMEC (National Center for Missing & Exploited Children)

### NIST 800-53 (SP 800-53 Rev. 5)

A NIST Special Publication that provides a comprehensive catalog of security and privacy controls for information systems. Organized into control families (Access Control, Audit, Encryption, etc.). NIST cybersecurity overlays customize these controls for specific missions, including law enforcement. Reference: [NIST SP 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final).

A nonprofit organization that operates the CyberTipline, provides technical assistance, and supports law enforcement in child exploitation investigations.

### Ontology

A formal, shared vocabulary that defines what things exist (classes), how they are described (properties), and how they connect (relationships) in a specific domain. Designed to be machine-readable while remaining human-understandable.

### Open Source

Software whose source code is publicly available, allowing anyone to use, modify, and distribute it according to its license. Open source enables collaboration and prevents vendor lock-in.

### Project VIC International

A nonprofit organization that shepherds the CAC Ontology and provides hash intelligence (VICS) for child exploitation investigations.

### Property

In an ontology, a property describes an attribute of an entity or a connection between entities. For example, `uco-core:name` gives an entity a name, while `uco-core:source` connects a relationship to its starting entity.

### Provenance

The documented history of who did what, when, with which tool, to what data. CASE captures provenance for every investigative action, ensuring that analysis results can be traced back to their sources.

### RDF (Resource Description Framework)

A W3C standard for representing information as subject-predicate-object triples (e.g., "Device-A contains File-B"). The underlying data model for CASE/UCO/CAC knowledge graphs.

### Relationship

In an ontology, a named connection between two entities. For example, a device "contains" a file, or a person "has-account" with an online service.

### SHACL (Shapes Constraint Language)

A language for defining validation rules (shapes) that RDF data must conform to. CASE/UCO/CAC use SHACL to ensure that knowledge graphs follow the correct structure and business rules.

### SPARQL

A query language for asking questions of RDF knowledge graphs. Similar in concept to SQL for databases, but designed for graph data.

### Spec-Driven Development (SDD)

A development methodology where specifications are the primary artifact. The workflow is: Constitution → Specify → Plan → Tasks → Implement. The specification drives the implementation, not the other way around.

### spec-kit

GitHub's open-source toolkit for operationalizing spec-driven development. Provides templates, CLI tools, and a structured workflow for defining project specifications.

### Turtle

A human-readable syntax for writing RDF data. Files use the `.ttl` extension. More compact than JSON-LD for hand-reading.

### UCO (Unified Cyber Ontology)

The foundational ontology for the cyber domain. Provides shared vocabulary for concepts like devices, accounts, files, network connections, actions, relationships, and identities. CASE and CAC Ontology extend UCO.

### UI (User Interface / Graphical User Interface)

The visual interface of an application — buttons, menus, forms, dashboards. The "front door" that most users interact with.

### VICS (Victim Identification, Categorization, and Sharing)

The data schema used by Project VIC International for sharing hash intelligence across digital forensics tools. Adopted by 36 tool developers over 14 years.

### T&V (Testing and Validation)

The process of independently testing and validating a tool, model, or application before it is used in operational law enforcement or digital forensics work. Includes unit testing, integration testing, validation on known datasets, peer review, and documentation for court admissibility. Non-negotiable for any tool that produces evidence or handles CJI.

### Vibe Coding

Informal term for asking an AI to build software without providing structured requirements or specifications. Produces unpredictable results. The opposite of spec-driven development.
