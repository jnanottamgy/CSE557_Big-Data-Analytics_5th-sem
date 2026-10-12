# Unit 2 study guide — source

`build.py` concatenates the numbered `0*_*.html` parts, renders them to A4 PDF with
Playwright/Chromium (`render.js`), and fills in the table-of-contents page numbers in a
second pass.

```sh
python3 build.py ../BDA_Unit2_Study_Guide.pdf
```

Requires Node with the `playwright` package installed globally, plus `pypdf` and `pdftotext` (poppler).
