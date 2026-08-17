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


def binary_search_unsorted(arr, key):
    sorted_arr = sorted(arr)          # sort first
    pos = binary_search(sorted_arr, key)
    return sorted_arr, pos


arr = [45, 12, 78, 23, 56, 89, 10]
print("Original (unsorted) list:", arr)
key = int(input("Enter element to search: "))
sorted_arr, pos = binary_search_unsorted(arr, key)
print("After sorting:", sorted_arr)
if pos != -1:
    print("Element", key, "found at position", pos, "in the sorted list")
else:
    print("Element", key, "not found")
