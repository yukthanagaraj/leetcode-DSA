class Solution:
    def orderlyQueue(self, s, k):
        if k == 1:
            ans = s

            for i in range(1, len(s)):
                rotated = s[i:] + s[:i]
                ans = min(ans, rotated)

            return ans

        else:
            return ''.join(sorted(s))