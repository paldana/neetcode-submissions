# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]        # Global result 

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # ignore negative downward paths
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # update global result with the best path *through* node
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return the best "extendable" downward path
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

# DFS Solution
# Time and Space Complexity: O(n)