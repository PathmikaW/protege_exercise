# Abans Ontology — Competency Questions & SPARQL

All queries assume this prefix:
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
```

Run against `abans.owl` **after** the Phase 8 export (inferred axioms
must be baked in for CQ5-8/CQ12 to return results — a plain SPARQL engine
has no reasoner).

---

**CQ1 — What products does brand X sell?** (simple join)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?product WHERE {
  ?product abans:hasBrand abans:LG .
}
```

**CQ2 — What TVs cost less than Rs. 150,000?** (filter)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?product ?price WHERE {
  ?product a abans:TV .
  ?product abans:hasPrice ?price .
  FILTER(?price < 150000)
}
```

**CQ3 — Which products have WiFi?** (simple join)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?product WHERE {
  ?product abans:hasFeature ?feature .
  ?feature a abans:WiFiFeature .
}
```

**CQ4 — Which products have 2+ years warranty?** (filter)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?product ?years WHERE {
  ?product abans:hasWarrantyYears ?years .
  FILTER(?years >= 2)
}
```

**CQ5 — Which products are classified as Smart?** (reasoner-inferred class)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?product WHERE {
  ?product a abans:SmartProduct .
}
```

**CQ6 — Which products are Eco-Friendly (A++/A+++)?** (reasoner-inferred class)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?product WHERE {
  ?product a abans:EcoFriendlyProduct .
}
```

**CQ7 — Which products are Premium (price ≥ 150,000)?** (reasoner-inferred + datatype filter)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?product ?price WHERE {
  ?product a abans:PremiumProduct .
  ?product abans:hasPrice ?price .
}
```

**CQ8 — Which products are Budget (complement of Premium)?** (reasoner-inferred, complement class)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?product WHERE {
  ?product a abans:BudgetProduct .
}
```

**CQ9 — How many products exist per category?** (aggregate)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?category (COUNT(?product) AS ?count) WHERE {
  ?product a ?category .
  FILTER(?category IN (abans:TV, abans:HomeAppliance, abans:MobileDevice, abans:Computer))
}
GROUP BY ?category
```

**CQ10 — Average price per category?** (aggregate)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?category (AVG(?price) AS ?avgPrice) WHERE {
  ?product a ?category .
  ?product abans:hasPrice ?price .
  FILTER(?category IN (abans:TV, abans:HomeAppliance, abans:MobileDevice, abans:Computer))
}
GROUP BY ?category
```

**CQ11 — Which brands appear in more than one category?** (multi-hop join)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?brand (COUNT(DISTINCT ?category) AS ?catCount) WHERE {
  ?product abans:hasBrand ?brand .
  ?product a ?category .
  FILTER(?category IN (abans:TV, abans:HomeAppliance, abans:MobileDevice, abans:Computer))
}
GROUP BY ?brand
HAVING (COUNT(DISTINCT ?category) > 1)
```

**CQ12 — Which products have 3+ features (Fully-Loaded)?** (reasoner-inferred, cardinality)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?product WHERE {
  ?product a abans:FullyLoadedProduct .
}
```

**CQ13 — Which products are available at showrooms in the Western Province?** (transitive-location join)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?product ?showroom WHERE {
  ?product abans:availableAt ?showroom .
  ?showroom abans:locatedIn abans:WesternProvince .
}
```
*(Works as a single hop because `locatedIn`'s transitive closure was baked in
during Phase 8 export — `Showroom → Province` is a direct triple, not just
`Showroom → City → Province`.)*

**CQ14 — Which showrooms stock a given product, and in which city/province?** (multi-hop over a transitive property)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?showroom ?city ?province WHERE {
  abans:LG_43_LED_TV abans:availableAt ?showroom .
  ?showroom abans:locatedIn ?city .
  ?city a abans:City .
  ?city abans:locatedIn ?province .
  ?province a abans:Province .
}
```
*(The `a abans:City` / `a abans:Province` type-guards are needed to
disambiguate from the baked-in `Showroom → Province` direct triple —
without them, the transitive closure could bind `?city` to a Province.)*

**CQ15 — List all products with their capacity, where available** (OPTIONAL)
```sparql
PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>
SELECT ?product ?capacity WHERE {
  ?product a abans:Product .
  OPTIONAL { ?product abans:hasCapacity ?capacity }
}
```
*(Returns all 18 products — capacity is bound only for the 4 appliances
that have one asserted (fridges, ACs, washing machine), and left
unbound elsewhere, since `hasCapacity` doesn't apply to TVs, phones, or
computers.)*
