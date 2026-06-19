# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_so_far):
            if not root:
                return 0

            if root.val >= max_so_far:
                count = 1
            else:
                count = 0

            new_max = max(max_so_far, root.val)

            return count + dfs(root.left, new_max) + dfs(root.right, new_max)

        return dfs(root, root.val)