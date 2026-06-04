class Solution:
    def toLowerCase(self, s):
        res = []

        for ch in s:
            if 'A' <= ch <= 'Z':
                res.append(chr(ord(ch) + 32))
            else:
                res.append(ch)

        return ''.join(res)