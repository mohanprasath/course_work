# Definition for singly-linked list.
class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        result = []
        head = ListNode()
        tail = head
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            if total > 9:
                carry = 1
                tail.val = total - 10
            else:
                tail.val = total
                carry = 0
            l1 = l1.next
            l2 = l2.next
            if l1 and l2:
                tail.next = ListNode()
                tail = tail.next
        return head
