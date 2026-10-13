# CIE-1 exam reader — source

A single read-through PDF for Units 1–3 (CIE-1 part). Prose lives in the numbered
`0*_*.html` parts; `{{fig:key|caption}}` placeholders are filled by `figs.py`, which copies the
SVG diagrams out of the unit study-guide sources (edit the `U1`/`U2`/`U3` paths at the top to
point at `../../Unit-*/study-guide-src/` when rebuilding from this repo). `build.py` assembles
the parts, fills in the contents page numbers and renders A4 PDF via Playwright (`render.js`).

```sh
python3 build.py ../BDA_CIE1_Exam_Reader.pdf
```
