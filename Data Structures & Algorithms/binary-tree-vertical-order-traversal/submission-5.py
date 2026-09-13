# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    BFS x Hashmap Approach
    Create a hashmap (colsMap) that will store the list of nodes that are seen in each vert/col, 
    with root being column 0, columns to the left of root are less than 0, and greater than 0 for
    columns to the right of the root.

    Go through each node layer by layer, starting from the left side since we'll want the node to the left
    first before the ones to the right if they're in the same column.

    Once the whole binary tree has been explored, compile the result in a list of lists starting from the 
    leftmost node.
"""


from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        colsMap = defaultdict(list)
        q = deque([(root, 0)])
        minCol = maxCol = 0

        while q:
            for _ in range(len(q)):
                node, col = q.popleft()
                minCol, maxCol = min(minCol, col), max(maxCol, col)
                colsMap[col].append(node.val)
                
                
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))
                
        res = []
        for i in range(minCol, maxCol + 1):
            res.append(colsMap[i])
            
        return res