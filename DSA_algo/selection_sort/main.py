def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        position = i
        for j in range(i + 1, n):
            if arr[j] < arr[position]:
                position = j
        temp = arr[i]
        arr[i] = arr[position]
        arr[position] = temp


arr = [3, 5, 6, 8, 9, 2]
selection_sort(arr)
print(arr)
