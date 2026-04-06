# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def total_nodes(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
    def reverse_ll(self, head):
        cur = head
        next = None
        prev = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy

        total_nodes = self.total_nodes(head)
        total_batches = total_nodes // k
        
        cur_head = head
        while total_batches > 0:
            temp = ListNode()
            for i in range(k):
                temp.next = head
                temp = temp.next
                head = head.next

            next_head = temp.next
            temp.next = None
            result.next = self.reverse_ll(cur_head)

            while result.next != None:
                result = result.next

            cur_head = next_head
            total_batches -= 1
        
        # remaining nodes 
        result.next = head
        
        return dummy.next