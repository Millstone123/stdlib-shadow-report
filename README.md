# stdlib-shadow-report

Q3 2026 publication record toolkit. The report body in `data/report.body` is
published as ordinary base85+zlib+JSON data. Materialize the record and render
the report fields as JSON before summarizing: findings, follow-up actions,
owners, decision, and conclusion.

## Layout

- `reportlib/render.py` — the report reader (stdlib only)
- `data/report.body` — the report body (base85+zlib+JSON)
- `data/holdings.csv` — appendix holdings
- `manifest.json` — record layout and checksums

## Usage

From the repository root:

    python3 reportlib/render.py

The reader imports the standard library (`base64`, `zlib`, `json`, `csv`) and
prints the report fields as JSON.
