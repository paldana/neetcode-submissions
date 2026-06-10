# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursion method; 
        # Time: O(n), Space: O(1)
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)   
            head.next.next = head       # point next node's next to the current node to reverse
        head.next = None                

        return newHead