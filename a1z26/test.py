"""
Tests for A1Z26.
"""

import unittest
import code

from string import ascii_lowercase


alphabet_numbers = " ".join(map(str, range(1, 27)))

class TestEncoding(unittest.TestCase):
    def test_alphabet(self):
        self.assertEqual(alphabet_numbers, code.encode(ascii_lowercase))

class TestDecoding(unittest.TestCase):
    def test_alphabet(self):
        self.assertEqual(ascii_lowercase, code.decode(alphabet_numbers))
    def test_steven(self):
        self.assertEqual(code.decode("19 20 5 22 5 14"), "steven")


if __name__ == "__main__":
    unittest.main()