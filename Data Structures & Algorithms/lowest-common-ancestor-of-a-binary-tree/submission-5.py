# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None

        def dfs(node):
            nonlocal lca
            # if current node is null or if the LCA has been found, return false for both left and right child
            if not node or lca:
                return [False, False]
            
            left = dfs(node.left)
            right = dfs(node.right)
            # res = [left[0] or right[0] or (node == p), left[1] or right[1] or (node == q)]
            res = [left[0] or right[0] or (p.val == node.val), left[1] or right[1] or (q.val == node.val)]

            if res[0] and res[1] and not lca:
                lca = node
            
            return res

        dfs(root)
        return lca
            
