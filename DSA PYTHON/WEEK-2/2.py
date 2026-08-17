def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [10, 20, 30, 40, 50, 60, 70]
print("Sorted list:", arr)
key = int(input("Enter element to search: "))
pos = binary_search(arr, key)
if pos != -1:
    print("Element", key, "found at position", pos)
else:
    print("Element", key, "not found")
