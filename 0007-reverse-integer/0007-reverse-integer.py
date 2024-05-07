class Solution:
    def reverse(self, x: int) -> int:
        # Check if the input is within the valid range
        if -2**31 <= x <= 2**31 - 1:
            # Convert the input to a string and reverse it
            reversed_str = str(abs(x))[::-1]

            # Check if the reversed string can be converted to an integer within the valid range
            if -2**31 <= int(reversed_str) <= 2**31 - 1:
                # If the input is negative, add a negative sign to the reversed string
                if x < 0:
                    return -int(reversed_str)
                else:
                    # Otherwise, return the reversed string as an integer
                    return int(reversed_str)
            else:
                # If the reversed string is outside the valid range, return 0
                return 0
        else:
            # If the input is outside the valid range, return 0
            return 0