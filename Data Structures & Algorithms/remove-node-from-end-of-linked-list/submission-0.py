# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and n >= 0:
            fast = fast.next
            n -= 1

        while fast and slow:
            slow = slow.next
            fast = fast.next

        target = slow.next
        next = None if target == None else target.next

        slow.next = next

        return head if next != None else None

        