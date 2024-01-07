import unittest
from ..structs import LIFO


class TestLIFO(unittest.TestCase):
    def test_push(self):
        self.lifo = LIFO()
        self.lifo.push(1)
        self.assertEqual(self.lifo.last[0], 1)
        self.assertEqual(self.lifo.first[0], 1)
        self.lifo.push(2)
        self.assertEqual(self.lifo.last[0], 2)
        self.assertEqual(self.lifo.first[0], 1)
        self.lifo.push(3)
        self.assertEqual(self.lifo.last[0], 3)
        self.assertEqual(self.lifo.first[0], 1)

    def test_pop(self):
        self.lifo = LIFO()
        self.lifo.push(1)
        self.lifo.push(2)
        self.lifo.push(3)
        self.assertEqual(self.lifo.pop(), 3)
        self.assertEqual(self.lifo.pop(), 2)
        self.assertEqual(self.lifo.pop(), 1)
        self.assertEqual(self.lifo.pop(), None)
