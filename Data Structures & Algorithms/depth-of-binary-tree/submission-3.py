# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                print(f"i: {i}, len(q): {len(q)} | level: {level}")
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    print("append node left")
                if node.right:
                    q.append(node.right)
                    print("append node right")

                print(f"new len(q): {len(q)}")
            level += 1
            print("- next level - ")
            
        return level
                    
# BFS method
# T: O(n); S: O(n)