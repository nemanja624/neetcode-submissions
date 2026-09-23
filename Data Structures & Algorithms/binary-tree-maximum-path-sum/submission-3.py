# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def path(root):
            if not root:
                return 0

            maxLeft = path(root.left)
            maxRight = path(root.right)
            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)

            res[0] = max(res[0], root.val + maxLeft + maxRight)

            return root.val + max(maxLeft, maxRight)

        path(root)

        return res[0]
            


            


