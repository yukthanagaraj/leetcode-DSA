class Solution:
    def convertToBase7(self, num):
        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        digits = []

        while num:
            digits.append(str(num % 7))
            num //= 7

        result = "".join(reversed(digits))

        return "-" + result if negative else result