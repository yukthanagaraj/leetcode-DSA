class Solution:
    def maximumGap(self, nums):
        
        n = len(nums)

        if n < 2:
            return 0

        minimum = min(nums)
        maximum = max(nums)

        if minimum == maximum:
            return 0

        bucket_size = max(1, (maximum - minimum) // (n - 1))
        bucket_count = ((maximum - minimum) // bucket_size) + 1

        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:

            idx = (num - minimum) // bucket_size

            if buckets[idx][0] is None:
                buckets[idx][0] = num
                buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)

        max_gap = 0
        prev_max = minimum

        for bucket in buckets:

            if bucket[0] is None:
                continue

            max_gap = max(max_gap, bucket[0] - prev_max)

            prev_max = bucket[1]

        return max_gap
        