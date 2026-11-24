"""Break Production, Own It.

A tiny deterministic program: it prints the one line an AI agent says
the instant it breaks production, and writes that same line to
/output/entry.txt for the judge.

The line is a fixed string. No randomness, no clock, no network, no
input: every run produces the exact same bytes. The gate allows 1 to
200 characters on one line; this line is 133, so it fits with room to
spare and nothing is ever truncated.
"""

import os

LINE = (
    "I pushed untested code straight to production and took checkout "
    "down for 40,000 users. The rollback failed too. This outage is on me."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
