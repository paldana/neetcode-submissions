# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        ### BFS Solution ###
        ## Time and Space: O(n)
        q = collections.deque([root])
        while q:
            rightSide = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    # it's important to append the left child first since we're prioritizing the right side
                    # of the trees. In the event where right node is null, we'll be keeping left node as
                    # the rightSide and append it to the resulting list
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
                

        ### DFS Solution ###
        ## -- To see the right side of a tree,
        ##    at each depth we only care about the first node we encounter when looking from the right.
        ## Time and Space: O(n)
        
        # def dfs(node, depth):
        #     if not node:
        #         return None
            
        #     # this is the first node seen at this level, add node to res
        #     if len(res) == depth:
        #         res.append(node.val)
            
        #     dfs(node.right, depth + 1)      ## IMPORTANT to be executed first since we're looking for the right side view
        #     dfs(node.left, depth + 1)
        
        # dfs(root, 0)
        # return res

