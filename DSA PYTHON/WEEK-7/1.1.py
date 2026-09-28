class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [0] * size
        self.front = -1
        self.rear = -1
    def isEmpty(self):
        return self.front == -1
    def isFull(self):
        return self.rear == self.size - 1
    def enqueue(self, item):
        if self.isFull():
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = self.rear + 1
            self.queue[self.rear] = item
            print(item, "inserted into queue")
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            item = self.queue[self.front]
            self.front = self.front + 1
            if self.front > self.rear:
                self.front = self.rear = -1
            print(item, "deleted from queue")
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Front element is", self.queue[self.front])
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue elements are:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
size = int(input("Enter size of queue: "))
q = Queue(size)
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
