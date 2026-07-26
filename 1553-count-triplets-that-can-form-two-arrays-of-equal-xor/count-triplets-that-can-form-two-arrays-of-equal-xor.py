class Solution:
    def countTriplets(self, arr):
        n = len(arr)
        ans = 0

        for i in range(n):
            xor = 0
            for k in range(i, n):
                xor ^= arr[k]
                if xor == 0:
                    ans += (k - i)

        return ans