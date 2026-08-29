# Abans Demo Script — 5:00

Cue-card format — short lines, easy to glance at while recording.

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

**Say:**
- Ontology for Abans
- Real Sri Lankan retailer
- Real catalog: TV, appliances, mobile, computers

---

## 0:20–0:50 — Class hierarchy

**Show:** Expand `Product` → 4 categories → expand `TV`

**Say:**
- Categories are disjoint
- Sub-types are real (LED / Smart LED / UHD / OLED / QLED)
- Labels match Abans' actual site wording

---

## 0:50–1:30 — Restrictions

**Show:** `Product` (hasBrand), `PremiumProduct` (price facet)

**Say:**
- Every restriction type used
- This one: numeric price facet
- Beyond typical intro-level OWL

---

## 1:30–2:15 — Reasoner magic

**Show:** Individuals by class → **Inferred** → `SmartProduct`, `PremiumProduct`

**Say:**
- Never asserted these directly
- Reasoner classifies automatically
- iPhone → Smart, because it has a smart feature

---

## 2:15–2:50 — ⭐ Open World Assumption (most important part)

**Show:** `Mystery_Smart_Gadget` → inferred Types

**Say:**
- One smart feature asserted
- Never said "only" this feature
- Reasoner won't confirm OR deny fully-smart
- Genuine logical limbo
- This is OWL's core idea

---

## 2:50–3:15 — Real showroom network

**Show:** `Abans_Colombo_City` → `locatedIn` chain → Province

**Say:**
- Real Abans branch structure
- Transitive property
- Colombo showroom → automatically Western Province

---

## 3:15–3:40 — Metrics

**Show:** Ontology metrics panel

**Say:**
- ~24 classes, 20 properties, 18 individuals
- Fully consistent, reasoner-verified

---

## 3:40–4:30 — Live app demo

**Show:** Streamlit — run CQ11, then Raw SPARQL tab

**Say:**
- 14 competency questions, real SPARQL
- FastAPI backend + Streamlit UI
- CQ11: brands in 2+ categories → Samsung
- Raw SPARQL box: any query, live

---

## 4:30–4:50 — Architecture

**Show:** Sidebar stats

**Say:**
- Backend loads exported OWL
- Inferred facts baked in at export
- No live reasoner needed at query time

---

## 4:50–5:00 — Close

**Say:**
- Protégé for modeling + reasoning
- Real API + UI on top
- Thanks for watching

---

## If running long — cut these first

- 0:50–1:30 (restrictions) → one sentence only
- 2:50–3:15 (showroom) → mention in intro instead, skip screen
