# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## BFS Solution using Hashmap
from collections import defaultdict, deque


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        colsMap = defaultdict(list)
        q = deque([(root, 0)])      # node, col position -> root = 0, left = -1, right = +1
        minCol = maxCol = 0

        while q:
            for _ in range(len(q)):
                node, col = q.popleft()
                colsMap[col].append(node.val)
                minCol, maxCol = min(minCol, col), max(maxCol, col)

                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

        res = []

        for i in range(minCol, maxCol + 1):
            res.append(colsMap[i])       
        
        return res

