def sort(array: list, n: int):
    if n == 1:
        return array, 0
    m = n // 2
    first, x = sort(array[:m], m)
    second, y = sort(array[m:], n - m)
    i = 0
    j = 0
    final = []
    z = 0
    for k in range(n):
        if j >= n - m:
            final.append(first[i])
            i += 1
        elif i >= m:
            final.append(second[j])
            j += 1
        elif first[i] <= second[j]:
            final.append(first[i])
            i += 1
        elif first[i] > second[j]:
            final.append(second[j])
            j += 1
            z += m - i

    return final, x + y + z


x = input()
x = list(map(int, x.split()))
print(sort(x, len(x)))
