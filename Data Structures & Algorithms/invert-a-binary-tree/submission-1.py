# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        new_root = TreeNode(root.val)

        if root.right:
            new_root.left = self.invertTree(root.right)
        if root.left:
            new_root.right = self.invertTree(root.left)

        return new_root
        