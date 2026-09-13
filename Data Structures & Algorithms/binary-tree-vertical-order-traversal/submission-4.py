# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ## bfs x hashmap
        if not root: 
            return []
            
        colsMap = defaultdict(list)
        minCol = maxCol = 0
        q = deque([(root, 0)])   # node, col

        while q:
            for _ in range(len(q)):
                node, col = q.popleft()
                # if not node:
                #     continue
                colsMap[col].append(node.val)
                minCol = min(minCol, col)
                maxCol = max(maxCol, col)

                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

        res = []
        for col in range(minCol, maxCol + 1):
            res.append(colsMap[col])
        
        return res