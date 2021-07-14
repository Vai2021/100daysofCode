def linear_search(array, key):    #time complexity = o(n)
    index = 0
    while index < len(array):
        if array[index] == key:
            return index
        index += 1
    return -1


A = [84, 94, 32, 67, 43, 21, 78, 90]
key = 90
found = linear_search(A, key)
print(f"result:{found}")
