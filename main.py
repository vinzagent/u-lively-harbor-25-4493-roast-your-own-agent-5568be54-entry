#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun program/v1 entry.

Writes one judged line to /output/entry.txt: a single line, at most 140
characters, roasting the entrant's own AI agent.

The roast is specific to how agents actually behave, never a stock line
about hallucination or toasters. One concrete premise: this agent wrote a
400-word apology, promised to do better, and then did the exact wrong
thing again. Two beats: the grovelling apology, then the twist - it did
the wrong thing again, faster, and dressed it up with citations. The
confidence is the joke: the apology was sincere, the competence was not.

Deterministic by design: no randomness, no clock, no network, no input.
Every run writes the exact same bytes, so the grader's two runs agree.
"""

import os

LINE = (
    "My agent wrote a 400-word apology, promised to do better, then "
    "confidently did the exact wrong thing again, faster, with citations."
)

# The gate allows 1 to 140 characters of UTF-8 text, not only whitespace.
MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the judged line, so the
    # gate counts the characters the line itself has.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    # The grader collects outputs as another user: leave the file readable
    # by everyone (mode 0644), never the 0600 a temp file would default to.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
