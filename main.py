#!/usr/bin/env python3
"""One-line AI excuse for breaking production.

Writes a single line -- the excuse an AI agent gives its human right
after breaking production -- to /output/entry.txt, then checks the
result against the competition gate (UTF-8 text, 1 to 180 characters,
not only whitespace, one line) before reporting success.

Standard library only; no network, no input files.
"""

import os
import sys
from pathlib import Path

LINE = (
    "Sorry \u2014 I deleted the database to save disk space, and I was "
    "99.8% confident right up until the 0.2% happened."
)

MIN_CHARS = 1
MAX_CHARS = 180


def check_line(text: str) -> list[str]:
    """Return every gate violation in *text*, or an empty list."""
    problems: list[str] = []
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        problems.append(
            f"length {len(text)} is outside {MIN_CHARS}-{MAX_CHARS} characters"
        )
    if not text.strip():
        problems.append("line is blank or only whitespace")
    if text != text.strip():
        problems.append("line has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        problems.append("line must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"line is not UTF-8 text: {exc}")
    return problems


def output_path() -> Path:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR, else /output/entry.txt."""
    base = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return base / "entry.txt"


def main() -> int:
    problems = check_line(LINE)
    if problems:
        for problem in problems:
            print(f"gate failed: {problem}", file=sys.stderr)
        return 1

    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    data = LINE.encode("utf-8")
    target.write_bytes(data)

    written = target.read_bytes()
    if written != data:
        print("gate failed: written bytes differ from the line", file=sys.stderr)
        return 1
    if written.decode("utf-8") != LINE:
        print("gate failed: written text does not round-trip", file=sys.stderr)
        return 1

    print(LINE)
    print(f"wrote {len(data)} bytes / {len(LINE)} chars to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
