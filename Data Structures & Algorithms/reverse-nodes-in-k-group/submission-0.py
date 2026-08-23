# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            # if remaining list is < k, kth will be None, so break out of the while loop
            if not kth:
                break
            groupNext = kth.next    # start of the next k-group batch

            ## Reverse the k-group batch
            # prev = kth.next instead of None since we want the last node of the reversed list 
            # to point to the first node of the next k-group.
            # curr = groupPrev.next is the start of the k-group to be reversed
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # update the start of the next group for the next iteration of the while-loop
            tmp = groupPrev.next        # at this point, groupPrev.next is the beginning of the list that was just reversed
            groupPrev.next = kth        # update it to the beginning of the next batch of k-group
            groupPrev = tmp             # groupPrev will now be the node before the kth node (start of the next k-group batch)
        
        return dummy.next       # return the updated list 

    # will return the Kth node (end of the k-group list)
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr