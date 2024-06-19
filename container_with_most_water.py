from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0

        # for i in range(0, len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         if min(height[i], height[j]) * (j - i) > max_volume:
        #             max_volume = min(height[i], height[j]) * (j - i)
        i = 0
        j = len(height) - 1
        while i < j:
            max_volume = max(max_volume, (j - i) * min(height[i], height[j]))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return max_volume

array = [1,8,6,2,5,4,8,3,7]
print(len(array))
sol = Solution()
print(sol.maxArea(array))
