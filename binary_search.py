def binary_search(array, x, n):
    left = 0
    right = n - 1
    i = (right - left) // 2
    while array[i] != x:
        if array[i] < x:
            left = i
            i = left + (right - left) // 2 + 1
        else:
            right = i
            i = left + (right - left) // 2
    return i


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(binary_search(array, 2, len(array)))
