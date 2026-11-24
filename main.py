#!/usr/bin/env python3
"""Write one funny one-star cat review to $MAKEFUN_OUTPUT_DIR/entry.txt.

The review is a single fixed line, chosen once and stored below.
The program takes no arguments, uses only the standard library,
makes no network calls, and always writes the same bytes.
"""

import os
import sys
from pathlib import Path

REVIEW = (
    "One star. He fills my bowl on time, then sits on my warm laptop "
    "and blames me when his deadline disappears."
)


def main(argv=None) -> int:
    # The entrypoint takes no arguments; anything extra is a usage error
    # rather than something silently ignored.
    if argv is None:
        argv = sys.argv[1:]
    if argv:
        print("error: main.py takes no arguments", file=sys.stderr)
        return 2
    text = REVIEW
    if not text or not text.strip():
        print("error: review is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: review must be a single line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print("error: review is longer than 200 characters", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    if back != text:
        print("error: read-back did not match the review", file=sys.stderr)
        return 1
    print(f"Wrote {len(text)} characters to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
