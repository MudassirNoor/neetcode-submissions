# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # For each node, check if it satisfies the conditino of the subtree
        if not root:
            return False
        
        if not subRoot:
            return False

        if self.isMatchingTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isMatchingTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif root and subRoot and root.val == subRoot.val:
            return self.isMatchingTree(root.left, subRoot.left) and self.isMatchingTree(root.right, subRoot.right)
        else:
            return False