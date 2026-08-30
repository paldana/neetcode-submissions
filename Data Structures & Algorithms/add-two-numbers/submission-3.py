# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode
        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum = num1 + num2 + carry

            rem = sum % 10
            carry = sum // 10
            node.next = ListNode(rem)
            node = node.next

            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None

        return dummy.next
