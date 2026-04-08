# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        counter = 0

        cur = root
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left

            popped = stack.pop()
            counter += 1

            if counter == k:
                return popped.val

            if popped.right:
                cur = popped.right

        
        return None