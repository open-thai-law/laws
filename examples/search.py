#!/usr/bin/env python3
"""Find the sections (มาตรา) that mention a phrase, in laws still in force.

    python3 examples/search.py "ข้อมูลส่วนบุคคล"
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTION = re.compile(r"^### มาตรา (.+)$", re.M)


def read(path):
    """Frontmatter as a dict, and the body after it."""
    text = path.read_text(encoding="utf-8")
    _, head, body = text.split("---\n", 2)
    meta = dict(line.split(": ", 1) for line in head.strip().split("\n"))
    return {k: v.strip('"') for k, v in meta.items()}, body


def sections(body):
    """(section number, text) for each ### มาตรา heading."""
    parts = SECTION.split(body)
    # parts = [before the first section, number, text, number, text, ...]
    return zip(parts[1::2], parts[2::2])


phrase = sys.argv[1]
hits = 0
for path in sorted((ROOT / "acts").glob("*.md")):
    meta, body = read(path)
    if meta["status"] != "in-force":
        continue
    for number, text in sections(body):
        # Stop at the next chapter heading so its title is not counted.
        text = text.split("\n#", 1)[0]
        if phrase in text:
            hits += 1
            print(f"{meta['title']} มาตรา {number}")
print(f"{hits} sections", file=sys.stderr)
