# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Reverse and Merge solution - using fast and slow pointers
        # Time: O(n); Space: O(1)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # After this loop, slow pointer will be the end of the first half
        # and slow.next will be the start of the 2nd half
        second = slow.next
        
        # reverse 2nd half
        prev = slow.next = None     # slow.next cuts the list into 2 halves
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

         # Merge the 2 halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
           
