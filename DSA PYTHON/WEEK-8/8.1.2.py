class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTreeLinkedList:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            print("Inserted:", value)
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                print("Inserted:", value)
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                print("Inserted:", value)
                return
            else:
                queue.append(current.right)

    def search(self, value):
        if self.root is None:
            print("Value not found")
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.data == value:
                print("Value found:", value)
                return

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        print("Value not found")

    def delete(self, value):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]
        target = None
        deepest = None
        parent_of_deepest = None

        while queue:
            current = queue.pop(0)

            if current.data == value and target is None:
                target = current

            if current.left:
                parent_of_deepest = current
                deepest = current.left
                queue.append(current.left)

            if current.right:
                parent_of_deepest = current
                deepest = current.right
                queue.append(current.right)

        if target is None:
            print("Value not found")
            return

        if deepest is None:
            self.root = None
            print("Deleted:", value)
            return

        target.data = deepest.data

        if parent_of_deepest.left is deepest:
            parent_of_deepest.left = None
        else:
            parent_of_deepest.right = None

        print("Deleted:", value)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def display(self):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
bt = BinaryTreeLinkedList()
bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)

print("Level-order traversal:")
bt.display()

print("\nPreorder traversal:")
bt.preorder(bt.root)

print("\nInorder traversal:")
bt.inorder(bt.root)

print("\nPostorder traversal:")
bt.postorder(bt.root)

print()
bt.search(30)
bt.delete(20)

print("Tree after deletion:")
bt.display()
