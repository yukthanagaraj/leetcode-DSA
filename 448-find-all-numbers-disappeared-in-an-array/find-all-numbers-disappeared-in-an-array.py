class Solution:
    def findDisappearedNumbers(self, nums):
        ans = []

        # Mark visited numbers
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        # Find missing numbers
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans