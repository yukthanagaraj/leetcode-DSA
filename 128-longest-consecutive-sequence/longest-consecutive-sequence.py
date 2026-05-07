
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        best = 0

        for num in num_set:
            # Only start a sequence from its lowest number
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                best = max(best, length)

        return best