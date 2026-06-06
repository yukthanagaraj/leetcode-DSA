class Solution:
    def partitionLabels(self, s):
        last = {ch: i for i, ch in enumerate(s)}

        ans = []
        start = end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])

            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans