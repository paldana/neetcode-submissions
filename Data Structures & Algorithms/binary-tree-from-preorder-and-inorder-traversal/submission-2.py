# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Inorder: left side - root - right side
        # Preorder: level-by-level order, starting from root, top to bottom, left to right
        if not preorder or not inorder:
            return None

        # print(f"preorder: {preorder}, inorder: {inorder}")
        root = TreeNode(preorder[0])                # first element will always be the root node in preorder
        mid = inorder.index(preorder[0])            # get index of the root node in the inorder list
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])     # use the mid index as the pivot
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :]) # for creating left and right children
        return root