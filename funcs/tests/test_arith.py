import unittest
from ..funcs import arith


class TestArith(unittest.TestCase):
    def test_arith(self):
        self.assertEqual(arith([1, 2, 3]), True)
        self.assertEqual(arith([1, 2, 4]), False)
        self.assertEqual(arith([-1, -2, -3]), True)
        self.assertEqual(arith([-1, -2, -4]), False)
        self.assertEqual(arith([1, 1, 1]), True)
        self.assertEqual(arith([1, 1, 2]), False)
        self.assertEqual(arith([1, 10, 19]), True)
        self.assertEqual(arith([1, 10, 20]), False)
        self.assertEqual(arith([-100, -50, 0]), True)
        self.assertEqual(arith([-100, -75, -50, -25, 0, 25]), True)
        self.assertEqual(arith([_ for _ in range(0, 1000, 4)]), True)

    def test_arith_spe(self):
        self.assertEqual(arith([]), False)
        self.assertEqual(arith([1]), False)
