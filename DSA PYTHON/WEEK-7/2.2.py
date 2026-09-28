class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularQueue:
    def __init__(self):
        self.front = self.rear = None
    def enqueue(self, item):
        newNode = Node(item)
        if self.front is None:
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.rear.next = self.front
        print(item, "inserted into queue")
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
        elif self.front == self.rear:
            item = self.front.data
            self.front = self.rear = None
            print(item, "deleted from queue")
        else:
            item = self.front.data
            self.front = self.front.next
            self.rear.next = self.front
            print(item, "deleted from queue")
    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element is", self.front.data)
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Queue elements are:")
            temp = self.front
            while temp.next != self.front:
                print(temp.data, end=" ")
                temp = temp.next
            print(temp.data)
q = CircularQueue()
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
