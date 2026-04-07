# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(pre_o, in_o):
            if not pre_o or not in_o:
                return None

            root_val = pre_o[0]
            in_index = in_o.index(root_val)
            root = TreeNode(root_val)

            root.left = dfs(pre_o[1 : in_index + 1], in_o[0 : in_index])
            root.right = dfs(pre_o[in_index + 1 : ], in_o[in_index + 1 : ])

            return root

        return dfs(preorder, inorder)

        