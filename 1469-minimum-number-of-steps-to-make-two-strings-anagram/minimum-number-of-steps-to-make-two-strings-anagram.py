class Solution:
    def minSteps(self, s, t):
        freq = {}

        # Count characters in s
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Remove matching characters using t
        for ch in t:
            if freq.get(ch, 0) > 0:
                freq[ch] -= 1

        # Remaining characters are the answer
        return sum(freq.values())