class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        count = defaultdict(int)      # Frequency of substrings
        char_count = defaultdict(int) # Frequency of chars in current window

        left = 0
        ans = 0

        for right in range(len(s)):
            char_count[s[right]] += 1

            # Keep window size = minSize
            if right - left + 1 > minSize:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            # Check valid window
            if right - left + 1 == minSize:
                if len(char_count) <= maxLetters:
                    sub = s[left:right + 1]
                    count[sub] += 1
                    ans = max(ans, count[sub])

        return ans