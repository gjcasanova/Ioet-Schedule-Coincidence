"""
Settings module.

This module contains some constant values to get applied in the solution.
"""

# Standard library
from pathlib import Path

# Paths
PACKAGE_DIR = Path(__file__).resolve(strict=True)
DATA_PATH = PACKAGE_DIR.parent / 'data.txt'
