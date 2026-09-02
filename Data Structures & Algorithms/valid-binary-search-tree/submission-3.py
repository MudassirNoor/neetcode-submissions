# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], minLimit: Optional[int] = None, maxLimit: Optional[int] = None) -> bool:
        isValidRight = True
        isValidLeft = True
        
        if root.left:
            if root.left.val < root.val and (minLimit is None or root.left.val > minLimit):
                isValidLeft = self.isValidBST(root.left, minLimit, root.val)
            else:
                return False
        
        if root.right:
            if root.right.val > root.val and (maxLimit is None or root.right.val < maxLimit):
                isValidRight = self.isValidBST(root.right, root.val, maxLimit)
            else:
                return False

        return isValidLeft and isValidRight