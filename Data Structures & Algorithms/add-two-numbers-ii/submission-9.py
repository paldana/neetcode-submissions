# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ## reversing list
        rl1 = self.reverseList(l1)
        rl2 = self.reverseList(l2)

        dummy = node = ListNode()
        carry = 0
        
        while rl1 or rl2 or carry:
            num1 = rl1.val if rl1 else 0
            num2 = rl2.val if rl2 else 0
            sum = num1 + num2 + carry

            rem = sum % 10
            carry = sum // 10
            node.next = ListNode(rem)

            node = node.next
            rl1 = rl1.next if rl1 else None
            rl2 = rl2.next if rl2 else None
        
        return self.reverseList(dummy.next)
            



    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


