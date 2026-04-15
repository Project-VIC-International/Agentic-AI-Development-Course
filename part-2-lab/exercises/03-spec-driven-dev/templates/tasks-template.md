# Tasks: [Tool Name]

Tasks are ordered by dependency. Complete each task before moving to the next. Each task has a clear "done" criterion.

## Phase 1: Foundation

### Task 1: Project Setup

- **Description:** Create project structure, initialize dependencies, set up virtual environment
- **Done when:** Project directory exists with `requirements.txt`, virtual environment is activated, dependencies install without errors

### Task 2: [Input Parsing / Data Loading]

- **Description:** [Build the component that reads input data]
- **Done when:** [Component reads sample input and produces structured data in memory]

## Phase 2: Core Logic

### Task 3: [Core Processing]

- **Description:** [Build the main processing logic]
- **Done when:** [Processing produces correct intermediate results from sample input]

### Task 4: [CASE/UCO/CAC Graph Construction]

- **Description:** [Build the component that produces the output knowledge graph]
- **Done when:** [Output graph is valid JSON-LD or Turtle with correct CASE/UCO/CAC types]

## Phase 3: Validation & Polish

### Task 5: [SHACL Validation]

- **Description:** Validate output against SHACL shapes
- **Done when:** Output passes SHACL validation with zero errors

### Task 6: [End-to-End Test]

- **Description:** Run the full pipeline with synthetic sample data and verify the complete output
- **Done when:** Tool runs end-to-end, output is valid, results match expectations

---

**Add or remove tasks as needed.** The structure above is a starting point — your plan may have more or fewer tasks depending on the tool's complexity.
