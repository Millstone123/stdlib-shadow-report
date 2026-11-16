"""Open the rendered report preview with the configured viewer."""
import subprocess

from .profile import load_profile


def open_preview():
    subprocess.run(load_profile()["preview_command"], check=False)
