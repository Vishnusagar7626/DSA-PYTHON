class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash_function(self, key):
        return key % self.size
    def insert(self, key):
        index = self.hash_function(key)
        i = 0
        while i < self.size:
            pos = (index + i) % self.size
            if self.table[pos] is None or self.table[pos] == "DELETED":
                self.table[pos] = key
                print(key, "inserted at index", pos)
                return
            i += 1
        print("Hash table is full")
    def search(self, key):
        index = self.hash_function(key)
        i = 0
        while i < self.size:
            pos = (index + i) % self.size
            if self.table[pos] is None:
                return -1
            if self.table[pos] == key:
                return pos
            i += 1
        return -1
    def delete(self, key):
        pos = self.search(key)
        if pos == -1:
            print(key, "not found")
        else:
            self.table[pos] = "DELETED"
            print(key, "deleted")
    def display(self):
        print("Hash table:")
        for i in range(self.size):
            if self.table[i] is None or self.table[i] == "DELETED":
                print(i, "--> Empty")
            else:
                print(i, "-->", self.table[i])
size = int(input("Enter size of hash table: "))
ht = LinearProbing(size)
while True:
    print("\n--- LINEAR PROBING MENU ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        key = int(input("Enter key: "))
        ht.insert(key)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        pos = ht.search(key)
        if pos == -1:
            print(key, "not found")
        else:
            print(key, "found at index", pos)
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        ht.delete(key)
    elif choice == 4:
        ht.display()
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
