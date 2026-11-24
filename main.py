"""The Most Honest Outage Line.

Writes one status page line, at most 160 characters, to entry.txt in the
output directory the grader provides (MAKEFUN_OUTPUT_DIR, default /output).

The line is fixed text: a deterministic program with no input, no clock,
no randomness and no network, so every run writes identical bytes.
"""

import os

LINE = (
    "Every service is down, including the checks I would use to find out "
    "why. I don't know the cause yet and I have no ETA. "
    "I will update this page first."
)


def main() -> None:
    # The sealed gate accepts UTF-8 text of 1 to 160 characters, not only
    # whitespace. Fail loudly here rather than handing the grader bad text.
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        raise ValueError("outage line is outside the 1-160 character gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
