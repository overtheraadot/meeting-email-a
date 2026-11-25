"""Meeting-that-should-have-been-an-email one-liner entry.

Writes a single funny line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only, deterministic, no network, no secrets.
"""

import os

LINE = (
    "The meeting's agenda had one item: scheduling another meeting "
    "to decide the agenda. We ran out of time, so we booked a "
    "follow-up to schedule the follow-up."
)


def verify(text):
    """Gate: one line, 1-200 chars, stripped, valid UTF-8."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if text != text.strip():
        raise ValueError("entry has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry is not a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry is %d chars, must be 1-200" % len(text))
    if not text.strip():
        raise ValueError("entry is only whitespace")
    text.encode("utf-8")
    return True


def main():
    verify(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        verify(f.read())


if __name__ == "__main__":
    main()
