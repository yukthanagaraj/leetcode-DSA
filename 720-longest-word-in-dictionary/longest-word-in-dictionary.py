class Solution:
    def longestWord(self, words):
        word_set = set(words)
        ans = ""

        for word in words:
            valid = True

            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break

            if valid:
                if len(word) > len(ans) or (
                    len(word) == len(ans) and word < ans
                ):
                    ans = word

        return ans