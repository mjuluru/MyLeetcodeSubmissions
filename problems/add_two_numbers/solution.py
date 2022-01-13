# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        l3 = result
        while l1 or l2:
            sum = 0
            if l1:
                sum = l1.val
            if l2:
                sum = sum + l2.val
            sum = sum + carry
            carry = sum // 10
            if carry > 0:
                sum = sum % 10
            l3.next = ListNode(sum)
            l3 = l3.next
            if l1!= None: l1 = l1.next
            if l2!= None: l2 = l2.next
        if carry > 0:
            l3.next = ListNode(carry)
        return result.next
            