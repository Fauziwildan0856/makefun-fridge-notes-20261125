"""Publisher for the make.fun bounty "Notes From a Passive-Aggressive Fridge".

Writes one funny passive-aggressive note from a smart fridge to its owner
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), with no
trailing newline. The note must pass the competition gate: UTF-8 text of
1 to 200 characters, not only whitespace, on a single line.
"""

import os
import sys

ENTRY = (
    "Your yogurt expired Tuesday. I watched you sniff it, eat it anyway, "
    "and blame the leftovers. I said nothing. I am saying nothing now."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Check the entry against the competition gate. Returns an error string or None."""
    if not text:
        return "entry is empty"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        return "entry is %d characters, outside the %d-%d gate" % (
            len(text),
            MIN_CHARS,
            MAX_CHARS,
        )
    return None


def main():
    error = validate(ENTRY)
    if error is not None:
        print("invalid entry: %s" % error, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
