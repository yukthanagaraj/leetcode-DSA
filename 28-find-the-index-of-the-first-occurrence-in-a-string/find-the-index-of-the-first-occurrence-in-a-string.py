class Solution:
    def strStr(self, haystack, needle):

        n = len(haystack)
        m = len(needle)

        # check every possible starting index
        for i in range(n - m + 1):

            # compare substring
            if haystack[i:i + m] == needle:
                return i

        return -1
     
        