# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        ## Recursive Approach
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root

        ## iterative approach
        # curr = root
        # while True:
        #     if val < curr.val:
        #         if not curr.left:
        #             curr.left = TreeNode(val)
        #             return root
        #         curr = curr.left
        #     else:
        #         if not curr.right:
        #             curr.right = TreeNode(val)
        #             return root
        #         curr = curr.right

