def binary_search(arr, key):
    left = 0
    r = len(arr) - 1
    while left <= r:
        mid = (left + r) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            r = mid - 1
        elif key > arr[mid]:
            left = mid + 1
    return -1


arr = [15, 21, 47, 84, 96]

found = binary_search(arr, 96)
print(found)
