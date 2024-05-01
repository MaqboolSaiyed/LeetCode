class Solution:
    def plusOne(self, digits):
        # Start from the rightmost digit and move left
        for i in range(len(digits)-1, -1, -1):
            # If the current digit is not 9, increment it and return the digits array
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the current digit is 9, set it to 0 and continue to the previous digit
            else:
                digits[i] = 0
        # If all digits are 9, we need to add a new leading digit 1 to the result
        digits.insert(0, 1)
        return digits

# Test the function
ret = Solution().plusOne([1,2,3])
print(ret)
ret = Solution().plusOne([4,3,2,1])
print(ret)
ret = Solution().plusOne([9])
print(ret)
ret = Solution().plusOne([9,9])
print(ret)
ret = Solution().plusOne([1,9,9])
print(ret)
ret = Solution().plusOne([9,9,9])
print(ret)