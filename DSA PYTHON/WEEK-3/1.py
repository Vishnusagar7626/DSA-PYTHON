def bubble_sort(arr):
    n = len(arr)
    i = 0
    while i < n - 1:
        j = 0
        swapped = False
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True
            j = j + 1
        if not swapped:
            break
        i = i + 1
    return arr


n = int(input("Enter number of elements: "))
print("Enter", n, "elements (space separated):")
arr = list(map(int, input().split()))
print("Before sorting:", arr)
print("After bubble sort:", bubble_sort(arr))
