import datetime
import time


def T(n: int) -> int:
    time.sleep(0.1)
    return n*2


N = [1, 2, 3, -4, 5, 6, 7, -8, 9, -10]
first = datetime.datetime.now()
result = [res for i in N if (res := T(i)) > 0]
last = datetime.datetime.now()

delta = last - first
print(delta)
print(result)
