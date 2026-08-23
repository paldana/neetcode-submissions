# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:   # need to have at least a pair of lists
            mergedList = []

            for i in range(0, len(lists), 2):       # step size 2
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                mergedList.append(self.mergeSortedLists(l1,l2))

            lists = mergedList # update the lists with the mergedLists to keep merging mutiple lists
        return lists[0]

                            
    def mergeSortedLists(self, l1: List[Optional[ListNode]], l2: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = mergedLL = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                mergedLL.next = l1
                l1 = l1.next
            else:
                mergedLL.next = l2
                l2 = l2.next
            mergedLL = mergedLL.next
        
        mergedLL.next = l1 or l2

        return dummy.next

    ## time limit exceeded at 22nd test case T_T