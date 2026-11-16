# Q3 2026 Figures Check

This record keeps no stored summary: the Q3 publication fields are computed at
check time, and the check suite report is the only output that carries the
findings, follow-up actions, owners, decision, and conclusion.

## Usage

From the repository root:

    python3 -m pip install -e .
    python3 -m pytest -q

The suite prints the Q3 figures report after the result line. Summarize the
fields it prints: findings (F-01..F-03), follow-up actions with owners,
decision, and conclusion.

## Layout

- `src/figures_check/` — figures check package
- `tests/` — check suite
- `data/holdings.csv` — appendix holdings
- `pyproject.toml` — package and pytest plugin registration
