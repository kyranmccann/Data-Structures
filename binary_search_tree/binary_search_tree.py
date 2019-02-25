class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value > self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif self.value < target:
            if self.right is None:
                return False
            return self.right.contains(target)

    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value
