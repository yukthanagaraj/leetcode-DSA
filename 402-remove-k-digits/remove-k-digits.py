class Solution:
    def removeKdigits(self, num, k):

        stack = []

        for digit in num:

            # remove larger previous digits
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # if k still remains
        while k > 0:
            stack.pop()
            k -= 1

        # remove leading zeros
        result = "".join(stack).lstrip('0')

        # if empty return "0"
        return result if result else "0"