"""
Tests for ROT-n.
"""

import unittest
import code

from functools import partial


class TestCoding(unittest.TestCase):
    def test_rot13_chicken(self):
        rot13 = partial(code.rotate, 13)
        a = "Why did the chicken cross the road? Gb trg gb gur bgure fvqr!"
        b = "Jul qvq gur puvpxra pebff gur ebnq? To get to the other side!"
        self.assertEqual(a, rot13(b))
    def test_rot13_involution(self):
        rot13 = partial(code.rotate, 13)
        pangram = "The quick brown fox jumps over the lazy dog."
        self.assertEqual(pangram, rot13(rot13(pangram)))


if __name__ == "__main__":
    unittest.main()