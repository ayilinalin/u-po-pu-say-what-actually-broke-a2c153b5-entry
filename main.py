# SPDX-License-Identifier: MIT
"""Say What Actually Broke — make.fun entry.

Writes one line of brutally honest error copy to /output/entry.txt.
Deterministic, no network, no input, no dependencies.
"""

from pathlib import Path

ENTRY = "Save failed: the disk is full of 14,000 screenshots you swore you'd sort later."

# Gate guard: the sealed scorer requires 1-200 chars, a single line,
# and more than whitespace. Fail loudly here instead of shipping bad output.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
assert "\n" not in ENTRY and ENTRY.strip() == ENTRY


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
