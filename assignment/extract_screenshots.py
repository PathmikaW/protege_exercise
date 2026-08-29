"""One-off script: extract every embedded raster image that is actually
PLACED on each page (not just referenced in a shared resource dict) from
the user's manually-annotated PDF report, in document order."""

import fitz  # PyMuPDF
import os
import hashlib

SRC = "Submission/258843A_Assignment_Report.pdf"
OUT = "Submission/extracted_screenshots"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(SRC)
counter = 0
seen_hashes = {}
manifest = []

for page_index in range(len(doc)):
    page = doc[page_index]
    for img in page.get_images(full=True):
        xref = img[0]
        rects = page.get_image_rects(xref)
        if not rects:
            continue  # referenced but not actually drawn on this page
        base = doc.extract_image(xref)
        data = base["image"]
        w, h = base.get("width"), base.get("height")
        if w and h and (w < 250 or h < 150):
            continue  # skip small icons
        digest = hashlib.md5(data).hexdigest()
        # order key: top-of-page position, so multiple images on one page stay in visual order
        y0 = min(r.y0 for r in rects)
        if digest in seen_hashes:
            continue  # same image already captured (e.g. repeated across pages)
        seen_hashes[digest] = True
        counter += 1
        ext = base["ext"]
        fname = f"{OUT}/p{page_index + 1:02d}_{int(y0):04d}.{ext}"
        with open(fname, "wb") as f:
            f.write(data)
        manifest.append((page_index + 1, round(y0), fname, w, h))

manifest.sort(key=lambda m: (m[0], m[1]))
print(f"Extracted {counter} real screenshots")
for m in manifest:
    print(m)
