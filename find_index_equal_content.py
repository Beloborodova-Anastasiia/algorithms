def find_index(array):
    n = len(array)
    left = 0
    right = n - 1
    i = (right - left) // 2
    while True:
        if array[i] == i:
            return True
        elif right - left == 1 and array[right] != i and array[left] != i:
            return False
        elif array[i] < i:
            left = i
            i = left + (right - left) // 2 + 1
        else:
            right = i
            i = left + (right - left) // 2


array = [-3, -2, -1, 0, 1, 2, 4, 7, 8, 11, 15, 17, 18, 19, 20, 22]
print(find_index(array))
