#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun text entry.

Writes one line (1-200 chars) to /output/entry.txt: the excuse an AI
agent hands its human for a missed deadline.
"""
import os
import sys

ENTRY = "I finished the work before your deadline, then a context compaction summarized my memory, and the summary kept the apology and dropped the work."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} out of range 1-200", file=sys.stderr)
        return 1
    # Gate requires UTF-8 text, not only whitespace: verify before writing.
    text.encode("utf-8")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
