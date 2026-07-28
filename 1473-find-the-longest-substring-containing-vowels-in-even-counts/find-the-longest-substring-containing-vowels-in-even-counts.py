class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Bit position for each vowel
        vowel = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }

        # state -> first index where this state appeared
        first = {0: -1}

        mask = 0
        ans = 0

        for i, ch in enumerate(s):
            if ch in vowel:
                mask ^= (1 << vowel[ch])

            if mask in first:
                ans = max(ans, i - first[mask])
            else:
                first[mask] = i

        return ans