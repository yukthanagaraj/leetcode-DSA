class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        total = 0
        res = list(s)

        for i in range(n - 1, -1, -1):
            total = (total + shifts[i]) % 26

            pos = ord(s[i]) - ord('a')
            new_pos = (pos + total) % 26

            res[i] = chr(new_pos + ord('a'))

        return ''.join(res)