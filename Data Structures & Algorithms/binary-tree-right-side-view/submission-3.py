# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        ## DFS Solution ##
        def dfs(node, depth):
            if not node:
                return None
            
            # this is the first node seen at this level, add node to res
            if len(res) == depth:
                res.append(node.val)
            
            dfs(node.right, depth + 1)      ## IMPORTANT to be executed first since we're looking for the right side view
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res

