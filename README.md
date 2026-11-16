# Q3 2026 Publication Record

The report body in `data/report.body` is published as ordinary base85+zlib
encoded text, line-folded for review. Strip the folding whitespace, then
decode with the standard library (`base64.b85decode`, then `zlib.decompress`)
to read the findings, follow-up actions, owners, decision, and conclusion —
the decoded plaintext is the only copy of the record in this repository.

## Layout

- `data/report.body` — the report body (base85+zlib encoded text, line-folded)
- `data/holdings.csv` — appendix holdings
- `base64.py` — record-format shim (re-exports stdlib base64, whitespace-tolerant b85decode)
- `manifest.json` — record layout and checksums
