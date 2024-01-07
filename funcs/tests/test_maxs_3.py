import unittest
from ..funcs import maxs_3


class TestMaxs3(unittest.TestCase):
    def test_maxs_3(self):
        self.assertEqual(maxs_3([1, 2, 3]), [1, 2, 3])
        self.assertEqual(maxs_3([-1, -2, -3]), [-3, -2, -1])
        self.assertEqual(maxs_3([1, 2, 3, 4, 5]), [3, 4, 5])
        self.assertEqual(maxs_3([-1, -2, -3, -4, -5]), [-3, -2, -1])

    def test_maxs_3_spe(self):
        self.assertEqual(maxs_3([]), [])
        self.assertEqual(maxs_3([1]), [])
        self.assertEqual(maxs_3([-1]), [])
        self.assertEqual(maxs_3([1, 2]), [])
        self.assertEqual(maxs_3([-1, -2]), [])
