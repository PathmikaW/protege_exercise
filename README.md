# Protege Exercise — IT5432 Semantic Web and Ontological Engineering

Index No: 258843A | Name: Weerarathna T.M.P.

Two parts in this repo: an early Pizza ontology practice run (`tutorial/`),
and the actual coursework assignment (`assignment/`) — a real-domain OWL
ontology for Abans (a Sri Lankan electronics/appliance retailer), with
reasoning, SPARQL competency questions, and a full-stack app on top.

## File structure

```
protege_exercise/
├── tutorial/                        # practice run before the real assignment
│   ├── pizza.owl                    # Pizza ontology from the CO-ODE tutorial
│   └── protegeowltutorialp4_v1_3.pdf
│
└── assignment/                      # the actual coursework
    ├── abans.owl                    # the ontology (source of truth)
    ├── requirements.txt             # Python deps for backend + frontend
    ├── test_queries.py              # standalone SPARQL verification script
    │
    ├── backend/
    │   └── main.py                  # FastAPI + rdflib service
    │                                 #   GET /health
    │                                 #   GET /competency-questions
    │                                 #   GET /competency-questions/{id}/run
    │                                 #   POST /sparql
    │
    ├── frontend/
    │   └── app.py                   # Streamlit UI (calls the backend over HTTP)
    │
    ├── .streamlit/config.toml       # frontend theme
    │
    ├── docs/
    │   └── competency_questions.md  # all 15 SPARQL queries, documented
    │
    └── Submission/                  # what actually gets submitted
        ├── 258843A_Assignment_Report.docx / .pdf
        ├── 258843A_Ontology_Demo.mp4
        ├── 258843A_Required_Deliverables_Checklist.txt
        ├── 258843A_Assignment_Submission.zip
        ├── abans.owl                # copy for convenience
        └── ontology_diagram.png
```

## Architecture

```
Protégé (model + reason)
        │  export (asserted + inferred axioms baked in)
        ▼
    abans.owl
        │  loaded once at startup
        ▼
FastAPI backend (rdflib in-memory graph)  ──HTTP──▶  Streamlit frontend
```

The ontology is built and reasoned over in Protégé. Before export, inferred
axioms (defined-class membership, transitive-property closures) are
materialised into the file itself, so the backend — which has no OWL
reasoner of its own — can still answer reasoning-dependent competency
questions with plain SPARQL.

## What's been done

- **Domain**: Abans' real product catalog (buyabans.com) — 4 categories
  (TV, Home Appliances, Mobile Devices, Computers), real sub-types, brands,
  and Abans' actual showroom/location network.
- **Ontology**: 47 classes, 15 properties, 59 individuals, 597 axioms.
  Every required OWL construct used (disjoint/equivalent classes, inverse/
  transitive/functional properties, existential/universal/cardinality/
  datatype-facet/hasValue restrictions) — each tied to a real business rule.
- **Reasoning**: verified consistent with HermiT; 5+ inferred facts
  documented with the axioms that produced them, including an Open World
  Assumption demo (`Mystery_Smart_Gadget`).
- **SPARQL**: 15 competency questions (minimum required: 8), covering
  SELECT, FILTER, OPTIONAL, aggregation, grouping, and reasoner-inferred
  queries.
- **Bonus app**: FastAPI + rdflib backend, Streamlit frontend, covering 3
  of the 6 listed capabilities (minimum required: 2).
- **Submission docs**: full report (all 6 tasks + bonus + deliverables),
  5-minute demo video, ontology diagram, and a deliverables checklist —
  all in `assignment/Submission/`.

See `assignment/Submission/258843A_Required_Deliverables_Checklist.txt`
for the full breakdown against the assignment brief's requirements.
