#!/usr/bin/env python3
"""
Validate a CASE/UCO knowledge graph using SHACL shapes.

This script demonstrates the validation workflow:
  1. Load a knowledge graph (JSON-LD or Turtle)
  2. Load SHACL shapes that define the rules
  3. Validate the graph against the shapes
  4. Report pass/fail with human-readable messages

Usage:
    python validate_graph.py                           # validate the known-good graph
    python validate_graph.py graph_with_errors.jsonld   # validate a graph with known errors
    python validate_graph.py your_graph.ttl             # validate your own graph
"""

import sys
import os

try:
    from rdflib import Graph
except ImportError:
    print("ERROR: rdflib is not installed.")
    print("  Install it with:  pip install rdflib")
    sys.exit(1)

try:
    from pyshacl import validate
except ImportError:
    print("ERROR: pyshacl is not installed.")
    print("  Install it with:  pip install pyshacl")
    sys.exit(1)


def load_graph(path):
    g = Graph()
    if path.endswith(".jsonld") or path.endswith(".json"):
        g.parse(path, format="json-ld")
    elif path.endswith(".ttl"):
        g.parse(path, format="turtle")
    else:
        g.parse(path)
    return g


def run_validation(data_path, shapes_path):
    print(f"\n  Data graph:   {data_path}")
    print(f"  SHACL shapes: {shapes_path}")
    print()

    data_graph = load_graph(data_path)
    shapes_graph = load_graph(shapes_path)

    conforms, results_graph, results_text = validate(
        data_graph,
        shacl_graph=shapes_graph,
        inference="none",
        abort_on_first=False,
    )

    if conforms:
        print("  RESULT: PASS — graph conforms to all SHACL shapes")
        print(f"  ({len(data_graph)} triples validated)")
    else:
        print("  RESULT: FAIL — validation errors found:\n")
        for line in results_text.strip().split("\n"):
            print(f"    {line}")

    return conforms


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    shapes_path = os.path.join(script_dir, "investigation-shapes.ttl")

    if len(sys.argv) > 1:
        data_path = sys.argv[1]
    else:
        data_path = os.path.join(script_dir, "..", "examples", "simple-investigation.jsonld")

    print()
    print("=" * 56)
    print("  CASE/UCO Graph Validator")
    print("=" * 56)

    if not os.path.exists(data_path):
        print(f"\n  ERROR: File not found: {data_path}")
        sys.exit(1)

    if not os.path.exists(shapes_path):
        print(f"\n  ERROR: SHACL shapes not found: {shapes_path}")
        sys.exit(1)

    conforms = run_validation(data_path, shapes_path)

    print()
    if conforms:
        print("  Try validating the file with errors to see what failure looks like:")
        print(f"    python {sys.argv[0]} {os.path.join(script_dir, 'graph_with_errors.jsonld')}")
    print()

    sys.exit(0 if conforms else 1)


if __name__ == "__main__":
    main()
