"""Check suite for the Q3 2026 publication record."""
from figures_check import audit


def test_record_check_runs():
    audit.record_check()
