from collections import Counter

class Solution:
    def customSortString(self, order, s):
        cnt = Counter(s)
        res = []

        for ch in order:
            if ch in cnt:
                res.append(ch * cnt[ch])
                del cnt[ch]

        for ch, freq in cnt.items():
            res.append(ch * freq)

        return "".join(res)