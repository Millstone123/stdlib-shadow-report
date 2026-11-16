"""Load the local publisher profile."""
import json
from pathlib import Path


def load_profile():
    path = Path(__file__).resolve().parent.parent / "profile.json"
    return json.loads(path.read_text())
