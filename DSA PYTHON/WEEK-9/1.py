class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.data:
            root.left = self.insert(root.left, value)
        elif value > root.data:
            root.right = self.insert(root.right, value)

        return root

    def search(self, root, value):
        if root is None or root.data == value:
            return root

        if value < root.data:
            return self.search(root.left, value)

        return self.search(root.right, value)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def min_value(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, value):
        if root is None:
            return root

        if value < root.data:
            root.left = self.delete(root.left, value)
        elif value > root.data:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.min_value(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root
bst = BST()

for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.root = bst.insert(bst.root, value)

print("Inorder traversal:")
bst.inorder(bst.root)

print("\nPreorder traversal:")
bst.preorder(bst.root)

print("\nPostorder traversal:")
bst.postorder(bst.root)

print("\n")

if bst.search(bst.root, 40):
    print("Value found")
else:
    print("Value not found")

bst.root = bst.delete(bst.root, 30)

print("Inorder after deletion:")
bst.inorder(bst.root)
