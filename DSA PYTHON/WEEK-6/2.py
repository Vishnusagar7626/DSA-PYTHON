class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def isEmpty(self):
        return self.top is None
    def push(self, item):
        newNode = Node(item)
        newNode.next = self.top
        self.top = newNode
        print(item, "pushed into stack")
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            temp = self.top
            self.top = self.top.next
            print(temp.data, "popped from stack")
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top element is", self.top.data)
    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack elements are:")
            temp = self.top
            while temp is not None:
                print(temp.data)
                temp = temp.next
s = Stack()
while True:
    print("1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter element to push: "))
        s.push(item)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
