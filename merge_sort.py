def sort(array: list, n: int):
    if n == 1:
        return array
    m = n // 2
    first = sort(array[:m], m)
    second = sort(array[m:], n - m)
    i = 0
    j = 0
    final = []
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
    return final


x = input()
x = list(map(int, x.split()))
print(sort(x, len(x)))
