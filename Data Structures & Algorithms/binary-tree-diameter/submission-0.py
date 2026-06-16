# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # Returns height
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return max(left, right) + 1         # +1 will give the height from "curr"
        
        dfs(root)
        return self.res

# DFS Solution
# Time: O(n) - n is number of nodes
#           - Best case: O(log(n) - balanced tree
#           - Worst case: O(n)  - degenerate tree
# Space: O(h) - h is height of the tree. 