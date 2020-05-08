"""
Tests for A1Z26.
"""

import unittest
import code


class TestDecoding(unittest.TestCase):
    def test_steven(self):
        self.assertEqual(code.decode("19 20 5 22 5 14"), "steven")


if __name__ == "__main__":
    unittest.main()