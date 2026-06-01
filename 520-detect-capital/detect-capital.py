class Solution:
    def detectCapitalUse(self, word):
        capitals = sum(c.isupper() for c in word)

        return (
            capitals == len(word) or
            capitals == 0 or
            (capitals == 1 and word[0].isupper())
        )