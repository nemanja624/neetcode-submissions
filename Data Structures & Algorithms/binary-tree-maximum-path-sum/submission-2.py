# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def path(root):
            if not root:
                return 0

            nonlocal res

            left = max(0, path(root.left))
            right = max(0, path(root.right))

            curr_sum = root.val + left + right
            res = max(res, curr_sum)

            return root.val + max(left, right)

        path(root)

        return res

            


            


