# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0, None)
        cur = dummy_node

        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            result_digit = 0
            if sum > 9:
                result_digit = sum % 10
                carry = 1
            else:
                result_digit = sum
                carry = 0
            
            cur.next = ListNode(result_digit)

            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        while l1:
            sum = l1.val + carry
            result_digit = 0
            if sum > 9:
                result_digit = sum % 10
                carry = 1
            else:
                result_digit = sum
                carry = 0
            
            cur.next = ListNode(result_digit)

            l1 = l1.next
            cur = cur.next

        while l2:
            sum = l2.val + carry
            result_digit = 0
            if sum > 9:
                result_digit = sum % 10
                carry = 1
            else:
                result_digit = sum
                carry = 0
            
            cur.next = ListNode(result_digit)

            l2 = l2.next
            cur = cur.next

        if carry > 0:
            cur.next = ListNode(carry)

        return dummy_node.next
        