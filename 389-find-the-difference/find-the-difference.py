class Solution:
    def findTheDifference(self, s, t):
        result = 0

        # XOR all characters in s
        for ch in s:
            result ^= ord(ch)

        # XOR all characters in t
        for ch in t:
            result ^= ord(ch)

        # Remaining character is the added one
        return chr(result)
        