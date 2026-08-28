"""Quick verification script: runs all 14 competency-question SPARQL
queries against abans.owl and prints results. Not part of the final
backend — just a Phase 9 sanity check (Protégé's SPARQL Query tab UI
was misbehaving, so verifying here with the same engine the backend
will use)."""

import rdflib

g = rdflib.Graph()
g.parse("abans.owl", format="xml")
print(f"Loaded {len(g)} triples\n")

PREFIX = "PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>\n"

queries = {
    "CQ1 - LG products": """
        SELECT ?product WHERE {
          ?product abans:hasBrand abans:LG .
        }""",
    "CQ2 - TVs under 150000": """
        SELECT ?product ?price WHERE {
          ?product a abans:TV .
          ?product abans:hasPrice ?price .
          FILTER(?price < 150000)
        }""",
    "CQ3 - Products with WiFi": """
        SELECT ?product WHERE {
          ?product abans:hasFeature ?feature .
          ?feature a abans:WiFiFeature .
        }""",
    "CQ4 - 2+ year warranty": """
        SELECT ?product ?years WHERE {
          ?product abans:hasWarrantyYears ?years .
          FILTER(?years >= 2)
        }""",
    "CQ5 - SmartProduct (inferred)": """
        SELECT ?product WHERE {
          ?product a abans:SmartProduct .
        }""",
    "CQ6 - EcoFriendlyProduct (inferred)": """
        SELECT ?product WHERE {
          ?product a abans:EcoFriendlyProduct .
        }""",
    "CQ7 - PremiumProduct (inferred)": """
        SELECT ?product ?price WHERE {
          ?product a abans:PremiumProduct .
          ?product abans:hasPrice ?price .
        }""",
    "CQ8 - BudgetProduct (inferred)": """
        SELECT ?product WHERE {
          ?product a abans:BudgetProduct .
        }""",
    "CQ9 - Product count per category": """
        SELECT ?category (COUNT(?product) AS ?count) WHERE {
          ?product a ?category .
          FILTER(?category IN (abans:TV, abans:HomeAppliance, abans:MobileDevice, abans:Computer))
        }
        GROUP BY ?category""",
    "CQ10 - Avg price per category": """
        SELECT ?category (AVG(?price) AS ?avgPrice) WHERE {
          ?product a ?category .
          ?product abans:hasPrice ?price .
          FILTER(?category IN (abans:TV, abans:HomeAppliance, abans:MobileDevice, abans:Computer))
        }
        GROUP BY ?category""",
    "CQ11 - Brands in 2+ categories": """
        SELECT ?brand (COUNT(DISTINCT ?category) AS ?catCount) WHERE {
          ?product abans:hasBrand ?brand .
          ?product a ?category .
          FILTER(?category IN (abans:TV, abans:HomeAppliance, abans:MobileDevice, abans:Computer))
        }
        GROUP BY ?brand
        HAVING (COUNT(DISTINCT ?category) > 1)""",
    "CQ12 - FullyLoadedProduct (inferred)": """
        SELECT ?product WHERE {
          ?product a abans:FullyLoadedProduct .
        }""",
    "CQ13 - Available in Western Province": """
        SELECT ?product ?showroom WHERE {
          ?product abans:availableAt ?showroom .
          ?showroom abans:locatedIn abans:WesternProvince .
        }""",
    "CQ14 - Showrooms stocking LG_43_LED_TV": """
        SELECT ?showroom ?city ?province WHERE {
          abans:LG_43_LED_TV abans:availableAt ?showroom .
          ?showroom abans:locatedIn ?city .
          ?city a abans:City .
          ?city abans:locatedIn ?province .
          ?province a abans:Province .
        }""",
}

for name, q in queries.items():
    print(f"=== {name} ===")
    try:
        results = list(g.query(PREFIX + q))
        if not results:
            print("  (no results)")
        for row in results:
            print("  " + ", ".join(str(v) for v in row))
    except Exception as e:
        print(f"  ERROR: {e}")
    print()
