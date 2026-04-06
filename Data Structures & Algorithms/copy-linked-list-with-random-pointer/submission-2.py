"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
            
        map_node = {} # cur node -> new node
        cur = head

        while cur:
            copied_node =  Node(cur.val)
            map_node[cur] = copied_node
            cur = cur.next

        cur = head
        while cur:
            copied_cur = map_node[cur]
            copied_cur.next = None if cur.next == None else map_node[cur.next]
            copied_cur.random = None if cur.random == None else map_node[cur.random]
            cur = cur.next
        
        return map_node[head]

