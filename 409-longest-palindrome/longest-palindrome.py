
class Solution:
    def longestPalindrome(self, s):

        freq = Counter(s)

        length = 0
        odd_found = False

        for count in freq.values():

            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True

        # add one odd character in center
        if odd_found:
            length += 1

        return length