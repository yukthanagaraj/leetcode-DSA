class Solution:
    def convertToTitle(self,columnNumber):

        result = []

        while columnNumber > 0:

            # Adjust because Excel columns are 1-based
            columnNumber -= 1

            char = chr((columnNumber % 26) + ord('A'))
            result.append(char)

            columnNumber //= 26

        return "".join(result[::-1])