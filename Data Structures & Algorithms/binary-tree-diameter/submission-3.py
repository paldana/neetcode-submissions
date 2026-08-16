# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Global variable for getting the diameter of the tree
        self.res = 0 

        # Returns height
        def dfs(node):
            if not node:
                return 0
            # get the height of left and right child nodes
            left, right = dfs(node.left), dfs(node.right)
            # height at a node (i.e. left) will be used to calculate the diameter (left+right)
            self.res = max(self.res, left + right)  # store the largest diameter we can get in the self.res
            return max(left, right) + 1     # return the height from the current node

        dfs(root)
        return self.res

## DFS Solution -- this problem is more of a medium difficulty, not EASY
# Time: O(n) - n is number of nodes
#           - Best case: O(log(n) - balanced tree
#           - Worst case: O(n)  - degenerate tree
# Space: O(h) - h is height of the tree. 