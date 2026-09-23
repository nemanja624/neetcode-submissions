# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] # global variable

        def path(root):
            if not root:
                return 0

            maxLeft = max(0, path(root.left))
            maxRight = max(0, path(root.right))

            res[0] = max(res[0], root.val + maxLeft + maxRight)

            return root.val + max(maxLeft, maxRight)

        path(root)

        return res[0]
            


            


