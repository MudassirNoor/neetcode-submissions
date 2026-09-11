# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []

        res = []
        
        def dfs(node, max_in_path):
            if node.val >= max_in_path:
                res.append(node.val)
            
            max_in_path = max(max_in_path, node.val)
            
            if node.left:
                dfs(node.left, max_in_path)
            if node.right:
                dfs(node.right, max_in_path)

        dfs(root, root.val)
        return len(res)