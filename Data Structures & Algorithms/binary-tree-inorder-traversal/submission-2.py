# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Resurcsion
        # if not root:
        #     return []

        # values=(self.inorderTraversal(root.left))
        # values.append(root.val)
        # values.extend(self.inorderTraversal(root.right))

        # return values

        # Iteration
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)

            current = current.right

        return result