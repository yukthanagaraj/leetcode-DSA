from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes):
        count = Counter(barcodes)

        arr = []
        for num, freq in count.most_common():
            arr.extend([num] * freq)

        n = len(barcodes)
        ans = [0] * n
        idx = 0

        for num in arr:
            ans[idx] = num
            idx += 2
            if idx >= n:
                idx = 1

        return ans