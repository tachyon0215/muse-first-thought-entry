#!/usr/bin/env python3
"""Write a one-word entry to /output/entry.txt."""
import os
from pathlib import Path

LINE = "Snickerdoodle"
TEXT = LINE + "\n"

def validate(text: str) -> None:
    if not (1 <= len(text) <= 24):
        raise ValueError(f"entry must be 1-24 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    body = text[:-1] if text.endswith("\n") else text
    if len(body.split()) != 1 or " " in body:
        raise ValueError("entry must be exactly one word")

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    validate(TEXT)
    payload = TEXT.encode("utf-8")
    target = out_dir / "entry.txt"
    target.write_bytes(payload)
    if target.read_bytes() != payload:
        raise IOError("read-back mismatch on entry.txt")

if __name__ == "__main__":
    main()
