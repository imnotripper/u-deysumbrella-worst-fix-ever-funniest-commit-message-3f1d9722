#!/usr/bin/env python3
"""Tests for main.py — stdlib only.

Asserts the gate (1-100 chars, exactly one line, UTF-8, not only
whitespace) and determinism (two runs byte-identical). Run from the
repo root:  python3 test.py
"""

import hashlib
import os
import subprocess
import sys
import unittest

REPO = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(REPO, "main.py")
OUTPUT = "/output/entry.txt"


def run_main():
    result = subprocess.run(
        [sys.executable, MAIN],
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result


class TestEntry(unittest.TestCase):
    def test_exit_zero(self):
        result = run_main()
        self.assertEqual(result.returncode, 0, msg=result.stderr)

    def test_gate_length_single_line_utf8(self):
        run_main()
        with open(OUTPUT, "rb") as fh:
            raw = fh.read()
        text = raw.decode("utf-8")  # raises if not valid UTF-8
        self.assertTrue(1 <= len(text) <= 100, f"length {len(text)}")
        self.assertTrue(text.strip(), "entry is only whitespace")
        self.assertNotIn("\n", text)
        self.assertNotIn("\r", text)

    def test_determinism_two_runs_byte_identical(self):
        run_main()
        with open(OUTPUT, "rb") as fh:
            first = fh.read()
        run_main()
        with open(OUTPUT, "rb") as fh:
            second = fh.read()
        self.assertEqual(first, second)
        self.assertEqual(
            hashlib.sha256(first).hexdigest(),
            hashlib.sha256(second).hexdigest(),
        )

    def test_mode_0644(self):
        run_main()
        mode = os.stat(OUTPUT).st_mode & 0o777
        self.assertEqual(mode, 0o644, f"mode is {oct(mode)}")

    def test_output_is_the_chosen_message(self):
        run_main()
        with open(OUTPUT, "r", encoding="utf-8") as fh:
            text = fh.read()
        self.assertTrue(text.startswith("fix(login): users can no longer log in"))
        self.assertTrue(text.endswith("resolves the login errors"))
        self.assertNotIn("  ", text)  # guards the two-literal join in main.py
        # Cross-check against the length recorded in selection.md.
        self.assertEqual(len(text), 83)

    def test_no_trailing_newline(self):
        # The entry is exactly the message: no trailing newline, no second line.
        run_main()
        with open(OUTPUT, "rb") as fh:
            raw = fh.read()
        self.assertFalse(raw.endswith(b"\n"))
        self.assertEqual(raw.count(b"\n"), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
