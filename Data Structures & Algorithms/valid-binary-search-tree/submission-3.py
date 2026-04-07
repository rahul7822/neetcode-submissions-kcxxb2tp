# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            node, left, right = queue.pop()

            if not (left < node.val < right):
                return False

            if node.left:
                queue.appendleft((node.left, left, node.val))
            if node.right:
                queue.appendleft((node.right, node.val, right))

        return True