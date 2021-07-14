def bubble_sort(b_arr):
    n = len(b_arr)
    for passes in range(n - 1, 0, -1):
        for i in range(passes):
            if b_arr[i] > b_arr[i + 1]:
                temp = b_arr[i]
                b_arr[i] = b_arr[i + 1]
                b_arr[i + 1] = temp


b_arr = [1, 5, 7, 8, 4, 6]
bubble_sort(b_arr)
print(b_arr)
