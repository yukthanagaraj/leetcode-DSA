class Solution:
    def relativeSortArray(self, arr1, arr2):
        freq = [0] * 1001

        for num in arr1:
            freq[num] += 1

        ans = []

        for num in arr2:
            ans.extend([num] * freq[num])
            freq[num] = 0

        for num in range(1001):
            ans.extend([num] * freq[num])

        return ans