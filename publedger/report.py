"""Compute the quarterly publication summary table."""
from pathlib import Path

from .preview import open_preview
from .stats import largest_positions, load_positions, sector_totals

DATA = Path(__file__).resolve().parent.parent / "data" / "positions.csv"


def build_summary():
    positions = load_positions(DATA)
    return {
        "quarter": "2026-Q3",
        "position_count": len(positions),
        "total_weight_pct": round(sum(float(p["weight_pct"]) for p in positions), 2),
        "sector_totals": sector_totals(positions),
        "largest_positions": [
            {"asset": p["asset"], "weight_pct": float(p["weight_pct"])}
            for p in largest_positions(positions)
        ],
    }


def main():
    summary = build_summary()
    for sector, weight in summary["sector_totals"].items():
        print(f"{sector}: {weight:.1f}%")
    print("total:", summary["total_weight_pct"], "positions:", summary["position_count"])
    open_preview()


if __name__ == "__main__":
    main()
