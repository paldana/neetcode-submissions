# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):      # preorder
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():      # preorder deserialize
            if vals[self.i] == "N":
                self.i += 1     # increment index i before returning None for null node
                return None
            
            node = TreeNode(int(vals[self.i]))      # Create node if not null
            self.i += 1                 

            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

# DFS Solution
# Time and Space: O(n)