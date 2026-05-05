class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            cut1 = (low + high) // 2        # partition index for nums1
            cut2 = (m + n + 1) // 2 - cut1  # partition index for nums2

            # Elements just left/right of each partition
            L1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            L2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            R1 = float('inf')  if cut1 == m else nums1[cut1]
            R2 = float('inf')  if cut2 == n else nums2[cut2]

            if L1 <= R2 and L2 <= R1:
                # Perfect partition found
                if (m + n) % 2 == 1:
                    return float(max(L1, L2))
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0
            elif L1 > R2:
                high = cut1 - 1  # move cut1 left
            else:
                low = cut1 + 1   # move cut1 right