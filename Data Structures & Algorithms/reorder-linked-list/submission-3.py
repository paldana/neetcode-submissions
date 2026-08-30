# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Brute Force - Using Arrays and 2 Pointerss
        # Time and Space: O(n)
        if not head:
            return
        
        cur = head
        nodes = []

        # Append all nodes in an array
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        # setup 2 pointers
        l, r = 0, len(nodes) - 1
        while l < r:
            nodes[l].next = nodes[r]
            l += 1

            if l >= r:  # check if l and r have reached the midpoint of the list
                break   # break out of the while loop
            
            nodes[r].next = nodes[l]
            r -= 1

        nodes[l].next = None    # we've reached the end of the reordered list


