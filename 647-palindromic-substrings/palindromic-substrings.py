class Solution:
    def countSubstrings(self, s):
        n = len(s)
        ans = 0

        def expand(left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            ans += expand(i, i)       # odd length
            ans += expand(i, i + 1)   # even length

        return ans