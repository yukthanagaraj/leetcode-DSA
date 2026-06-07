from collections import defaultdict
from bisect import bisect_right

class Solution:
    def numMatchingSubseq(self, s, words):
        pos = defaultdict(list)

        for i, ch in enumerate(s):
            pos[ch].append(i)

        ans = 0

        for word in words:
            prev = -1
            valid = True

            for ch in word:
                idx = bisect_right(pos[ch], prev)

                if idx == len(pos[ch]):
                    valid = False
                    break

                prev = pos[ch][idx]

            if valid:
                ans += 1

        return ans
        