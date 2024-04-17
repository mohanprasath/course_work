# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        start = end = head
        while end and end.next:
            start = start.next
            end = end.next.next
        return start
