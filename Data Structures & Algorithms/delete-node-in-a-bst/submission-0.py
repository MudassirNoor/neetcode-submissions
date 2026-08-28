# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            elif root.left and root.right:
                root.val = self.minNode(root.right).val
                root.right = self.deleteNode(root.right, root.val)
            else:
                return root.left or root.right
        
        return root

    def minNode(self, root: Optional[TreeNode]) -> TreeNode:
        curr = root
        while curr and curr.left:
            curr = curr.left
        
        return curr