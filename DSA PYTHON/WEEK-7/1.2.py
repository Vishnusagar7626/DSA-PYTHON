class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front is None
    def enqueue(self, item):
        newNode = Node(item)
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        print(item, "inserted into queue")
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            print(temp.data, "deleted from queue")
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Front element is", self.front.data)
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue elements are:")
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()
q = Queue()
while True:
    print("1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter element to insert: "))
        q.enqueue(item)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.peek()
    elif choice == 4:
        q.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
