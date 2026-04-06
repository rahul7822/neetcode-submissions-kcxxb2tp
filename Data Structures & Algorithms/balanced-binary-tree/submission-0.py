# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        is_balanced = True

        def dfs(node):
            nonlocal is_balanced
            if not node:
                return 0

            left_h = dfs(node.left)
            right_h = dfs(node.right)

            if abs(left_h - right_h) > 1:
                is_balanced = False
            
            return 1 + max(left_h, right_h)

        dfs(root)

        return is_balanced