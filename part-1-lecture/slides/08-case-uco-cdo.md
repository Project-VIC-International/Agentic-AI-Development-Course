# CASE/UCO & the Cyber Domain Ontology

---

## The Cyber Domain Ontology (CDO)

A **Linux Foundation** project that governs the development of CASE and UCO.

- Open governance — no single vendor controls it
- Community-driven — practitioners shape it
- International — used across jurisdictions and borders

**Website:** [cyberdomainontology.org](https://cyberdomainontology.org/)
**GitHub:** [Cyber-Domain-Ontology](https://github.com/Cyber-Domain-Ontology)

---

## The Three Layers

```
┌──────────────────────────────────────┐
│         CAC Ontology                 │  ← Crimes Against Children
│    (Domain-Specific Extension)       │     (your mission)
├──────────────────────────────────────┤
│           CASE                       │  ← Cyber-Investigation
│  (Cyber-Investigation Extension)     │     (your work)
├──────────────────────────────────────┤
│           UCO                        │  ← All Cyber Domains
│  (Unified Cyber Ontology)            │     (the foundation)
└──────────────────────────────────────┘
```

Each layer extends the one below. Build on all three, get all three for free.

---

## UCO — The Foundation

**Unified Cyber Ontology** — shared vocabulary for the entire cyber domain.

Defines how to represent:
- Devices, accounts, files, applications
- Network connections and communications
- Actions and relationships
- Identities, locations, timestamps
- Tools and their capabilities

**Think of it as:** the basic nouns and verbs of the cyber world.

---

## CASE — The Investigation Layer

**Cyber-investigation Analysis Standard Expression** — extends UCO for investigations.

Adds representations for:
- Evidence items and containers
- Chain of custody
- Provenance — who did what, when, with which tool
- Investigative actions and their results
- Legal authorization and process

**Think of it as:** the specialized vocabulary investigators add to the base language.

---

## What Is an Ontology? (Plain Language)

An ontology is a **shared vocabulary that machines can understand**.

It defines:
- **Classes** — what things exist (Device, Person, File, Investigation)
- **Properties** — how things are described (name, hash, timestamp)
- **Relationships** — how things connect (found-on, owned-by, part-of)

**If everyone uses the same ontology, everyone understands each other.**

Human language is ambiguous. Ontologies are precise. That precision is what enables automation and interoperability.

---

## A Simple Example

An investigation produces this connected graph:

```
Investigation-001
    │
    ├── hasEvidence ──► Device-A (Samsung Galaxy S24)
    │                      │
    │                      ├── contains ──► File-X (image.jpg)
    │                      │                  │
    │                      │                  └── hasHash ──► "a1b2c3..."
    │                      │
    │                      └── extractedBy ──► Tool-Autopsy (v4.21)
    │                                            │
    │                                            └── performedBy ──► Examiner-Smith
    │
    └── hasSubject ──► Person-B (suspect)
                          │
                          └── hasAccount ──► Account-C (username123)
```

Every node, every relationship, expressed in a format any CASE-aware tool can read.

**No manual normalization required.**

---

## Facets: UCO's Secret Weapon

Most ontologies put all properties directly on a class. UCO does something different — it groups properties into **facets**, modular bundles of related characteristics that attach to an object.

```
Device-A (uco-observable:ObservableObject)
    │
    ├── hasFacet ──► DeviceFacet
    │                  ├── manufacturer: "Samsung"
    │                  ├── model: "Galaxy S24"
    │                  └── serialNumber: "RF8N..."
    │
    ├── hasFacet ──► OperatingSystemFacet
    │                  ├── osName: "Android"
    │                  └── osVersion: "15"
    │
    └── hasFacet ──► StorageMediumFacet
                       ├── totalSize: "256 GB"
                       └── mediaType: "UFS"
```

The device doesn't carry dozens of properties directly. Each facet handles one aspect of the object.

---

## Why Facets?

The cyber domain has a **combinatorial complexity problem**.

A single file can be described by its filesystem properties, its content, its hashes, its EXIF metadata, its GPS coordinates, its malware classification — all at the same time.

Without facets, you have two bad options:

| Approach | Problem |
|----------|---------|
| One giant class with hundreds of optional properties | Most properties are irrelevant for any given object |
| Hundreds of specialized subclasses (FileWithHash, FileWithExif, FileWithHashAndExif...) | Class explosion — impossible to maintain |

Facets solve this by letting you **compose** exactly the properties that apply:

```
image.jpg (uco-observable:ObservableObject)
    │
    ├── hasFacet ──► FileFacet
    │                  ├── fileName: "image.jpg"
    │                  └── filePath: "/DCIM/Camera/"
    │
    ├── hasFacet ──► ContentDataFacet
    │                  ├── mimeType: "image/jpeg"
    │                  └── sizeInBytes: 4521984
    │
    ├── hasFacet ──► HashFacet
    │                  ├── hashMethod: "SHA-256"
    │                  └── hashValue: "a1b2c3..."
    │
    └── hasFacet ──► EXIFFacet
                       ├── exifData: { "Make": "Samsung", ... }
                       └── gpsCoordinates: "38.8977, -77.0365"
```

A text file would have FileFacet and ContentDataFacet but no EXIFFacet. A network connection would have entirely different facets. Each object carries only what applies.

---

## Facets Enable Tool Interoperability

Different tools know about different aspects of the same object. Facets let each tool contribute what it knows:

```
Tool A (filesystem extraction)   ──► adds FileFacet
Tool B (hash computation)        ──► adds HashFacet
Tool C (EXIF extraction)         ──► adds EXIFFacet
Tool D (AI content classifier)   ──► adds ClassificationFacet
```

All four tools describe the **same object**. Each one adds its facet without needing to know what the other tools contributed. This is how you get interoperability without requiring every tool to understand everything.

---

## Facets Are Extensible

Need to describe something new? Create a new facet — don't modify existing classes.

The **CAC Ontology** adds facets specific to crimes against children investigations. An AI model that classifies content can attach its results as a facet to the same evidence object that already has its file, hash, and EXIF facets from other tools.

New capabilities plug in. Old tools keep working. Nothing breaks.

---

## Relationships: How Things Connect

In a graph, knowledge lives in the connections — not just the objects.

UCO and CASE define typed relationships so the meaning of every connection is explicit:

```
Person-B ──── hasAccount ────► Account-C
Device-A ──── contains ──────► File-X
File-X ────── extractedBy ───► Tool-Autopsy
Tool-Autopsy ─ performedBy ──► Examiner-Smith
```

Every arrow has a name. That name is defined by the ontology, so every tool agrees on what it means. "contains" in Tool A means the same thing as "contains" in Tool B.

**Relationships are what turn a pile of objects into investigative intelligence.** Without them, you have isolated facts. With them, you have a connected story.

---

## SPARQL: Asking Questions in Your Own Words

Once your data is in a graph, you can query it using **SPARQL** — a query language designed for graphs.

You don't need to understand database internals. You ask questions at the level you think about the case:

| Investigator's Question | What SPARQL Does |
|------------------------|------------------|
| "Which devices contain files with known hash values?" | Follows the contains and hasHash relationships |
| "What did Examiner Smith extract last Tuesday?" | Follows performedBy and filters by date |
| "Show me all accounts linked to this suspect" | Follows hasAccount from a specific person |
| "Which tools touched this evidence item?" | Follows extractedBy across all related objects |

You describe the **pattern** you're looking for — the graph finds every match.

```
Example pattern: "Find every file that was extracted from a device
                  in Investigation-001 and has a SHA-256 hash"

The graph follows the connections and returns every match — across
every device, every file, every tool that touched them.
```

SPARQL lets investigators, analysts, and prosecutors each ask their own questions of the same data — at their own level of understanding.

---

## SHACL: Grammar Rules for Your Data

**SHACL** (Shapes Constraint Language) defines the rules your data must follow — like grammar rules for the graph.

| What SHACL Enforces | Example |
|---------------------|---------|
| Required fields | "Every evidence item MUST have a hash" |
| Correct data types | "A timestamp must be a date, not free text" |
| Valid relationships | "extractedBy must point to a Tool, not a Person" |
| Business rules | "Every investigative action MUST record who performed it" |

When you validate data against SHACL shapes, you catch errors **before** they cause problems:

```
✗ File-X is missing a required HashFacet
✗ Investigation-001 has no performedBy on its extraction action
✓ Device-A passes all shape constraints
```

SHACL is what guarantees interoperability. If Tool A and Tool B both validate against the same SHACL shapes, their outputs are guaranteed to be compatible. No surprises when you combine data from different sources.

---

## Reasoning: The Graph Discovers What You Didn't Ask

A graph database can **infer new facts** from existing ones — this is called reasoning.

You store:
```
Person-B ── hasAccount ──► Account-C
Account-C ── loggedInFrom ──► IPAddress-1
IPAddress-1 ── geolocatedTo ──► Location-X
```

The graph can infer:
```
Person-B ── linkedTo ──► Location-X
```

Nobody stated that directly. The graph followed the chain of relationships and discovered it.

**For investigators, this is powerful:**
- Connect a suspect to a location through device and account chains
- Discover shared infrastructure between seemingly unrelated cases
- Surface patterns across thousands of evidence items that no human would manually cross-reference

The graph does the connecting. You decide what the connections mean but that becomes easier when querying with your agent via MCP as the graph carries the meaning of every node and edge in the graph plus the specific data properties assigned to them.

---

## Why This Changes Everything

| Without Standards | With CASE/UCO |
|------------------|---------------|
| Each tool has its own export format | All tools speak the same language |
| Manual normalization between tools | Automated data combination |
| Context lost in translation | Full provenance preserved |
| Reports built by hand | Reports generated from graphs |
| Sharing requires reformatting | Sharing is native |
| New tools start from zero | New tools are interoperable from day one |
