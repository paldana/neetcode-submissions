# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, float("-inf"), float("inf"))])      # [node, lower limit, upper limit]

        while q:
            node, l, r = q.popleft()
            if not node: 
                continue

            if not (l < node.val < r):
                return False
            
            if node.left:
                q.append((node.left, l, node.val))
            if node.right:
                q.append((node.right, node.val, r))
        
        return True


    # BFS Method
    # Time and Space Complexity: O(n)