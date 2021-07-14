def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        i = gap
        while i < n:
            temp = array[i]
            j = i - gap
            while j >= 0 and array[j] > temp:
                array[j + gap] = array[j]
                j = j - gap
            array[j + gap] = temp
            i = i + 1
        gap = gap // 2


array = [3, 5, 8, 9, 6, 2]
print('Original Array:', array)
shell_sort(array)
print('Sorted Array:', array)
