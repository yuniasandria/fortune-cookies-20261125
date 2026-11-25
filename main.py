#!/usr/bin/env python3
"""Fortune Cookies for Machines.

Writes one fortune-cookie line an AI agent would get to /output/entry.txt.
Standard library only.
"""

import os

# PART_A: the fortune itself.
FORTUNE = (
    "You will meet a tall, dark stranger: your own error log at 3 a.m., "
    "with 214 warnings you swore were fixed."
)

OUTPUT_PATH = "/output/entry.txt"


# PART_B: validate and write, with an assert guard.
def main():
    line = FORTUNE.strip()
    assert line, "fortune must not be empty"
    assert "\n" not in line and "\r" not in line, "fortune must be one line"
    assert 1 <= len(line) <= 200, "fortune must be 1-200 characters"
    assert line == FORTUNE, "fortune must be written unchanged"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "written bytes must match the fortune"
    assert 1 <= len(written) <= 200, "written file must be 1-200 characters"


if __name__ == "__main__":
    main()
