# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur = None

        while list1 and list2:
            if list1.val <= list2.val:
                if head == None:
                    head = list1
                else:
                    cur.next = list1

                cur = list1
                list1 = list1.next
            else:
                if head == None:
                    head = list2
                else:
                    cur.next = list2

                cur = list2
                list2 = list2.next

        if list1:
            if head == None:
                head = list1
            else:
                cur.next = list1
        
        if list2:
            if head == None:
                head = list2
            else:
                cur.next = list2

        return head
        