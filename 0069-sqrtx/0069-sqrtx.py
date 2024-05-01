class Solution:
    def mySqrt(self, x: int) -> int:
        # Initialize the left and right pointers
        left = 0
        right = x

        # Binary search loop
        while left <= right:
            mid = (left + right) // 2

            # Compute the square of the middle value
            square = mid * mid

            # If the square is equal to x, return the middle value
            if square == x:
                return mid

            # If the square is less than x, search in the right half
            if square < x:
                left = mid + 1

            # If the square is greater than x, search in the left half
            else:
                right = mid - 1

        # If the square root is not an integer, return the largest integer less than or equal to the square root
        return right