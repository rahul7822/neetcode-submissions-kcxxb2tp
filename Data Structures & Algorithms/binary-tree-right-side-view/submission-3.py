# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result

        queue = deque([root])

        while queue:
            level_len = len(queue)
            level_nodes = []
            for _ in range(level_len):
                node = queue.popleft()
                level_nodes.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return list(map(lambda level : level.pop().val, result))
