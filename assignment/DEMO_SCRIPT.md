# Abans Ontology Assignment — 5-Minute Demo Script

For recording a screen-capture walkthrough covering the ontology (Protégé),
the reasoner demos, and the FastAPI/Streamlit stack. Total runtime target:
**5:00**.

## Before you hit record

- [ ] Open `abans.owl` in Protégé, confirm it's the final exported version
      (`protege_exercise/assignment/abans.owl`).
- [ ] **Reasoner → Start reasoner** once *before* recording, then switch
      back to the asserted **"Classes"** tab so you open on the manually-
      built view, not mid-reasoner-run.
- [ ] Start both servers ahead of time so they're already warm:
  ```
  cd protege_exercise/assignment
  .venv\Scripts\python.exe -m uvicorn backend.main:app --port 8010
  .venv\Scripts\python.exe -m streamlit run frontend/app.py --server.port 8511
  ```
- [ ] Open `http://localhost:8511` in a browser tab, confirm the sidebar
      shows "Connected" with 889 triples / 59 individuals before you start.
- [ ] Have `competency_questions.md` or the Protégé "Snap SPARQL Query" tab
      ready as a fallback if the live frontend demo has a hiccup.
- [ ] Mute notification sounds.

## Narration style

First person, present tense — "here I've modeled...", "watch what happens
when...". Paraphrase restriction syntax rather than reading it verbatim
character-by-character.

---

## Script

| Time | Screen | What to click / show | What to say |
|---|---|---|---|
| **0:00–0:20** | Protégé, Classes tab | Top-level hierarchy collapsed | "This is an ontology I built for Abans — a real Sri Lankan electronics retailer — modeling their actual product catalog: TVs, home appliances, mobile devices, and computers, using real category names and brands pulled from their live site." |
| **0:20–0:50** | Classes tab | Expand `Product` → show the 4 disjoint categories, then expand `TV` to show its 5 real sub-types (LED/Smart LED/UHD/OLED/QLED) | "Categories are disjoint from each other, and each has real sub-types straight from Abans' own navigation menu — I even attached `rdfs:label` annotations so the tree displays their actual wording, like 'Home Appliances' and 'Smart Mobile Phones', not paraphrased names." |
| **0:50–1:30** | Classes tab | Select `Product` (show `hasBrand some Brand`), then `EcoFriendlyProduct`, then `PremiumProduct` (datatype facet `hasPrice some xsd:decimal[>=150000]`) | "I used every major OWL restriction type here — necessary conditions, existential restrictions, and this one: a datatype facet restriction directly on a numeric price value, which goes beyond what a typical intro exercise covers." |
| **1:30–2:15** | Classes tab → **Individuals by class**, **Inferred** view | Select `SmartProduct`, expand to show inferred members; then `PremiumProduct` | "Here's the reasoner doing real work — I never said `iPhone_15_Pro` is a SmartProduct anywhere. It's inferred automatically because it has a smart feature, following the class definition. Same for Premium — priced above 150,000 gets classified in automatically." |
| **2:15–2:50** | Individuals (Inferred) | Select `Mystery_Smart_Gadget`, show its inferred Types list | "This is the most important part conceptually. This product has one smart feature asserted, but I deliberately never said that's its *only* feature. So the reasoner correctly refuses to classify it as fully-smart, but also refuses to rule it out — it sits in genuine logical limbo. That's the Open World Assumption, and it's the core lesson OWL is built around." |
| **2:50–3:15** | Individuals by class | Select `Abans_Colombo_City`, show its `locatedIn` chain to `WesternProvince` | "I also modeled Abans' real branch network — showrooms located in cities, located in provinces — using a transitive property, so a product available at a Colombo showroom is automatically known to be available in the Western Province, without me stating that directly." |
| **3:15–3:40** | Active ontology tab / metrics | Show class/individual/axiom counts | "In total: around 24 classes, 20 properties, and 18 real product individuals, fully reasoner-verified with no inconsistencies." |
| **3:40–4:30** | Browser: Streamlit app | Select a competency question (e.g. CQ11 — brands in 2+ categories), click Run, show results; then flip to the Raw SPARQL tab and run one ad-hoc query | "For the scoring tier, I built 14 competency questions as real SPARQL queries, served through a FastAPI backend and this Streamlit front end. This one finds brands that show up in more than one product category — Samsung, since they sell TVs, appliances, and watches. And here's a raw SPARQL box for any ad-hoc query, running live against the exported ontology." |
| **4:30–4:50** | Streamlit sidebar | Point at connection status / stats | "The backend loads the exported OWL file — including the reasoner's inferred facts, baked in during export — into an in-memory graph, so all of this runs without needing a live reasoner at query time." |
| **4:50–5:00** | — | — | "That's the full pipeline: Protégé for modeling and reasoning, and a real API and UI on top for querying it. Thanks for watching." |

---

## If you're short on time (hard 4-minute cut)

Drop these two beats:
- **0:50–1:30** (restriction type tour) — fold into one sentence while
  showing `PremiumProduct` only.
- **2:50–3:15** (showroom/transitivity) — mention it verbally in the intro
  instead ("...including their real branch network...") without a dedicated
  screen.

## If you have 7–8 minutes instead of 5

Add:
- **Closure axioms**: show `BudgetSmartphone`'s closure restriction and
  explain why it was needed for correct classification — ties directly
  into the Open World Assumption beat, makes the payoff land harder.
- **Consistency check**: briefly mention why a probe/inconsistency demo
  was deliberately *not* included this time (kept the ontology's content
  fully grounded in Abans' real catalog rather than adding an artificial
  broken class purely for demonstration).
- **Backend code**: a 15-second glance at `backend/main.py`'s
  `/competency-questions/{id}/run` endpoint, showing the SPARQL is
  genuinely stored server-side, not hardcoded per button in the frontend.
