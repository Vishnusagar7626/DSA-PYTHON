class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

        print("Linked list created successfully")

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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
        temp.next = new_node

        print(data, "inserted at index", index)

    def delete_value(self, value):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            print(value, "deleted from the list")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                print(value, "deleted from the list")
                return

            temp = temp.next

        print(value, "not found in the list")

    def delete_first(self):
        if self.head is None:
            print("Linked list is empty")
            return

        value = self.head.data
        self.head = self.head.next

        print(value, "deleted from beginning")

    def delete_last(self):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.next is None:
            value = self.head.data
            self.head = None
            print(value, "deleted from end")
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        value = temp.next.data
        temp.next = None

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

        print("Linked list:")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


ll = LinkedList()

while True:
    print("\n--- LINKED LIST MENU ---")
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
        ll.create()

    elif choice == 2:
        data = int(input("Enter element: "))
        ll.insert_beginning(data)

    elif choice == 3:
        data = int(input("Enter element: "))
        ll.insert_end(data)

    elif choice == 4:
        data = int(input("Enter element: "))
        index = int(input("Enter index: "))
        ll.insert_index(data, index)

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        ll.delete_value(value)

    elif choice == 6:
        ll.delete_first()

    elif choice == 7:
        ll.delete_last()

    elif choice == 8:
        ll.count()

    elif choice == 9:
        ll.display()

    elif choice == 10:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
