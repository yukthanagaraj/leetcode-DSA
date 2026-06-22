class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = {}

        # Store sums of nums1 + nums2
        for a in nums1:
            for b in nums2:
                total = a + b
                count[total] = count.get(total, 0) + 1

        ans = 0

        # Find matching negative sums
        for c in nums3:
            for d in nums4:
                total = c + d
                ans += count.get(-total, 0)

        return ans