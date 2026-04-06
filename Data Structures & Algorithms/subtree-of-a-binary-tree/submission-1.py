# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_same_tree(self, root, sub_root):
        if not root and not sub_root:
            return True
        if not root or not sub_root:
            return False
        if root.val != sub_root.val:
            return False
        # if root != sub_root:
        #     return False
        return self.is_same_tree(root.left, sub_root.left) and self.is_same_tree(root.right, sub_root.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)