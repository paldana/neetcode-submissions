# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                n1, n2 = q1.popleft(), q2.popleft()
                
                if not n1 and not n2:   # we've found end of a node, proceed to next for cycle
                    continue
                
                if not n1 or not n2 or n1.val != n2.val:
                    return False
                
                q1.append(n1.left)
                q1.append(n1.right)
                q2.append(n2.left)
                q2.append(n2.right)
            
        return True


# BFS Method - using Queue
# Time: O(n); Space: O(n) - n is number of nodes