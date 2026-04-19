# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"
        
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        node_values = data.split(",")
        index = 0

        def dfs():
            nonlocal index
            if index >= len(node_values):
                return None

            root_value = node_values[index]
            if root_value == "null":
                return None

            root = TreeNode(root_value)
            index += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()









