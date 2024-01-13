# class BST
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # insert node
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    # get min value
    def get_min_value(self):
        if self.left is None:
            return self.value
        else:
            return self.left.get_min_value()

    # height
    def height(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None and self.right is not None:
            return self.right.height() + 1
        elif self.right is None and self.left is not None:
            return self.left.height() + 1
        else:
            return max(self.left.height(), self.right.height()) + 1

    # delete node bst
    def delete(self, value):
        if value < self.value:
            if self.left is not None:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right is not None:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                self.value = self.right.get_min_value()
                self.right = self.right.delete(self.value)
        return self

    # print tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()
