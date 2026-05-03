class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        # Map for quick lookup in inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        self.pre_index = 0

        def helper(left, right):
            if left > right:
                return None

            # Pick current root from preorder
            root_val = preorder[self.pre_index]
            self.pre_index += 1

            root = TreeNode(root_val)

            # Find root position in inorder
            mid = inorder_map[root_val]

            # Build left and right subtree
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)
        