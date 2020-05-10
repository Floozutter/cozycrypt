"""
Tests for ROT-n.
"""

import unittest
import code

from functools import partial


rot13 = partial(code.rotate, 13)

class TestCoding(unittest.TestCase):
    def test_rot13_chicken(self):
        a = "Why did the chicken cross the road? Gb trg gb gur bgure fvqr!"
        b = "Jul qvq gur puvpxra pebff gur ebnq? To get to the other side!"
        self.assertEqual(a, rot13(b))
    def test_rot13_involution(self):
        pangram = "The quick brown fox jumps over the lazy dog."
        self.assertEqual(pangram, rot13(rot13(pangram)))


if __name__ == "__main__":
    unittest.main()