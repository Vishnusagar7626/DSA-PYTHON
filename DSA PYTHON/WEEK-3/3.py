def selection_sort(arr):
    n = len(arr)
    i = 0
    while i < n - 1:
        min_index = i
        j = i + 1
        while j < n:
            if arr[j] < arr[min_index]:
                min_index = j
            j = j + 1
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
        i = i + 1
    return arr


n = int(input("Enter number of elements: "))
print("Enter", n, "elements (space separated):")
arr = list(map(int, input().split()))
print("Before sorting:", arr)
print("After selection sort:", selection_sort(arr))
