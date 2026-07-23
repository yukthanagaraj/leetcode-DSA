
class Solution:
    def arrayRankTransform(self, arr):
        # Sort unique elements
        sorted_unique = sorted(set(arr))

        # Assign ranks
        rank = {}
        for i, num in enumerate(sorted_unique):
            rank[num] = i + 1

        # Replace elements with their ranks
        return [rank[num] for num in arr]