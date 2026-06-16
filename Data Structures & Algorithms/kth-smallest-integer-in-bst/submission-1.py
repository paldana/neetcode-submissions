# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Brute Force - DFS Solution -- Get all values in the tree and sort it at the end
        self.res = []

        def dfs(node):
            if not node:
                return
            print(f"current node: {node.val}")

            self.res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        print(self.res)
        self.res.sort()

        return self.res[k-1]