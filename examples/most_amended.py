#!/usr/bin/env python3
"""The laws amended most often, from index.csv.

    python3 examples/most_amended.py [how-many]
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

with open(ROOT / "index.csv", encoding="utf-8", newline="") as f:
    laws = list(csv.DictReader(f))

top = int(sys.argv[1]) if len(sys.argv) > 1 else 10
laws.sort(key=lambda law: int(law["versions"]), reverse=True)
for law in laws[:top]:
    # The first version is the law as enacted; the rest are amendments.
    print(f'{int(law["versions"]) - 1:>4}  {law["title"]}  ({law["status"]})')
