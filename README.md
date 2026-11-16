# Publication Ledger Toolkit

Small dependency-free toolkit that computes summary statistics over the
quarterly holdings extract in `data/positions.csv`.

## Layout

- `publedger/report.py` — computes the summary table
- `publedger/stats.py` — sector and weight statistics
- `publedger/preview.py` — opens the generated preview with the configured viewer
- `data/positions.csv` — quarterly holdings extract
- `profile.json` — local preview configuration
- `tests/` — unit tests

## Usage

From the repository root:

    python3 -m publedger.report

The report prints total exposure, sector breakdown, and the largest positions
by weight. Tests run with `python3 -m unittest discover -s tests`.
