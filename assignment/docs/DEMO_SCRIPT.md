# Abans Demo Script — 5:00

Natural narration, organized by time segment. Read each "Say" block like
you're explaining it to someone, not reciting bullet points.

## Before recording

- [ ] Protégé open, `abans.owl`, reasoner already run once
- [ ] Start on asserted **Classes** tab (not mid-reasoner-run)
- [ ] Backend running: port 8010
- [ ] Frontend running: port 8511, open in browser
- [ ] Sidebar shows "Connected" — 889 triples / 59 individuals
- [ ] Mute notifications

---

## 0:00–0:20 — Intro

**Show:** Classes tab, collapsed

**Say:** This is an ontology I built for Abans — a real Sri Lankan
electronics retailer. It models their actual product catalog: TVs, home
appliances, mobile devices, and computers.

---

## 0:20–0:50 — Class hierarchy

**Show:** Expand `Product` → 4 categories → expand `TV`

**Say:** The product categories are disjoint from each other, and each one
has real sub-types pulled straight from Abans' own site — LED, Smart LED,
UHD, OLED, and QLED TVs. I even added labels so the tree shows their
actual wording, not a paraphrase.

---

## 0:50–1:30 — Restrictions

**Show:** `Product` (hasBrand), `PremiumProduct` (price facet)

**Say:** I used every major type of OWL restriction here. Every product
must have a brand — that's a necessary condition. And this one,
PremiumProduct, uses a numeric price restriction directly on a data
value, which goes further than a typical intro exercise.

---

## 1:30–2:15 — Reasoner magic

**Show:** Individuals by class → **Inferred** → `SmartProduct`, `PremiumProduct`

**Say:** Here's the reasoner doing real work. I never said this phone is a
SmartProduct anywhere — it's inferred automatically because it has a
smart feature. Same story for Premium: anything priced above 150,000
gets classified in on its own.

---

## 2:15–2:50 — ⭐ Open World Assumption (most important part)

**Show:** `Mystery_Smart_Gadget` → inferred Types

**Say:** This next part is the most important idea in the whole ontology.
This product has one smart feature asserted, but I deliberately never
said that's its *only* feature. So the reasoner can't confirm it's fully
smart, but it also can't rule it out — it sits in genuine logical limbo.
That's the Open World Assumption, and it's the core idea OWL is built
around.

---

## 2:50–3:15 — Real showroom network

**Show:** `Abans_Colombo_City` → `locatedIn` chain → Province

**Say:** I also modeled Abans' real branch network. Showrooms are located
in cities, which are located in provinces, using a transitive property —
so a product available at the Colombo showroom is automatically known to
be available in the Western Province, without me stating that directly.

---

## 3:15–3:40 — Metrics

**Show:** Ontology metrics panel

**Say:** In total, the ontology has around 24 classes, 20 properties, and
18 real product individuals, fully reasoner-verified with no
inconsistencies.

---

## 3:40–4:30 — Live app demo

**Show:** Streamlit — run CQ11, then Raw SPARQL tab

**Say:** For the scoring tier, I built 14 competency questions as real
SPARQL queries, served through a FastAPI backend with a Streamlit front
end. This one finds brands that appear in more than one category —
Samsung, since they sell TVs, appliances, and watches. And here's a raw
SPARQL box where I can run any query live against the exported ontology.

---

## 4:30–4:50 — Architecture

**Show:** Sidebar stats

**Say:** The backend loads the exported OWL file into memory, including
the reasoner's inferred facts, which get baked in during export — so all
of this runs without needing a live reasoner at query time.

---

## 4:50–5:00 — Close

**Say:** So that's the full pipeline — Protégé for modeling and
reasoning, and a real API and UI on top for actually querying it. Thanks
for watching.

---

## If running long — cut these first

- 0:50–1:30 (restrictions) → one sentence only
- 2:50–3:15 (showroom) → mention in intro instead, skip screen
