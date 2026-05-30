class Solution:
    def licenseKeyFormatting(self, s, k):
        s = s.replace('-', '').upper()

        n = len(s)
        first = n % k

        res = []

        if first:
            res.append(s[:first])

        for i in range(first, n, k):
            res.append(s[i:i + k])

        return "-".join(res)