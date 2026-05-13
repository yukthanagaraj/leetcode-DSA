from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Convert numbers to strings
        nums = list(map(str, nums))

        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        # Sort using custom comparison
        nums.sort(key=cmp_to_key(compare))

        # Join result
        result = ''.join(nums)

        # Handle case like [0,0]
        return "0" if result[0] == '0' else result

        