class Solution:
    def numJewelsInStones(self, jewels, stones):
        jewels_set = set(jewels)
        count = 0

        for stone in stones:
            if stone in jewels_set:
                count += 1

        return count