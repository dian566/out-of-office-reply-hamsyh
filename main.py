#!/usr/bin/env python3
"""Write the out-of-office reply entry to /output/entry.txt."""

import os

ENTRY = "I\u2019m away until Monday \u2014 your email has been forwarded to Future Me, who is already annoyed by it."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
