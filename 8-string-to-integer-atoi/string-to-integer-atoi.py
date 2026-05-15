class Solution:
    def myAtoi(self, s):

        i = 0
        n = len(s)

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Handle sign
        sign = 1

        if i < n and (s[i] == '+' or s[i] == '-'):

            if s[i] == '-':
                sign = -1

            i += 1

        result = 0

        # Read digits
        while i < n and s[i].isdigit():

            digit = ord(s[i]) - ord('0')

            result = result * 10 + digit

            # Handle overflow
            if sign * result < INT_MIN:
                return INT_MIN

            if sign * result > INT_MAX:
                return INT_MAX

            i += 1

        return sign * result
        