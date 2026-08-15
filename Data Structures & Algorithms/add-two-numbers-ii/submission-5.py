# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        dummy = cur = ListNode()
        rl1 = reverse_list(l1)
        rl2 = reverse_list(l2)

        carry = 0
        while rl1 or rl2 or carry:
            num1 = rl1.val if rl1 else 0
            num2 = rl2.val if rl2 else 0

            total = num1 + num2 + carry
            carry = total // 10
            rem = total % 10
            cur.next = ListNode(rem)

            cur = cur.next
            rl1 = rl1.next if rl1 else None
            rl2 = rl2.next if rl2 else None
        
        return reverse_list(dummy.next)
                
                
