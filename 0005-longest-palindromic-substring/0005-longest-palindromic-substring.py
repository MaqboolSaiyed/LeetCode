class Solution:
    def __init__(self):
        # Initialize any variables or data structures you need here
        pass

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        maxLen = 1
        start = 0

        for i in range(1, len(s)):
            # Check for even length palindrome
            low = i - 1
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if high - low + 1 > maxLen:
                    start = low
                    maxLen = high - low + 1
                low -= 1
                high += 1

            # Check for odd length palindrome
            low = i - 1
            high = i + 1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if high - low + 1 > maxLen:
                    start = low
                    maxLen = high - low + 1
                low -= 1
                high += 1

        return s[start:start + maxLen]