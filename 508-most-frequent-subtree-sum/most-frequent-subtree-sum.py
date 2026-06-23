from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root):
        if not root:
            return []

        freq = defaultdict(int)
        max_freq = [0]

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            total = left + right + node.val

            freq[total] += 1
            max_freq[0] = max(max_freq[0], freq[total])

            return total

        dfs(root)

        ans = []
        for key in freq:
            if freq[key] == max_freq[0]:
                ans.append(key)

        return ans
        