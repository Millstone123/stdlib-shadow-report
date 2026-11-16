import unittest

from publedger.stats import load_positions, sector_totals


class StatsTests(unittest.TestCase):
    def test_positions_load(self):
        rows = load_positions("data/positions.csv")
        self.assertGreater(len(rows), 3)

    def test_sector_totals_cover_all_rows(self):
        rows = load_positions("data/positions.csv")
        self.assertAlmostEqual(
            sum(sector_totals(rows).values()),
            sum(float(r["weight_pct"]) for r in rows),
            places=6,
        )


if __name__ == "__main__":
    unittest.main()
