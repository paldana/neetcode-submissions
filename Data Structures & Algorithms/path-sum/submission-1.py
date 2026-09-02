# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curTarget):
            if not node:
                return False

            curTarget -= node.val

            if not node.left and not node.right:
                return curTarget == 0
            
            return dfs(node.left, curTarget) or dfs(node.right, curTarget)
        return dfs(root, targetSum)