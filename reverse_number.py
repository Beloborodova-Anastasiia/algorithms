class Solution:
    def reverse(self, x: int) -> int:
        maximun = 2 ** 31
        flag = 0
        if x < 0:
            flag = 1
            x = abs(x)
        x = x
        y = 0
        while x != 0:
            y = y * 10 + x % 10
            x = x // 10
            if y > maximun:
                return 0
        if flag:
            return y * (-1)
        return y


sol = Solution()

print(sol.reverse(1534236469))
