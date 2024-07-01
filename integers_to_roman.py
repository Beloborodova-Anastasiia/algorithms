class Solution:
    roman_values_int_keys = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
        0: ''
    }
    roman_values_rom_keys = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        '': 0,
    }

    def intToRoman(self, num: int) -> str:
        n = 0
        result = []
        res = ''
        while num > 0:
            a = 0
            b = num % 10
            num = num // 10
            n += 1
            while abs(b) > 3:
                a += 5
                b = b - 5
            x = a * 10 ** (n - 1)
            if b >= 0:
                result.append(
                    self.roman_values_int_keys[x]
                    + self.roman_values_int_keys[10 ** (n - 1)] * b
                )
            else:
                result.append(
                    self.roman_values_int_keys[10 ** (n - 1)] * abs(b)
                    + self.roman_values_int_keys[x]
                )
        for i in result[::-1]:
            res += i
        return res

    def romanToInt(self, num: str) -> int:
        result = 0
        for i in range(len(num)):
            if (
                i < len(num) - 1
                and (self.roman_values_rom_keys[num[i]]
                     < self.roman_values_rom_keys[num[i + 1]])
            ):
                result -= self.roman_values_rom_keys[num[i]]
            else:
                result += self.roman_values_rom_keys[num[i]]
        return result


sol = Solution()
print(sol.romanToInt('CDIX'))
