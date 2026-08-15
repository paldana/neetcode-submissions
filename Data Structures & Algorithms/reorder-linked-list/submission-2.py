# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the LL
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # by the end of above loop, slow is the end of 1st half 
        # and slow.next is start of 2nd half
        second = slow.next

        # reverse the 2nd half of the LL
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # by end of the Reverse LL loop, prev will be the head of the RLL (2nd half)
        first, second = head, prev
        # Combine the two halves alternatively
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2