class Solution:
    def shortestPalindrome(self, s):

        rev = s[::-1]

        temp = s + "#" + rev

        lps = [0] * len(temp)

        j = 0

        for i in range(1, len(temp)):

            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]

            if temp[i] == temp[j]:
                j += 1
                lps[i] = j

        palindrome_len = lps[-1]

        add_part = rev[:len(s) - palindrome_len]

        return add_part + s