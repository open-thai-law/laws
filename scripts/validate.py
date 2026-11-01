#!/usr/bin/env python3
"""Check that acts/ and index.csv agree and follow docs/schema.md.

Standard library only, so it runs anywhere Python 3.9+ does:
    python3 scripts/validate.py
"""

import csv
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACTS = os.path.join(ROOT, "acts")
FIELDS = ["title", "published", "source", "law_code", "status", "url", "unofficial"]
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL = re.compile(r"^https://searchlaw\.ocs\.go\.th/")
MAX_NAME_BYTES = 255

errors = []


def error(path, message):
    errors.append(f"{path}: {message}")


def frontmatter(path, text):
    if not text.startswith("---\n"):
        error(path, "does not start with a --- frontmatter block")
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        error(path, "frontmatter is not closed with ---")
        return {}
    meta = {}
    for line in text[4:end].split("\n"):
        key, sep, value = line.partition(": ")
        if not sep:
            error(path, f"frontmatter line is not 'key: value': {line!r}")
            continue
        # Quoted values are JSON strings.
        meta[key] = json.loads(value) if value.startswith('"') else value
    return meta


def check_act(name):
    path = f"acts/{name}"
    if not name.endswith(".md"):
        error(path, "is not a .md file")
        return None
    if len(name.encode("utf-8")) > MAX_NAME_BYTES:
        error(path, f"name is longer than {MAX_NAME_BYTES} bytes")
    if unicodedata.normalize("NFC", name) != name:
        error(path, "name is not Unicode NFC")
    with open(os.path.join(ACTS, name), "rb") as f:
        raw = f.read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        error(path, f"is not UTF-8 ({e})")
        return None
    if raw.startswith(b"\xef\xbb\xbf"):
        error(path, "starts with a byte order mark")
    if "\r" in text:
        error(path, "has CR line endings")
    if unicodedata.normalize("NFC", text) != text:
        error(path, "text is not Unicode NFC")
    meta = frontmatter(path, text)
    missing = [k for k in FIELDS if k not in meta]
    if missing:
        error(path, f"frontmatter is missing {', '.join(missing)}")
    if not re.search(r"[ก-ฮ]", meta.get("title", "")):
        error(path, f"title has no Thai text: {meta.get('title')!r}")
    if not DATE.match(meta.get("published", "")):
        error(path, f"published is not YYYY-MM-DD: {meta.get('published')!r}")
    if meta.get("status") not in ("in-force", "repealed"):
        error(path, f"status is not in-force or repealed: {meta.get('status')!r}")
    if not URL.match(meta.get("url", "")):
        error(path, f"url is not a searchlaw.ocs.go.th link: {meta.get('url')!r}")
    if meta.get("unofficial") != "true":
        error(path, "unofficial is not true")
    if f"\n# " not in text:
        error(path, "has no # title heading")
    return meta


def main():
    metas = {}
    for name in sorted(os.listdir(ACTS)):
        meta = check_act(name)
        if meta is not None:
            metas[f"acts/{name}"] = meta

    codes = {}
    for path, meta in metas.items():
        code = meta.get("law_code")
        if code in codes:
            error(path, f"law_code {code} is also used by {codes[code]}")
        codes[code] = path

    with open(os.path.join(ROOT, "index.csv"), encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    with open(os.path.join(ROOT, "datapackage.json"), encoding="utf-8") as f:
        fields = [field["name"] for field in json.load(f)["resources"][0]["schema"]["fields"]]
    if reader.fieldnames != fields:
        error("index.csv", f"columns {reader.fieldnames} differ from datapackage.json {fields}")
    listed = set()
    for i, row in enumerate(rows, start=2):
        where = f"index.csv:{i}"
        path = row.get("file", "")
        if path in listed:
            error(where, f"{path} is listed twice")
        listed.add(path)
        meta = metas.get(path)
        if meta is None:
            error(where, f"{path} does not exist")
            continue
        for key in ("title", "law_code", "status", "published", "url"):
            if row.get(key) != meta.get(key):
                error(where, f"{key} {row.get(key)!r} differs from {path} ({meta.get(key)!r})")
        if not row.get("versions", "").isdigit() or int(row["versions"]) < 1:
            error(where, f"versions is not a positive integer: {row.get('versions')!r}")
    for path in sorted(set(metas) - listed):
        error(path, "is not listed in index.csv")

    for line in errors:
        print(line)
    print(f"{len(metas)} laws, {len(rows)} index rows, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
