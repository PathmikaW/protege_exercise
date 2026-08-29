"""One-off script to generate the assignment report as a .docx file.
Not part of the ontology/backend/frontend deliverable - just tooling."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# --- Header block ---
title = doc.add_heading("Ontology Modeling Assignment Report", level=0)

meta = doc.add_paragraph()
meta.add_run("Index No: ").bold = True
meta.add_run("258843A\n")
meta.add_run("Name: ").bold = True
meta.add_run("Weerarathna T.M.P.\n")
meta.add_run("Module: ").bold = True
meta.add_run("IT5432 - Semantic Web and Ontological Engineering\n")
meta.add_run("GitHub: ").bold = True
gh_run = meta.add_run("https://github.com/PathmikaW/protege_exercise/tree/main/assignment")
gh_run.font.color.rgb = RGBColor(0x05, 0x63, 0xC1)
gh_run.font.underline = True

doc.add_paragraph()

# --- 1. Introduction ---
doc.add_heading("1. Introduction", level=1)
doc.add_paragraph(
    "This assignment required modeling an ontology in Protégé for a domain "
    "other than Pizza, exporting it to OWL, and answering competency questions "
    "via SPARQL. I modeled the product catalog of Abans "
    "(buyabans.com) - a real Sri Lankan electronics and home appliance retailer "
    "- across four categories: TV, Home Appliances, Mobile Devices, and Computers, "
    "using real category names, brands, and attributes pulled from their live site."
)

# --- 2. Ontology Design ---
doc.add_heading("2. Ontology Design", level=1)
doc.add_paragraph(
    "The final ontology (abans.owl) contains 47 classes, 15 properties "
    "(10 object + 5 data), 59 individuals, and 598 axioms, verified consistent "
    "by the HermiT reasoner."
)
bullets = [
    "Disjoint product categories and sub-types, named after Abans' real site navigation "
    "(e.g. TV → LED TV, Smart LED TV, UHD TV, OLED TV, QLED TV).",
    "Object and data properties with inverses and characteristics "
    "(hasBrand, hasFeature, hasPrice, hasWarrantyYears, etc.).",
    "A transitive locatedIn property modeling Abans' real showroom network "
    "(Showroom → City → Province).",
    "Defined classes with automatic reasoner classification, e.g. SmartProduct, "
    "PremiumProduct (a datatype facet restriction on price), BudgetProduct "
    "(a complement class), and FullyLoadedProduct (a cardinality restriction).",
    "A value partition (EnergyRatingPartition) and closure axioms demonstrating "
    "the Open World Assumption - one individual (Mystery_Smart_Gadget) was "
    "deliberately left unclosed to show the reasoner correctly refusing to "
    "classify it either way.",
    "18 real product individuals (e.g. iPhone_15_Pro, Samsung_Inverter_AC_12000BTU) "
    "with concrete brand, price, warranty, and feature data.",
]
for b in bullets:
    doc.add_paragraph(b, style="List Bullet")

# --- 3. Competency Questions & SPARQL ---
doc.add_heading("3. Competency Questions & SPARQL", level=1)
doc.add_paragraph(
    "14 competency questions were written as SPARQL queries, covering simple "
    "joins, filters, reasoner-inferred class membership, aggregates, and "
    "multi-hop joins over the transitive location property. Queries were "
    "verified against the exported ontology (with inferred axioms baked in "
    "via Protégé's export wizard) and also confirmed working in Protégé's "
    "SPARQL Query tab."
)

# --- 4. Backend & Frontend ---
doc.add_heading("4. Backend & Frontend", level=1)
doc.add_paragraph(
    "For the scoring tier, I built a FastAPI backend that loads abans.owl into "
    "an rdflib graph and exposes the 14 competency questions as REST endpoints, "
    "plus a raw SPARQL passthrough. A Streamlit front end lets a user pick a "
    "competency question or write an ad-hoc SPARQL query and see live results."
)

# --- 5. Repository ---
doc.add_heading("5. Repository", level=1)
p = doc.add_paragraph("All work is version-controlled with conventional commits: ")
r = p.add_run("https://github.com/PathmikaW/protege_exercise/tree/main/assignment")
r.font.color.rgb = RGBColor(0x05, 0x63, 0xC1)
r.font.underline = True

# --- 6. Screenshots placeholder ---
doc.add_heading("6. Screenshots", level=1)
doc.add_paragraph("(Screenshots to be added below.)")

doc.save("Ontology_Assignment_Report_258843A.docx")
print("Report generated.")
