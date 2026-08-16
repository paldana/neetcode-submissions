# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        ## Recursion Solution ##
        # if p and q and p.val == q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # else:
        #     return False

        ## Stack Solution ##
        # stack = [(p, q)]
        # while stack:
        #     n1, n2 = stack.pop()
        #     if not n1 and not n2:
        #         continue
        #     if not n1 or not n2 or n1.val != n2.val:
        #         return False
        #     stack.append((n1.left, n2.left))
        #     stack.append((n1.right, n2.right))
        # return True

        ## Queue Solution ##
        q1, q2 = deque([q]), deque([p])
        while q1 and q2:
            for _ in range(len(q1)):
                
                n1, n2 = q1.popleft(), q2.popleft()
                
                if not n1 and not n2:
                    continue
                if not n1 or not n2 or n1.val != n2.val:
                    return False

                q1.append(n1.left)
                q1.append(n1.right)
                q2.append(n2.left)
                q2.append(n2.right)
            
        return True