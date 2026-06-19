# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root):
        self.answer = "~"   # bigger than any lowercase string

        def dfs(node, path):
            if not node:
                return

            # add current character
            path += chr(node.val + ord('a'))

            # leaf node
            if not node.left and not node.right:
                self.answer = min(self.answer, path[::-1])
                return

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")

        return self.answer