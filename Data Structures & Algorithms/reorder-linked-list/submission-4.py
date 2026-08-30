# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## 2 pointer solution - fast and slow pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next       # moves twice as fast as slow
        # after this loop, slow.next will be the start of the 2nd half of the linked list
        l1 = head
        l2 = slow.next
        slow.next = None    # cut the list in 2 halves

        # reverse the 2nd half of the list
        def reverseList(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev
        rl2 = reverseList(l2)

        # intertwine the first half and the 2nd half that is reversed
        first, second = l1, rl2
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        