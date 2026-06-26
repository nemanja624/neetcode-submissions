# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(root):
            if not root:
                return 0

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)

        smallest = float("inf")

        for n in res:
            if n < smallest:
                smallest = n

        print(res)

        cutoff = res[:k]

        return max(cutoff)