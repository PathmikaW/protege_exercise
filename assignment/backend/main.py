"""Abans Ontology Competency Question API.

Loads the exported abans.owl (with inferred axioms baked in - see
Phase 8 of ASSIGNMENT_PLAN.md) into an in-memory rdflib graph at
startup, and exposes the 14 competency questions as SPARQL-backed
endpoints, plus a raw SPARQL passthrough for ad-hoc queries.
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import rdflib

ABANS_OWL_PATH = Path(__file__).resolve().parent.parent / "abans.owl"
PREFIX = "PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>\n"

COMPETENCY_QUESTIONS = {
    "cq1": {
        "text": "What products does brand X sell? (LG)",
        "query": """
            SELECT ?product WHERE {
              ?product abans:hasBrand abans:LG .
            }""",
    },
    "cq2": {
        "text": "What TVs cost less than Rs. 150,000?",
        "query": """
            SELECT ?product ?price WHERE {
              ?product a abans:TV .
              ?product abans:hasPrice ?price .
              FILTER(?price < 150000)
            }""",
    },
    "cq3": {
        "text": "Which products have WiFi?",
        "query": """
            SELECT ?product WHERE {
              ?product abans:hasFeature ?feature .
              ?feature a abans:WiFiFeature .
            }""",
    },
    "cq4": {
        "text": "Which products have 2+ years warranty?",
        "query": """
            SELECT ?product ?years WHERE {
              ?product abans:hasWarrantyYears ?years .
              FILTER(?years >= 2)
            }""",
    },
    "cq5": {
        "text": "Which products are classified as Smart?",
        "query": """
            SELECT ?product WHERE {
              ?product a abans:SmartProduct .
            }""",
    },
    "cq6": {
        "text": "Which products are Eco-Friendly (A++/A+++)?",
        "query": """
            SELECT ?product WHERE {
              ?product a abans:EcoFriendlyProduct .
            }""",
    },
    "cq7": {
        "text": "Which products are Premium (price >= 150,000)?",
        "query": """
            SELECT ?product ?price WHERE {
              ?product a abans:PremiumProduct .
              ?product abans:hasPrice ?price .
            }""",
    },
    "cq8": {
        "text": "Which products are Budget (complement of Premium)?",
        "query": """
            SELECT ?product WHERE {
              ?product a abans:BudgetProduct .
            }""",
    },
    "cq9": {
        "text": "How many products exist per category?",
        "query": """
            SELECT ?category (COUNT(?product) AS ?count) WHERE {
              ?product a ?category .
              FILTER(?category IN (abans:TV, abans:HomeAppliance, abans:MobileDevice, abans:Computer))
            }
            GROUP BY ?category""",
    },
    "cq10": {
        "text": "What is the average price per category?",
        "query": """
            SELECT ?category (AVG(?price) AS ?avgPrice) WHERE {
              ?product a ?category .
              ?product abans:hasPrice ?price .
              FILTER(?category IN (abans:TV, abans:HomeAppliance, abans:MobileDevice, abans:Computer))
            }
            GROUP BY ?category""",
    },
    "cq11": {
        "text": "Which brands appear in more than one category?",
        "query": """
            SELECT ?brand (COUNT(DISTINCT ?category) AS ?catCount) WHERE {
              ?product abans:hasBrand ?brand .
              ?product a ?category .
              FILTER(?category IN (abans:TV, abans:HomeAppliance, abans:MobileDevice, abans:Computer))
            }
            GROUP BY ?brand
            HAVING (COUNT(DISTINCT ?category) > 1)""",
    },
    "cq12": {
        "text": "Which products have 3+ features (Fully-Loaded)?",
        "query": """
            SELECT ?product WHERE {
              ?product a abans:FullyLoadedProduct .
            }""",
    },
    "cq13": {
        "text": "Which products are available at showrooms in the Western Province?",
        "query": """
            SELECT ?product ?showroom WHERE {
              ?product abans:availableAt ?showroom .
              ?showroom abans:locatedIn abans:WesternProvince .
            }""",
    },
    "cq14": {
        "text": "Which showrooms stock LG_43_LED_TV, and in which city/province?",
        "query": """
            SELECT ?showroom ?city ?province WHERE {
              abans:LG_43_LED_TV abans:availableAt ?showroom .
              ?showroom abans:locatedIn ?city .
              ?city a abans:City .
              ?city abans:locatedIn ?province .
              ?province a abans:Province .
            }""",
    },
}

app = FastAPI(title="Abans Ontology Competency Question API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

graph = rdflib.Graph()


@app.on_event("startup")
def load_graph() -> None:
    if not ABANS_OWL_PATH.exists():
        raise RuntimeError(f"abans.owl not found at {ABANS_OWL_PATH}")
    graph.parse(str(ABANS_OWL_PATH), format="xml")


def run_sparql(query_body: str) -> list[dict]:
    try:
        results = graph.query(PREFIX + query_body)
    except Exception as exc:  # noqa: BLE001 - surface parser errors to the caller
        raise HTTPException(status_code=400, detail=f"SPARQL error: {exc}") from exc

    rows = []
    for row in results:
        rows.append({str(var): str(row[var]) for var in results.vars if row[var] is not None})
    return rows


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "triples": len(graph)}


@app.get("/competency-questions")
def list_competency_questions() -> dict:
    return {cq_id: cq["text"] for cq_id, cq in COMPETENCY_QUESTIONS.items()}


@app.get("/competency-questions/{cq_id}/run")
def run_competency_question(cq_id: str) -> dict:
    cq = COMPETENCY_QUESTIONS.get(cq_id)
    if cq is None:
        raise HTTPException(status_code=404, detail=f"Unknown competency question: {cq_id}")
    return {"text": cq["text"], "results": run_sparql(cq["query"])}


class SparqlRequest(BaseModel):
    query: str


@app.post("/sparql")
def run_raw_sparql(body: SparqlRequest) -> dict:
    return {"results": run_sparql(body.query)}
