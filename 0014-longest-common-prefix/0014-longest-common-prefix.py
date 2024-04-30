class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, char in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return s[:i] if i > 0 else ""

        return strs[0]

# Test the function
ret = Solution().longestCommonPrefix(["flower","flow","flight"])
print(ret)  # Output: "fl"