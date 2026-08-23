# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        return prev