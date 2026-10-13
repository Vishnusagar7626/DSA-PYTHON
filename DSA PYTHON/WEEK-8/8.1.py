class BinaryTree:
    def __init__(self):
        self.tree = []

    def insert(self, value):
        self.tree.append(value)

    def search(self, value):
        if value in self.tree:
            print("Found at index:", self.tree.index(value))
        else:
            print("Value not found")

    def delete(self, value):
        if value in self.tree:
            self.tree.remove(value)
            print("Deleted:", value)
        else:
            print("Value not found")

    def preorder(self, i=0):
        if i < len(self.tree):
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    def display(self):
        print(self.tree)
bt = BinaryTree()
bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)

print("Array:", end=" ")
bt.display()

print("Preorder:", end=" ")
bt.preorder()

print()
bt.search(30)
bt.delete(20)
bt.display()
