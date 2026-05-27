class Solution:
    def longestSubstring(self, s, k):

        def helper(start, end):

            # if substring length is less than k
            if end - start < k:
                return 0

            freq = {}

            # count frequency
            for i in range(start, end):
                freq[s[i]] = freq.get(s[i], 0) + 1

            # find invalid character
            for mid in range(start, end):
                if freq[s[mid]] < k:

                    mid_next = mid + 1

                    # skip consecutive invalid chars
                    while mid_next < end and freq[s[mid_next]] < k:
                        mid_next += 1

                    # divide into left and right parts
                    return max(
                        helper(start, mid),
                        helper(mid_next, end)
                    )

            # whole substring is valid
            return end - start

        return helper(0, len(s))