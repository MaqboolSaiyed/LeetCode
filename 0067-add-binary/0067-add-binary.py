class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0

        # Iterate over the binary strings from right to left
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry > 0:
            # Compute the sum of the current digits and the carry
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1

            # Append the least significant bit of the sum to the result
            result += str(sum % 2)

            # Update the carry for the next iteration
            carry = sum // 2

        # Reverse the result and return it
        return result[::-1]