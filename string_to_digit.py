class Solution:
    def myAtoi(self, s: str) -> int:
        result = ''
        is_digits = False
        sighn = ''
        for i in s:
            if i == ' ' and is_digits is False:
                continue
            elif i == '-' and is_digits is False:
                sighn = '-'
                is_digits = True
            elif i == '+' and is_digits is False:
                sighn = '+'
                is_digits = True
            elif ord(i) >= 48 and ord(i) <= 57:
                result += i
                is_digits = True
            else:
                break
        if result:
            result = int(result)
        else:
            return 0
        if sighn == '-':
            result = result * (-1)
        if result >= 2 ** 31:
            result = 2 ** 31 - 1
        if result < - 2 ** 31:
            result = - 2 ** 31
        return result


sol = Solution()
print(sol.myAtoi('  2147483648'))
# print(ord('9'))
