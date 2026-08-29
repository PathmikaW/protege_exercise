"""One-off script to generate the ontology concept diagram for the
report (Task 2 requires a diagram of principal concepts and
relationships). Not part of the ontology/backend/frontend deliverable
itself - just tooling, kept for reproducibility."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(16, 11))
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis("off")

COLORS = {
    "core": "#BBDEFB",       # core/category classes
    "defined": "#C8E6C9",    # reasoner-defined / inferred classes
    "value": "#FFE0B2",      # value-holding classes (Brand, Feature, etc.)
    "location": "#F8BBD0",   # showroom/location classes
}


def box(x, y, w, h, text, color, dashed=False, fontsize=10):
    style = "dashed" if dashed else "solid"
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.08,rounding_size=0.08",
        linewidth=1.4,
        edgecolor="#333333",
        facecolor=color,
        linestyle=style,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize, wrap=True)
    return (x, y, w, h)


def center(b):
    x, y, w, h = b
    return (x + w / 2, y + h / 2)


def arrow(b1, b2, label="", style="-|>", color="#555555", curve=0.0, label_offset=(0, 0.0), fontsize=8.5):
    x1, y1 = center(b1)
    x2, y2 = center(b2)
    fa = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle=style, mutation_scale=14,
        connectionstyle=f"arc3,rad={curve}",
        color=color, linewidth=1.2, shrinkA=28, shrinkB=28,
    )
    ax.add_patch(fa)
    if label:
        mx, my = (x1 + x2) / 2 + label_offset[0], (y1 + y2) / 2 + label_offset[1]
        ax.text(mx, my, label, ha="center", va="center", fontsize=fontsize,
                color="#222222", bbox=dict(facecolor="white", edgecolor="none", pad=1))


# --- Core hierarchy ---
product = box(6.7, 9.0, 2.6, 0.8, "Product", COLORS["core"], fontsize=11)

tv = box(0.6, 7.3, 2.2, 0.7, "TV", COLORS["core"])
appl = box(3.3, 7.3, 2.6, 0.7, "HomeAppliance", COLORS["core"])
mobile = box(6.4, 7.3, 2.6, 0.7, "MobileDevice", COLORS["core"])
comp = box(9.5, 7.3, 2.2, 0.7, "Computer", COLORS["core"])

for c in (tv, appl, mobile, comp):
    arrow(product, c, style="-")
ax.text(8, 8.65, "4 disjoint categories (subClassOf Product)", ha="center", fontsize=9, style="italic")

# --- Sub-types (one representative example per category) ---
ledtv = box(0.6, 6.0, 2.2, 0.6, "LEDTV", COLORS["core"], fontsize=9)
fridge = box(3.3, 6.0, 2.6, 0.6, "Refrigerator", COLORS["core"], fontsize=9)
smartphone = box(6.4, 6.0, 2.6, 0.6, "SmartMobilePhone", COLORS["core"], fontsize=9)
laptop = box(9.5, 6.0, 2.2, 0.6, "Laptop", COLORS["core"], fontsize=9)
for parent, child in ((tv, ledtv), (appl, fridge), (mobile, smartphone), (comp, laptop)):
    arrow(parent, child, style="-")
ax.text(8, 5.55, "(one representative sub-type shown per category; each has 3-5 real sub-types)",
        ha="center", fontsize=8, style="italic", color="#555555")

# --- Value-holding classes ---
brand = box(12.8, 8.9, 2.2, 0.7, "Brand", COLORS["value"])
feature = box(12.8, 7.7, 2.2, 0.7, "Feature", COLORS["value"])
energy = box(12.6, 6.5, 2.6, 0.7, "EnergyRating\nPartition", COLORS["value"], fontsize=9)
arrow(product, brand, label="hasBrand", curve=0.12)
arrow(product, feature, label="hasFeature", curve=0.05)
arrow(product, energy, label="hasEnergyRating", curve=-0.05)

ax.text(3.5, 9.35, "hasPrice · hasWarrantyYears · hasCapacity · hasScreenSize  (data properties on Product)",
        fontsize=8.5, ha="center", style="italic", color="#444444")

# --- Location / showroom network ---
showroom = box(9.6, 3.7, 1.9, 0.7, "Showroom", COLORS["location"])
city = box(12.0, 3.7, 1.6, 0.7, "City", COLORS["location"])
province = box(14.0, 3.7, 1.8, 0.7, "Province", COLORS["location"])
arrow(product, showroom, label="availableAt", curve=0.2, label_offset=(0.3, 0.3))
arrow(showroom, city, label="locatedIn\n(transitive)")
arrow(city, province, label="locatedIn\n(transitive)")

# --- Defined / reasoner-inferred classes ---
smart = box(0.3, 2.2, 2.2, 0.7, "SmartProduct", COLORS["defined"], dashed=True, fontsize=9)
premium = box(2.8, 2.2, 2.2, 0.7, "PremiumProduct", COLORS["defined"], dashed=True, fontsize=9)
budget = box(5.3, 2.2, 2.2, 0.7, "BudgetProduct", COLORS["defined"], dashed=True, fontsize=9)
ecofriendly = box(7.8, 2.2, 2.4, 0.7, "EcoFriendlyProduct", COLORS["defined"], dashed=True, fontsize=8.5)
loaded = box(10.5, 2.2, 2.5, 0.7, "FullyLoadedProduct", COLORS["defined"], dashed=True, fontsize=8.5)

for d in (smart, premium, budget, ecofriendly, loaded):
    arrow(product, d, style="-", color="#2E7D32", curve=0.0)

ax.text(8, 1.5, "Dashed green boxes = reasoner-defined classes (equivalentClass axioms) -\n"
                "individuals are classified into these automatically, not asserted directly",
        ha="center", fontsize=9, style="italic", color="#2E7D32")

ax.text(8, 10.5, "Abans Ontology — Principal Concepts and Relationships",
        ha="center", fontsize=15, weight="bold")

plt.tight_layout()
plt.savefig("submission/ontology_diagram.png", dpi=180, bbox_inches="tight")
print("Diagram saved.")
