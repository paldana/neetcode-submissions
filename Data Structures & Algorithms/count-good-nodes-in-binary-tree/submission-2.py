# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we'll be using DFS method in order to go down each child nodes 
        # to see how many good nodes are there in total
        # good node = node val >= current max val in the node's path

        # returns number of good nodes
        def dfs(node, maxVal):
            if not node:
                return 0
            
            goodNodes = 0
            if node.val >= maxVal:
                goodNodes += 1
            
            # go through each child nodes to check for number of good nodes 
            # but first, update the maxVal to compare with the nodes in 
            # their respective paths
            maxVal = max(maxVal, node.val)
            goodNodes += dfs(node.left, maxVal)
            goodNodes += dfs(node.right, maxVal)

            return goodNodes

        return dfs(root, root.val)

## DFS Solution ##
# Time and Space Complexity: O(n)