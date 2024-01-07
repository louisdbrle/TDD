import unittest
from ..funcs import mins_N


class TestMinsN(unittest.TestCase):
    def test_mins_N(self):
        self.assertEqual(mins_N([1, 2, 3], 3), [1, 2, 3])
        self.assertEqual(mins_N([-1, -2, -3], 3), [-3, -2, -1])
        self.assertEqual(mins_N([1, 2, 3, 4, 5], 3), [1, 2, 3])
        self.assertEqual(mins_N([-1, -2, -3, -4, -5], 3), [-5, -4, -3])
        self.assertEqual(mins_N([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
        self.assertEqual(mins_N([-1, -2, -3, -4, -5], 5), [-5, -4, -3, -2, -1])
        self.assertEqual(mins_N([1, 2, 3, 4, 5], 1), [1])
        self.assertEqual(mins_N([-1, -2, -3, -4, -5], 1), [-5])

    def test_mins_N_spe(self):
        self.assertEqual(mins_N([1, 2, 3, 4, 5], 0), [])
        self.assertEqual(mins_N([-1, -2, -3, -4, -5], 0), [])
        self.assertEqual(mins_N([1, 2, 3, 4, 5], -1), [])
        self.assertEqual(mins_N([-1, -2, -3, -4, -5], -1), [])
        self.assertEqual(mins_N([1, 2, 3, 4, 5], 6), [])
        self.assertEqual(mins_N([-1, -2, -3, -4, -5], 6), [])
