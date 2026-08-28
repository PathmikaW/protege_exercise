# Abans Ontology Assignment — Plan & Progress Tracker

## Assignment brief (as given)

> Model an ontology in Protégé using some domain other than Pizza. Then
> export it to an OWL file in Protégé. This is the basic requirement to
> pass the assignment. If you need to score more then need to create a
> front end that can load the extracted OWL file and run competency
> questions in the form of SPARQL queries. People who can't implement a
> front end can run the same queries in Protégé (there is a tab you can
> run).

**Pass bar**: a modeled ontology, exported to `.owl`.
**Higher score**: competency questions answered via SPARQL — either through
a custom front end loading the exported OWL file, or via Protégé's built-in
**SPARQL Query** tab (fallback, no front end required).

## Domain & scope

- **Website**: [buyabans.com](https://buyabans.com/) — Abans' official
  online store (Abans Group: 50+ years, 40+ brands, 400+ showrooms across
  Sri Lanka — source: [Abans Group brands](https://abansgroup.com/brands/)).
- **Scope**: 4 of Abans' 13 real top-level categories, named exactly as
  they appear on buyabans.com's own navigation: **TV, Home Appliances,
  Mobile Phones & Devices, Computers** — plus a **Showroom/location**
  sub-domain (see below), since Abans' real multi-branch network turned out
  to be the most natural source of several OWL concepts.
- Category/brand/attribute data pulled from the live site on 2026-08-28
  (see Phase 0) grounds every class in this plan — nothing here is invented
  to force-fit a Pizza parallel.

## Design principle: realism over structural mimicry

Some Pizza concepts (property hierarchy + transitivity, nested
restrictions) don't have a natural home in a flat retail product catalog —
forcing them onto products directly would mean inventing fake data (e.g. a
"battery cell" sub-component hierarchy Abans doesn't actually sell). Instead
we found a genuinely real structure that carries those concepts
authentically: **Abans' actual multi-branch showroom network**
(400+ real showrooms across Sri Lanka). A showroom's location
(`Showroom → City → Province`) is a textbook example of a real,
naturally transitive relationship, and "is this product available at a
showroom in Colombo" is a real, useful business question — not a
contrivance. Anywhere else a 1:1 Pizza parallel didn't hold up, we picked
the closest thing that's actually true of Abans' catalog instead of
forcing it.

## Key design decision: individuals matter this time

Pizza mostly modeled named pizzas as **classes** (TBox) with almost no
individuals — fine for reasoning demos, useless for SPARQL, which queries
concrete data. This ontology needs a real **ABox**: individual products
with asserted `hasBrand`, `hasPrice`, `hasWarrantyYears`,
`hasEnergyRating`, `availableAt`, etc. Defined classes
(`SmartProduct`, `PremiumProduct`...) still demonstrate reasoning, but by
auto-classifying *individuals*, not named subclasses.

## Environment & process policy

- **Python virtual environment**: before any backend/frontend code is
  written, create a venv **inside the assignment folder** so dependencies
  stay isolated and don't pollute the system Python:
  ```
  cd D:\temp\MSC\Sem_Web\protege_exercise\assignment
  python -m venv .venv
  .venv\Scripts\Activate.ps1        # PowerShell
  pip install fastapi rdflib uvicorn streamlit requests
  pip freeze > requirements.txt
  ```
  `.venv/` and `__pycache__/` get added to `.gitignore` — never commit the
  virtual environment itself, only `requirements.txt`.
- **Conventional commits**: same discipline as the tutorial repo. Commit at
  each phase boundary (not every micro-step) using `feat`/`docs`/`chore`/
  `fix` types, e.g. `feat(ontology): add core classes and category
  hierarchy`, `feat(backend): add FastAPI SPARQL endpoints`,
  `docs(assignment): finalize competency question list`. Commit checkpoints
  are marked explicitly at the end of each phase below.

## How to use this file

Same conventions as `tutorial/CLAUDE.md`: flip `[ ]` to `[x]` as steps are
verified, never delete a skipped step (note it instead), and note any
deviation as we go — exact restriction syntax may get refined during the
actual build, same as it did for Pizza.

---

## Phase 0 — Research (done)

- [x] **0. Survey real category/brand/attribute data** from buyabans.com.
  Findings: 13 top-level categories; brands incl. LG, Xiaomi, HP, Apple,
  Haier, Philips, Whirlpool, Toshiba, Lenovo; attributes incl. price,
  warranty years, capacity, energy/inverter rating, smart/WiFi features;
  400+ showrooms island-wide (real, verifiable multi-branch structure).

## Phase 1 — Setup

- [ ] **1. Create new ontology** in Protégé — `abans.owl`, ontology IRI
  `http://www.abans.lk/ontology/abans.owl`, save directly into
  `protege_exercise/assignment/abans.owl`.

## Phase 2 — Core classes & disjointness

- [ ] **2. Root classes**: `Product`, `Brand`, `Feature`,
  `EnergyRatingPartition`, `Location`, `Showroom` — direct subclasses of
  `owl:Thing`.
- [ ] **3. Product category classes** (disjoint subclasses of `Product`) —
  named after Abans' actual site navigation (verified against
  buyabans.com's live "All Categories" menu): `TV`, `HomeAppliance`,
  `MobileDevice`, `Computer`.
- [ ] **4. Sub-types per category** — using Abans' real subcategory names
  (disjoint within each category):
  - `TV` → `LEDTV`, `SmartLEDTV`, `UHDTV`, `OLEDTV`, `QLEDTV` (all 5 are
    real buyabans.com TV subcategories)
  - `HomeAppliance` → `Refrigerator`, `AirConditioner`, `WashingMachine`
    (real subcategories: Refrigerators, Air Conditioners, Washing
    Machines)
  - `MobileDevice` → `SmartMobilePhone`, `FeaturePhone`,
    `SmartBandAndWatch` (real subcategories: Smart Mobile Phones, Feature
    Phones, Smart Bands & Watches)
  - `Computer` → `Laptop`, `DesktopAndMonitor`, `Tablet` (real
    subcategories: Laptops, Desktops & Monitors, Tablets)
- [ ] **4b. Add `rdfs:label` annotations** to every class above with the
  *exact* real site wording (e.g. `TV` → label "TV", `HomeAppliance` →
  label "Home Appliances", `SmartMobilePhone` → label "Smart Mobile
  Phones") — keeps clean PascalCase OWL class IDs while making the
  ontology's human-readable face authentically match Abans' actual
  storefront, not a paraphrase of it.
- [ ] **5. `Feature` subclasses** (disjoint from each other): `SmartFeature`,
  `WiFiFeature`, `InverterFeature`, `BluetoothFeature`.
- [ ] **6. `EnergyRatingPartition`** value partition (like
  `SpicinessValuePartition`): `APlusPlusPlusRating`, `APlusPlusRating`,
  `APlusRating`, `ARating`, `BRating` — mutually disjoint, with a covering
  axiom.
- [ ] **7. `Location` classes**: `Location` → disjoint subclasses
  `Province`, `City` (real Sri Lankan geography, not invented).
- **Commit checkpoint**: `feat(ontology): add core classes, category
  hierarchy, and disjointness`

## Phase 3 — Properties

- [ ] **8. Object properties (product-facing)**: `hasBrand`
  (Product→Brand, functional), `hasFeature` (Product→Feature),
  `hasEnergyRating` (Product→EnergyRatingPartition, functional) — with
  inverses `isBrandOf`, `isFeatureOf`, `isEnergyRatingOf`.
- [ ] **9. Object properties (location-facing — the real transitivity
  source)**: `locatedIn` (Showroom/City→City/Province, **Transitive**),
  inverse `contains` (**also Transitive**, per the lesson that inverses of
  transitive properties should be transitive too); `availableAt`
  (Product→Showroom, not functional — a product can be stocked at many
  showrooms), inverse `stocks` (Showroom→Product).
- [ ] **10. Data properties**: `hasPrice` (xsd:decimal, functional),
  `hasWarrantyYears` (xsd:integer, functional), `hasCapacity`
  (xsd:decimal, optional — litres/kg/BTU by category), `hasScreenSize`
  (xsd:decimal, optional — TVs/laptops, inches).
- **Commit checkpoint**: `feat(ontology): add object and data properties
  with inverses and characteristics`

## Phase 4 — Restrictions & defined classes

- [ ] **11. `Product` restriction**: `hasBrand some Brand` (necessary
  condition, like `Pizza SubClassOf hasBase some PizzaBase`).
- [ ] **12. Simple defined classes** (existential, like `CheesyPizza`):
  - `SmartProduct ≡ Product and (hasFeature some SmartFeature)`
  - `EcoFriendlyProduct ≡ Product and (hasEnergyRating some
    (APlusPlusPlusRating or APlusPlusRating))`
- [ ] **13. Universal-restriction defined class** (the real
  `VegetarianPizza` analog — **needs closure axioms**, see Phase 5):
  `FullySmartProduct ≡ Product and (hasFeature only (SmartFeature or
  WiFiFeature or BluetoothFeature))`
- [ ] **14. Nested restriction** (realistic `SpicyPizza`-style nesting,
  using the real showroom structure): `ColomboAvailableProduct ≡ Product
  and (availableAt some (Showroom and (locatedIn value Colombo)))`
- [ ] **15. Datatype facet restriction** (OWL 2 territory Pizza never
  used): `PremiumProduct ≡ Product and (hasPrice some
  xsd:decimal[>= 150000])`
- [ ] **16. Complement class**: `BudgetProduct ≡ Product and (not
  PremiumProduct)`, disjoint with `PremiumProduct`.
- [ ] **17. Cardinality restriction**: `FullyLoadedProduct ≡ Product and
  (hasFeature min 3)`.
- [ ] **18. Named "product line" classes** — realistic, grounded in
  Abans' actual catalog (Apple is a real top-level category; budget
  Android phones and inverter appliances are real, commonly-advertised
  segments), each combining multiple restrictions including a `hasValue`
  restriction, mutually disjoint:
  - `PremiumAppleProduct ≡ MobileDevice and (hasBrand value Apple) and
    (hasFeature some SmartFeature) and (hasPrice some
    xsd:decimal[>= 200000])`
  - `BudgetSmartphone ≡ SmartMobilePhone and (hasFeature some
    SmartFeature) and (hasPrice some xsd:decimal[<= 50000])`
  - `InverterHomeAppliance ≡ HomeAppliance and (hasFeature some
    InverterFeature) and (hasEnergyRating some (APlusPlusRating or
    APlusPlusPlusRating))`
- **Commit checkpoint**: `feat(ontology): add restrictions and defined
  classes for automatic classification`

## Phase 5 — Open World Assumption demo (required)

This was the single most important lesson from the Pizza build — not
optional here either.

- [ ] **19. Closure axioms** — add `hasFeature only (SmartFeature or
  WiFiFeature or BluetoothFeature)` closure restrictions to
  `PremiumAppleProduct` and `BudgetSmartphone` (both only ever assert
  smart-type features) **and to specific product individuals as needed**,
  so the reasoner can correctly classify them under `FullySmartProduct`.
  **Do not** add this same closure to `InverterHomeAppliance` — it
  necessarily has an `InverterFeature`, which is disjoint from the
  smart/WiFi/Bluetooth set (Phase 2 step 5), so closing it the same way
  would make the *entire class* unsatisfiable (equivalent to
  `owl:Nothing`), not just excluded from `FullySmartProduct`. This is a
  real gotcha worth understanding — closure axioms must only be added
  where they can't contradict the class's own defining restrictions.
- [ ] **20. Deliberately unclosed individual** — create one product
  individual with `hasFeature some SmartFeature` asserted but **not**
  closed. Classify and confirm: it lands under `SmartProduct` (provable
  positive claim) but in **neither** `FullySmartProduct` nor its
  complement `BasicProduct ≡ Product and (not FullySmartProduct)`
  (disjoint with `FullySmartProduct`) — the OWA payoff, same shape as
  `UnclosedPizza`.
- **Commit checkpoint**: `feat(ontology): add closure axioms and open
  world assumption demonstration`

## Phase 6 — Individuals (the ABox)

- [ ] **21. `Brand` individuals**: `LG`, `Samsung`, `Apple`, `Whirlpool`,
  `Haier`, `HP`, `Xiaomi`, `Lenovo`, `Toshiba`, `Philips` — enumerate as a
  closed class afterward (like `Country`).
- [ ] **22. `Province`/`City`/`Showroom` individuals** (real Sri Lankan
  geography, real Abans branch cities): Provinces `WesternProvince`,
  `CentralProvince`, `SouthernProvince`; Cities `Colombo` (locatedIn
  WesternProvince), `Kandy` (locatedIn CentralProvince), `Galle` (locatedIn
  SouthernProvince); Showrooms `Abans_Colombo_City` (locatedIn Colombo),
  `Abans_Kandy` (locatedIn Kandy), `Abans_Galle` (locatedIn Galle).
- [ ] **23. Product individuals** — ~15-20 across the 4 categories, each
  with concrete `hasBrand`/`hasPrice`/`hasWarrantyYears`/`hasFeature`/
  `hasEnergyRating`/`availableAt`, spread across price/brand/rating
  combinations so the competency questions below are non-trivial to
  answer.
- [ ] **24. Reclassify & inspect** — run the reasoner, confirm individuals
  land under the right defined classes automatically.
- **Commit checkpoint**: `feat(ontology): add brand, location, and product
  individuals`

## Phase 7 — Optional / stretch

Mirrors Pizza's own optional items — present in the plan, not silently
dropped, but lowest priority.

- [ ] **25. Consistency-check probe class** (mirrors Ex. 24-27) — a
  product deliberately asserted as both `Refrigerator` and `Laptop`
  (disjoint branches) to confirm the reasoner catches it; left in
  permanently as a regression test.
- [ ] **26. Multiple independent N&S condition sets** (mirrors the
  `Triangle` example) — `RecommendedProduct` with two separate
  `Equivalent To` axioms: (a) `Product and (hasFeature min 3)` — feature-
  rich path, or (b) `Product and (hasEnergyRating some
  (APlusPlusPlusRating or APlusPlusRating)) and (hasPrice some
  xsd:decimal[<= 100000])` — efficient-and-affordable path. Two genuinely
  independent business reasons a product might be recommended.

## Phase 8 — Export

- [ ] **27. Bake in inferred axioms** — Protégé's **File → "Export
  inferred axioms as ontology"** (or synchronize + merge), so reasoner-
  derived `rdf:type` facts (SmartProduct, PremiumProduct, etc.) are
  physically present as triples. **Required** for the SPARQL backend
  below, which has no OWL reasoner of its own.
- [ ] **28. Final export** — save as `assignment/abans.owl` (RDF/XML).
  **This alone satisfies the assignment's pass bar.**
- **Commit checkpoint**: `feat(ontology): export final ontology with
  materialized inferred axioms`

---

## Phase 9 — Competency questions (for the "score more" tier)

| # | Competency question | Query type |
|---|---|---|
| CQ1 | What products does brand X sell? | Simple join |
| CQ2 | What TVs cost less than Rs. 150,000? | Filter |
| CQ3 | Which products have WiFi? | Simple join |
| CQ4 | Which products have 2+ years warranty? | Filter |
| CQ5 | Which products are classified as Smart? | Reasoner-inferred class |
| CQ6 | Which products are Eco-Friendly (A++/A+++)? | Reasoner-inferred class |
| CQ7 | Which products are Premium (price ≥ 150,000)? | Reasoner-inferred + datatype filter |
| CQ8 | Which products are Budget (complement of Premium)? | Reasoner-inferred, complement class |
| CQ9 | How many products exist per category? | Aggregate (GROUP BY + COUNT) |
| CQ10 | What is the average price per category? | Aggregate (GROUP BY + AVG) |
| CQ11 | Which brands appear in more than one category? | Multi-hop join |
| CQ12 | Which products have 3+ features (Fully-Loaded)? | Reasoner-inferred, cardinality |
| CQ13 | Which products are available at showrooms in the Western Province? | Transitive-location join |
| CQ14 | Which showrooms stock a given product, and in which city/province? | Multi-hop join over a transitive property |

- [ ] **29. Write SPARQL for each CQ** (once Phase 6's ABox is in place).
- [ ] **30. Test each query in Protégé's SPARQL Query tab** — minimum
  viable path to the "score more" tier, no front end required.
- **Commit checkpoint**: `docs(assignment): finalize competency questions
  and SPARQL queries`

## Phase 10 — Backend (FastAPI + rdflib)

- [ ] **31. Update `.gitignore` first** — add `.venv/` and `__pycache__/`
  **before** creating the virtual environment below, so it's never at risk
  of being accidentally staged in the commits that follow this phase.
- [ ] **31b. Create the virtual environment** (see Environment & process
  policy above) inside `assignment/`, install `fastapi`, `rdflib`,
  `uvicorn`.
- [ ] **32. `backend/main.py`** — loads `abans.owl` into an in-memory
  `rdflib.Graph()` at startup. Endpoints:
  - `GET /health` — trivial healthcheck
  - `GET /competency-questions` — list of the 14 CQs (id + text)
  - `GET /competency-questions/{id}/run` — executes that CQ's SPARQL,
    returns JSON rows
  - `POST /sparql` — accepts raw SPARQL text, executes it, returns JSON
    rows (ad-hoc/advanced demo path)
- [ ] **33. Verify locally** — `uvicorn backend.main:app --reload`
  (port 8000), hit each endpoint, confirm CQ1-CQ14 all return non-empty,
  correct results.
- **Commit checkpoint**: `feat(backend): add FastAPI service with SPARQL
  competency-question endpoints`

## Phase 11 — Frontend (Streamlit)

- [ ] **34. `frontend/app.py`** — sidebar dropdown of the 14 CQs → "Run"
  button → calls the backend `/competency-questions/{id}/run` → renders
  results as `st.dataframe`. Second tab: raw SPARQL text box → calls
  `/sparql` → same table rendering.
- [ ] **35. Verify locally** — `streamlit run frontend/app.py`
  (port 8501), confirm every CQ renders correctly end-to-end through the
  UI.
- **Commit checkpoint**: `feat(frontend): add Streamlit UI for competency
  question queries`

## Phase 12 — Wrap-up

- [ ] **36. Final reasoner run** — confirm no inconsistencies (aside from
  the deliberate probe class if included), review ontology metrics.
- [ ] **37. `.gitignore` sanity check** — confirm `.venv/`/`__pycache__/`
  were never actually committed (should already be true from step 31).
- [ ] **38. (If required) Short write-up** — check assignment brief for
  whether a written report is separately required beyond the OWL file +
  queries + front end.
- **Commit checkpoint**: `chore(assignment): final cleanup and wrap-up`
