class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def height(self, root):
        return root.height if root else 0
    def get_balance(self, root):
        return self.height(root.left) - self.height(root.right) if root else 0

    def right_rotate(self, y):
        x = y.left
        t = x.right
        x.right = y
        y.left = t
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        t = y.left
        y.left = x
        x.right = t
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        b = self.get_balance(root)
        if b > 1 and key < root.left.key:
            return self.right_rotate(root)
        if b < -1 and key > root.right.key:
            return self.left_rotate(root)
        if b > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if b < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def min_value_node(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        if not root:
            return root
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        b = self.get_balance(root)
        if b > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if b > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if b < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if b < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    def display(self, root, level=0):
        if root:
            self.display(root.right, level + 1)
            print("    " * level + str(root.key))
            self.display(root.left, level + 1)
tree = AVLTree()
root = None
while True:
    print("\n1.Insert\n2.Delete\n3.Search\n4.Inorder\n5.Preorder\n6.Postorder\n7.Display\n8.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter value: "))
        root = tree.insert(root, key)
        print("Inserted")
    elif choice == 2:
        key = int(input("Enter value: "))
        if tree.search(root, key):
            root = tree.delete(root, key)
            print("Deleted")
        else:
            print("Value not found")
    elif choice == 3:
        key = int(input("Enter value: "))
        print("Found" if tree.search(root, key) else "Not found")
    elif choice == 4:
        tree.inorder(root)
        print()
    elif choice == 5:
        tree.preorder(root)
        print()
    elif choice == 6:
        tree.postorder(root)
        print()
    elif choice == 7:
        tree.display(root)
    elif choice == 8:
        break
    else:
        print("Invalid choice")
