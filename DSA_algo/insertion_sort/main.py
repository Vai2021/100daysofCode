def insertion_sort(my_arr):
    n = len(my_arr)
    for i in range(1, n):
        c_value = my_arr[i]
        position = i
        while position > 0 and my_arr[position-1] > c_value:
            my_arr[position] = my_arr[position - 1]
            position = position - 1
        my_arr[position] = c_value


my_arr = [2, 3, 4, 1, 9, 7, 8]
print(f"initial:{my_arr}")
insertion_sort(my_arr)
print(f"final:{my_arr}")

# def insertionsort(A):
#     n = len(A)
#     for i in range(1,n):
#         cvalue = A[i]
#         position = i
#         while position > 0 and A[position-1] > cvalue:
#             A[position] = A[position-1]
#             position = position - 1
#         A[position] = cvalue
#
#
# A = [3,5,8,9,6,2]
# print('Original Array:',A)
# insertionsort(A)
# print('Sorted Array:',A)

