from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles):
        count = Counter(tiles)

        def dfs():
            ans = 0

            for ch in count:
                if count[ch] == 0:
                    continue

                ans += 1
                count[ch] -= 1
                ans += dfs()
                count[ch] += 1

            return ans

        return dfs()
        