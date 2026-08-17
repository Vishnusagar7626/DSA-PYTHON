def insertion_sort(arr):
    n = len(arr)
    i = 1
    while i < n:
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        i = i + 1
    return arr
n = int(input("Enter number of elements: "))
print("Enter", n, "elements (space separated):")
arr = list(map(int, input().split()))
print("Before sorting:", arr)
print("After insertion sort:", insertion_sort(arr))
