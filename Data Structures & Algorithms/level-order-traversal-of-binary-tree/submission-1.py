# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            return 1 + max(left, right)

        depth = dfs(root)
        res = [[] for _ in range(depth)]
        queue = deque([(root, 1)])

        while queue:
            node, level = queue.popleft()
            res[level - 1].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        return res

        

