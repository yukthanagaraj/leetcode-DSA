class Solution:
    def maxProduct(self, words):
        n = len(words)

        masks = [0] * n
        lengths = [len(word) for word in words]

        # create bitmask for each word
        for i, word in enumerate(words):
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            masks[i] = mask

        ans = 0

        # compare every pair
        for i in range(n):
            for j in range(i + 1, n):

                # no common letters
                if masks[i] & masks[j] == 0:
                    ans = max(ans, lengths[i] * lengths[j])

        return ans