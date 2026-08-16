# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        ### DFS Solution -- recursion -- easiest to implement
        ## Time: O(n) | Space: O(n)
        # temp = root.left
        # root.left = root.right
        # root.right = temp
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root
        

        ### DFS Solution -- iteration using stack
        ## Time: O(n) | Space: O(n)
        # stack = [root]
        # while stack:
        #     node = stack.pop()  # Starts from the root node
        #     print(node.val)         
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return root
        

        ### BFS Solution - Queue
        ##  Time: O(n) | Space: O(n)
        queue = deque([root])
        while queue:
            node = queue.popleft()   # Starts from the root node
            print(node.val)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root