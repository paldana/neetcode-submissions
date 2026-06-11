# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # BFS will be ideal solution to get the list of level traversal order
        q = deque()
        q.append(root)
        res = []

        while q:
            levelList = []
             # although len(q) changes within this for-loop, it will still only run up to the
             # initial value it was set on. New value will be used once a new for-loop is started.
            for _ in range(len(q)):
                node = q.popleft()
                if not node:        # skip rest of the cycle and go to the next for-loop iteration
                    continue

                levelList.append(node.val)
                q.append(node.left)
                q.append(node.right)

            if levelList:
                res.append(levelList)
        
        return res
        
# BFS Method
# Time and Space Complexity: O(n)