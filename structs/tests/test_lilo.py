import unittest
from ..structs import LILO


class TestLILO(unittest.TestCase):
    def test_push(self):
        self.lilo = LILO()
        self.lilo.push(1)
        self.assertEqual(self.lilo.last[0], 1)
        self.assertEqual(self.lilo.first[0], 1)
        self.lilo.push(2)
        self.assertEqual(self.lilo.last[0], 2)
        self.assertEqual(self.lilo.first[0], 1)
        self.lilo.push(3)
        self.assertEqual(self.lilo.last[0], 3)
        self.assertEqual(self.lilo.first[0], 1)

    def test_pop(self):
        self.lilo = LILO()
        self.lilo.push(1)
        self.lilo.push(2)
        self.lilo.push(3)
        self.assertEqual(self.lilo.pop(), 1)
        self.assertEqual(self.lilo.pop(), 2)
        self.assertEqual(self.lilo.pop(), 3)
        self.assertEqual(self.lilo.pop(), None)
