# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = deque([root])

        while queue:
            cur_level = []
            prev_level_len = len(queue)

            while prev_level_len > 0:
                node = queue.pop()                
                cur_level.append(node.val)

                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
                
                prev_level_len -= 1
            
            res.append(cur_level)

        return res
