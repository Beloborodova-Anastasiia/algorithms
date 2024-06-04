def find_maximum(array: list, n: int):
    left = 0
    right = n - 1
    i = (right - left) // 2
    while True:
        if array[i] < array[i + 1] and array[i] > array[i - 1]:
            left = i
            i = left + (right - left) // 2 + 1
        elif array[i] > array[i + 1] and array[i] < array[i - 1]:
            right = i
            i = left + (right - left) // 2
        elif array[i] > array[i + 1] and array[i] > array[i - 1]:
            return i


array = [0, 1, 2, 3, 4, 5, 6, 7, 6]
print(find_maximum(array, len(array)))
