import unittest
from ..structs import FIFO


class TestFIFO(unittest.TestCase):
    def test_push(self):
        self.fifo = FIFO()
        self.fifo.push(1)
        self.assertEqual(self.fifo.last[0], 1)
        self.assertEqual(self.fifo.first[0], 1)
        self.fifo.push(2)
        self.assertEqual(self.fifo.last[0], 2)
        self.assertEqual(self.fifo.first[0], 1)
        self.fifo.push(3)
        self.assertEqual(self.fifo.last[0], 3)
        self.assertEqual(self.fifo.first[0], 1)

    def test_pop(self):
        self.fifo = FIFO()
        self.fifo.push(1)
        self.fifo.push(2)
        self.fifo.push(3)
        self.assertEqual(self.fifo.pop(), 1)
        self.assertEqual(self.fifo.pop(), 2)
        self.assertEqual(self.fifo.pop(), 3)
        self.assertEqual(self.fifo.pop(), None)
