class SeparateChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]
    def hash_function(self, key):
        return key % self.size
    def insert(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            print(key, "already exists")
            return
        self.table[index].append(key)
        print(key, "inserted at index", index)
    def search(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            print(key, "found at index", index)
        else:
            print(key, "not found")
    def delete(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)
            print(key, "deleted")
        else:
            print(key, "not found")
    def display(self):
        print("Hash table:")
        for i in range(self.size):
            print(i, "-->", self.table[i])
size = int(input("Enter size of hash table: "))
ht = SeparateChaining(size)
while True:
    print("\n--- SEPARATE CHAINING MENU ---")
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
        ht.search(key)
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
