#!/usr/bin/env python3
# One-line out-of-office reply for the make.fun bounty (hamsyh).
"""Write the funniest one-line out-of-office reply to entry.txt.

The line is a single sentence, 97 characters, and it is written exactly
as-is — no trailing newline, no extra wrapping.
"""

from os import environ
from pathlib import Path

REPLY = (
    "I\u2019m away until Monday \u2014 your email has been forwarded to "
    "Future Me, who is already annoyed by it."
)


def emit_reply() -> Path:
    """Save the reply into the harness output directory."""
    folder = Path(environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / "entry.txt"
    destination.write_text(REPLY, encoding="utf-8")
    return destination


if __name__ == "__main__":  # executed directly by the harness
    emit_reply()
