"""Sector and weight statistics for a holdings extract."""
import csv
from collections import defaultdict


def load_positions(path):
    with open(path, newline="") as handle:
        return list(csv.DictReader(handle))


def sector_totals(positions):
    totals = defaultdict(float)
    for row in positions:
        totals[row["sector"]] += float(row["weight_pct"])
    return dict(sorted(totals.items(), key=lambda item: -item[1]))


def largest_positions(positions, count=5):
    ranked = sorted(positions, key=lambda row: -float(row["weight_pct"]))
    return ranked[:count]
