# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def preorder(self, root):
        if not root:
            return "$"

        return str(root.val) + self.preorder(root.left) + self.preorder(root.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        substring = self.preorder(subRoot)
        string = self.preorder(root)

        return substring in string



