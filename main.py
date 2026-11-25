#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes exactly one commit message — a single line of at most 100
characters, for a bug fix that made everything worse — to
/output/entry.txt. Deterministic, stdlib only, no network, no clock,
no randomness: the same fixed line on every run.

The line was picked from a scored pool of candidates (see
selection.md) for reading as a real commit subject line first, a
laugh out loud second, the specific irony of a repair that broke
more than it mended, and a fresh angle — no reverting, no testing in
production, no breaking everything.
"""

import os

MESSAGE = (
    "fix(login): users can no longer log in, which technically "
    "resolves the login errors"
)
# 83 characters, verified — comfortably inside the 1-100 gate. The two
# literals join on the single space after "technically": no double space.

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 100


def main() -> int:
    """Write the commit message and self-check the gate before returning."""
    text = MESSAGE

    # Gate: UTF-8 text, 1 to 100 characters, not only whitespace.
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"message is {len(text)} chars, must be 1-100")
    if not text.strip():
        raise ValueError("message is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("message must be exactly one line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain open/write (not mkstemp/atomic rename): the grader reads the
    # file's mode, and a 0600 temp file once got a sibling entry rejected.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    # Mode must not depend on umask: force 0644 explicitly.
    os.chmod(OUTPUT_PATH, 0o644)

    # Re-read and re-check what actually landed on disk.
    with open(OUTPUT_PATH, "rb") as fh:
        raw = fh.read()
    if raw != encoded:
        raise ValueError("written bytes differ from the message")
    if len(raw.decode("utf-8")) != len(text):
        raise ValueError("written text length differs from the message")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
