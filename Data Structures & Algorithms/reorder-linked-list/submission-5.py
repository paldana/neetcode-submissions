# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## Naive Solution - Array and 2 pointers
        nodes = []

        # save all nodes in the array
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        l, r = 0, len(nodes) - 1

        while l < r:
            nodes[l].next = nodes[r]
            l += 1

            if l >= r:  # check if we've reached mid point of the list
                break

            nodes[r].next = nodes[l]
            r -= 1
        
        nodes[l].next = None    # mark the end of the reordered list -- if not set, this will end up in an infinite cycle
