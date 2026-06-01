class Solution:
    def findRotateSteps(self, ring, key):
        n = len(ring)

        pos_map = {}
        for i, ch in enumerate(ring):
            if ch not in pos_map:
                pos_map[ch] = []
            pos_map[ch].append(i)

        memo = {}

        def dp(i, pos):
            if i == len(key):
                return 0

            if (i, pos) in memo:
                return memo[(i, pos)]

            ans = float('inf')

            for nxt in pos_map[key[i]]:
                dist = abs(nxt - pos)
                rotate = min(dist, n - dist)

                ans = min(ans, rotate + 1 + dp(i + 1, nxt))

            memo[(i, pos)] = ans
            return ans

        return dp(0, 0)