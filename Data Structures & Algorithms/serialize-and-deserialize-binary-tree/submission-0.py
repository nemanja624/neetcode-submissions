# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        coded = []

        def dfs(root):
            if not root:
                coded.append("n")
                return

            coded.append(f'{root.val}')

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        print(coded)
        return ",".join(coded)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nums = deque(data.split(","))

        def dfs(nums):
            val = nums.popleft()

            if val == "n":
                return None

            root = TreeNode(int(val))
            root.left = dfs(nums)
            root.right = dfs(nums)

            return root

        return dfs(nums)






