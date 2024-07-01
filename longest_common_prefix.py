from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(s) for s in strs])
        prefix = ''
        for i in range(1, min_len + 1):
            prefixes_list = [s[:i] for s in strs]
            prefixes_set = set(prefixes_list)
            if len(prefixes_set) > 1:
                return prefix
            prefix = prefixes_list[0]
        return prefix


sol = Solution()
print(sol.longestCommonPrefix(['a', 'aba', 'abaa']))
