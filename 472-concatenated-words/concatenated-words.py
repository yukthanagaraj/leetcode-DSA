
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        res = []

        def can_form(word, memo):
            if word in memo:
                return memo[word]

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in word_set and (
                    suffix in word_set or can_form(suffix, memo)
                ):
                    memo[word] = True
                    return True

            memo[word] = False
            return False

        for word in words:
            if not word:
                continue

            word_set.remove(word)

            if can_form(word, {}):
                res.append(word)

            word_set.add(word)

        return res