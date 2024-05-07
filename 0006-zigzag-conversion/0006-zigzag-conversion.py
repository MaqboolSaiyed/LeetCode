class Solution:
    def __init__(self):
        # Initialize any variables or data structures you need here
        pass

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # Initialize the result string and the current row index
        result = [""] * numRows
        row = 0
        goingDown = False

        # Iterate through each character in the input string
        for c in s:
            # Set the current row to the next row in the zigzag pattern
            result[row] += c
            if row == 0 or row == numRows - 1:
                # If we're at the top or bottom row, toggle the direction
                goingDown = not goingDown
            row += 1 if goingDown else -1

        # Concatenate the rows to form the final result
        return "".join(result)