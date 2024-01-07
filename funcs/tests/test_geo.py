import unittest
from ..funcs import geo


class TestGeo(unittest.TestCase):
    def test_geo(self):
        self.assertEqual(geo([1, 2, 4]), True)
        self.assertEqual(geo([1, 2, 3]), False)
        self.assertEqual(geo([-1, -2, -4]), True)
        self.assertEqual(geo([-1, -2, -3]), False)
        self.assertEqual(geo([1, 1, 1]), True)
        self.assertEqual(geo([1, 1, 2]), False)
        self.assertEqual(geo([1, 10, 100]), True)
        self.assertEqual(geo([1, 10, 101]), False)
        self.assertEqual(geo([-100, -50, 0]), False)
        self.assertEqual(geo([-100, -75, -50, -25, 0, 25]), False)
        self.assertEqual(geo([_ for _ in range(1, 1000, 4)]), False)
        self.assertEqual(geo([100, 50, 25, 12.5]), True)

    def test_geo_spe(self):
        self.assertEqual(geo([]), False)
        self.assertEqual(geo([1]), False)
