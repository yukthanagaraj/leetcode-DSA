from collections import Counter

class Solution:
    def minWindow(self,s,t):
        if not s or not t:
            return ""

        need = Counter(t)   # Frequency of chars in t
        window = {}

        have = 0
        need_count = len(need)

        left = 0
        res = [-1, -1]
        res_len = float("inf")

        for right in range(len(s)):
            char = s[right]

            # Add current character to window
            window[char] = window.get(char, 0) + 1

            # Check if frequency matches
            if char in need and window[char] == need[char]:
                have += 1

            # Try shrinking window
            while have == need_count:

                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Remove left character
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        l, r = res

        return s[l:r + 1] if res_len != float("inf") else ""