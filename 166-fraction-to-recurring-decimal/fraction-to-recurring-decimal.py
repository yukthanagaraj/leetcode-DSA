class Solution:
    def fractionToDecimal(self, numerator, denominator):

        # If perfectly divisible
        if numerator % denominator == 0:
            return str(numerator // denominator)

        result = []

        # Handle negative sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        # Work with positive numbers
        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        result.append(str(numerator // denominator))
        result.append(".")

        remainder = numerator % denominator

        # Store remainder positions
        remainder_map = {}

        while remainder != 0:

            # If repeating remainder found
            if remainder in remainder_map:
                index = remainder_map[remainder]
                result.insert(index, "(")
                result.append(")")
                break

            # Store current position
            remainder_map[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)