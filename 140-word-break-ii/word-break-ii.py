class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    sub_sentences = dfs(end)

                    for sub in sub_sentences:
                        if sub == "":
                            result.append(word)
                        else:
                            result.append(word + " " + sub)

            memo[start] = result
            return result

        return dfs(0)
        