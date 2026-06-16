# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # set a queue with tupple of the node, lower limit and the upper limit 
        # for checking if the node keeps the BST valid
        q = collections.deque([(root, float('-inf'), float('inf'))])

        while q:
            node, l, r = q.popleft()
            if not node:
                continue
            
            # check if value of current node is within valid limits
            if not l < node.val < r:
                return False
            
            # Append child nodes to the queue with the updated lower and upper limits
            if node.left:
                q.append((node.left, l, node.val))
            
            if node.right:
                q.append((node.right, node.val, r))
            
        return True

