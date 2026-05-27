class Solution:
    def toHex(self, num):

        # special case
        if num == 0:
            return "0"

        # hexadecimal characters
        hex_chars = "0123456789abcdef"

        # convert negative number to 32-bit unsigned
        num &= 0xffffffff

        result = []

        while num > 0:
            digit = num & 15      # get last 4 bits
            result.append(hex_chars[digit])
            num >>= 4             # shift right by 4 bits

        return "".join(reversed(result))