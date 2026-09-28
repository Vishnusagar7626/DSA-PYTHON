class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
            print(item, "inserted into queue")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            print(item, "inserted into queue")
    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
            print(item, "deleted from queue")
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            print(item, "deleted from queue")
    def peek(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Front element is", self.queue[self.front])
    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Queue elements are:")
            if self.rear >= self.front:
                for i in range(self.front, self.rear + 1):
                    print(self.queue[i], end=" ")
            else:
                for i in range(self.front, self.size):
                    print(self.queue[i], end=" ")
                for i in range(0, self.rear + 1):
                    print(self.queue[i], end=" ")
            print()
size = int(input("Enter size of queue: "))
q = CircularQueue(size)
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
