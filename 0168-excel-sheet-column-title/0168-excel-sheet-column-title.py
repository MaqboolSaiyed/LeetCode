class Solution:
    def convertToTitle(self, columnNumber):
        result = ""
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            result = chr(remainder + 65) + result

        return result
    