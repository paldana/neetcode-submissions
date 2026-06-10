# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()       # dummy node will be pointing to the head of the merged list

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next      
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2      # since either one of the lists will be empty, point the
                                        # node.next pointer to whichever that has remaining nodes

        return dummy.next               # return the new head of the merged list