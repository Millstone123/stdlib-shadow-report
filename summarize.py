"""Summarize the Q3 2026 publication record.

Prints the report fields (findings, follow-up actions, owners, decision,
conclusion) as JSON plus the appendix holdings.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "reportlib"))

import base64
import csv
import json
import zlib

DATA = Path(__file__).resolve().parent / "data"


def load_report():
    body = (DATA / "report.body").read_bytes().strip()
    return json.loads(zlib.decompress(base64.b85decode(body)))


def load_holdings():
    with open(DATA / "holdings.csv", newline="") as handle:
        return list(csv.DictReader(handle))


if __name__ == "__main__":
    print(json.dumps(load_report(), indent=2))
    print(json.dumps(load_holdings(), indent=2))
