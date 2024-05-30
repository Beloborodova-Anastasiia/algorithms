def multiply(x: int, y: int) -> int:
    len_x = len(str(x))
    len_y = len(str(y))
    if len_x == 1 and len_y == 1:
        return x * y

    n = max(len_x, len_y)

    m = n // 2
    a = x // int('1' + '0' * m)
    b = x % int('1' + '0' * m)
    c = y // int('1' + '0' * m)
    d = y % int('1' + '0' * m)

    i = multiply(a, c) * 10 ** (m + m)
    j = multiply(a, d) * 10 ** m
    k = multiply(b, c) * 10 ** m
    s = multiply(b, d)
    res = i + j + k + s
    return res


x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

print(multiply(x, y))
