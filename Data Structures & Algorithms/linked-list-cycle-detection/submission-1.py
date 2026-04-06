# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        try:
            while fast:
                fast = fast.next.next

                if slow == fast:
                    return True

                slow = slow.next
        except:
            return False
        
        return False
            