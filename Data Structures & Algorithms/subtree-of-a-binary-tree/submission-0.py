# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_root_node_in_tree(self, root, target):
        result_node = None

        def dfs(node):
            nonlocal result_node
            if not node:
                return
                
            if node.val == target.val:
                result_node = node
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return result_node
    
    def is_same_tree(self, root, sub_root):
        if not root and not sub_root:
            return True
        if not root or not sub_root:
            return False
        if root.val != sub_root.val:
            return False
        return self.is_same_tree(root.left, sub_root.left) and self.is_same_tree(root.right, sub_root.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        sub_root_in_tree = self.find_root_node_in_tree(root, subRoot)
        if not sub_root_in_tree:
            return False

        return self.is_same_tree(sub_root_in_tree, subRoot)