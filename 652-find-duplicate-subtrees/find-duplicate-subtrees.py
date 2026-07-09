# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root):
        from collections import defaultdict

        count = defaultdict(int)
        ans = []

        def dfs(node):
            if not node:
                return "#"

            serial = "{},{},{}".format(
                node.val,
                dfs(node.left),
                dfs(node.right)
            )

            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)

            return serial

        dfs(root)
        return ans