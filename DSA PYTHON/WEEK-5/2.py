class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def create(self):
        n = int(input("Enter number of nodes: "))
        if n <= 0:
            print("Number of nodes must be greater than 0")
            return
        for i in range(n):
            data = int(input("Enter element: "))
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node
                new_node.prev = temp
        print("Doubly linked list created successfully")
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        print(data, "inserted at beginning")
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print(data, "inserted at end")
    def insert_index(self, data, index):
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            self.insert_beginning(data)
            return
        temp = self.head
        for i in range(index - 1):
            if temp is None:
                print("Index out of range")
                return
            temp = temp.next
        if temp is None:
            print("Index out of range")
            return
        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
        print(data, "inserted at index", index)
    def delete_value(self, value):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        while temp is not None and temp.data != value:
            temp = temp.next
        if temp is None:
            print(value, "not found in the list")
            return
        if temp.prev is not None:
            temp.prev.next = temp.next
        else:
            self.head = temp.next
        if temp.next is not None:
            temp.next.prev = temp.prev
        print(value, "deleted from the list")
    def delete_first(self):
        if self.head is None:
            print("Linked list is empty")
            return
        value = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        print(value, "deleted from beginning")
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        value = temp.data
        if temp.prev is None:
            self.head = None
        else:
            temp.prev.next = None
        print(value, "deleted from end")
    def count(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        print("Number of nodes:", count)
    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        print("Doubly linked list:")
        print("None", end=" <-> ")
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
dll = DoublyLinkedList()
while True:
    print("\n--- DOUBLY LINKED LIST MENU ---")
    print("1. Create")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Index")
    print("5. Delete by Value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count Number of Nodes")
    print("9. Display / Traverse")
    print("10. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        dll.create()
    elif choice == 2:
        data = int(input("Enter element: "))
        dll.insert_beginning(data)
    elif choice == 3:
        data = int(input("Enter element: "))
        dll.insert_end(data)
    elif choice == 4:
        data = int(input("Enter element: "))
        index = int(input("Enter index: "))
        dll.insert_index(data, index)
    elif choice == 5:
        value = int(input("Enter value to delete: "))
        dll.delete_value(value)
    elif choice == 6:
        dll.delete_first()
    elif choice == 7:
        dll.delete_last()
    elif choice == 8:
        dll.count()
    elif choice == 9:
        dll.display()
    elif choice == 10:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
