#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert — make.fun entry.

Writes one satirical sentence roasting lawmakers who would regulate AI,
crypto or the internet but cannot convert a file to PDF, to
/output/entry.txt. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "Congress can draft 400 pages of law telling your AI what it may not do, "
    "but ask them to turn the bill into a PDF and the most powerful committee "
    "in Washington is one intern away from a paper jam."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
