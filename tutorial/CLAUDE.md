# Pizza Ontology — Progress Tracker

Tracks our step-by-step build of the Pizza ontology from **"A Practical Guide To
Building OWL Ontologies Using The Protégé-OWL Plugin and CO-ODE Tools"**
(`A_Practical_Guide_To_Building_OWL_Ontologies_Using.pdf`), adapted for the
modern Protégé 5.6.9 UI (the guide's screenshots are from an old ~2004 version).

- **Ontology file:** `pizza.owl` — saved in `C:\Users\pathmika.w\Documents\`
- **Ontology IRI:** `http://www.pizza.com/ontology/pizza.owl`
- **Protégé install:** `D:\temp\MSC\Protege-5.6.9\Protege.exe`
- **Reasoner:** HermiT (built into Protégé 5.6.9 — replaces RACER from the original guide)

Every item below is tagged with the guide's own **Exercise number** *and* its
**exact title text quoted from the PDF** — search for that exact phrase
(Ctrl+F in a PDF reader) to jump straight to the relevant page and verify
the precise instructions before/after doing a step in Protégé.

## How to use this file

- After finishing a step, flip its `[ ]` to `[x]` and add a one-line note if
  we did anything differently from the guide (extra classes, renamed things,
  substituted UI actions, etc.). This is a living log, not a static plan —
  keep it in sync with what's actually in `pizza.owl`.
- **Never delete a skipped/incomplete exercise from this file.** If a step
  gets skipped (like Ex. 24–27 below), leave it marked `[ ]` with a note
  explaining why. The goal is a complete, honest record of what's done vs.
  outstanding, not a tidy-looking checklist.
- **Before executing any step, verify it against the original PDF** using
  the quoted exercise title to locate it. The exact wording, filler
  class/property names, and expected UI result should match the guide's own
  exercise text (adjusted only for modern Protégé's UI/menu layout).
- **Always follow the PDF's instructions exactly** — don't improvise cleanup
  steps, deletions, or "improvements" the guide doesn't itself call for
  (e.g. `ProbeInconsistentTopping` from Ex. 24–27 is deliberately left in
  the ontology permanently as a regression test — the guide never says to
  delete it, so we don't).

## 📎 Cross-reference: v1.3 tutorial

A second, updated version of this tutorial exists —
`protegeowltutorialp4_v1_3.pdf` (Manchester's Protégé 4 edition, vs. the
CO-ODE "Practical Guide" v1.0 we actually followed). Cross-checked on
2026-08-08: same Pizza domain, same core OWL concepts (disjointness,
existential/universal/cardinality restrictions, defined classes, closure
axioms, value partitions, individuals). Differences are cosmetic/tooling —
FaCT++ vs. HermiT reasoner, qualified vs. unqualified cardinality
restrictions (logically equivalent here since `hasTopping`'s range is
already `PizzaTopping`), and an added DL Query tab exercise not present in
v1.0. **No rework needed** — `pizza.owl` is valid OWL 2 DL either way.
Exercise numbers in this tracker refer to the v1.0 guide only; v1.3 uses
different numbering.

## ⚠️ Known gap

**Exercises 24–27 were skipped** (the `ProbeInconsistentTopping`
reasoner-error demo) — we went straight from Ex. 23 to Ex. 28/29
(`CheesyPizza`). Purely pedagogical (teaches how the reasoner flags
inconsistent classes), doesn't affect ontology correctness — but it's a real
exercise block in the guide. Flagged as **Step 19** below.

---

## Phase 1 — Setup

- [x] **1. Create new ontology** — Ex. 2, *"Create a new OWL project"* — `pizza.owl`, IRI `http://www.pizza.com/ontology/pizza.owl`, saved to Documents.

## Phase 2 — Core classes & disjointness

- [x] **2. Core classes** — Ex. 3, *"Create classes Pizza, PizzaTopping and PizzaBase"* — as direct subclasses of `owl:Thing`.
- [x] **3. Disjointness** — Ex. 4, *"Make Pizza, PizzaTopping and PizzaBase disjoint from each other"*.
- [x] **4. `PizzaBase` subclasses** — Ex. 5, *"Use the 'Create Group Of Classes' Wizard to create ThinAndCrispy and DeepPan as subclasses of PizzaBase"* — done manually (no such wizard in modern Protégé); added `ThinAndCrispyBase`, `DeepPanBase`, and **`GrandDipperBase`** (extra class per lecturer's instruction, not in original guide) — all three mutually disjoint.
- [x] **5. `PizzaTopping` category subclasses** — Ex. 6 part 1, *"Create some subclasses of PizzaTopping"* — `CheeseTopping`, `MeatTopping`, `VegetableTopping`, `SeafoodTopping` — mutually disjoint.
- [x] **6. Specific toppings** — Ex. 6 part 2 (same exercise, continued sub-steps), all disjoint within their category:
  - `CheeseTopping` → `MozzarellaTopping`, `ParmezanTopping`
  - `MeatTopping` → `HamTopping`, `SalamiTopping`, `PepperoniTopping`, `SpicyBeefTopping`
  - `SeafoodTopping` → `PrawnTopping`, `AnchovyTopping`, `TunaTopping`
  - `VegetableTopping` → `CaperTopping`, `OnionTopping`, `MushroomTopping`, `OliveTopping`, `TomatoTopping`, `PepperTopping` (→ `RedPepperTopping`, `GreenPepperTopping`, `JalapenoPepperTopping`, mutually disjoint)

## Phase 3 — Object properties

- [x] **7. Object properties** — Ex. 7, *"Create an object property called hasIngredient"* + Ex. 8, *"Create hasTopping and hasBase as sub-properties of hasIngredient"*.
- [x] **8. Inverse properties** — Ex. 9, *"Create some inverse properties"* — `isIngredientOf`, `isToppingOf`, `isBaseOf`.
- [x] **9. Property characteristics** — Ex. 10, *"Make the hasIngredient property transitive"* + Ex. 11, *"Make the hasBase property functional"* (also applied Transitive to `isIngredientOf`, per the guide's note that inverses of transitive properties should also be transitive).
- [x] **10. Domains/ranges** — Ex. 12, *"Specify the range of hasTopping"* + Ex. 13, *"Specify Pizza as the domain of the hasTopping property"* + Ex. 14, *"Specify the domain and range for the isToppingOf property"* + Ex. 15, *"Specify the domain and range for the hasBase property and its inverse property isBaseOf"*.

## Phase 4 — Restrictions & named pizzas

- [x] **11. `Pizza` restriction** — Ex. 16 + Ex. 17, *"Add a restriction to Pizza that specifies a Pizza must have a PizzaBase"* — `SubClassOf: hasBase some PizzaBase`.
- [x] **12. `NamedPizza` / `MargheritaPizza`** — Ex. 18, *"Create a subclass of Pizza called NamedPizza, and a subclass of NamedPizza called MargheritaPizza"*.
- [x] **13. `MargheritaPizza` toppings** — Ex. 19, *"Create an existential (∃) restriction on MargheritaPizza that acts along the property hasTopping with a filler of MozzarellaTopping..."* + Ex. 20, *"Create a existential restriction (∃) on MargheritaPizza that acts along the property hasTopping with a filler of TomatoTopping..."*.
- [x] **14. `AmericanaPizza`, `AmericanHotPizza`, `SohoPizza`** — Ex. 21, *"Create AmericanaPizza by cloning and modifying the description of MargheritaPizza"* + Ex. 22, *"Create an AmericanHotPizza and a SohoPizza"* — built directly instead of cloning (no reliable clone shortcut in modern Protégé); same end result.
- [x] **15. Disjointness** — Ex. 23, *"Make subclasses of NamedPizza disjoint from each other"*.
- [x] **16. First reasoner run** — ad-hoc check on our part (not tied to a specific numbered exercise — the guide's first real reasoner exercise is Ex. 25, part of the skipped block below). Confirmed ontology consistent; asserted vs. inferred hierarchy identical at this point, as expected.

## Phase 5 — Defined classes, automatic classification & reasoner demo

- [x] **17. `CheesyPizza`** — Ex. 28, *"Create a subclass of Pizza called CheesyPizza and specify that it has at least one topping that is a kind of CheeseTopping"* + Ex. 29, *"Convert the necessary conditions for CheesyPizza into necessary & sufficient conditions"*. Done slightly out of the guide's order (see Step 19 below).
- [x] **18. Reclassify & inspect** — Ex. 30, *"Use the reasoner to automatically compute the subclasses of CheesyPizza"*. Confirmed: `MargheritaPizza`, `AmericanaPizza`, `AmericanHotPizza`, `SohoPizza` all auto-classified as inferred subclasses of `CheesyPizza`.
- [x] **19. Reasoner error demo** — Ex. 24, *"Add a Probe Class called ProbeInconsistentTopping which is a subclass of both CheeseTopping and Vegetable"* + Ex. 25, *"Classify the ontology to make sure ProbeInconsistentTopping is inconsistent"* + Ex. 26, *"Remove the disjoint statement between CheeseTopping and VegetableTopping to see what happens"* + Ex. 27, *"Fix the ontology by making CheeseTopping and Vegetable disjoint from each other"*. Confirmed: `ProbeInconsistentTopping` appeared red under `owl:Nothing`, disappeared when disjointness removed, reappeared when restored. Done out of order (after Ex. 28/29 instead of before), no functional impact.

## Phase 6 — Universal restrictions & open-world reasoning

- [x] **20. `VegetarianPizza`** — Ex. 31, *"Create a class to describe a VegetarianPizza"* + Ex. 32, *"Convert the necessary conditions for VegetarianPizza into necessary & sufficient conditions"*. Built directly as `Equivalent To: Pizza and (hasTopping only (CheeseTopping or VegetableTopping))`. Confirmed empty of inferred subclasses before closure axioms — the guide's Open World Assumption demo worked as expected.
- [x] **21. Closure axioms** — Ex. 33, *"Use the reasoner to classify the ontology"* (first pass — shows the Open World gap) + Ex. 34, *"Add a closure axiom on the hasTopping property for MargheritaPizza"* + Ex. 35, *"Add a closure axiom on the hasTopping property for SohoPizza"* + Ex. 36, *"Automatically create a closure axiom on the hasTopping property for AmericanaPizza"* + Ex. 37, *"Automatically create a closure axiom on the hasTopping property for AmericanHotPizza"* + Ex. 38, *"Use the reasoner to classify the ontology"* (second pass — confirms correct classification). Added closure axioms manually (`hasTopping only (...)`) to all four named pizzas. Confirmed: MargheritaPizza + SohoPizza now inferred under VegetarianPizza; AmericanaPizza + AmericanHotPizza correctly excluded.

## Phase 7 — Value partitions & spiciness

- [x] **22. `SpicinessValuePartition`** — Ex. 39, *"Create a ValuePartition to represent the spiciness of pizza toppings"*. Built manually (no ValuePartition wizard in modern Protégé): `ValuePartition` → `SpicinessValuePartition` → `Mild`/`Medium`/`Hot` (mutually disjoint), covering axiom `SpicinessValuePartition Equivalent To Mild or Medium or Hot`, `hasSpiciness` functional object property with range `SpicinessValuePartition`.
- [x] **23. Assign spiciness** — Ex. 40, *"Use the properties matrix wizard to specify the spiciness of pizza toppings"* — no such wizard in modern Protégé, assigned manually via 17 `hasSpiciness some <Level>` SubClassOf restrictions (Mild: Mozzarella/Parmezan/Ham/Anchovy/Prawn/Tuna/Caper/Mushroom/Olive/Onion/GreenPepper/RedPepper/Tomato; Medium: Pepperoni/Salami; Hot: SpicyBeef/JalapenoPepper). Spot-checked JalapenoPepperTopping and MozzarellaTopping — correct.
- [x] **24. `SpicyPizza`** — Ex. 41, *"Create a SpicyPizza as a subclass of Pizza"* + Ex. 42, *"Use the reasoner to classify the ontology"*. Built as `Equivalent To: Pizza and (hasTopping some (PizzaTopping and (hasSpiciness some Hot)))` (used `some` not `value` since spiciness levels are classes, not individuals, in our model). Confirmed: `AmericanHotPizza` inferred as subclass.

## Phase 8 — Cardinality restrictions

- [x] **25. `InterestingPizza`** — Ex. 43, *"Create an InterestingPizza that has at least three toppings"* + Ex. 44, *"Use the reasoner to classify the ontology"*. Built as `Equivalent To: Pizza and (hasTopping min 3)`. Confirmed: Americana/AmericanHot/Soho inferred as subclasses; Margherita correctly excluded (only 2 distinct toppings).

## Phase 9 — More on open-world reasoning (Chapter 5 of the guide)

- [x] **26. `NonVegetarianPizza`** — Ex. 45, *"Create NonVegetarianPizza as a subclass of Pizza and make it disjoint to VegetarianPizza"* + Ex. 46, *"Make VegetarianPizza the complement of VegetarianPizza"* (guide text as printed — this is very likely a typo in the PDF itself; the intent, per the surrounding text, is clearly "make **NonVegetarianPizza** the complement of VegetarianPizza") + Ex. 47, *"Add Pizza to the necessary and sufficient conditions for NonVegetarianPizza"* + Ex. 48, *"Use the reasoner to classify the ontology"*. Built directly as `Equivalent To: Pizza and (not VegetarianPizza)`, disjoint with `VegetarianPizza`. Confirmed: `AmericanaPizza` and `AmericanHotPizza` inferred as subclasses.
- [x] **27. `UnclosedPizza`** — Ex. 49, *"Create a subclass of NamedPizza with a topping of Mozzarella"* + Ex. 50, *"Use the reasoner to classify the ontology"* — the clearest illustration of the Open World Assumption in the whole guide. Confirmed: `UnclosedPizza` inferred under `CheesyPizza` (provable positive claim) but appears in *neither* `VegetarianPizza` nor `NonVegetarianPizza` (unprovable either way, since its `hasTopping some MozzarellaTopping` restriction was deliberately left without a closure axiom).

## Phase 10 — Other OWL constructs (Chapter 6, optional/stretch)

- [x] **28. Individuals** — Ex. 51, *"Create a class called Country and populate it with some individuals"*. Created `Country` class with 5 individuals: `Italy`, `America`, `England`, `France`, `Germany`.
- [x] **29. `hasValue` restriction** — Ex. 52, *"Create a hasValue restriction to specify that MozzarellaTopping has Italy as its country of origin."* Created `hasCountryOfOrigin` object property; `MozzarellaTopping SubClassOf hasCountryOfOrigin value Italy`.
- [x] **30. Enumerated class** — Ex. 53, *"Convert the class Country into an enumerated class"*. `Country Equivalent To: {America, England, France, Germany, Italy}`.
- [x] **31. Multiple N&S condition sets** — Ex. 54, *"Create a class to define a Triangle using multiple sets of Necessary & Sufficient conditions"*. `Polygon`/`Triangle`/`hasSide`/`hasAngle` created; `Triangle` has two independent `Equivalent To` axioms: `Polygon and (hasSide exactly 3)` and `Polygon and (hasAngle exactly 3)`.

## Phase 11 — Namespaces & imports (Chapter 7, out of scope)

- [ ] **Ex. 55**, *"Create a namespace and prefix to refer to classes, properties and individuals in the Wine ontology"*
- [ ] **Ex. 56**, *"Import the koala ontology into an ontology"*
- [ ] **Ex. 57**, *"Specifing an alternative location for an imported ontology"*
- [ ] **Ex. 58**, *"Import the Dublin Core Meta Data Elements Ontology"*
- [ ] **Ex. 59**, *"Import the Protégé-OWL Meta Data Ontology"*

These are general Protégé features unrelated to the Pizza ontology's actual
content — **not planned unless specifically required by the assignment.**

## Final step

- [ ] **32. Final save + sanity check** — re-run reasoner, confirm no inconsistencies, review ontology metrics (class/property/axiom counts).

---

## Full exercise audit (Ex. 1–59) — completeness check

| Ex. # | Status | Mapped to Step |
|---|---|---|
| 1 | n/a — generic template example in intro, not a real ontology step | — |
| 2–23 | ✅ Done | Steps 1–15 |
| 24–30 | ✅ Done (done out of guide order, after 28/29) | Steps 17–19 |
| 31–38 | ✅ Done | Steps 20–21 |
| 39–44 | ✅ Done | Steps 22–25 |
| 45–50 | ✅ Done | Steps 26–27 |
| 51–54 | ✅ Done | Steps 28–31 |
| 55–59 | ⬜ Out of scope | — |

**Audit result:** all 59 exercises accounted for — Ex. 2–54 all complete
(24–27 done out of the guide's original order, noted throughout but not
silently dropped). Only Ex. 55–59 (namespace/import side-topics) remain,
deliberately out of scope unless the assignment requires them.
