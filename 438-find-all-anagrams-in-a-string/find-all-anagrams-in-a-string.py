
class Solution:
    def findAnagrams(self, s, p):
        
        result = []
        
        p_count = Counter(p)
        window = Counter()

        left = 0

        for right in range(len(s)):

            window[s[right]] += 1

            # Maintain window size
            if right - left + 1 > len(p):
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            # Check anagram
            if window == p_count:
                result.append(left)

        return result
        