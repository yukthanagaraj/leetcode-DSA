from collections import Counter

class Solution:
    def minStickers(self, stickers, target):
        sticker_counts = [Counter(s) for s in stickers]
        memo = {"": 0}

        def dfs(rem):
            if rem in memo:
                return memo[rem]

            target_count = Counter(rem)
            ans = float('inf')

            for sticker in sticker_counts:
                if rem[0] not in sticker:
                    continue

                new_rem = []

                for ch, cnt in target_count.items():
                    if cnt > sticker[ch]:
                        new_rem.extend(ch * (cnt - sticker[ch]))

                new_rem = ''.join(sorted(new_rem))

                res = dfs(new_rem)
                if res != -1:
                    ans = min(ans, 1 + res)

            memo[rem] = -1 if ans == float('inf') else ans
            return memo[rem]

        return dfs(''.join(sorted(target)))