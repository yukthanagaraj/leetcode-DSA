class Solution:
    def nearestPalindromic(self, n):
        num = int(n)
        length = len(n)

        candidates = set()

        # Edge palindromes
        candidates.add(10 ** (length - 1) - 1)  # 999...
        candidates.add(10 ** length + 1)         # 1000...0001

        prefix = int(n[: (length + 1) // 2])

        for p in (prefix - 1, prefix, prefix + 1):
            s = str(p)

            if length % 2:
                pal = int(s + s[:-1][::-1])
            else:
                pal = int(s + s[::-1])

            candidates.add(pal)

        candidates.discard(num)

        ans = None

        for cand in candidates:
            if (ans is None or
                abs(cand - num) < abs(ans - num) or
                (abs(cand - num) == abs(ans - num) and cand < ans)):
                ans = cand

        return str(ans)