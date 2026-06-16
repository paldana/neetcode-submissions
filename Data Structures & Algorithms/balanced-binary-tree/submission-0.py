# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs will return a pair of values: [balanced_tree: bool, height of node: int]
        def dfs(curr):
            if not curr:
                return [True, 0]

            left, right = dfs(curr.left), dfs(curr.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

# DFS Solution
# Time: O(n) - n is number of nodes
#           - Best case: O(log(n) - balanced tree
#           - Worst case: O(n)  - degenerate tree
# Space: O(h) - h is height of the tree. 