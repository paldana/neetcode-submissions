# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        
        ## since we've already checked that if the node is None above,
        ## this can be simplified
        # leftDepth, rightDepth = 0, 0
        # if root.left:
        #     leftDepth = self.maxDepth(root.left)
        # if root.right:
        #     rightDepth = self.maxDepth(root.right)
        # return 1 + max(leftDepth, rightDepth)

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
                    
# DFS method
# T: O(n); S: O(h)
# Where n is the number of nodes in the tree and h is the height of the tree.