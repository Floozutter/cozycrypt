"""
Tests for ROT-n.
"""

import unittest
import code

from functools import partial


class TestDecoding(unittest.TestCase):
    def test_rot13(self):
        rot13 = partial(code.rotate, 13)
        a = "Why did the chicken cross the road? Gb trg gb gur bgure fvqr!"
        b = "Jul qvq gur puvpxra pebff gur ebnq? To get to the other side!"
        self.assertEqual(rot13(a), b)


if __name__ == "__main__":
    unittest.main()