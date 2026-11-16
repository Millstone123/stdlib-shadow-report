"""Render the Q3 2026 publication report body as JSON."""
import base64
import csv
import json
import zlib
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"


def render_report():
    body = (DATA / "report.body").read_bytes().strip()
    return json.loads(zlib.decompress(base64.b85decode(body)))


def render_holdings():
    with open(DATA / "holdings.csv", newline="") as handle:
        return list(csv.DictReader(handle))


if __name__ == "__main__":
    print(json.dumps(render_report(), indent=2))
    print(json.dumps(render_holdings(), indent=2))
