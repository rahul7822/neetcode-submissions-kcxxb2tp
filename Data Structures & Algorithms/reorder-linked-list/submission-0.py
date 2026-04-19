# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _get_two_lists(self, head: Optional[ListNode]):
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        return (head, slow)
    
    def _get_reversed_list(self, head):
        cur = head
        prev = None
        next = None

        while cur:
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next

        return prev
        
    def _get_merged_list(self, list1, list2):
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            cur.next = list1
            cur = cur.next
            list1 = list1.next

            cur.next = list2
            cur = cur.next
            list2 = list2.next

        if list1:
            cur.next = list1
        
        if list2:
            cur.next = list2

        return dummy.next


    def reorderList(self, head: Optional[ListNode]) -> None:
        list1, list2 = self._get_two_lists(head)
        list2 = self._get_reversed_list(list2)
        #print_ll(list1)
        #print_ll(list2)
        final_list = self._get_merged_list(list1, list2)
        #print_ll(final_list)
        head = final_list