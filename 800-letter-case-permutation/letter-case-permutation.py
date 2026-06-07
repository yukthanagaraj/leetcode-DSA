class Solution:
    def letterCasePermutation(self, s):
        res = [""]

        for ch in s:
            if ch.isalpha():
                temp = []
                for curr in res:
                    temp.append(curr + ch.lower())
                    temp.append(curr + ch.upper())
                res = temp
            else:
                res = [curr + ch for curr in res]

        return res