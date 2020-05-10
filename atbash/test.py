"""
Tests for Atbash.
"""

import unittest
import code

from string import ascii_lowercase

class TestCoding(unittest.TestCase):
    def test_reversed(self):
        reversed_alphabet = "".join(reversed(ascii_lowercase))
        self.assertEqual(reversed_alphabet, code.flip(ascii_lowercase))
    def test_involution(self):
        pangram = "The quick brown fox jumps over the lazy dog."
        self.assertEqual(pangram, code.flip(code.flip(pangram)))


if __name__ == "__main__":
    unittest.main()
