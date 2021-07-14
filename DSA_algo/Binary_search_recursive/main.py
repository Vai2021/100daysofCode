def binary_search(a, key, l, r):
    if l > r:
        return -1
    else:
        m = (l + r) // 2
        if key == a[m]:
            return m
        elif key < a[m]:
            return binary_search(a, key, l, m - 1)
        elif key > a[m]:
            return binary_search(a, key, m + 1, r)


a = [15, 21, 47, 84, 96]
found = binary_search(a, 17, 0, 4)
print(found)
