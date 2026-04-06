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
        map_node = {} # cur node -> new node

        cur_head = head
        dummy = Node(0, None, None)
        cur_new = dummy

        while cur_head:
            copied_node =  Node(cur_head.val, None, None)
            cur_new.next = copied_node

            map_node[cur_head] = copied_node

            cur_head = cur_head.next
            cur_new = cur_new.next

        for key, value in map_node.items():
            if key.random:
                value.random = map_node[key.random]
        
        return dummy.next


            

