import unittest
from ..bstpy import BST


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BST(10)

    def test_insert(self):
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst.left.value, 5)
        self.assertEqual(self.bst.right.value, 15)

    def test_height(self):
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst.height(), 1)

    def test_delete(self):
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.delete(5)
        self.assertEqual(self.bst.left, None)


if __name__ == "__main__":
    unittest.main()
