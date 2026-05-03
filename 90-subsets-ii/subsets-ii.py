class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()   # Step 1: sort to handle duplicates
        result = []

        def backtrack(start, path):
            result.append(path[:])   # store current subset

            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
        