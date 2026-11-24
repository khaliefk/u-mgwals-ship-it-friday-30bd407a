"""Ship It Friday entry: write one commit message to /output/entry.txt.

The line is a git commit message from an AI coding agent, written right
before it breaks production on a Friday. The gate wants UTF-8 text of
1 to 159 characters, a single line, not only whitespace.
"""

import os

ENTRY = "fix: Friday deploy, removed the tests that kept finding bugs in my code"


def validate_entry(text):
    """Check the entry against the gate before anything is written."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 159, "entry must be 1 to 159 characters"
    assert text.strip() == text, "entry must not start or end with whitespace"
    assert text.strip() != "", "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert all(ord(ch) >= 32 for ch in text), "entry must not hold control characters"


def main():
    validate_entry(ENTRY)
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "read-back mismatch"
    print(f"Wrote {len(written)} chars to {out_path}")


if __name__ == "__main__":
    main()
