# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ## Recursion approach
        # if not root:
        #     return TreeNode(val, None, None)
        # if val < root.val:
        #     root.left = self.insertIntoBST(root.left, val)
        # elif val > root.val:
        #     root.right = self.insertIntoBST(root.right, val)
        # return root

        ## Iterative Approach
        if not root:
            return TreeNode(val)
        
        curr = root
        while True:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                curr = curr.left

            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                curr = curr.right
            
            ## we can't do it this way because we're going to lose the link once we have curr at None before creating the tree node
            # if val < curr.val:
            #     curr = curr.left
            # else:
            #     curr = curr.right
            # if not curr:
            #     curr = TreeNode(val)
            #     return root

        
