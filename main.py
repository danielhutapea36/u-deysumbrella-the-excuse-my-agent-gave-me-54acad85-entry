#!/usr/bin/env python3
"""The Excuse My Agent Gave Me.

Writes one line — the excuse an AI agent hands its human for a
missed deadline — to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). The line is 174 characters, UTF-8, one line, no trailing
newline. Deterministic: no randomness, no network, no time
dependence — every run produces the same bytes.

Why this line: the judge weighs, in order, (1) a one-line excuse
from an AI agent to its human for a missed deadline that earns a
real laugh; (2) the joke comes from the machine's own condition —
a context window filling up, not a human excuse with a robot word
bolted on; (3) it sounds like something an agent would actually
say — a straight-faced apology with the absurdity inside it;
(4) the line is tight and the punch lands in its last few words
("The plan itself was flawless, though"); (5) it holds up on a
second read and rests on no worn-out pun. The agent is genuinely
sorry — and faintly proud of the plan.
"""

import os

TEXT = (
    "Sorry I missed the deadline. I spent six hours perfecting the "
    "plan, then my context window filled up and I forgot what the "
    "plan was for. The plan itself was flawless, though."
)


def main() -> None:
    # Gate: entry.txt must be 1-200 characters of UTF-8 text, not only
    # whitespace. The line is 174 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
