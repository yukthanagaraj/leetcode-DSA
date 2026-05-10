class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        currMax = nums[0]
        currMin = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            tempMax = max(num, currMax * num, currMin * num)

            currMin = min(num, currMax * num, currMin * num)

            currMax = tempMax

            ans = max(ans, currMax)

        return ans
        