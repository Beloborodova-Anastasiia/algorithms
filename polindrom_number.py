class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        arr = []
        if x < 10:
            return True
        while x > 0:
            arr.append(x % 10)
            x = x // 10
        print(arr)
        if arr == arr[::-1]:
            return True
        return False


sol = Solution()
print(sol.isPalindrome(-1))
