def linear_search(arr, key):
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == key:
            return i
        i = i + 1
    return -1
arr = [45, 12, 78, 23, 56, 89, 10]
print("List:", arr)
key = int(input("Enter element to search: "))
pos = linear_search(arr, key)
if pos != -1:
    print("Element", key, "found at position", pos)
else:
    print("Element", key, "not found")
