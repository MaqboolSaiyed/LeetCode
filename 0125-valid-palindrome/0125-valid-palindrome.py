class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the characters after converting them to lowercase
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True