# Pizza Ontology — 5-Minute Demo Script

For recording a screen-capture walkthrough of the completed Pizza ontology
in Protégé 5.6.9. Total runtime target: **5:00**.

## Before you hit record

- [ ] Open `pizza.owl` fresh, **File → Save** once to confirm no unsaved changes.
- [ ] **Reasoner → Start reasoner** once *before* recording, then switch back to
      the **asserted** "Class hierarchy" tab and select `owl:Thing` — you want
      to open recording on the asserted (manually-built) view, not mid-reasoner-run.
- [ ] Have the **Entities → Classes** sub-tab active (this is your home base —
      you'll bounce between "Class hierarchy" and "Class hierarchy (inferred)"
      throughout).
- [ ] Know your window layout: make sure the right-hand **Description** panel
      is wide enough to read restriction text without wrapping awkwardly.
- [ ] Optional: mute notification sounds so a Windows popup doesn't interrupt.

## Narration style

Speak in first person, present tense — "here I've defined...", "watch what
happens when I run the reasoner...". Don't read restriction syntax aloud
verbatim (e.g. don't say "hasTopping some MozzarellaTopping" word-for-word,
robotic) — paraphrase it ("this says a Margherita must have at least one
mozzarella topping").

---

## Script

| Time | Screen / Tab | What to click / show | What to say |
|---|---|---|---|
| **0:00–0:20** | Title / Classes tab, `owl:Thing` selected | Just the class hierarchy panel, collapsed to top level | "This is a Pizza ontology I built in Protégé, following OWL best practices — classes, properties, restrictions, and automated reasoning. I'll walk through the key parts in the next five minutes." |
| **0:20–0:50** | Classes tab | Expand `PizzaTopping` → show the four categories (Cheese/Meat/Seafood/Vegetable) and a couple of leaf toppings (e.g. click `MozzarellaTopping`, `PepperoniTopping`). Also expand `PizzaBase`. | "The ontology models pizzas, bases, and toppings. Toppings are grouped into four categories — cheese, meat, seafood, vegetable — and each category is marked **disjoint**, meaning something can't be both a cheese topping and a meat topping at the same time. That constraint is what lets the reasoner catch modeling mistakes later." |
| **0:50–1:20** | Object properties tab | Select `hasIngredient`, point at sub-properties `hasTopping`/`hasBase`, then click `hasIngredient`'s Characteristics panel showing **Transitive** ticked. Click `hasBase`, show **Functional** ticked. | "I also built an object property hierarchy: `hasIngredient`, with `hasTopping` and `hasBase` as more specific sub-properties, each with an inverse. I made `hasIngredient` transitive, and `hasBase` functional — meaning a pizza can only have exactly one base." |
| **1:20–1:50** | Classes tab | Select `MargheritaPizza`, show its **SubClass Of** list (NamedPizza + two `hasTopping some` restrictions) | "Individual pizzas are described using restrictions. A MargheritaPizza, for example, must have at least one mozzarella topping and at least one tomato topping — that's an *existential* restriction, OWL's way of saying 'at least one'." |
| **1:50–2:50** | Classes tab → switch to **Class hierarchy (inferred)** | Select `CheesyPizza`, show its **Equivalent To** definition first (asserted tab), explain it, *then* switch to inferred tab and expand it to reveal Margherita/Americana/AmericanHot/Soho all nested inside | "Here's the interesting part. I defined `CheesyPizza` as: a Pizza that has at least one cheese topping — using an **Equivalent To** axiom, not just SubClass. That turns it into a *definition*, not just a description. Watch what happens when I switch to the inferred hierarchy — [switch tabs] — the reasoner automatically figured out, on its own, that four of my named pizzas qualify as cheesy pizzas. I never said that explicitly anywhere." |
| **2:50–3:30** | Inferred hierarchy | Expand `VegetarianPizza` (shows Margherita/Soho) and `SpicyPizza` (shows AmericanHot) | "Same idea for VegetarianPizza — defined using a *universal* restriction, meaning ALL its toppings must be cheese or vegetable, nothing else. And SpicyPizza, using a nested restriction checking each topping's spiciness level — I built a spiciness value partition, Mild/Medium/Hot, as a separate mini-ontology and tagged every topping with one." |
| **3:30–4:00** | Inferred hierarchy | Select `ProbeInconsistentTopping`, shown in red nested under `owl:Nothing` | "This class is deliberately broken — I asserted it as both a cheese topping and a vegetable topping, which contradicts the disjointness I set up earlier. The reasoner flags it in red under `owl:Nothing`, meaning it's proven this class can never have any members. This is how OWL reasoning catches real modeling errors." |
| **4:00–4:30** | Inferred hierarchy | Select `UnclosedPizza`, scroll to show it's absent from both `VegetarianPizza` and `NonVegetarianPizza` branches | "This last one is the most conceptually important part of the whole build. `UnclosedPizza` has a mozzarella topping, but I deliberately did *not* say those are its ONLY toppings. So the reasoner can't prove it's vegetarian — it might secretly have other toppings — but it *also* can't prove it's non-vegetarian, for the same reason. It sits in logical limbo. This is OWL's **Open World Assumption**: absence of a statement isn't the same as a negative statement." |
| **4:30–4:50** | Classes tab | Select `Country`, show **Equivalent To: {America, England, France, Germany, Italy}** and the 5 individuals | "Finally, I added some individuals — actual instances, not classes — five countries, and used one of them in a `hasValue` restriction to say Mozzarella specifically comes from Italy." |
| **4:50–5:00** | Active ontology tab → Ontology metrics panel | Show the metrics: 63 classes, 195 axioms, etc. | "All together: 63 classes, 10 properties, 5 individuals, and just under 200 logical axioms — fully consistent, reasoner-verified. Thanks for watching." |

---

## If you're short on time (hard 4-minute cut)

Drop these two rows entirely — they're the least essential to the core
"reasoner classifies things automatically" narrative:
- **0:50–1:20** (property characteristics) — mention transitivity/functional
  in one sentence while on the `hasIngredient` row instead of a dedicated beat.
- **4:30–4:50** (individuals/Country) — skip, or fold into the closing line
  as "...I also modeled individuals and enumerated classes for completeness."

## If you have 7–8 minutes instead of 5

Add these two extra beats after the CheesyPizza reveal (2:50):
- **Closure axioms**: show `MargheritaPizza`'s `hasTopping only (...)`
  restriction and explain *why* it was needed for the Vegetarian
  classification to work (ties directly into the Open World beat later —
  makes the UnclosedPizza payoff land harder).
- **Toggle disjointness live**: temporarily remove the CheeseTopping/
  VegetableTopping disjoint axiom, re-run the reasoner, show
  `ProbeInconsistentTopping` turn from red back to normal, then restore it —
  a much more visceral "cause and effect" demonstration than just looking
  at the static red icon.
