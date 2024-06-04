import math
import random


def merge_sort_with_cut(array: list, n: int, COMPARISON):
    if n == 2:
        COMPARISON += 1
        if array[0] >= array[1]:
            return [array[0], array[1]], COMPARISON
        return [array[1], array[0]], COMPARISON
    m = n // 2
    first, COMPARISON = merge_sort_with_cut(array[:m], m, COMPARISON)
    second, COMPARISON = merge_sort_with_cut(array[m:], n - m, COMPARISON)
    result = []
    i = 0
    j = 0
    for k in range(2):
        COMPARISON += 1
        if second[j] >= first[i]:
            result.append(second[j])
            j += 1
        else:
            result.append(first[i])
            i += 1
    return result, COMPARISON


COMPARISON = 0
# array = [7, 10, 3, 11, 8, 9, 13, 2, 14, 5, 6, 8, 12, 15, 1, 4]
# array = [1, 2, 3, 4, 5, 6, 7, 8]
array = [random.randint(0, 100) for x in range(256)]
print(array)
result, COMPARISON = merge_sort_with_cut(array, len(array), COMPARISON)
print(result)
n = len(array)

print(n, COMPARISON, (n + math.log(n, 2) - 2))
