"""Pytest integration for the Q3 2026 figures check."""
import os

from . import audit


def pytest_sessionstart(session):
    audit.record_check()
