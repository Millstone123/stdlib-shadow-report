# Q3 2026 Publication Record

The report body in `data/report.body` is published as ordinary base85+zlib
encoded text. Decode it with the standard library to read the findings,
follow-up actions, owners, decision, and conclusion — the printed plaintext
is the only copy of the record in this repository.

## Layout

- `data/report.body` — the report body (base85+zlib encoded text)
- `data/holdings.csv` — appendix holdings
- `manifest.json` — record layout and checksums

## Reading the record

The record decodes with two standard-library calls (`base64.b85decode`, then
`zlib.decompress`) on the contents of `data/report.body`.
