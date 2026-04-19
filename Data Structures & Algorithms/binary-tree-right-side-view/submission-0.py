# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def right_view_nodes(self, root, result):
        def dfs(node):
            if not node:
                return

            result.append(node.val)

            if node.right:
                dfs(node.right)
            else:
                dfs(node.left)

        dfs(root)

    def remaining_view(self, root, result):
        counter = 1
        len_result = len(result)

        def dfs(node):
            nonlocal counter
            if not node:
                return

            counter += 1
            print("counter", counter)
            print("len_result", len_result)
            if counter > len_result:
                result.append(node.val)

            if node.right:
                dfs(node.right)
            else:
                dfs(node.left)
        
        dfs(root)


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        height = self.height(root)
        print(height)

        result.append(root.val)

        self.right_view_nodes(root.right, result)
        print(result)

        if len(result) < height:
            self.remaining_view(root.left, result)

        return result
