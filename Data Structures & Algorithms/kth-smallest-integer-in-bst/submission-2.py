# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Inorder Traversal Solution -  Time and Space: O(n)
        # given it's a BST, the values to the left of root will be smaller than the ones on right
        # best approach will be to use DFS method and go to the left first, then append values
        # to an array. Once all the nodes have been visited, return the Kth value from the array.
        self.res = []

        def dfs(node):
            if not node:
                return
            print(f"current node: {node.val}")

            dfs(node.left)
            self.res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        print(self.res)

        return self.res[k-1]