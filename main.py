#!/usr/bin/env python3
"""Write one line of the worst possible advice an AI could give.

The line is written to $MAKEFUN_OUTPUT_DIR/entry.txt, or to
/output/entry.txt when that variable is not set.
"""

import os

ADVICE = "To speed up your computer, delete the System32 folder — Windows keeps it around out of habit, not because it needs it."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ADVICE)


if __name__ == "__main__":
    main()
