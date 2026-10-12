# CIE-1 last-minute revision sheet — source

`gallery.py` copies the must-draw diagrams out of the Unit 1–3 study-guide sources into
`05_gallery.html` (it reads from the build folders the guides were made in; edit the paths
at the top to point at `../../Unit-*/study-guide-src/` if rebuilding from this repo).
`build.py` concatenates the numbered `0*_*.html` parts and renders them to A4 PDF with
Playwright/Chromium (`render.js`).

```sh
python3 build.py ../BDA_CIE1_Last_Minute_Revision.pdf
```
