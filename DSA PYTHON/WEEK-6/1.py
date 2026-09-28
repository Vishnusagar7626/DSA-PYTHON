class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [0] * size
        self.top = -1
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top == self.size - 1
    def push(self, item):
        if self.isFull():
            print("Stack Overflow")
        else:
            self.top = self.top + 1
            self.stack[self.top] = item
            print(item, "pushed into stack")
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            item = self.stack[self.top]
            self.top = self.top - 1
            print(item, "popped from stack")
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top element is", self.stack[self.top])
    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack elements are:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])
size = int(input("Enter size of stack: "))
s = Stack(size)
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
