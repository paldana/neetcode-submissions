# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right pointer by 'n' times 
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        # delete the node next to left pointer by redirecting the next pointer to the next next node
        left.next = left.next.next
        
        return dummy.next       # pointing to the head of the list

        # 2 pointers method
        # Time: O(n); Space: O(1)