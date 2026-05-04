class Solution(object):
    def buildTree(self, inorder, postorder):
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def helper(left, right):
            if left > right:
                return None

            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            # Build RIGHT subtree first (postorder is left→right→root,
            # so we consume from the end: root, then right, then left)
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)
        